# START : cadrage et recommandations conditionnelles

- Date : 2026-11-14 ; statut : décidé pour le lot 3.
- Question : transformer une idée en documents exploitables sans nouvel agent ni installation.
- Sources : [backlog lot 3](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md), [playbook START](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/docs/06_PLAYBOOKS_ET_AUDITS.md), [questionnaire](../src/vcr/start_questions.py), [options](../src/vcr/start_options.py), [tests](../tests/test_start.py) et [cas de stack](../tests/test_start_options.py).

## Résultats et limites

- **Confirmé sur fixtures** : les réponses sont réutilisées sans répétition ; les champs manquants sont demandés ; action et résultat fournis apparaissent dans les critères ; six profils produisent des options conditionnelles avec avantages, inconvénients et coûts qualitatifs.
- **Confirmé sur fixtures** : contradictions local/public et site avec données sensibles ou persistantes signalées ; un dossier existant n'est pas écrasé.
- **Limite** : les options sont des règles indicatives, pas une étude comparative ni une garantie de pertinence ; les besoins, coûts et critères exigent une validation humaine. Les réponses sont enregistrées en clair, sans détecteur de secrets.
- **Non vérifié** : Windows et utilisabilité par une personne extérieure au projet.

## Options et décision

- Questionnaire déterministe et Markdown : local, inspectable, réutilisable ; formulation et règles limitées aux cas prévus.
- Modèle externe : interprétation potentiellement plus riche ; dépendance, coût et traitement de données supplémentaires. Non retenu, conformément au périmètre local sans nouvel agent.
- Décision : réponses versionnées en JSON, documents Markdown, prompt facultatif pour un agent déjà choisi. Les réponses manquantes sont explicitées plutôt que déduites.
