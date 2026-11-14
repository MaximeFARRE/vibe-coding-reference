"""Diagnostic descriptif et rendu local sans contenu de trace."""
import json
from pathlib import Path

LABELS = {
    'input_tokens': 'Entrées cumulées déclarées', 'output_tokens': 'Sorties cumulées déclarées',
    'cache_read_tokens': 'Entrées lues depuis le cache déclarées', 'cache_write_tokens': 'Écritures de cache déclarées',
    'volume_total_tokens': 'Somme entrées + sorties', 'uncached_input_tokens': 'Entrées hors cache lu',
    'cost_declared': 'Coût déclaré', 'subscription_quota': 'Quota d’abonnement', 'success_per_cost': 'Succès par coût',
}
IMMEDIATE = [
    'Délimiter une session par objectif et conserver une courte note de passation lorsque le contexte change.',
    'Rechercher les fichiers et passages pertinents avant de charger une documentation entière, sans omettre les dépendances utiles.',
    'Privilégier des sorties ciblées tout en conservant erreurs, preuves et détails nécessaires à la vérification.',
]


def render(data):
    lines = ['# TOKEN EFFICIENCY — diagnostic local', '', 'Ce diagnostic ne mesure pas à lui seul la réussite, le quota ou des gains. Les compteurs importés sont déclarés par la source et non vérifiés indépendamment.']
    if not data['trace_supplied']:
        lines += ['', '**Aucune trace fournie :** diagnostic descriptif, sans mesure de consommation ni surveillance implicite.']
    else:
        lines += ['', f"**Trace sélectionnée :** format {data['source_format']}, {data['record_count']} enregistrements. Chaque compteur représente une réponse choisie selon le format indiqué ; une somme cumulée ne correspond pas nécessairement à un contexte unique."]
    lines += ['', '## Checklist — questions à examiner', '- [ ] Les recherches et lectures sont-elles ciblées sur le besoin ?', '- [ ] Les sorties d’outils gardent-elles les preuves et erreurs utiles ?', '- [ ] La session mélange-t-elle des sujets ou des boucles d’échec ?', '- [ ] Les outils activés et les paliers de tests sont-ils adaptés au travail ?']
    lines += ['', '## Trois recommandations immédiates'] + [f'{i}. {x}' for i, x in enumerate(IMMEDIATE, 1)]
    lines += ['', '## Mesures disponibles']
    for key, label in LABELS.items():
        item = data['metrics'][key]
        value = '' if item['value'] is None else f" : {item['value']}" + (f" {item['currency']}" if 'currency' in item else '')
        lines.append(f"- **{label} — {item['status']}**{value}. {item['reason']}")
    cost = data['metrics']['cost_declared']
    if 'references' in cost:
        refs = ', '.join(f"enregistrement {r['record']} (date {r['date']})" for r in cost['references'])
        lines.append('- Provenance des montants : ' + refs + ' ; fournisseur déclaré dans le champ `cost.provider` de chaque enregistrement cité (non recopié). Dix références au plus.')
    s = data['signals']
    conditional = []
    lines += ['', '## Indices de la trace']
    if data['trace_supplied']:
        if s['search_coverage']:
            lines.append(f"- Recherches identiques déclarées : {len(s['repeated_searches'])} groupes affichés au maximum ; couverture {s['search_coverage']}/{data['record_count']} enregistrements. Références dans `tokens.json` ; contenu non reproduit.")
            if s['repeated_searches']:
                conditional.append('Si ces recherches concernent le même besoin, examiner pourquoi elles se répètent avant de modifier le workflow.')
        if s['topic_coverage']:
            lines.append(f"- Sessions déclarées multi-sujets observées : {s['multi_topic_sessions']} ; couverture {s['topic_coverage']}/{data['record_count']} enregistrements.")
            if s['multi_topic_sessions']:
                conditional.append('Si les sujets sont indépendants, envisager des sessions distinctes avec une passation concise.')
        if s['command_coverage']:
            lines.append(f"- Commandes déclarées d’au moins 1 000 caractères : {s['long_command_count']} ; couverture {s['command_coverage']}/{data['record_count']}. Seuil descriptif, pas une preuve de gaspillage ; contenu non reproduit.")
            if s['long_command_count']:
                conditional.append('Si une commande longue est répétée ou produit trop de sortie, vérifier si une forme ciblée conserve les preuves nécessaires.')
        if s['tools_coverage']:
            lines.append(f"- Outils : {len(s['tools'])} groupes anonymisés affichés au maximum ; couverture {s['tools_coverage']}/{data['record_count']}. Une faible fréquence ne prouve pas qu’un outil est inutile.")
            if any(x['occurrences'] == 1 for x in s['tools']):
                conditional.append('Si un outil apparaît peu, vérifier son utilité et ses usages hors trace avant toute désactivation réversible.')
        if s['search_coverage'] == s['topic_coverage'] == s['command_coverage'] == s['tools_coverage'] == 0:
            lines.append('- Aucun indice d’outil, recherche, session multi-sujets ou longueur de commande n’est fourni.')
        if data['metrics']['cache_read_tokens']['status'] == 'measured' and data['metrics']['cache_read_tokens']['value']:
            conditional.append('Si le volume de cache lu paraît important dans votre contexte, vérifier ses conditions de facturation auprès de la source compétente ; ne pas le compter deux fois.')
    else:
        lines.append('- Sans trace, ces indices sont indisponibles.')
        conditional = ['Si des sorties semblent trop longues, cibler les résultats sans masquer les preuves.', 'Si plusieurs sujets se mélangent, envisager une passation entre sessions.', 'Si des outils semblent inutilisés, vérifier leurs usages avant une désactivation réversible.']
    lines += ['', '## Recommandations conditionnelles (trois maximum)']
    lines += [f'{i}. {x}' for i, x in enumerate(conditional[:3], 1)] if conditional else ['Aucune : les champs disponibles ne justifient pas de recommandation conditionnelle supplémentaire.']
    lines += ['', '## Limites', '- Aucun calcul de quota, tarif forfaitaire, économie financière ou performance de modèle.', '- Les sorties ne contiennent ni noms de modèles/outils/sessions, ni prompts, ni commandes ; les références numériques renvoient aux enregistrements de la trace choisie.', '- Une couverture partielle ne décrit pas les données absentes ; les références et groupes sont limités dans le rendu.']
    return '\n'.join(lines) + '\n'


def write_report(data, output, project=None):
    output = Path(output).expanduser().resolve(strict=False)
    if project is not None:
        root = Path(project).expanduser().resolve(strict=True)
        if not root.is_dir() or output == root or output.is_relative_to(root) or root.is_relative_to(output):
            raise ValueError('La sortie doit être extérieure au dossier de projet.')
    if output.exists():
        raise ValueError('Le dossier de sortie existe déjà ; choisissez un nouveau chemin.')
    output.mkdir(parents=True, exist_ok=False)
    (output / 'tokens.json').write_text(json.dumps(data, ensure_ascii=True, indent=2) + '\n', encoding='utf-8')
    (output / 'report.md').write_text(render(data), encoding='utf-8')
    (output / 'ASK_CODEX_TO_REVIEW.md').write_text('# Revue TOKEN EFFICIENCY\n\nLis `report.md` et `tokens.json`. Distingue données déclarées, calculs et éléments indisponibles. Confirme les références dans la trace volontairement fournie si nécessaire, sans recopier de secret. Ne déduis ni quota ni économies financières ; ne modifie aucun projet ni configuration sans accord.\n', encoding='utf-8')
    return output
