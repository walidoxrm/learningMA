# Exemple de premier script Python
# Ce fichier montre un exemple basique que tu peux adapter à ton projet

# ============================================
# EXEMPLE 1 : Calculer une moyenne de scores
# ============================================

# Liste de scores (comme un tableau en algo)
scores = [15, 20, 18, 22, 19]

# Calculer la somme
somme = 0
for score in scores:
    somme = somme + score

# Calculer la moyenne
moyenne = somme / len(scores)

# Afficher le résultat
print("Les scores sont :", scores)
print("La moyenne est :", moyenne)

# ============================================
# EXEMPLE 2 : Tirer un élément au hasard
# ============================================

import random  # Module pour le hasard

# Liste de morceaux
morceaux = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]

# Tirer un morceau au hasard
morceau_choisi = random.choice(morceaux)
print("Morceau choisi :", morceau_choisi)

# ============================================
# EXEMPLE 3 : Question simple
# ============================================

# Question
question = "Quelle est la capitale de la France ?"
reponse_correcte = "Paris"

print(question)
reponse_utilisateur = input("Ta réponse : ")

if reponse_utilisateur == reponse_correcte:
    print("Bravo ! ✅")
else:
    print("Faux, la réponse était", reponse_correcte)

