"""Validation limitée et prudente des constats produits par VCR."""
from copy import deepcopy
from pathlib import Path

STATUSES = {'confirmed', 'suspected', 'not_checked', 'not_applicable'}
CONFIDENCES = {'high', 'medium', 'low', 'unknown'}
ORIGINS = {'static_check', 'command', 'agent_review', 'user_provided'}
CATEGORIES = {'security', 'data', 'architecture', 'code', 'testing', 'performance', 'operations', 'documentation', 'context', 'tokens', 'product', 'dependencies', 'other'}
SEVERITIES = {'P0', 'P1', 'P2', 'P3', 'info'}
KINDS = {'file', 'command', 'log', 'configuration', 'user_statement', 'source'}
CHECKS = {'passed', 'failed', 'skipped', 'not_checked', 'not_applicable'}


def normalize(run, repo):
    """Retourne une copie ; erreurs de contrat fatales et preuves partielles signalées."""
    run = deepcopy(run)
    repo = Path(repo).resolve(strict=True)
    if run.schema_version != '0.1' or run.workflow not in {'start', 'rescue', 'improve', 'tokens'}:
        raise ValueError('Version ou workflow de rapport invalide.')
    if not run.run_id or not run.created_at or not isinstance(run.target, dict):
        raise ValueError('Identité, date ou cible du rapport invalide.')
    if any(not c.id or c.status not in CHECKS for c in run.checks):
        raise ValueError('Identifiant ou statut de vérification invalide.')
    unique = set()
    dedup = set()
    accepted = []
    for finding in run.findings:
        if (not finding.id or not finding.title or not isinstance(finding.summary, str)
                or finding.category not in CATEGORIES or finding.severity not in SEVERITIES
                or finding.status not in STATUSES or finding.confidence not in CONFIDENCES
                or finding.origin not in ORIGINS):
            raise ValueError('Constat invalide : identifiant, champs obligatoires ou énumération.')
        if finding.id in unique:
            raise ValueError('Identifiant de constat en double.')
        unique.add(finding.id)
        invalid = False
        for e in finding.evidence:
            if e.kind not in KINDS or not isinstance(e.summary, str) or not e.summary:
                raise ValueError('Preuve invalide : type ou résumé manquant.')
            has_lines = e.line_start is not None or e.line_end is not None
            lines_valid = (type(e.line_start) is int and e.line_start > 0
                           and (e.line_end is None or type(e.line_end) is int and e.line_end >= e.line_start))
            path_valid = False
            if e.path:
                path = Path(e.path)
                try:
                    full = repo / path
                    path_valid = (not path.is_absolute() and '..' not in path.parts
                                  and all(not (repo.joinpath(*path.parts[:i])).is_symlink() for i in range(1, len(path.parts) + 1))
                                  and full.resolve(strict=True).is_relative_to(repo) and full.is_file())
                except (OSError, ValueError):
                    path_valid = False
                if not path_valid:
                    e.path = None
                    invalid = True
            if has_lines:
                # Ne jamais lire un fichier sensible pour vérifier ses lignes.
                if not path_valid or not lines_valid or Path(e.path).name.startswith('.env'):
                    lines_valid = False
                else:
                    try:
                        full = repo / e.path
                        if full.stat().st_size > 1024 * 1024:
                            lines_valid = False
                        else:
                            with full.open('rb') as stream:
                                count = sum(1 for _ in stream)
                            lines_valid = (e.line_end or e.line_start) <= count
                    except OSError:
                        lines_valid = False
                if not lines_valid:
                    e.line_start = e.line_end = None
                    invalid = True
        if invalid or not finding.evidence:
            finding.confidence = 'low' if finding.confidence != 'unknown' else 'unknown'
            if finding.status == 'confirmed':
                finding.status = 'suspected'
            finding.limitations.append('Preuve absente ou localisation invalide : vérification complémentaire nécessaire.')
        # Ne fusionner que si règle, cause et emplacement précis sont tous explicites.
        locations = tuple((e.path, e.line_start, e.line_end) for e in finding.evidence if e.path)
        key = (finding.rule_id, finding.cause, locations)
        if finding.rule_id and finding.cause and locations and key in dedup:
            run.limitations.append('Constat dupliqué écarté : même règle, cause et emplacement.')
            continue
        if finding.rule_id and finding.cause and locations:
            dedup.add(key)
        accepted.append(finding)
    run.findings = accepted
    return run
