import argparse
import sys
from pathlib import Path

from .catalog import load_catalog, render as render_catalog
from .feedback import DECISIONS, record_feedback
from .improve import prepare, write_improve
from .improve_registry import STATUSES, update_status
from .rescue import audit, write_reports
from .start import write_start
from .start_questions import ask, load_answers
from .tokens_analysis import analyse
from .tokens_report import render as render_tokens, write_report as write_tokens_report
from .tokens_trace import load_trace


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
    improve = sub.add_parser("improve", help="Proposer des améliorations à partir de sources choisies")
    improve.add_argument("--project", required=True, help="Dossier du projet concerné")
    improve.add_argument("--from", dest="reports", action="append", default=[], help="Rapport RESCUE run.json ; option répétable")
    improve.add_argument("--note", action="append", default=[], help="Note volontairement fournie ; option répétable")
    improve.add_argument("--log", action="append", default=[], help="Journal volontairement fourni ; option répétable")
    improve.add_argument("--registry", help="Registre IMPROVE précédent du même projet")
    improve.add_argument("--out", required=True, help="Nouveau dossier de sortie, extérieur au projet")
    improve_feedback = sub.add_parser("improve-feedback", help="Enregistrer une décision sur une proposition")
    improve_feedback.add_argument("--registry", required=True, help="Chemin du fichier registry.json")
    improve_feedback.add_argument("--proposal", required=True, help="Identifiant de la proposition")
    improve_feedback.add_argument("--decision", required=True, choices=sorted(STATUSES - {'pending'}))
    tokens = sub.add_parser("tokens", help="Diagnostiquer le contexte, avec ou sans trace volontaire")
    tokens.add_argument("--from", dest="trace", help="Trace locale au format vcr-token-trace-v1")
    tokens.add_argument("--out", help="Nouveau dossier de rapport (facultatif)")
    tokens.add_argument("--project", help="Projet à protéger : la sortie doit être extérieure à ce dossier")
    sources = sub.add_parser("sources", help="Consulter le catalogue local des sources et outils")
    sources.add_argument("--topic", help="Thème exact, par exemple tokens ou navigation")
    feedback = sub.add_parser("feedback", help="Enregistrer une décision dans le dossier du rapport")
    feedback.add_argument("--report", required=True, help="Dossier contenant run.json")
    feedback.add_argument("--finding", required=True, help="Identifiant du constat")
    feedback.add_argument("--decision", required=True, choices=sorted(DECISIONS))
    args = parser.parse_args(argv)
    if args.command is None:
        print("Vibe Coding Reference — outil local\n[1] START — cadrer un projet\n[2] RESCUE — analyser un projet\n[3] IMPROVE — examiner des observations\n[4] TOKENS — examiner le contexte\n[5] SOURCES — explorer le catalogue\n[0] Quitter")
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
            elif choice == '3':
                args.command = 'improve'
                args.project = input("Dossier du projet : ").strip()
                args.out = input("Nouveau dossier de sortie extérieur au projet : ").strip()
                args.reports, args.note, args.log, args.registry = [], [], [], None
                while True:
                    path = input("Rapport RESCUE run.json (vide pour terminer) : ").strip()
                    if not path:
                        break
                    args.reports.append(path)
            elif choice == '4':
                args.command = 'tokens'
                args.trace = input("Trace VCR facultative (vide pour diagnostic descriptif) : ").strip() or None
                args.out = input("Nouveau dossier de rapport facultatif (vide pour afficher) : ").strip() or None
                args.project = None
                if args.out:
                    args.project = input("Dossier du projet à protéger facultatif : ").strip() or None
            elif choice == '5':
                args.command = 'sources'
                args.topic = input("Thème facultatif (ex. tokens, navigation) : ").strip() or None
            else:
                return 0
        except (EOFError, KeyboardInterrupt):
            print("\nAnnulé.")
            return 0
    if args.command == 'sources':
        try:
            print(render_catalog(load_catalog(), args.topic), end='')
            return 0
        except (OSError, ValueError) as exc:
            print(f"Erreur : {exc}", file=sys.stderr)
            return 2
    if args.command == 'tokens':
        try:
            records = load_trace(args.trace) if args.trace else None
            data = analyse(records)
            if args.out:
                output = write_tokens_report(data, args.out, args.project)
                print(f"Rapport TOKEN EFFICIENCY créé : {output}")
            else:
                print(render_tokens(data), end='')
            return 0
        except (OSError, ValueError) as exc:
            print(f"Erreur : {exc}", file=sys.stderr)
            return 2
    if args.command == 'improve':
        try:
            project, registry, proposals, limitations = prepare(args.project, args.reports, args.note, args.log, args.registry)
            output = write_improve(project, args.out, registry, proposals, limitations)
            print(f"Rapport IMPROVE créé : {output} ; propositions : {len(proposals)}")
            return 0
        except (OSError, ValueError) as exc:
            print(f"Erreur : {exc}", file=sys.stderr)
            return 2
    if args.command == 'improve-feedback':
        try:
            update_status(args.registry, args.proposal, args.decision)
            print('Décision enregistrée dans le registre IMPROVE.')
            return 0
        except (OSError, ValueError) as exc:
            print(f"Erreur : {exc}", file=sys.stderr)
            return 2
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
