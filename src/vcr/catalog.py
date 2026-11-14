"""Catalogue local : classification de complexité et état de preuve séparés."""
import json
from copy import deepcopy
from datetime import date
from importlib.resources import files
from urllib.parse import urlsplit


def valid_url(value):
    if not isinstance(value, str) or len(value) > 2048:
        return False
    try:
        url = urlsplit(value)
        return bool(url.scheme == 'https' and url.hostname and not url.username and not url.password and not any(c.isspace() for c in value) and url.port != 0)
    except ValueError:
        return False


def valid_date(value):
    try:
        return isinstance(value, str) and date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def load_catalog():
    try:
        data = json.loads(files('vcr').joinpath('catalog.json').read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError('Catalogue local illisible ou invalide.') from exc
    return normalize_catalog(data)


def normalize_catalog(data):
    if not isinstance(data, dict) or data.get('version') != 1 or not isinstance(data.get('entries'), list):
        raise ValueError('Format du catalogue invalide.')
    review = data.get('review_date')
    if not valid_date(review):
        review = None
    normalized = []
    ids = set()
    for source in data['entries']:
        if not isinstance(source, dict) or not isinstance(source.get('id'), str) or not source['id'] or not isinstance(source.get('name'), str) or not source['name']:
            raise ValueError('Entrée de catalogue sans identifiant ou nom valide.')
        if source['id'] in ids:
            raise ValueError('Identifiant de catalogue dupliqué.')
        ids.add(source['id'])
        item = deepcopy(source)
        topics = item.get('topics')
        if not isinstance(topics, list) or any(not isinstance(t, str) or not t.strip() for t in topics):
            raise ValueError('Liste de thèmes invalide.')
        if item.get('kind') not in {'tool', 'publication'} or item.get('level') not in {'A', 'B', 'C'}:
            raise ValueError('Type ou niveau du catalogue invalide.')
        item['official_url'] = item.get('official_url') if valid_url(item.get('official_url')) else None
        item['scientific_url'] = item.get('scientific_url') if valid_url(item.get('scientific_url')) else None
        maintenance = item.get('maintenance_status')
        item['maintenance_status'] = maintenance if isinstance(maintenance, str) and maintenance in {'verified', 'unverified'} else 'unverified'
        if item['maintenance_status'] == 'verified' and (not valid_date(item.get('maintenance_verified_at')) or not valid_url(item.get('maintenance_source'))):
            item['maintenance_status'] = 'unverified'
        if (item.get('evidence_status') != 'verified' or not item['official_url'] or item['maintenance_status'] != 'verified'
                or review is None or not valid_date(item.get('evidence_verified_at')) or not valid_url(item.get('verification_source'))):
            item['evidence_status'] = 'unverified'
        item['recommended_by_default'] = False
        for key in ('evidence_type', 'problem', 'incompatibilities', 'hidden_costs', 'permissions', 'license', 'verification', 'rollback', 'maintainer', 'version'):
            if not isinstance(item.get(key), str) or not item[key].strip():
                item[key] = 'Non vérifié ou non renseigné.'
                item['evidence_status'] = 'unverified'
        normalized.append(item)
    return {'version': 1, 'review_date': review, 'review_basis': data.get('review_basis') if isinstance(data.get('review_basis'), str) else 'Non renseigné.', 'entries': normalized}


def search(catalog, topic=None):
    if not topic or not topic.strip():
        return list(catalog['entries'])
    query = topic.strip().casefold()
    return [item for item in catalog['entries'] if any(tag.casefold() == query for tag in item['topics'])]


def render(catalog, topic=None):
    entries = search(catalog, topic)
    available = sorted({tag for item in catalog['entries'] for tag in item['topics']})
    lines = ['# SOURCES — catalogue local', '', f"Date de la revue documentaire : {catalog['review_date'] or 'non vérifiée'}. {catalog['review_basis']}", 'Niveau A = référence simple ; B = optionnel ; C = recherche avancée. Ce niveau n’est pas un niveau de preuve.', 'Statut de preuve : `unverified` = à vérifier ; `verified` = vérification documentée dans les données. Aucun outil n’est installé ou recommandé par défaut.']
    if not entries:
        lines += ['', 'Aucun résultat pour ce thème. Thèmes disponibles : ' + ', '.join(available) + '.']
    for item in entries:
        lines += ['', f"## {item['name']} — {item['id']}", f"- **Type / thèmes :** {item['kind']} ; {', '.join(item['topics'])}", f"- **Niveau de complexité :** {item['level']}", f"- **Statut de preuve :** {item['evidence_status']} ; nature : {item['evidence_type']}", f"- **Maintenance :** {item['maintenance_status']} ; **installation par défaut :** non recommandée."]
        if item['evidence_status'] == 'verified':
            lines.append(f"- **Vérification de preuve :** {item['evidence_verified_at']} ; {item['verification_source']}")
        if item['maintenance_status'] == 'verified':
            lines.append(f"- **Vérification de maintenance :** {item['maintenance_verified_at']} ; {item['maintenance_source']}")
        lines.append(f"- **Mainteneur :** {item['maintainer']} **Version :** {item['version']}")
        for label, key in [('Problème traité', 'problem'), ('Incompatibilités / limites', 'incompatibilities'), ('Coûts cachés', 'hidden_costs'), ('Permissions', 'permissions'), ('Licence', 'license')]:
            lines.append(f"- **{label} :** {item[key]}")
        lines.append('- **Source officielle :** ' + (item['official_url'] or 'non renseignée ou URL invalide.'))
        lines.append('- **Source scientifique éventuelle :** ' + (item['scientific_url'] or 'non identifiée dans cette fiche ; recherche non exhaustive.'))
        lines += [f"- **Vérifications avant usage :** {item['verification']}", f"- **Retrait / retour arrière :** {item['rollback']}"]
    lines += ['', 'Les liens ne sont pas ouverts par VCR. Vérifier licence, version, permissions et retrait avant tout essai ; demander l’accord nécessaire avant installation ou exécution.']
    return '\n'.join(lines) + '\n'
