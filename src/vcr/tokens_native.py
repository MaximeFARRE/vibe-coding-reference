"""Import volontaire d'une seule réponse API ; jamais de collecte automatique."""
import json
from decimal import Decimal
from pathlib import Path

from .tokens_trace import MAX_BYTES, invalid_constant, unique_object

FORMATS = ('vcr', 'openai-responses', 'anthropic-messages')


def counter(mapping, key):
    value = mapping.get(key)
    if value is None:
        return None
    if type(value) is not int or value < 0 or value > 10**15:
        raise ValueError('Compteur de consommation invalide.')
    return value


def read_response(filename, kind):
    path = Path(filename).expanduser()
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_BYTES:
            raise ValueError('Fichier absent, lien symbolique ou fichier trop volumineux.')
        data = json.loads(path.read_text(encoding='utf-8'), parse_float=Decimal, parse_constant=invalid_constant, object_pairs_hook=unique_object)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError('Réponse JSON illisible ou invalide.') from exc
    if not isinstance(data, dict) or 'usage' not in data or (data['usage'] is not None and not isinstance(data['usage'], dict)):
        raise ValueError('Réponse API invalide : objet usage attendu.')
    usage = data['usage'] or {}
    record = {}
    output = counter(usage, 'output_tokens')
    if output is not None:
        record['output_tokens'] = output
    derived = False
    if kind == 'openai-responses':
        value = counter(usage, 'input_tokens')
        if value is not None:
            record['input_tokens'] = value
        details = usage.get('input_tokens_details')
        if details is not None and not isinstance(details, dict):
            raise ValueError('Détails de consommation OpenAI invalides.')
        if details:
            for source, target in [('cached_tokens', 'cache_read_tokens'), ('cache_write_tokens', 'cache_write_tokens')]:
                value = counter(details, source)
                if value is not None:
                    record[target] = value
    elif kind == 'anthropic-messages':
        ordinary = counter(usage, 'input_tokens')
        read = counter(usage, 'cache_read_input_tokens')
        write = counter(usage, 'cache_creation_input_tokens')
        if read is not None:
            record['cache_read_tokens'] = read
        if write is not None:
            record['cache_write_tokens'] = write
        if all(x is not None for x in (ordinary, read, write)):
            total = ordinary + read + write
            if total > 10**15:
                raise ValueError('Total de consommation hors limites.')
            record['input_tokens'] = total
            derived = True
    else:
        raise ValueError('Format de réponse API inconnu.')
    if 'input_tokens' in record and record.get('cache_read_tokens', 0) > record['input_tokens']:
        raise ValueError('Cache lu supérieur aux tokens d’entrée déclarés.')
    return [record], derived
