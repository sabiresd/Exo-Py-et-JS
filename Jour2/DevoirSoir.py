import re

class Etudiant:
    def __init__(self, nom, email, notes_dict, moyenne, remarque):
        self.nom = nom
        self.email = email
        self.notes_dict = notes_dict
        self.moyenne = moyenne
        self.remarque = remarque

def obtenir_remarque(moyenne):
    if moyenne >= 16: return "Excellent : Un travail remarquable."
    if moyenne >= 12: return "Satisfaisant : Bon travail d'ensemble."
    if moyenne >= 10: return "Juste : Doit redoubler d'efforts pour sécuriser l'année."
    return "Insuffisant : Un plan de soutien est nécessaire."

def systeme_evaluation():
    archive_etudiants = []
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Saisir un nouvel étudiant")
        print("2. Afficher tous les étudiants (Archive)")
        print("3. Quitter")
        
        choix_menu = input("Votre choix : ").strip()

        if choix_menu == "3":
            break

        if choix_menu == "2":
            if not archive_etudiants:
                print("\n/!\ Archive vide.")
                continue
            
            for etu in archive_etudiants:
                print(f"\n--- {etu.nom.upper()} ({etu.email}) ---")
                print(f"Moyenne : {etu.moyenne:.2f}/20")
                print(f"Remarque : {etu.remarque}")
                print("Détails : " + ", ".join([f"{m}: {n}/20" for m, n in etu.notes_dict.items()]))
            continue

        if choix_menu == "1":
            while True:
                nom = input("\nNom de l'étudiant : ").strip()
                if re.match(r"^[A-Za-zÀ-ÿ\s\-]{2,30}$", nom):
                    break
                print("✗ Erreur : Nom invalide (2-30 lettres).")

            while True:
                email = input("Email de l'étudiant : ").strip()
                if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                    break
                print("✗ Erreur : Format d'email invalide (ex: exemple@domaine.com).")

            notes_saisies = {}
            coefficients = {}
            
            while True:
                nb = input("Nombre de matières : ")
                if re.match(r"^\d+$", nb) and int(nb) > 0:
                    nb_matieres = int(nb)
                    break
                print("✗ Entrez un nombre entier supérieur à 0.")

            for i in range(nb_matieres):
                while True:
                    nom_mat = input(f"Nom matière {i+1} : ").strip()
                    if re.match(r"^[A-Za-z\s]{2,20}$", nom_mat):
                        break
                    print("✗ Nom de matière invalide.")

                while True:
                    s_note = input(f"Note {nom_mat} (0-20) : ").replace(',', '.')
                    if re.match(r"^(20(\.0+)?|[0-1]?\d(\.\d+)?|\d(\.\d+)?)$", s_note):
                        note = float(s_note)
                        notes_saisies[nom_mat] = note
                        break
                    print("✗ Note invalide (0-20).")

                while True:
                    s_coeff = input(f"Coeff {nom_mat} : ")
                    if re.match(r"^[1-9](\.\d+)?$", s_coeff):
                        coefficients[nom_mat] = float(s_coeff)
                        break
                    print("✗ Coefficient invalide.")

            total_pts = sum(notes_saisies[m] * coefficients[m] for m in notes_saisies)
            total_coef = sum(coefficients.values())
            moyenne = total_pts / total_coef
            remarque = obtenir_remarque(moyenne)

            archive_etudiants.append(Etudiant(nom, email, notes_saisies, moyenne, remarque))

            print(f"\nSaisie réussie pour {nom} ! Moyenne : {moyenne:.2f}/20")

    print("\nFin du programme.")

if __name__ == "__main__":
    systeme_evaluation()