# État du prototype

Dernier lot : 4, IMPROVE supervisé opérationnel sur les sources et règles ci-dessous. Branche locale `feat/initial-publication` ; les notes de recherche et les lots 2–4 ne sont pas poussés. Python 3.12.9 sur macOS ; `pytest` absent, tests `unittest` sans dépendance. Installation editable et Windows non vérifiés.

Fonctionnalités : START génère un cadrage et des options conditionnelles à partir de réponses réutilisables. RESCUE produit des rapports passifs et des décisions hors cible. IMPROVE accepte des rapports RESCUE d'un même projet, des notes/logs explicitement fournis avec marqueurs, ou un registre antérieur ; il conserve les observations et décisions hors cible et propose des pistes après deux sources distinctes. Aucun changement ou test n'est appliqué à la cible.

Vérification exécutée : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` : 35 tests réussis. Démonstration locale sur fixture temporaire : deux commandes `rescue`, puis `improve --project ... --from ... --from ... --out ...`, puis `improve-feedback ... --decision deferred` ; deux références, décision enregistrée et cible intacte vérifiées. Les tests couvrent une seule source, deux constats confirmés déclarés, registres repris, doublons, rejets/faux positifs, notes/logs et absence de modification de la cible. Pas de données personnelles ni benchmark de performance/tokens.

Limites IMPROVE : seules les règles explicites sont reconnues ; le texte libre sans marqueur n'est pas interprété. Les preuves et statuts des sources sont déclaratifs, sans vérification indépendante ; deux observations ne prouvent ni deux incidents ni une cause commune. Les chemins des sources apparaissent dans les sorties. Les retours RESCUE sont synchronisés seulement lors de la réimportation du rapport ; le Markdown doit être régénéré après une décision sur le registre. Le fonctionnement face aux modifications concurrentes hostiles n'est pas garanti.

Limites existantes : START conserve les réponses en clair et propose des choix indicatifs à confirmer ; RESCUE vérifie partiellement les schémas, ne lit pas les contenus `.env` et couvre partiellement les monorepos. Pas de validation d'ergonomie externe, HTML ni tri automatique.

Cas du backlog : T001–T008, T010–T014 couverts ; T007 simulé et T013 testé seulement sur macOS avec espaces. T009 attend TOKENS, T015 attend le catalogue. Prochain lot : TOKEN EFFICIENCY (lot 5), puis catalogue et épreuve de vérité. Licence MIT choisie par le propriétaire.
