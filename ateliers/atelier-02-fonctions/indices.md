# Indices - Atelier 2

## 🔑 Fonctions en Python

### Syntaxe de base

```python
# Fonction sans paramètre
def dire_bonjour():
    print("Bonjour !")

# Appeler la fonction
dire_bonjour()
```

### Fonction avec paramètres

```python
# Fonction qui prend des paramètres
def calculer_moyenne(scores):
    somme = 0
    for score in scores:
        somme = somme + score
    moyenne = somme / len(scores)
    return moyenne

# Utiliser la fonction
mes_scores = [15, 20, 18]
resultat = calculer_moyenne(mes_scores)
print("Moyenne :", resultat)
```

### Fonction qui retourne une valeur

```python
# Le mot-clé 'return' renvoie une valeur
def additionner(a, b):
    resultat = a + b
    return resultat

# Utiliser le résultat
somme = additionner(5, 3)
print(somme)  # Affiche 8
```

### Fonction sans retour (procédure)

```python
# Fonction qui ne retourne rien (juste affiche)
def afficher_scores(scores):
    print("Les scores sont :")
    for score in scores:
        print("-", score)
    # Pas de return, ou return None

afficher_scores([15, 20, 18])
```

## 📥 Interaction avec l'utilisateur

### Lire une entrée

```python
# input() attend que l'utilisateur tape quelque chose
nom = input("Quel est ton nom ? ")
print("Bonjour", nom)

# Attention : input() retourne toujours une chaîne de caractères !
age_str = input("Quel est ton âge ? ")
age = int(age_str)  # Convertir en nombre entier
```

### Convertir les types

```python
# Convertir une chaîne en nombre
nombre_str = input("Entrez un nombre : ")
nombre = int(nombre_str)  # Pour un entier
# ou
nombre = float(nombre_str)  # Pour un décimal

# Convertir un nombre en chaîne
age = 25
age_str = str(age)
```

## 🎯 Exemple complet : Menu interactif

```python
def afficher_menu():
    print("=== Menu ===")
    print("1. Calculer la moyenne")
    print("2. Afficher les scores")
    print("3. Quitter")

def calculer_moyenne(scores):
    if len(scores) == 0:
        return 0
    somme = sum(scores)
    return somme / len(scores)

def afficher_scores(scores):
    print("Les scores sont :")
    for i, score in enumerate(scores):
        print(f"  {i+1}. {score}")

# Programme principal
scores = []

while True:
    afficher_menu()
    choix = input("Choisis une option (1-3) : ")
    
    if choix == "1":
        moyenne = calculer_moyenne(scores)
        print(f"La moyenne est : {moyenne}")
    elif choix == "2":
        afficher_scores(scores)
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Option invalide !")
```

## 🔄 Boucle principale

```python
# Boucle infinie (se termine avec break)
while True:
    # Code qui se répète
    choix = input("Continue ? (o/n) : ")
    if choix == "n":
        break  # Sortir de la boucle
```

## 💡 Bonnes pratiques

1. **Nommer clairement tes fonctions**
   ```python
   # ✅ Bon
   def calculer_moyenne(scores):
   
   # ❌ Mauvais
   def calc(s):
   ```

2. **Une fonction = une responsabilité**
   ```python
   # ✅ Bon : deux fonctions séparées
   def calculer_moyenne(scores):
       # ...
   
   def afficher_moyenne(moyenne):
       # ...
   
   # ❌ Moins bon : tout mélangé
   def tout_faire(scores):
       # calcule ET affiche
   ```

3. **Documenter avec des commentaires**
   ```python
   def calculer_moyenne(scores):
       """
       Calcule la moyenne d'une liste de scores.
       
       Paramètres:
       - scores: liste de nombres
       
       Retourne:
       - la moyenne (float)
       """
       # Code ici...
   ```

## 🐛 Erreurs fréquentes

1. **Oublier les deux-points après `def`**
   ```python
   # ❌ Faux
   def ma_fonction()
   
   # ✅ Correct
   def ma_fonction():
   ```

2. **Oublier le `return` si tu veux récupérer une valeur**
   ```python
   # ❌ Faux
   def additionner(a, b):
       resultat = a + b
       # Oubli du return !
   
   # ✅ Correct
   def additionner(a, b):
       resultat = a + b
       return resultat
   ```

3. **Confondre `print` et `return`**
   ```python
   # print() affiche mais ne retourne rien
   def mauvaise_fonction():
       print(5)  # Affiche 5 mais ne retourne rien
   
   # return retourne une valeur qu'on peut utiliser
   def bonne_fonction():
       return 5  # Retourne 5 qu'on peut stocker dans une variable
   ```

