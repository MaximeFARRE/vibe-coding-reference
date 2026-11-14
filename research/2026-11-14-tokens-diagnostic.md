# TOKENS : diagnostic et données déclarées

- Date : 2026-11-14 ; statut : décidé pour le lot 5.
- Question : rendre les leviers de contexte compréhensibles sans inventer de quota, coût ou gain.
- Sources : [backlog lot 5](../plans/03_BACKLOG_ET_LIVRAISON.md), [playbook TOKENS](../docs/06_PLAYBOOKS_ET_AUDITS.md), [format d'import](../docs/TOKEN_TRACE_FORMAT.md), [calculs](../src/vcr/tokens_analysis.py), [tests](../tests/test_tokens.py) et [validation](../tests/test_tokens_trace.py).

## Résultats et limites

- **Confirmé sur fixtures** : sans trace, diagnostic descriptif ; sans cache ou coût, champs `unavailable` et aucune valeur monétaire inventée. Les compteurs cumulés et sommes calculées sont distingués ; aucun quota d'abonnement n'est déduit.
- **Confirmé sur fixtures** : traces partielles, devises mélangées, formats inconnus, champs dupliqués et valeurs invalides sont traités explicitement ; identifiants, empreintes et contenus sensibles fictifs ne sont pas recopiés.
- **Limite** : mesures et coûts sont déclarés par l'importateur et ne sont pas vérifiés sur une source de facturation ; le format impose une requête distincte par enregistrement. Les noms de fichiers sources ne sont pas mémorisés : conserver la trace pour vérifier les références.
- **Non vérifié** : conversion de traces natives Codex/Claude, ergonomie externe et Windows. Aucune preuve de gain de tokens ou de performance propre à VCR.

## Options et décision

- Diagnostic sans trace : immédiatement utilisable, sans surveillance ; ne mesure pas l'usage réel.
- Format VCR explicite avec champs facultatifs : sémantique stable et séparation des absences ; conversion manuelle nécessaire pour d'autres formats, avec risque d'erreur de l'importateur.
- Parser natif multi-fournisseur : plus direct pour certains utilisateurs ; formats et interprétations variables, maintenance et risques de données privées. Non retenu tant que les formats réels et permissions ne sont pas étudiés.
- Décision : format JSON volontaire, borné et documenté ; aucune télémétrie ni tarification figée. Statuts `measured` pour valeurs déclarées, `estimated` pour calculs dérivés ou coût déclaré estimé, `unavailable` si non calculable.

## Mise à jour du 2026-11-14 — sources publiques autorisées

- La précédente limitation « conversion manuelle nécessaire pour tous les formats fournisseurs » est partiellement remplacée : imports explicites d'une réponse Responses API OpenAI ou Messages API Anthropic, sans accès automatique aux comptes ni journaux privés.
- [OpenAI — observabilité et usage](https://developers.openai.com/api/docs/guides/agents-api/observability) : cache lu inclus dans l'entrée ; raisonnement inclus dans la sortie ; compteurs d'usage potentiellement manquants et non équivalents à une facture.
- [Anthropic — prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) : les compteurs d'entrée ordinaire, cache lu et création de cache sont distincts ; le total n'est calculé que si les trois sont disponibles.
- **Confirmé sur fixtures** : import d'une réponse, champs partiels indisponibles, aucun contenu fictif privé recopié ; voir [tests](../tests/test_tokens_native.py). **Non vérifié** : journaux natifs de session Codex/Claude Code, conversion de plusieurs réponses ou trace de production réelle.
