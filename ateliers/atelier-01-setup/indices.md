# Indices - Atelier 1

## 🔑 Syntaxe Python de base

### Variables
En Python, pas besoin de déclarer le type. C'est automatique !

```python
# En algo tu écrirais : "score = 15"
# En Python c'est exactement pareil !
score = 15
nom = "Mohamed"
moyenne = 18.5
```

### Listes (tableaux)
```python
# Créer une liste
scores = [15, 20, 18, 22, 19]

# Accéder à un élément (indice commence à 0)
premier_score = scores[0]  # vaut 15

# Longueur d'une liste
nombre_scores = len(scores)  # vaut 5

# Ajouter un élément
scores.append(25)
```

### Afficher du texte
```python
# Afficher du texte
print("Bonjour !")
print("Mon score est", score)

# Afficher plusieurs choses
print("Score:", score, "Moyenne:", moyenne)
```

### Calculs
```python
# Les opérations sont comme en algo
somme = 10 + 5
produit = 3 * 4
division = 15 / 3
reste = 10 % 3  # modulo (reste de la division)
```

### Boucles
```python
# Boucle for (parcourir une liste)
scores = [15, 20, 18]
for score in scores:
    print(score)

# Boucle for avec indice
for i in range(len(scores)):
    print("Score", i, ":", scores[i])

# Boucle while (comme en algo)
i = 0
while i < 5:
    print(i)
    i = i + 1
```

### Conditions
```python
# if/else (comme en algo)
if score > 20:
    print("Excellent !")
elif score > 15:
    print("Bien !")
else:
    print("Peut mieux faire")
```

## 🎯 Exemple complet : Calculer une moyenne

```python
# Liste de scores
scores = [15, 20, 18, 22, 19]

# Calculer la somme
somme = 0
for score in scores:
    somme = somme + score

# Calculer la moyenne
moyenne = somme / len(scores)

# Afficher le résultat
print("La moyenne est :", moyenne)
```

## 🐛 Erreurs fréquentes

1. **Oubli des deux-points `:` après `if`, `for`, `while`**
   ```python
   # ❌ Faux
   if score > 20
   
   # ✅ Correct
   if score > 20:
   ```

2. **Indentation (espaces au début de la ligne)**
   - En Python, l'indentation est obligatoire !
   - Utilise 4 espaces (ou une tabulation)
   ```python
   # ✅ Correct
   if score > 20:
       print("Excellent")
   
   # ❌ Faux (pas d'indentation)
   if score > 20:
   print("Excellent")
   ```

3. **Guillemets pour les chaînes de caractères**
   ```python
   # ✅ Correct
   nom = "Mohamed"
   nom = 'Mohamed'
   
   # ❌ Faux
   nom = Mohamed  # Python pense que c'est une variable
   ```

## 💡 Astuce

Si tu as une erreur, lis le message d'erreur ! Il te dit souvent exactement où est le problème (ligne et type d'erreur).

