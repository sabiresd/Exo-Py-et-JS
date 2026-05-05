class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

        # Saisie et affichage type/id pour chaque note
        note1 = input("Entrez la note de logique     (coeff 30%): ")
        print(f"  type: {type(note1).__name__}  |  id: {id(note1)}")
        
        note2 = input("Entrez la note de Python      (coeff 35%): ")
        print(f"  type: {type(note2).__name__}  |  id: {id(note2)}")
        
        note3 = input("Entrez la note de JavaScript  (coeff 25%): ")
        print(f"  type: {type(note3).__name__}  |  id: {id(note3)}")
        
        note4 = input("Entrez la note d'API/JSON     (coeff 10%): ")
        print(f"  type: {type(note4).__name__}  |  id: {id(note4)}")

        # Conversion en int après affichage
        self.note_logique    = int(note1)
        self.note_python     = int(note2)
        self.note_javascript = int(note3)
        self.note_api        = int(note4)

    def calculer_moyenne(self):
        return (
            self.note_logique    * 0.30 +
            self.note_python     * 0.35 +
            self.note_javascript * 0.25 +
            self.note_api        * 0.10
        )

    def afficher(self):
        moyenne = self.calculer_moyenne()
        print("\n========== Fiche Étudiant ==========")
        print(f"Nom         : {self.nom}")
        print(f"Prénom      : {self.prenom}")
        print(f"Logique     : {self.note_logique}")
        print(f"Python      : {self.note_python}")
        print(f"JavaScript  : {self.note_javascript}")
        print(f"API/JSON    : {self.note_api}")
        print(f"------------------------------------")
        print(f"Moyenne     : {moyenne:.2f}/20")
        print("Résultat    :", "ADMIS ✓" if moyenne >= 10 else "REDOUBLANT ✗")
        print("====================================")


# --- Programme principal ---
nom    = input("Entrez le nom    : ")
prenom = input("Entrez le prénom : ")

etudiant = Etudiant(nom, prenom)
etudiant.afficher()