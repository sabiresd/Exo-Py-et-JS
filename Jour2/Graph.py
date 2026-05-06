import networkx as nx
import matplotlib.pyplot as plt

def creer_graphe_manuel():
    G = nx.Graph()

    # 1. Saisie des Nœuds
    try:
        nb_noeuds = int(input("Combien de nœuds voulez-vous créer ? "))
        for i in range(nb_noeuds):
            nom_noeud = input(f"Nom du nœud n°{i+1} : ").strip()
            G.add_node(nom_noeud)
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier.")
        return None

    # 2. Saisie des Arêtes (Liens)
    try:
        nb_aretes = int(input("\nCombien d'arêtes (liens) voulez-vous créer ? "))
        print("Format : noeud1,noeud2 (ex: A,B)")
        
        compteur = 0
        while compteur < nb_aretes:
            lien = input(f"Arête n°{compteur+1} : ").strip()
            if "," in lien:
                u, v = lien.split(",")
                u, v = u.strip(), v.strip()
                
                if G.has_node(u) and G.has_node(v):
                    G.add_edge(u, v)
                    compteur += 1
                else:
                    print(f"✗ Erreur : L'un des nœuds ({u} ou {v}) n'existe pas.")
            else:
                print("✗ Format invalide. Utilisez la virgule (ex: A,B).")
    except ValueError:
        print("Erreur : Nombre d'arêtes invalide.")
        return None

    return G

def menu_graphe(G):
    if G is None: return

    while True:
        print("\n--- MENU GRAPHE ---")
        print("1. Afficher le graphe (Visualisation)")
        print("2. Calculer le plus court chemin")
        print("3. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, font_weight='bold')
            plt.title("Votre Graphe Personnalisé")
            plt.show()

        elif choix == "2":
            depart = input("Nœud de départ : ").strip()
            arrivee = input("Nœud d'arrivée : ").strip()
            
            try:
                # Calcul du chemin le plus court (Algorithme de Dijkstra par défaut)
                chemin = nx.shortest_path(G, source=depart, target=arrivee)
                print(f"✔ Plus court chemin trouvé : {' -> '.join(chemin)}")
            except nx.NetworkXNoPath:
                print("✗ Aucun chemin n'existe entre ces deux nœuds.")
            except nx.NodeNotFound as e:
                print(f"✗ Erreur : {e}")

        elif choix == "3":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide.")

# Lancement du programme
mon_graphe = creer_graphe_manuel()
menu_graphe(mon_graphe)