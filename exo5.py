# Exercice 05 – Répartition optimale des titres (gabarit)
# Fait par - Hamza Gharbi et Yanis Ben Boudaoud
# Note - Avec bonus

# Étape 1 - Lire n via input (prompt EXACT) et convertir en int
n = int(input("Entrez le nombre total de trajets à effectuer : "))

# Étape 2 - Calculer la répartition exacte (30 -> 10 -> 1) et le prix total
n_30 = n // 30
r_30 = n % 30
n_10 = r_30 // 10
n_reste = r_30 % 10

prix = n_30 * 75 + n_10 * 30 + n_reste * 3.75

# Étape 3 - Affichage des résultats de la répartition exacte (4 lignes)
print(f"Carnets de 30 billets - {n_30}")
print(f"Carnets de 10 billets - {n_10}")
print(f"Billets simples - {n_reste}")     
print(f"Prix total - {prix:.2f}$")

# Étape bonus - Trouver une sur-couverture
"""
Un carnet de 30 billets = 2,50$ chaque billet
Un carnet de 10 billets = 3,00$ chaque billet
Un billet = 3,75$
Mettre un carnet de 10 billets est meilleur que 9 billets
Mettre un carnet de 30 billets est meilleur si t'as entre 26 et 29 billets
"""
surplus = 0
if n_reste == 9:
    n_reste = 0 # Met de 9 billets seuls à un carnet de 10
    n_10 += 1
    r_30 += 1
    surplus += 1
if r_30 > 25:
    if r_30 != 30:
        surplus = 30 - r_30 # Pour éviter un cas unique où le reste = 30 (quand ça passe de 29 à 30)
    n_reste = 0
    n_10 = 0
    n_30 += 1
if surplus != 0:
    nouveau_prix = n_30 * 75 + n_10 * 30 + n_reste * 3.75
    print(f"Il existe une combinaison sur-couvrante moins chère : {str(n_30)}, {str(n_10)}, {str(n_reste)} : {nouveau_prix:.2f}$ (surplus : {surplus} trajet(s))")