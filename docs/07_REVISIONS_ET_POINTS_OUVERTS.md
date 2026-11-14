# 07 — Changements depuis la v0.2, erreurs corrigées et décisions ouvertes

**Date : 14 novembre 2026.** Ce dossier ne remplace pas rétroactivement les documents v0.1/v0.2 : il les conserve et signale les choix d'implémentation qui ont changé.

## Ce qui a changé depuis la v0.2

| Sujet | v0.2 au 12/11 | Direction prototype du 14/11 |
|---|---|---|
| Type de livrable | référentiel essentiellement documentaire | dépôt documentaire + outil local minimal + rapports et prompts, sans nouveau modèle |
| Parcours | START / RESCUE, domaines transversaux | START / RESCUE / IMPROVE supervisé, TOKEN EFFICIENCY accessible |
| Agent | bibliographie, prompts, procédures | scripts locaux pour produire preuves + agent hôte existant pour interpréter |
| Interface | non décidée | menu CLI et rapports Markdown/JSON ; HTML statique optionnel ; pas de SaaS |
| Harness auto-améliorant | piste émergente | gestion de propositions basées sur incidents ; boucle récursive non activée |
| Graphes/RAG | recherche avancée | interfaces prévues, intégrations au laboratoire seulement, recherche native d'abord |
| Skills | catalogue de compétences externes, sélection | aucune création maison, aucune installation en bloc, fiches versionnées |
| Tokens | domaine transversal, distinction coûts | commande dédiée avec données réellement disponibles et limites explicites |
| Qualité | qualité des tests et validations | schémas, preuves, statut de confirmation, tests de sûreté et fixtures |

## Corrections factuelles importantes

1. **SWE-Skills-Bench :** prendre la **version 2 d'octobre 2026** comme référence courante pour les résultats 98/92/4/2. Les chiffres de la première version de mars ne sont pas interchangeables.
2. **Pas de gain universel de skills :** la compétence officielle ou populaire peut être utile mais non validée expérimentalement ; l'étude de référence est contextuelle.
3. **Tokens ≠ prix ≠ quotas :** une compression peut dégrader la réussite et augmenter le coût. Ne pas convertir un cache read en consommation normale ni inventer une facture d'abonnement.
4. **Graphes/vectoriel :** la littérature ne permet pas de les recommander systématiquement ; une étude de onze harness de production trouve de la recherche de code déterministe sans récupération de code par embeddings dans cet échantillon.
5. **Le papier de la capture « The End of Harness Engineering » :** existence d'un visuel/social post, mais source scientifique primaire non établie par la capture. Ne pas le citer comme une publication vérifiée ou preuve que l'humain est dispensable.
6. **Google Harness² :** véritable dépôt + papier de recherche vérifiés ; les conditions du setup Codex impliquent des précautions de sandbox. Ne pas installer sur le dépôt réel par défaut.
7. **Le cas « Patrimoine » de v0.1 :** exemple historique de RESCUE, pas fixture ni source de code disponible à réutiliser. Ne jamais déduire que le présent dépôt a accès au code réel de l'utilisateur.
8. **Fichier AGENTS.md :** des recherches ont des résultats contradictoires ; conserver uniquement une courte orientation opérationnelle, pas une énorme politique obligatoire.

## Décisions qu'un humain devra confirmer avant publication

- **Licence** du nouveau dépôt open source : MIT ou Apache 2.0, selon responsabilité, redistribution et contributions ; ne pas mélanger des codes externes sans vérifier.
- **Nom public** du projet et slogan ; « Vibe Coding Reference » reste le nom de travail.
- **Plates-formes promises** (macOS/Linux d'abord, Windows si tests disponibles).
- **Éventuelle UI HTML** en plus du terminal ; le choix doit être guidé par la facilité réelle pour le novice.
- **Politique de collecte des traces Codex/Claude** si une importation plus avancée est proposée : consentement, masquage, rétention, effacement.
- **Régime des extensions tierces** : qui est autorisé à recommander/installer et comment isoler leurs permissions.
- **Maintien du catalogue** : rythme de revue et responsables, pour éviter les recommandations périmées.

## Hypothèses qui ne doivent pas devenir des faits dans Codex

- « Monolithe modulaire = architecture optimale pour tous les agents » — non prouvé.
- « Ajouter un second agent relecteur augmente systématiquement la qualité » — dépend du contexte et du coût.
- « Plus d'outils de navigation = moins de tokens » — dépend du succès et du cache.
- « Une PR verte prouve la qualité métier » — non.
- « Une détection de secret par regex est un incident confirmé » — non.
- « Aucun import = code mort » — non.

## Condition de changement du périmètre

Si Codex découvre une option radicalement plus simple ou beaucoup plus puissante, il doit :

1. résumer le problème concret visé ;
2. citer la preuve ou dire qu'il s'agit d'une hypothèse ;
3. comparer coût de mise en place et maintenance avec la solution minimale ;
4. expliquer implications de sécurité et compatibilité ;
5. proposer une bascule réversible et la soumettre à validation humaine.

L'innovation complexe est autorisée, mais jamais **cachée dans le backend simplement parce qu'elle est techniquement intéressante**.
