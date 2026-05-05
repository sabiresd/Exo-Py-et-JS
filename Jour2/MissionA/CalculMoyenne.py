somme = 0
note1 = input("Entrez la première note : ")
somme += int(note1)
note2 = input("Entrez la deuxième note : ") 
somme += int(note2)
note3 = input("Entrez la troisième note : ")
somme += int(note3)
moyenne = somme / 3
print("La moyenne des trois notes est : " + str(moyenne))