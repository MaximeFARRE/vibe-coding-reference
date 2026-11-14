import argparse
import sys
from pathlib import Path

from .rescue import audit, write_reports


def main(argv=None):
    parser = argparse.ArgumentParser(description="VCR — audit local passif, sans clé API.", epilog="Exemple : python -m vcr rescue --repo ./projet --out ./rapports")
    sub = parser.add_subparsers(dest="command")
    rescue = sub.add_parser("rescue", help="Analyser un dossier sans le modifier")
    rescue.add_argument("--repo", required=True, help="Dossier à analyser")
    rescue.add_argument("--out", required=True, help="Nouveau dossier de rapports, extérieur au projet")
    args = parser.parse_args(argv)
    if args.command is None:
        print("Vibe Coding Reference — outil local\n[1] RESCUE — analyser un projet\n[0] Quitter\nSTART, IMPROVE, TOKENS et SOURCES : pas encore disponibles.")
        if not sys.stdin.isatty():
            return 0
        try:
            if input("Votre choix : ").strip() != "1":
                return 0
            repo = input("Dossier à analyser : ").strip()
            out = input("Nouveau dossier de rapports extérieur au projet : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAnnulé.")
            return 0
    else:
        repo, out = args.repo, args.out
    try:
        target = Path(repo).expanduser().resolve(strict=True)
        output = Path(out).expanduser().resolve(strict=False)
        if not target.is_dir():
            raise ValueError("Le projet doit être un dossier existant.")
        if output == target or output.is_relative_to(target) or target.is_relative_to(output):
            raise ValueError("Le dossier de sortie doit être distinct du projet et hors de celui-ci.")
        if output.exists():
            raise ValueError("Le dossier de sortie existe déjà ; choisissez un nouveau chemin.")
        print(f"Périmètre : {target}\nAnalyse passive ; aucun test du projet ne sera exécuté.")
        run = audit(target)
        write_reports(run, output)
        print(f"Rapports créés dans : {output}")
        return 0
    except (OSError, ValueError) as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        return 2
