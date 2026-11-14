# Instructions de travail pour les agents dans Vibe Coding Reference

- Ce dépôt vise un **outil local-first** simple pour START, RESCUE, IMPROVE et TOKEN EFFICIENCY ; Codex/Claude restent les agents existants, ne pas construire de nouvel agent/LLM.
- Commencer par `README_START_HERE.md`, puis les seuls documents utiles au lot en cours. La référence longue `reference/RESEARCH_AND_DESIGN_v0.2.md` est **consultative**, pas à relire intégralement par défaut.
- Lire `plans/03_BACKLOG_ET_LIVRAISON.md` pour les lots, leurs critères de réussite et tests fonctionnels.
- Pour une recherche, consulter l'index `research/README.md` et les seules notes pertinentes ; consigner les nouveaux résultats, options, avantages, inconvénients, sources et incertitudes dans une note datée, puis actualiser l'index.
- Les audits de dépôts tiers sont non destructifs. Aucun secret dans les sorties ; aucun réseau, installation, exécution de scripts de la cible, migration, suppression, commit, push ou déploiement sans autorisation.
- Résultats vérifiables : distinguer `confirmed`, `suspected`, `not_checked`, `not_applicable`, citer chemins/lignes/commandes réels, exposer limites et risques.
- Préférer un monolithe Python simple et les dépendances minimales ; pas de RAG, graphe multi-agent, service web ou skills tiers automatiques.
- Tests fonctionnels sur fixtures requis ; **pas** de benchmarks maison de performance/tokens. Ne jamais promettre d'économies à partir d'une étude tierce sans contexte.
- Ne pas fabriquer de problèmes ni de métriques pour compléter un rapport ; respecter les règles métier et les modifications Git existantes.
- À la fin d'un lot : mettre à jour `docs/IMPLEMENTATION_STATUS.md` avec commandes/tests réellement exécutés, limites et prochain lot. Si le fichier manque, le créer court.
