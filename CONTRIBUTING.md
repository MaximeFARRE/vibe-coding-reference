# Contribuer à Vibe Coding Reference

Merci de votre intérêt ! Les rapports de bugs, retours d'utilisation, corrections de documentation, traductions et tests sont bienvenus, en français ou en anglais. VCR est un prototype maintenu selon les disponibilités des mainteneurs ; aucun délai de réponse n'est garanti.

## Avant de commencer

- Cherchez une issue existante. Pour une modification importante, ouvrez une issue pour discuter du besoin et du périmètre avant d'écrire le code.
- Ne publiez jamais de secrets, données personnelles, rapports privés ou historiques de session. Pour un problème de sécurité, consultez [SECURITY.md](SECURITY.md).
- Utilisez des projets fictifs et des données artificielles pour les reproductions et les tests.
- Consultez [AGENTS.md](AGENTS.md) pour les règles du projet et [l'état du prototype](docs/IMPLEMENTATION_STATUS.md) pour les limites connues.

## Préparer et vérifier une modification

Python 3.11 ou supérieur et Git sont nécessaires. Depuis un clone du dépôt :

```sh
git switch -c fix/description-courte
export PYTHONPATH="$PWD/src"
python3 -m vcr --help
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

Sur PowerShell, utilisez `$env:PYTHONPATH = "$PWD/src"` et `python` si nécessaire. Ce parcours Windows n'a pas encore été vérifié. Les tests utilisent des fixtures et ne nécessitent ni clé API ni réseau. Il n'est pas nécessaire d'installer les dépendances de développement pour cette commande.

Gardez les modifications ciblées et ajoutez des tests fonctionnels pertinents pour tout comportement modifié. Les changements de documentation doivent être vérifiés, notamment les commandes et liens. VCR ne lance pas les scripts d'un projet audité, ne modifie pas sa cible et ne contacte pas de service pendant son utilisation. Les propositions restent soumises à un humain ; les faits observés et les limites doivent rester distincts. Aucun benchmark maison de tokens ou de performance n'est demandé.

## Proposer le changement

1. Créez une branche et ouvrez une pull request vers `main` depuis votre fork ou votre branche autorisée.
2. Décrivez le problème, la solution, les commandes exécutées et les limites ; utilisez le modèle proposé.
3. Attendez la revue et les vérifications CI. Une discussion peut conduire à une autre approche ou à ne pas accepter le changement.

Pour un bug, indiquez les versions de VCR, Python et du système, les étapes sur une fixture minimale et les résultats observés et attendus. Les instructions pour les agents ne remplacent pas le jugement humain ni les règles de contribution.
