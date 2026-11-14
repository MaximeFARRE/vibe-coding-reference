# Format de trace TOKENS V1

Le format `vcr-token-trace-v1` ci-dessous est accepté par défaut. Deux imports explicites d'une réponse API individuelle sont également disponibles (voir plus bas) ; aucun historique Codex ou Claude Code n'est lu automatiquement. L'utilisateur choisit volontairement le fichier et doit vérifier la signification de ses données avant toute conversion. Fichier UTF-8, JSON, 4 Mio et 10 000 enregistrements maximum pour VCR ; champs VCR inconnus, valeurs invalides, clés JSON dupliquées et liens symboliques directs refusés.

Chaque élément de `records` représente **une requête distincte**, pas un compteur cumulatif ni un instantané. Ne pas importer plusieurs fois la même requête. Les champs sont optionnels : leur absence signifie « indisponible », jamais zéro. Chaque entier est positif ou nul ; les booleens ne sont pas des entiers. Les totaux ne sont calculés que si tous les enregistrements contiennent le champ nécessaire. Les montants ne sont pas une estimation de quota ni d'économie.

```json
{
  "format": "vcr-token-trace-v1",
  "records": [
    {
      "input_tokens": 1000,
      "output_tokens": 200,
      "cache_read_tokens": 400,
      "cache_write_tokens": 50,
      "model": "modele-fictif",
      "session_id": "session-fictive",
      "tool": "outil-fictif",
      "command_chars": 1200,
      "search_fingerprint": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "topic_count": 2,
      "cost": {
        "amount": 0.001,
        "currency": "EUR",
        "kind": "actual",
        "provider": "source-fictive",
        "date": "2026-11-14"
      }
    }
  ]
}
```

Les nombres et noms ci-dessus sont des **fixtures inventées** pour décrire le format ; aucun tarif n'est fourni ni recommandé.

| Champ | Sens déclaré par l'importateur |
|---|---|
| `input_tokens`, `output_tokens` | Compteurs de la requête, entrée et sortie. La sortie doit déjà inclure tout raisonnement que le fournisseur y compte : VCR ne l'ajoute pas séparément. |
| `cache_read_tokens` | Partie de `input_tokens` lue depuis le cache. Si les deux champs sont présents, la première valeur ne peut dépasser la seconde. |
| `cache_write_tokens` | Compteur d'écriture séparément déclaré ; son inclusion éventuelle dans l'entrée dépend de la source. VCR ne l'ajoute pas à l'entrée ou à la sortie. |
| `model`, `session_id`, `tool` | Identifiants fournis, non recopiés dans les sorties. `tool` décrit l'outil associé à l'enregistrement ; une seule valeur par requête. Sans inventaire complet des outils, une faible fréquence ne démontre pas l'inutilité. |
| `command_chars` | Nombre de caractères d'une commande, pas la commande elle-même. Le seuil d'affichage de 1 000 caractères est descriptif et ne prouve pas de gaspillage. |
| `search_fingerprint` | Empreinte SHA-256 en 64 caractères hexadécimaux minuscules, déjà calculée par l'importateur, sans recherche en clair. Les comparaisons exigent aussi un `session_id`. Ne pas utiliser de données confidentielles pour produire une empreinte partageable. |
| `topic_count` | Nombre de sujets distincts déclaré pour la session associée à cet enregistrement. VCR ne déduit pas les sujets à partir du contenu. |
| `cost` | Objet complet : `amount` numérique, `currency` en trois lettres majuscules, `kind` (`actual` ou `estimated`), `provider` et `date` ISO `AAAA-MM-JJ`. Montants par requête non dupliqués, 18 décimales maximum. Le fournisseur et les montants sont déclaratifs : VCR ne vérifie pas la facture. |

`measured` désigne une somme de compteurs ou un coût réel **déclarés**, pas une mesure indépendante. `estimated` indique ici un calcul dérivé (entrée + sortie ou entrée − cache lu) ou un coût fourni comme estimé. `unavailable` indique qu'une valeur manque ou que les unités/natures de coût ne permettent pas de total fiable. Les devises ne sont jamais converties ; si elles ou les natures diffèrent, aucun total de coût n'est calculé.

Une somme des entrées sur plusieurs requêtes peut inclure plusieurs fois du contexte réutilisé : elle n'est pas le nombre de tokens uniques. Le total entrée + sortie ne doit pas être confondu avec le coût. Cache lu et écriture sont présentés séparément ; l'entrée hors cache lu peut inclure les écritures selon la source. Aucun quota d'abonnement n'est déduit. Aucun prix ni pourcentage de gain n'est calculé.

Les champs libres (`model`, `session_id`, `tool`, `provider`), empreintes et contenus bruts ne sont pas recopiés dans les rapports. Les références `record_refs` utilisent les positions **à partir de 1** dans `records` ; les sorties listent dix références/groupes au plus et indiquent les couvertures partielles. Le code de l'outil ne possède ni collecte automatique, ni télémétrie, ni envoi externe. L'utilisateur reste responsable de sécuriser le fichier importé et de contrôler les sorties avant partage.

## Import volontaire d'une réponse API individuelle

`--format openai-responses` accepte un objet JSON contenant le champ `usage` d'une réponse **Responses API** OpenAI unique. Le compteur `input_tokens` inclut les entrées mises en cache, dont `input_tokens_details.cached_tokens` ; la sortie inclut les éventuels tokens de raisonnement. VCR ne les additionne pas une seconde fois. Si une valeur manque ou vaut `null`, elle reste indisponible. Référence : [OpenAI — observabilité et usage](https://developers.openai.com/api/docs/guides/agents-api/observability) et [OpenAI — prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching).

`--format anthropic-messages` accepte un objet JSON contenant le champ `usage` d'une réponse **Messages API** Anthropic unique. Le total d'entrée est calculé uniquement si les trois champs `input_tokens`, `cache_read_input_tokens` et `cache_creation_input_tokens` sont présents : ils sont distincts selon [Anthropic — prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching). Si l'un manque, le total est indisponible ; le cache observé reste séparé. La somme est indiquée comme calculée (`estimated`), les compteurs source comme déclarés (`measured`).

```sh
python3 -m vcr tokens --format openai-responses --from "/chemin/reponse-openai.json"
python3 -m vcr tokens --format anthropic-messages --from "/chemin/reponse-anthropic.json"
```

Il appartient à l'utilisateur de sélectionner **une seule réponse** de l'API indiquée, pas une synthèse de session, une liste de réponses ni un compteur cumulé. Un `usage` nul reste indisponible. Le contenu de réponse et les champs non nécessaires sont ignorés et non recopiés ; aucun appel API n'est effectué. Ces formats ne sont **pas** les journaux natifs de session Codex ou Claude Code et ne permettent pas de déduire leur quota ni le coût d'un abonnement. Aucun coût n'est déduit de ces réponses.
