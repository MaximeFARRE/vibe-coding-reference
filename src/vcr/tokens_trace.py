"""Import explicite du format VCR, sans conserver contenu de prompts ou commandes."""
import json
import re
from datetime import date
from decimal import Decimal
from pathlib import Path

MAX_BYTES = 4 * 1024 * 1024
METRICS = ('input_tokens', 'output_tokens', 'cache_read_tokens', 'cache_write_tokens')
RECORD_FIELDS = set(METRICS) | {'model', 'session_id', 'tool', 'command_chars', 'search_fingerprint', 'topic_count', 'cost'}
COST_FIELDS = {'amount', 'currency', 'kind', 'provider', 'date'}


def invalid_constant(_):
    raise ValueError('Nombre non fini interdit.')


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Champ JSON dupliqué interdit.')
        result[key] = value
    return result


def load_trace(filename):
    path = Path(filename).expanduser()
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_BYTES:
            raise ValueError('Trace absente, lien symbolique ou fichier trop volumineux.')
        data = json.loads(path.read_text(encoding='utf-8'), parse_float=Decimal, parse_constant=invalid_constant, object_pairs_hook=unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError('Trace JSON illisible ou invalide.') from exc
    if not isinstance(data, dict) or set(data) != {'format', 'records'} or data['format'] != 'vcr-token-trace-v1' or not isinstance(data['records'], list):
        raise ValueError('Format inconnu : format vcr-token-trace-v1 requis.')
    if len(data['records']) > 10000:
        raise ValueError('Trace trop volumineuse : 10 000 enregistrements maximum.')
    for record in data['records']:
        if not isinstance(record, dict) or set(record) - RECORD_FIELDS:
            raise ValueError('Enregistrement invalide ou champ non pris en charge.')
        for field in (*METRICS, 'command_chars', 'topic_count'):
            if field in record and (type(record[field]) is not int or record[field] < 0 or record[field] > 10**15):
                raise ValueError('Mesure entière invalide : entier positif ou nul requis.')
        for field in ('model', 'session_id', 'tool'):
            if field in record and (not isinstance(record[field], str) or not 1 <= len(record[field]) <= 256):
                raise ValueError('Identifiant de trace invalide.')
        if 'search_fingerprint' in record and (not isinstance(record['search_fingerprint'], str) or not re.fullmatch(r'[0-9a-f]{64}', record['search_fingerprint'])):
            raise ValueError('Empreinte de recherche invalide : SHA-256 attendu.')
        if ('cache_read_tokens' in record and 'input_tokens' in record
                and record['cache_read_tokens'] > record['input_tokens']):
            raise ValueError('Cache lu supérieur aux tokens d’entrée déclarés.')
        if 'cost' in record:
            validate_cost(record['cost'])
    return data['records']


def validate_cost(cost):
    if not isinstance(cost, dict) or set(cost) != COST_FIELDS:
        raise ValueError('Coût invalide : montant, devise, nature, fournisseur et date requis.')
    amount = cost['amount']
    if isinstance(amount, bool) or not isinstance(amount, (int, Decimal)) or (isinstance(amount, Decimal) and not amount.is_finite()):
        raise ValueError('Montant invalide.')
    if amount < 0 or amount > 10**15:
        raise ValueError('Montant hors limites.')
    if isinstance(amount, Decimal) and amount.as_tuple().exponent < -18:
        raise ValueError('Précision du montant trop élevée (18 décimales maximum).')
    if not isinstance(cost['currency'], str) or not re.fullmatch(r'[A-Z]{3}', cost['currency']):
        raise ValueError('Devise invalide : code à trois lettres attendu.')
    if cost['kind'] not in ('actual', 'estimated') or not isinstance(cost['provider'], str) or not 1 <= len(cost['provider']) <= 256:
        raise ValueError('Nature ou fournisseur du coût invalide.')
    try:
        if not isinstance(cost['date'], str) or date.fromisoformat(cost['date']).isoformat() != cost['date']:
            raise ValueError
    except ValueError as exc:
        raise ValueError('Date du coût invalide : AAAA-MM-JJ attendu.') from exc
