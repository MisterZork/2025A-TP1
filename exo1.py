# Exercice 01 – Usage hebdomadaire du métro (gabarit)
# Fait par - Hamza Gharbi

# Étape 1 - Demander à l'utilisateur les informations d'entrée (nom et déplacements hebdomadaires)
nom = str(input("Veuillez entrer votre nom complet : "))
nb_mouvement = int(input("Veuillez entrer le nombre de déplacements par semaine : "))

# Étape 2 - Faire le calcul des déplacements annuels
mouvement_annuels = nb_mouvement * 52 # Considérant qu'il y a 52 semaines en 1 année

# Étape 3 - Afficher la réponse de sortie
print(f"Bonjour {nom}")
print(f"Vous effectuez environ {mouvement_annuels} déplacements par an sur le réseau STM.")

# TODO : Demander au prof si on doit vérifier le nb_mouvement en nombre ENTIER