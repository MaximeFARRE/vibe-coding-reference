# IMPROVE : récurrence et registre supervisé

- Date : 2026-11-14 ; statut : décidé pour le lot 4.
- Question : proposer des améliorations à partir de sources choisies sans inventer une récurrence ni modifier le projet.
- Sources : [backlog lot 4](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [collecte](../src/vcr/improve_sources.py), [registre](../src/vcr/improve_registry.py), [tests rapports](../tests/test_improve.py), [tests notes](../tests/test_improve_notes.py).

## Résultats

- **Confirmé sur fixtures** : deux rapports RESCUE d'un même projet avec la même règle produisent une proposition et deux références ; une source isolée reste à surveiller. Un même `run_id` ou un texte copié ne crée pas de deuxième occurrence.
- **Confirmé sur fixtures** : les choix humains persistent à la reprise ; un faux positif RESCUE est retiré du registre lors de la réimportation de son rapport. Les sources texte sans marqueur explicite ne sont pas interprétées ni recopiées.
- **Limite** : deux observations peuvent refléter un seul état persistant, sans incident répété ni cause commune. Les statuts et preuves sont déclarés par les sources fournies et ne sont pas confirmés indépendamment.
- **Non vérifié** : analyse sémantique des journaux ou instructions ; compatibilité Windows ; ergonomie auprès d'une personne extérieure.

## Options et décision

- Règles explicites et marqueurs texte : simples et inspectables ; reconnaissance limitée, marquage manuel nécessaire pour notes et logs.
- Analyse sémantique automatique des sources : interprétation potentiellement plus riche ; risque de conclusions inventées, données sensibles et dépendance supplémentaire. Non retenue dans ce prototype sans modèle ajouté.
- Décision : seules les sources sélectionnées sont utilisées ; registre horodaté extérieur à la cible, propositions réversibles à valider humainement et aucune application automatique. Les retours RESCUE ne sont synchronisés qu'à la réimportation de leurs rapports.
