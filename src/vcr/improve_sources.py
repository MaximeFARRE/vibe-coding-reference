"""Lecture bornée de rapports et de notes volontairement sélectionnés."""
import hashlib
import json
import re
from pathlib import Path

from .improve_rules import RULES

MAX_INPUT = 1024 * 1024
MARKER = re.compile(r'^VCR_OBSERVATION ([a-z0-9-]+) (confirmed|suspected)$')


def read_file(path):
    path = Path(path).expanduser()
    if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_INPUT:
        raise ValueError('Source absente, lien symbolique ou fichier trop volumineux.')
    try:
        return path.resolve(strict=True), path.read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        raise ValueError('Source illisible ou non encodée en UTF-8.') from exc


def read_sources(project, reports, notes, logs):
    observations, limitations = [], []
    seen_runs, seen_texts = set(), set()
    for name in reports:
        path, text = read_file(name)
        try:
            data = json.loads(text)
            run_id = data['run_id']
            target = data['target']['path']
            findings = data['findings']
            if (data['schema_version'] != '0.1' or data['workflow'] != 'rescue'
                    or not isinstance(run_id, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,128}', run_id)
                    or not isinstance(target, str) or not Path(target).is_absolute()
                    or Path(target).resolve(strict=False) != project or not isinstance(findings, list)):
                raise ValueError('Rapport RESCUE incompatible ou projet différent.')
        except (KeyError, TypeError, json.JSONDecodeError) as exc:
            raise ValueError('Rapport RESCUE invalide.') from exc
        if run_id in seen_runs:
            limitations.append('Un rapport portant le même run_id a été ignoré : aucune occurrence supplémentaire.')
            continue
        seen_runs.add(run_id)
        feedback_path = path.parent / 'feedback.json'
        excluded = set()
        if feedback_path.exists() or feedback_path.is_symlink():
            _, feedback_text = read_file(feedback_path)
            try:
                feedback = json.loads(feedback_text)
                if feedback['run_id'] != run_id or not isinstance(feedback['decisions'], dict):
                    raise ValueError('Retours RESCUE incompatibles avec le rapport.')
                excluded = {k for k, v in feedback['decisions'].items() if isinstance(v, dict) and v.get('status') in {'false_positive', 'rejected'}}
            except (KeyError, TypeError, json.JSONDecodeError) as exc:
                raise ValueError('Retours RESCUE invalides.') from exc
        observed_ids = set()
        for index, finding in enumerate(findings):
            if not isinstance(finding, dict):
                raise ValueError('Constat RESCUE invalide.')
            rule = finding.get('rule_id') or finding.get('id')
            status = finding.get('status')
            if not isinstance(rule, str) or not isinstance(finding.get('id'), str):
                raise ValueError('Identifiant de constat RESCUE invalide.')
            if rule not in RULES or status not in {'confirmed', 'suspected'} or finding['id'] in excluded:
                continue
            evidence = finding.get('evidence')
            if not isinstance(evidence, list) or not any(isinstance(e, dict) and e.get('kind') and e.get('summary') for e in evidence):
                limitations.append('Un constat sans preuve déclarée a été ignoré.')
                continue
            if rule in observed_ids:
                continue
            observed_ids.add(rule)
            observations.append({'rule': rule, 'status': status, 'source': str(path), 'reference': f'/findings/{index}', 'identity': 'run:' + run_id, 'origin': 'rapport RESCUE fourni'})
    for kind, sources in [('note', notes), ('log', logs)]:
        for name in sources:
            path, text = read_file(name)
            digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
            if digest in seen_texts:
                limitations.append('Une note ou un journal identique a été ignoré : aucune occurrence supplémentaire.')
                continue
            seen_texts.add(digest)
            found = False
            seen_rules = set()
            for number, line in enumerate(text.splitlines(), 1):
                match = MARKER.fullmatch(line.strip())
                if match and match.group(1) in RULES and match.group(1) not in seen_rules:
                    rule, status = match.groups()
                    observations.append({'rule': rule, 'status': status, 'source': str(path), 'reference': f'ligne {number}', 'identity': 'text:' + digest, 'origin': kind + ' fourni par l’utilisateur'})
                    seen_rules.add(rule)
                    found = True
            if not found:
                limitations.append('Une note ou un journal ne contient aucun marqueur VCR reconnu ; aucune conclusion n’en est déduite.')
    return observations, limitations
