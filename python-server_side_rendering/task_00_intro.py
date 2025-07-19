def generate_invitations(template, attendees):
    # Vérifie que template est une chaîne de caractères
    if not isinstance(template, str):
        return "template must be a string"
    
    # Vérifie que attendees est une liste
    if not isinstance(attendees, list):
        return "attendees must be a list"
    
    # Vérifie si le template est vide
    if template == "":
        return "Template is empty, no output files generated."
    
    # Vérifie si la liste d'invités est vide
    if attendees == []:
        return "No data provided, no output files generated."

    # Liste des clés attendues dans chaque dictionnaire
    key_list = ["name", "event_title", "event_date", "event_location"]

    # Boucle sur chaque invité
    for i, element in enumerate(attendees):
        result = template  # Copie du template à modifier

        # Remplace chaque placeholder par sa valeur ou "N/A" si manquant
        for key in key_list:
            value = element.get(key)
            if value is None:
                value = "N/A"
            result = result.replace("{" + "{}".format(key) + "}", value)

        # Crée un fichier output_X.txt avec le contenu personnalisé
        with open("output_{}.txt".format(i + 1), 'w', encoding='UTF-8') as fichier:
            fichier.write(result)
