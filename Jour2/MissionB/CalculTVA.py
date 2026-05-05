TVA = float(input("Entrez le taux de TVA en pourcentage : "))
prix_ht = float(input("Entrez le prix hors taxe : "))
quantity = int(input("Entrez la quantité : "))
prix_total_ht = prix_ht * quantity
prix_total_ttc = prix_total_ht + (prix_total_ht * TVA / 100)
print("Le prix total hors taxe est : " + str(prix_total_ht) + " DH")
print("Le prix total TTC est : " + str(prix_total_ttc) + " DH")
