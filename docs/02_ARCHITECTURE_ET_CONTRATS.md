# 02 — Architecture cible : système léger, extensible et inspectable

**Contrat technique à donner à Codex.** Ce document prescrit l'architecture du **premier prototype**, et non une réécriture ou une théorie universelle de l'architecture des agents.

## 1. Choix de base et justification

**Recommandation initiale : Python 3.11+**, bibliothèque standard autant que possible, `pytest` comme dépendance de développement, CLI intégrée en `argparse`, modèles de données typés via `dataclasses`/`typing`, JSON Schema en fichier documentaire. Alternative Click/Typer seulement si un besoin utilisateur réel le justifie. Le code peut être entièrement généré par Codex, mais doit rester compréhensible pour un non-développeur.

Pourquoi Python pour **l'outil VCR** (et pas pour les applications de ses utilisateurs) : simple automatisation locale, multi-plateforme, collecte Git/filesystem/JSON et interfaces de plugins. Cela **ne signifie pas** recommander Python comme framework universel pour START. Ne pas exiger Next.js/React/serveur/SQLite pour la V0. Ne pas ajouter un système de tâches distribué.

Le composant LLM est **l'agent hôte existant** (Codex/Claude Code). VCR n'appelle aucune API de modèle dans P0.1 : il fournit des scripts déterministes, une collecte de preuves, des prompts structurés et un format de restitution. Cette séparation évite de réinventer un harness.

## 2. Architecture logique

```mermaid
flowchart TD
    U[Utilisateur: START / RESCUE / IMPROVE / TOKENS]
    I[Entrée locale simple: menu CLI + prompts]
    W[Workflow: préflight, collecte, compte rendu]
    P[Profils de contrôles: TS/JS, Python, générique]
    C[Collecteurs déterministes: git, manifestes, fichiers, tests existants]
    A[Agent hôte existant: Codex / Claude Code]
    N[Normalisation: constats, preuves, statuts, limites]
    R[Rapport Markdown + JSON + HTML statique facultatif]
    H{Approbation humaine?}
    X[Plan de modification séparé: branche, tests, rollback]
    U-->I-->W
    W-->P-->C-->N
    W-.prompt ciblé.->A
    A-.constats proposés.->N
    N-->R-->H
    H--non-->U
    H--oui, tâche distincte-->X
```

**Ne pas interpréter le schéma comme un ordre de coder un orchestrateur de modèles.** Les flèches vers l'agent signifient un prompt ou un rapport que l'utilisateur donne à l'agent déjà utilisé.

## 3. Proposition d'arborescence du code P0.1

```text
vibe-coding-reference/
├── README.md                   # prise en main en français + rapide EN
├── AGENTS.md                   # petit sommaire agent, instructions test/sécurité
├── pyproject.toml              # paquet Python léger (pas de framework web)
├── src/vcr/
│   ├── __main__.py             # python -m vcr
│   ├── cli.py                  # 4 commandes + menu interactif
│   ├── domain/
│   │   ├── findings.py         # Finding, Evidence, Plan, limitations
│   │   ├── profiles.py         # Profile, Check, Applicability
│   │   └── runs.py             # Run, Provenance, command outcomes
│   ├── collectors/
│   │   ├── filesystem.py       # filtres .gitignore, chemins, tailles
│   │   ├── git.py              # statut, branches, dirty
│   │   ├── manifests.py        # pyproject, requirements, package.json, lockfiles
│   │   └── scripts.py          # scripts/commandes repérés, sans les exécuter
│   ├── checks/
│   │   ├── base.py             # interface check sans side effects
│   │   ├── common.py           # gitignore, secrets exposés [sans valeur], docs...
│   │   ├── python.py           # contrôle basique Python
│   │   └── javascript.py       # contrôle basique JS/TS
│   ├── workflows/
│   │   ├── start.py
│   │   ├── rescue.py
│   │   ├── improve.py
│   │   └── tokens.py
│   ├── reports/
│   │   ├── normalize.py
│   │   ├── markdown.py
│   │   └── html.py             # optionnel; sans JS externe/CDN
│   ├── adapters/               # interfaces pour extensions FUTURES
│   │   ├── locator.py          # native | serena | graph (seule native en V0)
│   │   └── evidence.py         # normalisation collecteurs
│   └── assets/                 # mini-template HTML si nécessaire
├── prompts/
│   ├── start.md
│   ├── rescue.md
│   ├── improve.md
│   └── token-efficiency.md
├── catalog/
│   ├── sources.json            # données sourcées, revue et licence
│   └── extensions.json         # jamais auto-installées
├── docs/
│   ├── getting-started.md
│   ├── checks.md
│   ├── limitations.md
│   └── architecture.md
├── tests/
│   ├── fixtures/               # dépôts locaux artificiels et sans secrets
│   ├── test_cli.py
│   ├── test_checks.py
│   ├── test_reporting.py
│   ├── test_safety.py
│   └── test_schema.py
└── .github/workflows/ci.yml
```

**Note anti-usine-à-gaz :** cette arborescence représente des responsabilités. Si certains modules sont très courts, les regrouper. Pas de couches/interface abstraite supplémentaires sans consommateur. Au départ, aucun `services/`, `repositories/`, `providers/` ou microservices fictifs.

## 4. Parcours utilisateur concrets

### Menu pour débutant

```text
Vibe Coding Reference — outil local
[1] START       Bien démarrer un projet
[2] RESCUE      Analyser un dépôt existant
[3] IMPROVE     Proposer des améliorations de l'environnement IA
[4] TOKENS      Comprendre les gaspillages de contexte/coût
[5] SOURCES     Explorer les études et outils existants
