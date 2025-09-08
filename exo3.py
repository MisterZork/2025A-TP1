# Exercice 03 – Marcher ou attendre le bus ? (gabarit)
# Fait par - Hamza Gharbi

# Étape 1 - Lire distance et attente via input
dist = float(input("Entrez la distance jusqu'à la destination (en kilomètres) : "))
attente = float(input("Entrez le temps d'attente avant le prochain bus (en minutes) : "))

# Étape 2 - Calcul temps_marche et temps_bus (en minutes)
temps_marche = dist * 60 / 5
temps_bus = attente + dist * 60 / 20

# Étape 3 - Comparaison et affichage de la phrase EXACTE
if temps_marche < temps_bus:
    print("Il est plus rapide de marcher.")
elif temps_marche > temps_bus:
    print("Il est plus rapide de prendre le bus.")
else:
    print("Les deux options prennent le même temps.")

# TODO : Demander au prof si on peux vérifier que les valeurs soient positives.