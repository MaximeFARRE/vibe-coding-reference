# Notes de recherche — index pour agents

Objectif : conserver les résultats, sources, options, avantages, inconvénients et questions ouvertes du projet. Notes courtes en Markdown, une question ou décision par fichier ; pas de base de données ni de format à parser obligatoirement.

## Utilisation

- Chercher dans cet index puis avec `rg 'mot-clé' research docs reference` ; lire uniquement les notes utiles au sujet.
- Ajouter une note `AAAA-MM-JJ-sujet.md` lorsqu'une recherche produit un résultat ou une décision. Mettre à jour l'index ci-dessous dans le même changement.
- Consigner aussi les résultats négatifs, désaccords, options écartées, raisons et questions non résolues ; ne pas inventer de résultat pour remplir le modèle.
- Sources : chemin et emplacement vérifiable pour le local ; URL exacte, auteur/version/date et limites pour l'externe lorsqu'ils sont disponibles. Distinguer observation directe, conclusion de source, hypothèse et décision ; préciser ce qui n'a pas été vérifié. Ne pas faire passer une source historique pour une vérification actuelle.
- Mettre à jour une note si une preuve évolue, en conservant les conclusions précédentes et la date de correction. Indiquer si une décision est remplacée et par laquelle.
- Aucun secret, donnée personnelle, extrait sensible ou historique privé. Ne pas dupliquer intégralement les documents sources ; les lier.
- Les études externes ne prouvent pas de gains propres à VCR ; aucun benchmark maison de performance/tokens.

## Modèle minimal

```markdown
# Sujet
- Date : AAAA-MM-JJ ; mise à jour : AAAA-MM-JJ
- Statut : ouvert | décidé | remplacé
- Question / périmètre : ...
- Sources et preuves : [référence précise, date ou commande] ...
- Résultats : [confirmé | suspecté | non vérifié | non applicable] ...
- Options : option A — avantages / inconvénients / limites ; option B — ...
- Décision / justification : ... ou « aucune »
- Incertitudes / prochaine vérification : ...
```

## Index

| Sujet | Note | État |
|---|---|---|
| Base existante, architecture et limites du prototype | [2026-11-14-socle-et-recherche-existante.md](2026-11-14-socle-et-recherche-existante.md) | Ouvert |
| Preuves, rapport et décisions utilisateur | [2026-11-14-rapport-et-preuves.md](2026-11-14-rapport-et-preuves.md) | Décidé (lot 2) |
| Questionnaire START et choix de stack | [2026-11-14-start-guide.md](2026-11-14-start-guide.md) | Décidé (lot 3) |
| IMPROVE : observations et registre | [2026-11-14-improve-preuves.md](2026-11-14-improve-preuves.md) | Décidé (lot 4) |
| TOKENS : diagnostic et import volontaire | [2026-11-14-tokens-diagnostic.md](2026-11-14-tokens-diagnostic.md) | Décidé (lot 5) |
| Catalogue : liens et maintenance | [2026-11-14-catalogue-sources.md](2026-11-14-catalogue-sources.md) | Décidé (lot 6) |
| Épreuve fonctionnelle et CI | [2026-11-14-epreuve-fonctionnelle.md](2026-11-14-epreuve-fonctionnelle.md) | Décidé (lot 7) |
