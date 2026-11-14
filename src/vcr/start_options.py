"""Options conditionnelles indicatives, sans installation ni promesse comparative."""


def suggest(a):
    warnings = []
    kind, access = a['kind'], a['access']
    if kind == 'local' and access in {'private', 'public'}:
        warnings.append('Le type « outil local » et un accès partagé/public sont contradictoires : confirmer le mode d’accès avant de choisir.')
    if kind == 'site' and (a['persistence'] == 'yes' or a['sensitive'] == 'yes'):
        warnings.append('Le site vitrine seul ne couvre pas forcément la conservation ou la protection des données : clarifier les flux et le backend éventuel.')
    if a['python'] == 'yes' and kind == 'site':
        warnings.append('La contrainte Python et le site vitrine peuvent concerner des parties distinctes : confirmer avant de séparer frontend et calcul.')
    if a['persistence'] == 'yes':
        storage = ('Fichier local ou SQLite selon concurrence et sauvegardes.' if access == 'local' else
                   'Base adaptée aux accès concurrents et sauvegardée ; choix à confirmer avec les besoins.')
    elif a['persistence'] == 'no':
        storage = 'Aucune base requise par défaut ; confirmer qu’aucune conservation n’est nécessaire.'
    else:
        storage = 'À déterminer : la persistance n’est pas encore clarifiée.'
    if access == 'local':
        infrastructure = 'Exécution sur la machine ; organiser sauvegardes et mises à jour si nécessaire.'
    elif access == 'private':
        infrastructure = 'Hébergement privé et contrôle d’accès à choisir selon l’équipe.'
    elif access == 'public':
        infrastructure = 'Hébergement public à choisir ; domaine, déploiement et exploitation à évaluer.'
    else:
        infrastructure = 'À déterminer selon le mode d’accès ; aucun hébergement présumé.'

    def option(name, language, framework, architecture, advantage, drawback, condition, cost):
        return {'name': name, 'language': language, 'framework': framework, 'architecture': architecture,
                'infrastructure': infrastructure, 'database': storage, 'advantage': advantage,
                'drawback': drawback, 'condition': condition, 'cost': cost}

    if a['python'] == 'yes' or kind == 'python':
        options = [option('Backend Python avec pages simples', 'Python ; HTML/CSS pour l’interface', 'Django/HTMX à évaluer', 'Calcul et règles métier côté Python ; pages et formulaires côté serveur.', 'Les calculs restent près du métier.', 'Django peut être excessif pour un script très simple.', 'Pertinent si les calculs Python sont centraux et une interface web est nécessaire.', 'Maintenance serveur et dépendances à prévoir ; hébergement selon accès.')]
        if access == 'local' or kind == 'local':
            options.append(option('Outil Python local', 'Python', 'Interface standard ou Streamlit selon besoins', 'Programme local directement connecté aux calculs.', 'Peu de composants pour un usage individuel.', 'Partage multi-utilisateur et accès distant demandent une autre conception.', 'Si l’usage est réellement local et individuel.', 'Exploitation locale ; sauvegardes et installation à prévoir.'))
        else:
            options.append(option('API Python et interface séparée', 'Python côté API ; langage du frontend à choisir', 'FastAPI et frontend à choisir si justifiés', 'API Python et interface indépendante.', 'Front et calcul peuvent évoluer séparément.', 'Deux composants et contrat API à maintenir.', 'Si une interface riche ou plusieurs clients exigent une API.', 'Maintenance et déploiement de plusieurs composants.'))
    elif kind == 'local' and access not in {'private', 'public'}:
        options = [option('Utilitaire local', 'Python ou langage déjà maîtrisé', 'Bibliothèque standard ou interface légère', 'Programme local unique.', 'Peu de composants à maintenir.', 'Pas de partage distant implicite.', 'Si l’usage est individuel sur une machine.', 'Exploitation locale et sauvegardes à organiser.')]
    elif kind == 'site' and a['persistence'] != 'yes' and a['sensitive'] != 'yes' and a['interaction'] != 'rich':
        options = [option('Site statique', 'HTML/CSS et JavaScript si nécessaire', 'Aucun ou Astro selon la complexité', 'Pages statiques ; pas de backend par défaut.', 'Peu de composants à exploiter.', 'Les comptes et données dynamiques nécessitent d’autres composants.', 'Si le contenu est surtout public et sans données à conserver.', 'Hébergement statique et maintenance de contenu.'),
                   option('Site avec backend', 'Langage maîtrisé par l’équipe', 'Framework serveur à choisir', 'Pages et traitement côté serveur.', 'Permet des fonctions dynamiques si elles deviennent nécessaires.', 'Plus d’exploitation et de surface à maintenir.', 'Seulement si formulaires, comptes ou données l’exigent.', 'Serveur et maintenance supplémentaires.')]
    elif kind == 'crud':
        options = [option('Application de gestion côté serveur', 'Python ou langage maîtrisé', 'Django/HTMX ou équivalent à évaluer', 'Formulaires et règles côté serveur.', 'Parcours administratifs regroupés.', 'La gestion des permissions et des données reste à concevoir.', 'Pour des formulaires et tableaux avec besoins de gestion.', 'Maintenance serveur, accès et sauvegardes.')]
    elif kind in {'fullstack', 'interactive'} or a['interaction'] == 'rich' or access in {'private', 'public'}:
        options = [option('Application web intégrée', 'TypeScript ou langage maîtrisé', 'Next.js, SvelteKit ou équivalent à évaluer', 'Interface et fonctions serveur dans une application.', 'Une base de code peut couvrir les parcours web courants.', 'Les choix de déploiement et frontières métier restent à définir.', 'Si l’accès web et les interactions le justifient.', 'Maintenance du framework, hébergement et sauvegardes éventuelles.'),
                   option('Pages serveur simples', 'Python ou langage maîtrisé', 'Django/HTMX ou équivalent à évaluer', 'Formulaires et rendu côté serveur.', 'Moins de séparation entre interface et logique.', 'Moins adapté si les interactions très riches sont essentielles.', 'Si les interactions restent surtout des formulaires et tableaux.', 'Maintenance serveur ; infrastructure selon accès.')]
    else:
        warnings.append('Le type de produit ou le mode d’accès reste à préciser ; aucune stack définitive ne peut être déduite.')
        options = [option('Prototype local minimal', 'Langage déjà maîtrisé', 'Aucun par défaut', 'Un programme simple pour valider le parcours.', 'Hypothèse facile à revoir.', 'Ne couvre pas nécessairement un accès partagé.', 'Seulement pour clarifier le besoin avant un choix durable.', 'Faible infrastructure initiale ; effort dépendant du périmètre.')]
    return options, warnings
