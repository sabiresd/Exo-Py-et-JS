import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Chemin du fichier CSV (à adapter selon ton PC)
file_path = r"C:\Users\LENOVO\Downloads\etudiants_marocains_notes.csv"

def charger_donnees():
    """Charge le fichier CSV dans un DataFrame Pandas."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print("✗ Erreur : Le fichier est introuvable au chemin spécifié.")
        return None

def sauvegarder_donnees(df):
    """Enregistre les modifications dans le fichier CSV."""
    df.to_csv(file_path, index=False, encoding='utf-8-sig')
    print("✓ Modifications enregistrées avec succès.")

def afficher_stats(df, cols_notes):
    """Sous-menu pour les analyses statistiques avec NumPy."""
    while True:
        print("\n--- 📊 SOUS-MENU STATISTIQUES ---")
        print("a. Global (Max, Min, Moyenne de la classe)")
        print("b. Par Matière (Moyenne, Max, Min)")
        print("c. Taux de réussite (Valides vs Non-Valides)")
        print("q. Retour au menu principal")
        
        sub_choix = input("Votre choix : ").lower()

        # Transformation des notes en matrice NumPy pour la performance
        notes_array = df[cols_notes].to_numpy()
        # Calcul des moyennes par étudiant (ligne par ligne)
        moyennes_etudiants = df[cols_notes].mean(axis=1)

        if sub_choix == "a":
            print(f"\n[GLOBAL] Note Max : {np.max(notes_array)}")
            print(f"[GLOBAL] Note Min : {np.min(notes_array)}")
            print(f"[GLOBAL] Moyenne Générale : {np.mean(notes_array):.2f}")
        
        elif sub_choix == "b":
            print("\n--- DÉTAILS PAR MATIÈRE ---")
            stats_mat = pd.DataFrame({
                'Moyenne': df[cols_notes].mean(),
                'Max': df[cols_notes].max(),
                'Min': df[cols_notes].min()
            })
            print(stats_mat)

        elif sub_choix == "c":
            valides = np.sum(moyennes_etudiants >= 10)
            non_valides = np.sum(moyennes_etudiants < 10)
            total = len(df)
            print(f"\n--- RÉSULTATS D'ADMISSION ---")
            print(f"Admis (Moyenne >= 10)   : {valides} ({ (valides/total)*100:.1f}%)")
            print(f"Ajournés (Moyenne < 10) : {non_valides} ({ (non_valides/total)*100:.1f}%)")

        elif sub_choix == "q":
            break

def visualiser_donnees(df, cols_notes):
    """Génère des graphiques pour visualiser les résultats."""
    print("\n--- 📈 GÉNÉRATION DES GRAPHIQUES ---")
    print("1. Bar Chart : Moyennes par matière")
    print("2. Pie Chart : Répartition Admis / Ajournés")
    print("q. Annuler")
    
    choix_visu = input("Votre choix : ")

    if choix_visu == "1":
        df[cols_notes].mean().plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title("Moyenne par Matière")
        plt.ylabel("Note / 20")
        plt.show()

    elif choix_visu == "2":
        moyennes = df[cols_notes].mean(axis=1)
        valides = np.sum(moyennes >= 10)
        non_valides = np.sum(moyennes < 10)
        
        plt.pie([valides, non_valides], labels=['Admis', 'Ajournés'], autopct='%1.1f%%', colors=['#66b3ff','#ff9999'])
        plt.title("Répartition de la réussite")
        plt.show()

def menu():
    """Menu principal de l'application."""
    df = charger_donnees()
    if df is None: return

    # Détection automatique des colonnes contenant des notes
    cols_notes = [c for c in df.columns if 'Note' in c]

    while True:
        print("\n" + "="*30)
        print("   SYSTÈME DE GESTION SCOLAIRE")
        print("="*30)
        print("1. Statistiques avancées")
        print("2. Ajouter un nouvel étudiant")
        print("3. Supprimer un étudiant")
        print("4. Visualisation Graphique")
        print("5. Afficher la liste complète")
        print("6. Quitter")
        
        choix = input("\nVotre choix : ")

        if choix == "1":
            afficher_stats(df, cols_notes)

        elif choix == "2":
            nouveau = {'Nom': input("Nom : "), 'Prénom': input("Prénom : ")}
            for col in cols_notes:
                nouveau[col] = float(input(f"Note {col} : "))
            df = pd.concat([df, pd.DataFrame([nouveau])], ignore_index=True)
            sauvegarder_donnees(df)

        elif choix == "3":
            print(df[['Nom', 'Prénom']])
            idx = int(input("Index de l'étudiant à supprimer : "))
            if idx in df.index:
                df = df.drop(idx)
                sauvegarder_donnees(df)
            else:
                print("✗ Index invalide.")

        elif choix == "4":
            visualiser_donnees(df, cols_notes)

        elif choix == "5":
            print("\n", df.to_string())

        elif choix == "6":
            print("Au revoir !")
            break

if __name__ == "__main__":
    menu()