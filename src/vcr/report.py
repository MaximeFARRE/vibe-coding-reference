"""Rendu des mêmes constats normalisés que le rapport JSON."""
from urllib.parse import quote


DECISIONS = {
    'git-dirty': ('Des modifications préexistantes pourraient être écrasées lors d’une correction.', 'Examiner les changements avec leur propriétaire.', 'Reporter toute modification jusqu’à clarification.', 'Une mauvaise manipulation peut perdre du travail.', 'Les changements et données existants.', 'Vérifier le statut Git avant et après toute intervention.'),
    'tests-unknown': ('Sans tests identifiés, une régression pourrait être difficile à détecter.', 'Rechercher les tests et leur documentation.', 'Définir avec le propriétaire un test métier ciblé si aucun test adapté n’existe.', 'Un test incomplet peut donner une confiance excessive.', 'Les comportements métier existants.', 'Faire valider la commande et son périmètre avant exécution.'),
    'architecture-doc': ('La navigation dans le projet peut demander plus de recherche.', 'Chercher une documentation existante sous un autre nom.', 'Proposer une courte carte des composants si elle manque réellement.', 'Une carte non maintenue peut devenir trompeuse.', 'La documentation et les conventions existantes.', 'Faire relire les liens et descriptions par le propriétaire.'),
    'env-present': ('Une exposition de configuration pourrait être sensible, sans preuve de secret ici.', 'Vérifier localement le suivi Git et les permissions sans divulguer les valeurs.', 'Demander au propriétaire de vérifier le fichier et sa gestion.', 'Modifier une configuration peut interrompre l’application.', 'Les valeurs, accès et comportements existants.', 'Contrôler localement sans recopier ni transmettre les valeurs.'),
}


def render(run):
    lines = ['# Rapport RESCUE', '', '**Verdict : inconclusif.** Cette inspection ne démontre ni qualité générale ni sécurité.', '', 'Profils détectés : ' + ', '.join(run.profile), '', '## Choisir une observation', '', 'Priorité indicative : considérer ensemble impact possible, confiance et facilité de revenir en arrière. Aucun score automatique ; les éléments ci-dessous ne sont pas classés par importance.']
    if not run.findings:
        lines += ['', 'Aucun constat dans le périmètre limité de ces contrôles.']
    for f in run.findings:
        default = ('Impact à déterminer.', 'Confirmer la preuve et consulter le propriétaire.', 'Différer la décision en attendant une preuve suffisante.', 'Risques de correction à déterminer.', 'Préserver les données et comportements existants.', 'Définir une vérification adaptée avant toute modification.')
        impact, a, b, risk, preserve, verify = DECISIONS.get(f.id, default)
        impact = f.impact or impact
        a = f.recommendations[0] if f.recommendations else a
        b = f.alternatives[0] if f.alternatives else b
        risk = '; '.join(f.risks_of_fix) or risk
        preserve = '; '.join(f.invariants_to_preserve) or preserve
        verify = '; '.join(f.verification_plan) or verify
        lines += ['', f'### {f.title} — `{f.id}`', f'**Statut :** {f.status} ; **confiance :** {f.confidence} ; **origine :** {f.origin} ; **gravité :** {f.severity}.', '', '**Problème :** ' + f.summary, '', '**Preuves :**']
        if not f.evidence:
            lines.append('- Aucune preuve localisable fournie.')
        for e in f.evidence:
            location = ''
            if e.path:
                label = e.path + (f':{e.line_start}' if e.line_start else '')
                # Un lien local reste relatif au dépôt cible ; il ne transmet rien au réseau.
                url = (run.target['path'].rstrip('/') + '/' + e.path)
                location = f' [{label}]({quote(url, safe="/:")})'
                if e.line_start:
                    location += f' (ligne {e.line_start}' + (f' à {e.line_end}' if e.line_end else '') + ')'
            if e.command:
                location += f' Commande : `{e.command}` (code {e.exit_code}).'
            lines.append('- ' + e.summary + location)
        lines += ['', '**Impact possible :** ' + impact, '', '**Solution A :** ' + a, '', '**Solution B :** ' + b, '', '**Coût / risque :** ' + risk, '', '**À préserver :** ' + preserve, '', '**Comment vérifier :** ' + verify, '', '**Approbation humaine :** nécessaire avant toute modification ou exécution de commande du projet.']
        if f.limitations:
            lines += ['', '**Limites :** ' + ' '.join(f.limitations)]
        lines += ['', '**Ordre de revue à copier :**', '', '```text', f'Examine le constat {f.id} dans le rapport RESCUE. Confirme ses preuves et ses limites ; propose une solution et une alternative en préservant les données et le métier. Ne modifie rien et ne lance aucune commande du projet sans mon accord.', '```']
    lines += ['', '## Vérifications et limites']
    lines += [f'- **{c.id} — {c.status}** : {c.reason}' for c in run.checks]
    lines += ['', '## Non vérifié et prudence'] + ['- ' + x for x in run.limitations]
    lines += ['', 'Vous pouvez retenir, rejeter, différer ou marquer un constat comme faux positif avec la commande `feedback` (voir README).']
    return '\n'.join(lines) + '\n'
