# Vibe Coding Reference — prototype local

RESCUE inspecte passivement un dossier et produit un rapport en français, un fichier JSON et un prompt de revue. Il ne lance aucun test du projet, ne contacte aucun service et ne modifie pas le projet analysé. Python 3.11 ou supérieur est requis. Les autres modes ne sont pas encore disponibles.

> **Prototype en cours de développement.** L'analyse est partielle et ne remplace ni les tests du projet ni une revue de sécurité.

**English:** VCR is a local-first prototype for passive repository inspection. Its RESCUE workflow generates JSON and French Markdown reports without running project scripts or using an API. Other workflows are planned, not yet implemented.

Les recherches et décisions sont conservées dans les [notes destinées aux agents](research/README.md), avec leurs sources et limites.

## Démarrage sans installation

Dans ce dossier, sur macOS ou Linux :

```sh
export PYTHONPATH="$PWD/src"
python3 -m vcr --help
python3 -m vcr
python3 -m vcr rescue --repo "/chemin/du/projet" --out "/chemin/vers/nouveau-rapport"
```

Sous Windows PowerShell, remplacer la première ligne par `$env:PYTHONPATH = "$PWD/src"` et utiliser `python` si nécessaire. Il est aussi possible d'installer le paquet localement avec `python -m pip install --no-build-isolation -e .` si `pip` et les outils de construction sont déjà disponibles ; cette installation n'a pas été vérifiée dans cette session. Aucun téléchargement n'est nécessaire pour l'utilisation avec `PYTHONPATH`.

Le dossier `--out` doit être nouveau, extérieur au projet, et ne pas contenir le projet. Ouvrir `report.md` ; `run.json` contient les mêmes constats structurés et `ASK_CODEX_TO_REVIEW.md` un prompt facultatif. Pour supprimer l'outil utilisé sans installation, supprimer son dossier et les rapports créés séparément. Si le paquet a été installé, utiliser aussi `python -m pip uninstall vibe-coding-reference`.

## Ce qui est examiné

Inventaire limité, filtres de dossiers, règles Git ignore lorsque Git fonctionne, statut et HEAD Git, manifestes courants, indices de scripts test/lint/build, noms de documentation d'architecture et fichiers `.env` non exclus. Les commandes et valeurs de manifestes ne sont pas recopiées. Les fichiers `.env` ne sont jamais lus ; leur présence n'établit pas qu'un secret existe. Les fichiers ignorés ne sont pas inspectés. Les dépendances sont comptées partiellement, sans analyse de vulnérabilités.

Un constat `confirmed` correspond à un fait observé ; `suspected` demande vérification. Les contrôles `not_checked` n'ont pas été établis ; `not_applicable` signifie non applicable. L'absence d'alerte ne prouve ni sécurité ni bon fonctionnement. Le verdict reste inconclusif. L'analyse ne couvre ni le métier ni l'exécution. Les noms et chemins du dossier ciblé, le hash Git et les observations figurent dans les rapports : vérifiez-les avant partage. Ne copiez pas de données sensibles dans un agent sans les examiner.

L'inventaire exclut les liens symboliques et les fichiers de plus de 1 Mio ; il est limité à 10 000 fichiers. Un dépôt modifié simultanément peut changer pendant l'analyse : ne pas auditer une arborescence contrôlée activement par un tiers hostile. Les erreurs de lecture et les règles Git non disponibles sont indiquées. Les règles de fichiers ignorés ne sont pas évaluées hors Git ; plusieurs manifestes sont relevés, sans interprétation complète des monorepos.

## Tests locaux

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Les tests créent des projets artificiels temporaires et ne nécessitent ni réseau ni données privées. `pytest` est proposé en dépendance de développement facultative, mais n'est pas nécessaire à cette commande. Voir [l'état d'avancement](docs/IMPLEMENTATION_STATUS.md) pour les cas couverts et les limites.

## Licence

Ce projet est distribué sous [licence MIT](LICENSE).
