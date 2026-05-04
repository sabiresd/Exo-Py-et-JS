# ===== Exercice 1 =====
nom = 'Sara'
age = 20
ville = 'Casablanca'
specialite = 'IA'
print(f"Bonjour, je m'appelle {nom}, j'ai {age} ans, j'habite à {ville} et je souhaite apprendre {specialite}.")


# ===== Exercice 2 =====
note = 15
if note >= 16:
    print("Excellent")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Non validé")


# ===== Exercice 3 =====
for i in range(1, 11):
    print(i)
print("Somme =", sum(range(1, 11)))


# ===== Exercice 4 =====
def calculer_moyenne(notes):
    return sum(notes) / len(notes)

print(calculer_moyenne([12, 15, 18, 10]))


# ===== Exercice 5 =====
students = ['Ali', 'Sara', 'Youssef']
for student in students:
    print('Bonjour ' + student)