"""Registre par projet : décisions persistées uniquement hors cible."""
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from .improve_rules import RULES
from .improve_sources import read_file

STATUSES = {'pending', 'accepted', 'rejected', 'deferred', 'false_positive', 'obsolete'}


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def load_registry(path, project):
    _, content = read_file(path)
    try:
        data = json.loads(content)
        if (not isinstance(data, dict) or data.get('version') != 1
                or data.get('project') != str(project) or not isinstance(data.get('entries'), dict)):
            raise ValueError('Registre incompatible avec ce projet.')
        for rule, entry in data['entries'].items():
            if (rule not in RULES or not isinstance(entry, dict) or entry.get('approval_status') not in STATUSES
                    or not isinstance(entry.get('sources'), list) or not isinstance(entry.get('updated_at'), str)
                    or not isinstance(entry.get('reevaluate_when'), str)):
                raise ValueError('Entrée de registre invalide.')
            identities = set()
            for source in entry['sources']:
                if (not isinstance(source, dict) or source.get('rule') != rule
                        or source.get('status') not in {'confirmed', 'suspected'}
                        or any(not isinstance(source.get(k), str) or len(source[k]) > 4096 or not source[k] for k in ('source', 'reference', 'identity', 'origin'))):
                    raise ValueError('Source de registre invalide.')
                if source['identity'] in identities:
                    raise ValueError('Source dupliquée dans le registre.')
                identities.add(source['identity'])
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError('Registre JSON invalide.') from exc
    return data


def merge(project, observations, previous=None):
    registry = previous or {'version': 1, 'project': str(project), 'entries': {}}
    for obs in observations:
        rule = obs['rule']
        if rule not in registry['entries']:
            registry['entries'][rule] = {'sources': [], 'approval_status': 'pending', 'updated_at': timestamp(), 'reevaluate_when': 'Réexaminer après une nouvelle preuve, un changement de contexte ou une correction vérifiée.'}
        entry = registry['entries'][rule]
        if all(existing['identity'] != obs['identity'] for existing in entry['sources']):
            entry['sources'].append(obs)
            entry['updated_at'] = timestamp()
    return registry


def save_json(path, data):
    path = Path(path)
    if path.is_symlink():
        raise ValueError('Lien symbolique de registre interdit.')
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent, prefix='.vcr-registry-', delete=False) as temp:
            temp_name = temp.name
            json.dump(data, temp, ensure_ascii=True, indent=2)
            temp.write('\n')
        os.replace(temp_name, path)
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)


def update_status(registry_path, proposal_id, status):
    path = Path(registry_path).expanduser()
    if path.is_symlink() or not path.is_file():
        raise ValueError('Registre absent ou lien symbolique interdit.')
    # Le projet déclaré sert uniquement de garde-fou, pas d'autorisation d'y écrire.
    _, raw = read_file(path)
    try:
        project_value = json.loads(raw)['project']
        if not isinstance(project_value, str) or not Path(project_value).is_absolute():
            raise ValueError('Chemin de projet invalide.')
        project = Path(project_value).resolve(strict=False)
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ValueError('Registre invalide.') from exc
    directory = path.resolve(strict=True).parent
    if directory == project or directory.is_relative_to(project) or project.is_relative_to(directory):
        raise ValueError('Le registre doit être extérieur au projet.')
    registry = load_registry(path, project)
    if status not in STATUSES - {'pending'} or proposal_id not in registry['entries']:
        raise ValueError('Décision ou identifiant inconnu.')
    registry['entries'][proposal_id]['approval_status'] = status
    registry['entries'][proposal_id]['updated_at'] = timestamp()
    save_json(path, registry)
