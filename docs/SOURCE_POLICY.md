# Politique des sources

Le catalogue est une sélection locale de pistes, pas une recommandation d'installation ni une preuve de sécurité ou de gain. VCR reste hors ligne par défaut.

- Privilégier la source primaire : dépôt ou documentation officielle pour les capacités et permissions, publication originale pour les résultats de recherche. Conserver l'URL, l'auteur ou mainteneur, la date de consultation et la version ou le commit lorsqu'ils sont connus.
- Distinguer un lien ouvert, une métadonnée d'activité constatée et une affirmation de performance vérifiée. Un dépôt non archivé ou une date de push ne garantit ni maintenance effective, ni compatibilité, ni fiabilité.
- Conserver les limites du protocole, la date et les conditions d'application d'une étude ; ne pas transformer un résultat publié en gain promis pour VCR ou pour un utilisateur.
- Identifier séparément licence, composants, permissions, accès réseau, stockage, coûts possibles, version compatible et procédure de retrait. Si une information manque, la noter `unverified` ou non renseignée ; ne pas la déduire d'une popularité ou d'un README.
- Pour passer un statut à `verified`, conserver une source précise et une date dans le catalogue. Réexaminer les informations avant utilisation : les liens, licences, versions et mainteneurs peuvent évoluer.
- Les niveaux A/B/C indiquent une complexité d'adoption indicative, séparée de la qualité des preuves. Aucune entrée n'est installée ou recommandée automatiquement.
- Pour toute expérimentation : inspection préalable du code, des permissions et de la licence ; environnement fictif isolé, sauvegarde et retour arrière ; accord humain pour les actions non autorisées par le projet.

Les fiches et leurs limites actuelles sont accessibles avec `python -m vcr sources` et conservées dans `src/vcr/catalog.json` ; leur modification doit s'accompagner de tests et d'une note de recherche si elle découle d'une nouvelle étude.
