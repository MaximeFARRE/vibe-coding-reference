# 06 — Playbooks opérationnels pour START, RESCUE, IMPROVE et TOKENS

Ces procédures sont à implémenter dans le prototype, puis à exposer sous forme de **prompts copiable-collable** et de commandes simples. Elles n'exigent ni qu'un débutant connaisse l'architecture du dépôt, ni que VCR devienne un agent autonome.

## 1. START — questions en français ordinaire

**Objectif :** passer d'une idée d'application à un document de besoin fiable et une recommandation de départ raisonnable.

**Questions minimales** :

1. Qu'est-ce que l'application doit permettre de faire ? Quel est son parcours principal ?
2. Qui va l'utiliser : toi seul, petite équipe, clients sur internet ?
3. Où devra-t-elle fonctionner : local, entreprise, site web public ?
4. Quelles données doit-elle mémoriser ? Y a-t-il des informations confidentielles ?
5. Faut-il une interface élaborée, beaucoup de formulaires, de calculs Python, ou du référencement Google ?
6. As-tu des contraintes d'hébergement, de budget, de performance, d'intégration à d'autres services ?

**Ne demander les autres détails que s'ils changent un choix réel.** En cas de réponse manquante, faire une hypothèse explicitée et réversible, sans bloquer l'utilisateur inutilement.

**Sorties souhaitées** :

```markdown
# Besoin métier
- Utilisateurs, objectif, parcours principaux, données.
- Fonctionnalités IN / OUT.
- Contraintes non négociables.
- Hypothèses à confirmer.

# Stack proposée
- Recommandation conditionnelle ; pourquoi.
- Option plus simple si elle existe.
- Coût d'exploitation et niveau de maintenance attendus (qualitatif).
- Dépendances à NE PAS ajouter au démarrage.

# Critères de réussite
- Étant donné [situation], quand [action], alors [résultat observé].
- Que faire en cas d'erreur, absence de réseau, doublon ou permissions insuffisantes ?
- Comment vérifier sans expertise en code ?
```

**Exemples de décisions (indicatives)** :

- Site vitrine statique simple + SEO → HTML/Astro possibles ; pas de BDD/API par défaut.
- App web full-stack avec tableaux et comptes → Next.js/TS, SvelteKit, Django/HTMX ou Rails selon l'écosystème, équipe et coût opérationnel ; pas de vainqueur universel.
- Calculs et imports Python au cœur du métier → Django/HTMX ou FastAPI + frontend seulement si interactions le justifient.
- Utilitaire local mono-utilisateur → script + UI simple/Streamlit selon métier ; pas de cluster.

## 2. RESCUE — procédure d'audit détaillée

### Prévol

- Vérifier que le chemin correspond au bon dépôt ; afficher la racine Git ; capturer HEAD/branche si disponibles ; préserver modifications non commitées.
- Inventorier fichiers et stack avec filtres explicites ; relever limitations.
- Demander la permission **avant** tests, build, migrations, installations, commandes non passives ou connexions à un compte.
- Définir le périmètre : tout, sécurité, architecture, fiabilité, données, contexte, tokens, etc.

### Les 10 axes (depuis v0.1/v0.2, maintenus)

| Axe | Chercher | Pièges à éviter |
|---|---|---|
| Produit / UX | parcours métier, redondances, états d'erreur | supprimer sans comprendre le besoin |
| Architecture | flux, modules-centres, imports, frontière API | gros fichier ≠ mauvais code |
| Code | duplication réelle, fonctions mortes confirmées, complexité | imports dynamiques, reflection, feature flags |
| Dépendances | lockfile, audit vulnérabilités, versions | « dépendance vieille » ≠ exploitable |
| Sécurité | secrets, droits, origines, validations, uploads | révéler secrets ou inventer exploitabilité |
| Tests/fiabilité | tests critiques, assertion, intégration, erreurs | tests verts ≠ absence de bug |
| Données/migrations | schéma, transactions, sauvegarde/restauration | toucher données réelles, migration sur lecture |
| Performances | N+1, I/O répétés, parcours coûteux | chiffres de latence non mesurés |
| Infrastructure | démarrage, CI, déploiement, rollback | imposer Docker/Postgres arbitrairement |
| Documentation/IA | AGENTS, navigation, index, drift, coûts de contexte | générer des kilomètres de documentation |

### Distinguer trois couches de preuve

1. **Certain** : `package.json` indique tel script ; `git status` indique des modifications ; une route HTTP contient tel code à telle ligne ; une commande a vraiment échoué.
2. **Interprétation forte** : l'absence probable d'un test adapté ; un module concentrant plusieurs responsabilités ; une frontière non respectée.
3. **Question ouverte** : une fonctionnalité semble obsolète, mais il manque la mesure d'usage ; un fichier paraît inutile mais peut être chargé dynamiquement.

### Verdicts

- **KEEP** : fondations saines, quelques corrections utiles.
- **REFACTOR** : même stack et produit, changements ciblés et vérifiables.
- **PARTIAL REBUILD** : reconstruire une sous-zone avec migration/risque limité, comportement figé par tests.
- **REBUILD** : seulement si l'existant est structurellement inadapté, la réparation plus risquée/coûteuse, données/fonctions migrables et justificatif solide.
- **INCONCLUSIVE** : manque de contexte ou de vérifications, verdict reporté.

### Fiche type d'un finding

```markdown
### P1 — Validation insuffisante dans une route sensible (EXEMPLE)
État : suspecté, à confirmer sur source précise
Preuve : fichier/route/ligne, commande ou extrait REDIGÉ
Pourquoi : risque de modification sans entrée valide
Impact : intégrité / permission / expérience utilisateur
Proposition A : validation runtime à la frontière HTTP + refus clair
Proposition B : validation du service interne + route minimale
À préserver : compatibilité des clients existants et métier
Vérification : tests de route autorisé/refusé + non-régression
Risque de la correction : changement de comportements attendus
Décision humaine : valider contrat API avant modification
```
