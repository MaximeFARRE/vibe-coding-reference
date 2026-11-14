import argparse
import sys
from pathlib import Path

from .feedback import DECISIONS, record_feedback
from .rescue import audit, write_reports
from .start import write_start
from .start_questions import ask, load_answers


def main(argv=None):
    parser = argparse.ArgumentParser(description="VCR — cadrage et audit local, sans clé API.", epilog="Exemples : python -m vcr start --interactive ; python -m vcr rescue --repo ./projet --out ./rapports")
    sub = parser.add_subparsers(dest="command")
    start = sub.add_parser("start", help="Cadrer une idée de projet")
    start.add_argument("--interactive", action="store_true", help="Poser les questions en terminal (mode par défaut)")
    start.add_argument("--out", help="Nouveau dossier pour les documents START")
    start.add_argument("--from", dest="answers_from", help="Reprendre un fichier answers.json")
    rescue = sub.add_parser("rescue", help="Analyser un dossier sans le modifier")
    rescue.add_argument("--repo", required=True, help="Dossier à analyser")
    rescue.add_argument("--out", required=True, help="Nouveau dossier de rapports, extérieur au projet")
    feedback = sub.add_parser("feedback", help="Enregistrer une décision dans le dossier du rapport")
    feedback.add_argument("--report", required=True, help="Dossier contenant run.json")
    feedback.add_argument("--finding", required=True, help="Identifiant du constat")
    feedback.add_argument("--decision", required=True, choices=sorted(DECISIONS))
    args = parser.parse_args(argv)
    if args.command is None:
        print("Vibe Coding Reference — outil local\n[1] START — cadrer un projet\n[2] RESCUE — analyser un projet\n[0] Quitter\nIMPROVE, TOKENS et SOURCES : pas encore disponibles.")
        if not sys.stdin.isatty():
            return 0
        try:
            choice = input("Votre choix : ").strip()
            if choice == '1':
                args.command, args.out, args.answers_from = 'start', None, None
            elif choice == '2':
                args.command = 'rescue'
                args.repo = input("Dossier à analyser : ").strip()
                args.out = input("Nouveau dossier de rapports extérieur au projet : ").strip()
            else:
                return 0
        except (EOFError, KeyboardInterrupt):
            print("\nAnnulé.")
            return 0
    if args.command == 'start':
        try:
            output = args.out or input("Nouveau dossier pour les documents START : ").strip()
            if not output:
                raise ValueError("Un dossier de sortie est nécessaire.")
            output = Path(output).expanduser().resolve(strict=False)
            if output.exists():
                raise ValueError("Le dossier de sortie existe déjà ; choisissez un nouveau chemin.")
            answers = load_answers(args.answers_from) if args.answers_from else {}
            answers = ask(answers)
            write_start(answers, output)
            print(f"Documents START créés dans : {output}")
            return 0
        except (EOFError, KeyboardInterrupt):
            print("\nAnnulé ; aucun document généré.")
            return 1
        except (OSError, ValueError) as exc:
            print(f"Erreur : {exc}", file=sys.stderr)
            return 2
    if args.command == 'feedback':
        try:
            path = record_feedback(args.report, args.finding, args.decision)
            print(f"Décision enregistrée : {path}")
            return 0
        except (OSError, ValueError) as exc:
            print(f"Erreur : {exc}", file=sys.stderr)
            return 2
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
