# Exercice 05 – Répartition optimale des titres (gabarit)
# Fait par - Hamza Gharbi

"""
BONUS (optionnel mais recommandé) :
- Si une SUR-COUVERTURE (acheter un peu plus de trajets) est moins chère,
  afficher en plus :
  "Il existe une combinaison sur-couvrante moins chère : A, B, C : PPP.PP$ (surplus : S trajet(s))"
"""

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
Un pack de 30 billets = 2,50$ chaque
Un pack de 10 billets = 3,00$ chaque
Un billet = 3,75$
10 billets > 1 billets si ça termine à 9 billets
30 billets > 10 si c'est à 26-29 billets
"""

surplus = 0
if n_reste == 9:
    n_reste = 0
    n_10 += 1
    r_30 += 1
    surplus += 1
if r_30 > 25:
    if r_30 != 30:
        surplus = 30 - r_30
    n_reste = 0
    n_10 = 0
    n_30 += 1
if surplus != 0:
    prix = n_30 * 75 + n_10 * 30 + n_reste * 3.75
    print(f"Il existe une combinaison sur-couvrante moins chère : {str(n_30)}, {str(n_10)}, {str(n_reste)} : {prix:.2f}$ (surplus : {surplus} trajet(s))")