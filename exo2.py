# Exercice 02 – Taux d’occupation d’un bus (gabarit)
# Fait par - Hamza Gharbi et Yanis Ben Boudaoud

# Étape 1 - Demander à l'utilisateur le taux d'occupation et vérifier sa validité
taux = int(input("Entrez le taux d'occupation d'un bus (en %): "))
if taux < 0 or taux > 100:
    print("Taux d'occupation invalide.") # À corriger selon le résultat du issue sur GitHub
    quit()

# Étape 2 - Calculer les valeurs des blocs qui vont s'afficher dans la barre.
blocs = (taux + 5) // 10

# Étape 3 - Affichage final du programme
print("[" + "❚" * blocs + " " * (10 - blocs) + "]")
print(f"{taux}%")
