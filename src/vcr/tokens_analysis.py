"""Calculs bornés sur des mesures déclarées, sans estimation de quota."""
from collections import defaultdict
from decimal import Decimal, localcontext

from .tokens_trace import METRICS


def unavailable(reason):
    return {'status': 'unavailable', 'value': None, 'reason': reason}


def measure(records, field):
    present = sum(field in r for r in records)
    if not records or present != len(records):
        return unavailable(f'Champ présent dans {present} enregistrements sur {len(records)} ; total non calculable.')
    return {'status': 'measured', 'value': sum(r[field] for r in records), 'reason': 'Somme des valeurs déclarées pour chaque enregistrement, non vérifiées indépendamment.'}


def cost_measure(records):
    if not records or any('cost' not in r for r in records):
        return unavailable('Coût absent pour au moins un enregistrement, ou aucune trace.')
    costs = [r['cost'] for r in records]
    if len({c['currency'] for c in costs}) != 1 or len({c['kind'] for c in costs}) != 1:
        return unavailable('Devises ou natures de coûts mélangées ; aucun total calculé.')
    with localcontext() as context:
        context.prec = 50
        total = sum((Decimal(c['amount']) for c in costs), Decimal(0))
    return {'status': 'measured' if costs[0]['kind'] == 'actual' else 'estimated', 'value': str(total), 'currency': costs[0]['currency'], 'reason': 'Montants déclarés par l’import, non vérifiés sur une facture ; aucun tarif externe appliqué.', 'references': [{'record': i, 'date': c['date']} for i, c in enumerate(costs, 1)][:10]}


def analyse(records=None):
    supplied = records is not None
    records = records or []
    metrics = {field: measure(records, field) for field in METRICS}
    input_total, output_total, cache = (metrics[x] for x in ('input_tokens', 'output_tokens', 'cache_read_tokens'))
    if input_total['status'] == output_total['status'] == 'measured':
        total = {'status': 'estimated', 'value': input_total['value'] + output_total['value'], 'reason': 'Addition des compteurs déclarés ; valeur calculée, pas quantité de contexte unique.'}
    else:
        total = unavailable('Entrées ou sorties incomplètes : somme totale non calculable.')
    if input_total['status'] == cache['status'] == 'measured' and all(r['cache_read_tokens'] <= r['input_tokens'] for r in records):
        uncached = {'status': 'estimated', 'value': input_total['value'] - cache['value'], 'reason': 'Différence calculée avec cache_read inclus dans input ; peut inclure les écritures de cache.'}
    else:
        uncached = unavailable('Entrées ou cache lu incomplets : différence non calculable.')
    metrics['volume_total_tokens'] = total
    metrics['uncached_input_tokens'] = uncached
    metrics['cost_declared'] = cost_measure(records)
    metrics['subscription_quota'] = unavailable('Aucun quota d’abonnement déduit des traces ou coûts API.')
    metrics['success_per_cost'] = unavailable('Résultat correct et coût complet non établis par ce format.')

    tools, searches, topics, long_commands = defaultdict(list), defaultdict(list), set(), []
    for i, record in enumerate(records, 1):
        if 'tool' in record:
            tools[record['tool']].append(i)
        if 'session_id' in record and 'search_fingerprint' in record:
            searches[(record['session_id'], record['search_fingerprint'])].append(i)
        if 'session_id' in record and record.get('topic_count', 0) > 1:
            topics.add(record['session_id'])
        if record.get('command_chars', 0) >= 1000:
            long_commands.append(i)
    tool_groups = sorted(tools.values(), key=lambda v: (len(v), v[0]))
    repeated = [v for v in searches.values() if len(v) > 1]
    signals = {
        'tools': [{'occurrences': len(v), 'record_refs': v[:10]} for v in tool_groups[:10]],
        'tools_coverage': sum('tool' in r for r in records),
        'repeated_searches': [{'occurrences': len(v), 'record_refs': v[:10]} for v in repeated[:10]],
        'search_coverage': sum('session_id' in r and 'search_fingerprint' in r for r in records),
        'multi_topic_sessions': len(topics) if any('session_id' in r and 'topic_count' in r for r in records) else None,
        'topic_coverage': sum('session_id' in r and 'topic_count' in r for r in records),
        'long_command_records': long_commands[:10],
        'long_command_count': len(long_commands) if any('command_chars' in r for r in records) else None,
        'command_coverage': sum('command_chars' in r for r in records),
    }
    return {'trace_supplied': supplied, 'record_count': len(records) if supplied else None, 'metrics': metrics, 'signals': signals}
