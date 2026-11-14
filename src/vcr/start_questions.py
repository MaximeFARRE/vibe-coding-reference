"""Questionnaire START et reprise explicite de réponses locales."""
import json
from pathlib import Path

QUESTIONS = (
    ('goal', 'Que doit permettre de faire le projet ?', None),
    ('action', 'Quelle action concrète la personne effectue-t-elle ? (ex. cliquer sur Ajouter)', None),
    ('outcome', 'Quel résultat visible doit-elle obtenir ?', None),
    ('kind', 'Type : 1 site vitrine, 2 application web, 3 gestion administrative, 4 calcul Python, 5 outil local, 6 interface très interactive, 0 à préciser', {'1': 'site', '2': 'fullstack', '3': 'crud', '4': 'python', '5': 'local', '6': 'interactive', '0': 'unknown'}),
    ('audience', 'Qui utilisera le projet ? (ex. moi seul, équipe, clients)', None),
    ('access', 'Accès : 1 local, 2 équipe privée, 3 public sur internet, 0 à préciser', {'1': 'local', '2': 'private', '3': 'public', '0': 'unknown'}),
    ('data', 'Quelles informations faut-il manipuler ? Ne saisissez aucune donnée réelle ou secrète.', None),
    ('sensitive', 'Données sensibles : 1 oui, 2 non, 0 à préciser', {'1': 'yes', '2': 'no', '0': 'unknown'}),
    ('persistence', 'Faut-il conserver des données entre deux utilisations : 1 oui, 2 non, 0 à préciser', {'1': 'yes', '2': 'no', '0': 'unknown'}),
    ('seo', 'Référencement sur les moteurs de recherche : 1 nécessaire, 2 non, 0 à préciser', {'1': 'yes', '2': 'no', '0': 'unknown'}),
    ('interaction', 'Interface : 1 simple, 2 très interactive, 0 à préciser', {'1': 'simple', '2': 'rich', '0': 'unknown'}),
    ('python', 'Python imposé pour le métier : 1 oui, 2 non, 0 à préciser', {'1': 'yes', '2': 'no', '0': 'unknown'}),
    ('constraints', 'Budget, hébergement, maintenance ou autres contraintes ? (facultatif)', None),
)


def load_answers(path):
    try:
        data = json.loads(Path(path).expanduser().read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError('Impossible de lire les réponses JSON indiquées.') from exc
    if not isinstance(data, dict) or data.get('version') != 1 or not isinstance(data.get('answers'), dict):
        raise ValueError('Format de réponses START inconnu.')
    answers = data['answers']
    known = {key: choices for key, _, choices in QUESTIONS}
    if set(answers) - set(known):
        raise ValueError('Champ de réponse START inconnu.')
    for key, value in answers.items():
        if not isinstance(value, str) or len(value) > 2000 or (known[key] and value not in known[key].values()):
            raise ValueError(f'Réponse invalide : {key}.')
    return dict(answers)


def ask(existing=None, input_fn=None, print_fn=print):
    if input_fn is None:
        input_fn = input
    answers = dict(existing or {})
    print_fn('START — répondez sans copier de secrets ni de données personnelles. Entrée vide : à préciser.')
    for key, prompt, choices in QUESTIONS:
        if key in answers:
            continue
        while True:
            response = input_fn(prompt + ' : ').strip()
            if len(response) > 2000:
                print_fn('Réponse trop longue (2 000 caractères maximum).')
                continue
            if choices:
                response = response or '0'
                if response not in choices:
                    print_fn('Choisissez un numéro indiqué.')
                    continue
                answers[key] = choices[response]
            else:
                answers[key] = response
            break
    return answers
