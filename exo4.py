# Exercice 04 – Hauteur atteinte par un escalier mécanique (gabarit)
# Fait par - Hamza Gharbi

from math import sin, radians

# Étape 1 - Lire longueur et angle via input (prompts EXACTS) et convertir en float
longueur = float(input("Entrez la longueur de l'escalier (en mètres) : "))
angle = float(input("Entrez l'angle de l'escalier par rapport à l'horizontale (en degrés) : "))

# Étape 2 - Validation des entrées
if longueur < 0 or angle < 0 or angle > 90:
    print("Erreur - données invalides.")
    quit()

# Étape 3 - Calcul hauteur et affichage
hauteur = longueur * sin(radians(angle))
print(f"{hauteur:.2f} m")

