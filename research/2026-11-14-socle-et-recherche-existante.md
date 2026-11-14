# Socle et recherche existante

- Date : 2026-11-14 ; statut : ouvert.
- Question : où retrouver les décisions, les preuves et les limites antérieures à ce répertoire de notes ?
- Périmètre : références existantes du projet ; pas de nouvelle revue indépendante des publications.

## Résultats et références

- **Confirmé dans les documents** : les parcours visés sont START, RESCUE, IMPROVE et TOKEN EFFICIENCY ; RESCUE est prioritaire. Sources : [vision](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/docs/01_VISION_ET_DECISIONS.md), [backlog](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/plans/03_BACKLOG_ET_LIVRAISON.md).
- **État documenté** : le prototype RESCUE est partiel ; 8 tests sur fixtures ont été exécutés lors de sa réalisation. La couverture et les limites figurent dans [l'état d'implémentation](../docs/IMPLEMENTATION_STATUS.md). Ce constat n'établit pas l'état d'une version future.
- **Recherche existante, non revérifiée ici** : la [revue critique](../docs/04_RECHERCHE_ET_SOURCES.md) recense publications, limites et sources ; la [revue des outils](../docs/05_PROJETS_EXTERNES_ET_SKILLS.md) documente options et risques. Référence historique détaillée : [v0.2](../reference/RESEARCH_AND_DESIGN_v0.2.md). Vérifier la source primaire et son actualité avant de reprendre une affirmation.
- **Décision documentée** : monolithe Python local et dépendances minimales ; aucun LLM ajouté, service web ou intégration avancée imposée. Source : [architecture](https://github.com/MaximeFARRE/vibe-coding-reference/blob/c8d94cb14c27270f430277034d4b280431001d3f/docs/02_ARCHITECTURE_ET_CONTRATS.md), sections 1–3.

## Options de conservation

- Markdown indexé et recherche textuelle : simple à modifier, lire et versionner ; l'index doit être entretenu et la recherche dépend des termes employés.
- Base structurée ou index vectoriel : recherches potentiellement plus sophistiquées ; infrastructure, synchronisation et maintenance supplémentaires. Besoin non démontré à ce stade.
- Décision : Markdown concis avec références, sans recopie massive. Réévaluer si des recherches réelles ne retrouvent plus les éléments pertinents.

## Incertitudes et suite

- Les sources externes historiques et leur applicabilité actuelle ne sont pas vérifiées par cette note.
- Les notes futures doivent distinguer résultats observés, hypothèses et conclusions attribuées, et décrire les options rejetées lorsqu'elles ont été réellement examinées.
