"""Décisions utilisateur stockées uniquement dans un dossier de rapport."""
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

DECISIONS = {'accepted', 'rejected', 'false_positive', 'deferred'}


def record_feedback(report_dir, finding_id, decision):
    if decision not in DECISIONS:
        raise ValueError('Décision inconnue.')
    directory = Path(report_dir).expanduser().resolve(strict=True)
    if not directory.is_dir():
        raise ValueError('Le rapport doit être un dossier.')
    report = directory / 'run.json'
    if report.is_symlink() or not report.is_file():
        raise ValueError('run.json absent ou lien symbolique interdit.')
    try:
        data = json.loads(report.read_text(encoding='utf-8'))
        target = Path(data['target']['path']).expanduser().resolve(strict=False)
        ids = {f['id'] for f in data['findings']}
        run_id = data['run_id']
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ValueError('Rapport JSON invalide.') from exc
    if directory == target or directory.is_relative_to(target) or target.is_relative_to(directory):
        raise ValueError('Le dossier de rapport doit être extérieur au projet.')
    if finding_id not in ids:
        raise ValueError('Identifiant de constat inconnu dans ce rapport.')
    destination = directory / 'feedback.json'
    if destination.is_symlink():
        raise ValueError('Lien symbolique de retour interdit.')
    if destination.exists():
        try:
            feedback = json.loads(destination.read_text(encoding='utf-8'))
            if feedback['run_id'] != run_id or not isinstance(feedback['decisions'], dict):
                raise ValueError('Fichier de retours incompatible avec ce rapport.')
        except (KeyError, TypeError, json.JSONDecodeError) as exc:
            raise ValueError('Fichier de retours invalide.') from exc
    else:
        feedback = {'run_id': run_id, 'decisions': {}}
    feedback['decisions'][finding_id] = {'status': decision, 'updated_at': datetime.now(timezone.utc).isoformat()}
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=directory, prefix='.feedback-', delete=False) as temp:
            temp_name = temp.name
            json.dump(feedback, temp, ensure_ascii=True, indent=2)
            temp.write('\n')
        os.replace(temp_name, destination)
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)
    return destination
