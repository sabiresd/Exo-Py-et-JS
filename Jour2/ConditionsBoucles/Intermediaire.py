# ============ FONCTIONS UTILITAIRES ============

def saisir_note_valide(message):
    while True:
        saisie = input(message).strip()
        if saisie == "":
            print("Erreur ✗ — la note ne peut pas être vide.")
            continue
        try:
            note = float(saisie)
            if 0 <= note <= 20:
                return note
            else:
                print("Note invalide ✗ — doit être entre 0 et 20, réessayez.")
        except ValueError:
            print("Erreur ✗ — veuillez entrer un nombre, pas du texte.")

def saisir_nom_valide(message):
    while True:
        saisie = input(message).strip()
        if saisie == "":
            print("Erreur ✗ — ce champ ne peut pas être vide.")
        elif any(char.isdigit() for char in saisie):
            print("Erreur ✗ — le nom ne peut pas contenir de chiffres.")
        else:
            return saisie

def saisir_coefficient_valide(matiere):
    while True:
        saisie = input(f"Coefficient de {matiere} (ex: 30 pour 30%) : ").strip()
        if saisie == "":
            print("Erreur ✗ — le coefficient ne peut pas être vide.")
            continue
        try:
            coeff = float(saisie)
            if 0 < coeff <= 100:
                return coeff / 100
            else:
                print("Erreur ✗ — le coefficient doit être entre 1 et 100.")
        except ValueError:
            print("Erreur ✗ — veuillez entrer un nombre, pas du texte.")

def get_mention(note):
    if note >= 16:
        return "Très Bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez Bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"

def saisir_matieres_coefficients():
    matieres     = []
    coefficients = []

    while True:
        saisie = input("Combien de matières ? ").strip()
        if saisie == "":
            print("Erreur ✗ — ce champ ne peut pas être vide.")
            continue
        try:
            nombre = int(saisie)
            if nombre > 0:
                break
            else:
                print("Erreur ✗ — le nombre de matières doit être supérieur à 0.")
        except ValueError:
            print("Erreur ✗ — veuillez entrer un nombre entier.")

    for i in range(1, nombre + 1):
        matiere = saisir_nom_valide(f"Nom de la matière {i} : ")
        coeff   = saisir_coefficient_valide(matiere)
        matieres.append(matiere)
        coefficients.append(coeff)

    total_coeff = sum(coefficients)
    if round(total_coeff, 2) != 1.0:
        print(f"⚠ Attention : la somme des coefficients est {total_coeff:.0%} (devrait être 100%)")

    return matieres, coefficients


# ============ FONCTIONS PRINCIPALES ============

def classification_etudiant():
    print("\n--- 1. Classification d'un étudiant ---")
    note = saisir_note_valide("Entrez la note : ")
    print(f"Mention : {get_mention(note)}")

def calculer_moyenne():
    print("\n--- 2. Calcul de moyenne ---")
    matieres, coefficients = saisir_matieres_coefficients()
    notes = []

    for i, matiere in enumerate(matieres):
        note = saisir_note_valide(f"Note en {matiere} (coeff {coefficients[i]:.0%}) : ")
        notes.append(note)

    moyenne = sum(n * c for n, c in zip(notes, coefficients))
    print(f"\nMoyenne pondérée : {moyenne:.2f}/20")
    print(f"Mention          : {get_mention(moyenne)}")

def fiche_etudiant():
    print("\n--- 3. Fiche étudiant ---")
    nom    = saisir_nom_valide("Nom    : ")
    prenom = saisir_nom_valide("Prénom : ")

    matieres, coefficients = saisir_matieres_coefficients()
    notes = []

    for matiere in matieres:
        note = saisir_note_valide(f"Note en {matiere} : ")
        notes.append(note)

    moyenne = sum(n * c for n, c in zip(notes, coefficients))

    print("\n========== Fiche Étudiant ==========")
    print(f"Nom         : {nom}")
    print(f"Prénom      : {prenom}")
    print("------------------------------------")
    for i, matiere in enumerate(matieres):
        print(f"{matiere:15} : {notes[i]:.2f}/20")
    print("------------------------------------")
    print(f"Moyenne     : {moyenne:.2f}/20")
    print(f"Mention     : {get_mention(moyenne)}")
    print("Résultat    :", "ADMIS ✓" if moyenne >= 10 else "REDOUBLANT ✗")
    print("====================================")

# ============ PROGRAMME PRINCIPAL ============

choix = ""
while choix != "0":
    print("\n==============================")
    print("       MENU PRINCIPAL        ")
    print("==============================")
    print("1. Classification d'un étudiant")
    print("2. Calculer une moyenne")
    print("3. Fiche étudiant complète")
    print("0. Quitter")
    choix = input("Choisissez une option : ")

    if choix == "1":
        classification_etudiant()
    elif choix == "2":
        calculer_moyenne()
    elif choix == "3":
        fiche_etudiant()
    elif choix == "0":
        print("Au revoir !")
    else:
        print("Choix invalide, réessayez.")