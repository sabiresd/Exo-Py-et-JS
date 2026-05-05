TVA = 30
prix_ht = input("Entrez le prix hors taxe : ")
quantity = input("Entrez la quantité : ")
prix_total_ht = int(prix_ht) * int(quantity)
prix_total_ttc = prix_total_ht + (prix_total_ht * TVA / 100)
print("Le prix total hors taxe est : " + str(prix_total_ht) + " DH")
print("Le prix total TTC est : " + str(prix_total_ttc) + " DH")
