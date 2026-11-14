"""Collecte bornée : aucune exécution de commande du projet ni lecture de .env."""
import json
import os
import re
import subprocess
import tomllib
import uuid
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from .models import CheckResult, Evidence, Finding, Run

EXCLUDED = {'.git', 'node_modules', '.next', '.venv', 'venv', '__pycache__', '.pytest_cache', 'dist', 'build'}
MANIFESTS = {'package.json', 'pyproject.toml', 'requirements.txt', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'uv.lock', 'poetry.lock'}
MAX_FILES = 10000
MAX_SIZE = 1024 * 1024


def git(repo, *args, input_bytes=None):
    env = os.environ.copy()
    for key in list(env):
        if key.startswith('GIT_'):
            del env[key]
    env.update(GIT_CONFIG_NOSYSTEM='1', GIT_CONFIG_GLOBAL=os.devnull, GIT_OPTIONAL_LOCKS='0', GIT_TERMINAL_PROMPT='0')
    try:
        result = subprocess.run(['git', '--no-optional-locks', '-c', 'core.fsmonitor=false', '-c', 'core.untrackedCache=false', '-C', str(repo), *args], input=input_bytes, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=10, env=env, check=False)
        return result.returncode, result.stdout
    except (OSError, subprocess.TimeoutExpired):
        return None, b''


def audit(repo):
    checks, findings = [], []
    limits = ['Audit statique partiel : aucune exécution des tests, build, analyse réseau ou revue métier.', 'Les contenus du projet ne sont pas recopiés ; les fichiers sensibles ne sont pas lus.', 'Verdict : inconclusive ; ces contrôles ne permettent pas de conclure sur la qualité ou la sécurité.']
    def check(name, status, reason):
        checks.append(CheckResult(name, status, reason))
    def finding(id, title, category, severity, status, summary, evidence, advice):
        findings.append(Finding(id, title, category, severity, status, 'high' if status == 'confirmed' else 'low', 'static_check', summary, evidence, [advice]))

    code, top = git(repo, 'rev-parse', '--show-toplevel')
    is_git = code == 0
    head = None
    dirty = None
    if is_git:
        code, raw = git(repo, 'rev-parse', '--verify', 'HEAD')
        if code == 0 and re.fullmatch(rb'[0-9a-f]{40,64}\n?', raw):
            head = raw.decode().strip()
        code, raw = git(repo, 'status', '--porcelain=v1', '--untracked-files=normal', '--', '.')
        if code == 0:
            dirty = bool(raw)
            check('git_status', 'passed', 'État Git relevé sans recopier les noms ou contenus.')
            if dirty:
                finding('git-dirty', 'Modifications Git présentes', 'operations', 'info', 'confirmed', 'Le périmètre contient des changements suivis ou non suivis.', [Evidence('command', 'La sortie non vide indique des changements.', command='git status --porcelain=v1 --untracked-files=normal -- .', exit_code=0)], 'Préserver ces modifications avant toute intervention.')
        else:
            check('git_status', 'not_checked', 'Échec ou délai dépassé de git status.')
    else:
        check('git_status', 'not_checked', 'Git indisponible, échec de commande ou dossier hors dépôt Git.')
    check('git_head', 'passed' if head else 'not_checked', 'HEAD relevé.' if head else 'HEAD indisponible ou dépôt sans commit.')

    files = []
    excluded = 0
    errors = []
    ignored_checked = is_git
    stack = [repo]
    while stack and len(files) < MAX_FILES:
        directory = stack.pop()
        try:
            entries = list(os.scandir(directory))
        except OSError:
            errors.append('Un dossier est illisible.')
            continue
        candidates = []
        for entry in entries:
            try:
                if entry.is_symlink() or entry.name in EXCLUDED:
                    excluded += 1
                else:
                    candidates.append(entry)
            except OSError:
                errors.append('Un élément est inaccessible.')
        ignored = set()
        if is_git and candidates:
            payload = b''.join(os.fsencode(os.path.relpath(e.path, repo)) + b'\0' for e in candidates)
            rc, result = git(repo, 'check-ignore', '-z', '--stdin', input_bytes=payload)
            if rc in (0, 1):
                ignored = set(result.split(b'\0'))
            else:
                ignored_checked = False
                errors.append('Les règles Git ignore ne peuvent pas être évaluées pour un dossier.')
                continue
        for entry in candidates:
            rel = os.path.relpath(entry.path, repo)
            if os.fsencode(rel) in ignored:
                excluded += 1
                continue
            try:
                if entry.is_dir(follow_symlinks=False):
                    stack.append(Path(entry.path))
                elif entry.is_file(follow_symlinks=False):
