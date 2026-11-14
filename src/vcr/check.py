"""Contrôles de présence fondés sur l'inventaire passif partagé avec RESCUE."""
from .models import CheckResult, Evidence
from .rescue import audit, git


def health_checks(repo, files, incomplete, is_git, scripts, full=False):
    names = {p.name for p in files}
    paths = {str(p) for p in files}
    results = []

    def add(id, status, reason, *, evidence=None, method='inventaire passif', applicability='Applicabilité indéterminée ou contrôle informatif.', limitation=None):
        results.append(CheckResult(id, status, reason, evidence, method, applicability, limitation))

    def presence(id, candidates, label, applicability):
        found = sorted(names & set(candidates))
        matching = sorted((p for p in files if p.name in candidates), key=str)
        evidence = None
        if found:
            first = matching[0]
            evidence = [Evidence('file', f'Fichier reconnu : {first.name}.', path=str(first) if len(first.parts) == 1 else None)]
        add(id, 'passed' if found else 'not_checked',
            f'{label} : {", ".join(found)} ; présence uniquement.' if found else
            f'{label} non identifié dans l’inventaire retenu ; absence ou applicabilité non établie.',
            evidence=evidence, applicability=applicability, limitation='Présence seulement ; contenu et fonctionnement non vérifiés. Inventaire borné et filtré.')

    add('GIT-01', 'passed' if is_git else 'not_checked',
        'git rev-parse --show-toplevel : dépôt détecté.' if is_git else 'Git indisponible, erreur ou dossier hors dépôt.', evidence=[Evidence('command', 'Git confirme le dépôt.', command='git rev-parse --show-toplevel', exit_code=0)] if is_git else None, method='commande Git en lecture', applicability='Tout dossier analysé.', limitation='La commande ne vérifie pas la qualité du dépôt.')
    if is_git:
        rc, raw = git(repo, 'ls-files', '-z', '--', '.')
        if rc == 0:
            tracked = [part.rsplit(b'/', 1)[-1] for part in raw.split(b'\0') if part]
            sensitive = any(n == b'.env' or (n.startswith(b'.env.') and n not in {b'.env.example', b'.env.sample', b'.env.template'}) for n in tracked)
            add('SEC-01', 'failed' if sensitive else 'passed', 'Noms .env suivis par Git détectés ; contenu non lu.' if sensitive else 'Aucun nom .env sensible suivi détecté ; les autres secrets ne sont pas recherchés.', evidence=[Evidence('command', 'Liste des noms suivis examinée ; contenu non lu.', command='git ls-files -z -- .', exit_code=0, redacted=True)], method='commande Git en lecture', applicability='Dépôt Git détecté.', limitation='Recherche limitée aux noms .env ; ne prouve pas l’absence de secrets.')
        else:
            add('SEC-01', 'not_checked', 'Liste des fichiers suivis indisponible.', method='commande Git en lecture', applicability='Dépôt Git détecté ; liste des fichiers suivis indisponible.')
        rc, raw = git(repo, 'remote')
        add('GIT-03', 'passed' if rc == 0 and raw.strip() else 'not_checked', 'Remote configurée ; URL et accessibilité non vérifiées.' if rc == 0 and raw.strip() else 'Remote non identifiée ou commande indisponible ; une remote est facultative.', evidence=[Evidence('command', 'Au moins une remote configurée.', command='git remote', exit_code=0)] if rc == 0 and raw.strip() else None, method='commande Git en lecture', applicability='Dépôt Git détecté ; remote facultative.', limitation='URL, accessibilité et sauvegarde non vérifiées.')
    else:
        add('SEC-01', 'not_checked', 'Suivi Git non vérifié.', method='commande Git en lecture', applicability='Aucun dépôt Git utilisable détecté ; suivi des fichiers inconnu.')
        add('GIT-03', 'not_checked', 'Remote Git non vérifiée.', method='commande Git en lecture', applicability='Aucun dépôt Git utilisable détecté ; remote facultative.')
    presence('GIT-02', {'.gitignore'}, 'Fichier .gitignore', 'Recherche informative ; aucun usage de Git obligatoire.')
    presence('GIT-05', {'README', 'README.md', 'README.rst', 'README.txt', 'readme.md'}, 'README', 'Recherche documentaire pour tout dossier ; absence non considérée comme un échec.')
    presence('ENV-01', {'package.json', 'pyproject.toml', 'requirements.txt'}, 'Manifeste reconnu', 'Recherche limitée aux manifestes Node et Python ; autres technologies possibles.')
    manifests = [p for p in files if p.name == 'package.json']
    locks = {p.name for p in files if p.name in {'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml'} and any(p.parent == m.parent for m in manifests)}
    if locks:
        add('ENV-03', 'passed', 'Manifeste Node et lockfile détectés : ' + ', '.join(sorted(locks)) + ' ; cohérence du contenu non vérifiée.', evidence=[Evidence('log', 'Un manifeste Node et un lockfile reconnu sont dans le même dossier.')], applicability='Manifeste Node et lockfile détectés dans le même dossier.', limitation='Le contenu, le gestionnaire utilisé et les versions ne sont pas vérifiés.')
    else:
        add('ENV-03', 'not_checked', 'Lockfile Node non identifié ou applicabilité indéterminée ; autres gestionnaires non évalués.', applicability='Un manifeste Node et un lockfile doivent être repérés dans le même dossier ; absence non considérée comme un échec.')
    presence('CI-01', {'.gitlab-ci.yml', 'Jenkinsfile', '.travis.yml'}, 'Configuration CI reconnue', 'Recherche informative ; une CI ne convient pas nécessairement à tous les projets.') if not any(p.startswith('.github/workflows/') and p.endswith(('.yml', '.yaml')) for p in paths) else add('CI-01', 'passed', 'Fichier YAML présent dans .github/workflows ; exécution non vérifiée.', evidence=[Evidence('log', 'Fichier YAML retenu dans .github/workflows.')], applicability='Fichier de configuration GitHub Actions détecté ; sa validité n’est pas établie.', limitation='Présence seulement ; exécution et contenu non vérifiés.')
    presence('CTX-03', {'AGENTS.md', 'CLAUDE.md'}, 'Instructions agents', 'Recherche informative ; instructions pour agents facultatives.')
    presence('ENV-05', {'.env.example', '.env.sample', '.env.template'}, 'Exemple de configuration environnement', 'Recherche informative ; le besoin de variables environnement n’est pas établi.')
    presence('CODE-02', {'tsconfig.json', 'mypy.ini', '.mypy.ini', 'pyrightconfig.json'}, 'Configuration de typage reconnue', 'Recherche de noms de configuration connus ; le typage n’est pas obligatoire.')
    for id, script in [('CODE-01', 'lint'), ('TEST-01', 'test'), ('BUILD-01', 'build')]:
        found = script in scripts
        add(id, 'passed' if found else 'not_checked', f'Script {script} déclaré dans package.json ; non exécuté.' if found else f'Script {script} non identifié ; recherche limitée.', evidence=[Evidence('configuration', f'Clé scripts.{script} non vide dans un package.json retenu.')] if found else None, method='lecture limitée des manifestes', applicability='Script reconnu dans un package.json.' if found else 'Aucun script reconnu ; applicabilité et autres outils indéterminés.', limitation='La commande et son résultat ne sont pas vérifiés.')
    if full:
        for id, script in [('CODE-01-EXEC', 'lint'), ('CODE-02-EXEC', 'typecheck'), ('TEST-01-EXEC', 'test'), ('BUILD-01-EXEC', 'build')]:
            add(id, 'skipped' if script in scripts else 'not_checked',
                f'Script {script} déclaré mais non exécuté : exécution de commandes du projet non prise en charge.' if script in scripts else f'Commande {script} non identifiée ; aucune exécution.', evidence=[Evidence('configuration', f'Clé scripts.{script} non vide dans un package.json retenu.')] if script in scripts else None, method='lecture limitée des manifestes', applicability='Script reconnu ; exécution non prise en charge.' if script in scripts else 'Aucun script reconnu ; applicabilité indéterminée.', limitation='Exécution de code projet non prise en charge.')
    return results


def run_checks(repo, full=False):
    run = audit(repo, health=True, full=full)
    run.workflow = 'check'
    run.findings = []
    run.limitations.append('Restauration et vulnérabilités des dépendances non contrôlées.')
    return run
