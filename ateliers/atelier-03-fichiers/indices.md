# Indices - Atelier 3

## 🔑 Travailler avec des fichiers

### Lire un fichier texte simple

```python
# Ouvrir et lire un fichier
with open("mon_fichier.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    print(contenu)

# Lire ligne par ligne
with open("mon_fichier.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne.strip())  # strip() enlève les retours à la ligne
```

### Écrire dans un fichier texte

```python
# Écrire dans un fichier (écrase le contenu existant)
with open("mon_fichier.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Première ligne\n")
    fichier.write("Deuxième ligne\n")

# Ajouter à la fin d'un fichier (sans écraser)
with open("mon_fichier.txt", "a", encoding="utf-8") as fichier:
    fichier.write("Nouvelle ligne\n")
```

## 📄 Format JSON (recommandé pour commencer)

JSON est un format simple pour stocker des données structurées.

### Structure JSON

```json
{
  "scores": [15, 20, 18, 22, 19],
  "joueur": "Mohamed",
  "date": "2024-01-15"
}
```

### Lire un fichier JSON

```python
import json

# Lire un fichier JSON
with open("donnees.json", "r", encoding="utf-8") as fichier:
    donnees = json.load(fichier)

# Utiliser les données
scores = donnees["scores"]
print(scores)
```

### Écrire dans un fichier JSON

```python
import json

# Données à sauvegarder
donnees = {
    "scores": [15, 20, 18, 22, 19],
    "joueur": "Mohamed"
}

# Sauvegarder
with open("donnees.json", "w", encoding="utf-8") as fichier:
    json.dump(donnees, fichier, indent=2, ensure_ascii=False)
```

### Gérer le cas où le fichier n'existe pas

```python
import json
from pathlib import Path

def charger_donnees(nom_fichier):
    """Charge les données depuis un fichier JSON."""
    fichier = Path(nom_fichier)
    
    # Si le fichier n'existe pas, retourner des données par défaut
    if not fichier.exists():
        return {"scores": []}  # Données par défaut
    
    # Sinon, lire le fichier
    with open(nom_fichier, "r", encoding="utf-8") as f:
        return json.load(f)
```

## 📊 Format CSV (pour des tableaux)

### Lire un CSV

```python
import csv

# Lire un fichier CSV
with open("joueurs.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        print(ligne["nom"], ligne["score"])

# Ou avec csv.reader (liste de listes)
with open("joueurs.csv", "r", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        print(ligne)
```

### Écrire un CSV

```python
import csv

# Écrire dans un CSV
donnees = [
    {"nom": "Mohamed", "score": 20},
    {"nom": "Ahmed", "score": 18}
]

with open("joueurs.csv", "w", encoding="utf-8", newline="") as fichier:
    writer = csv.DictWriter(fichier, fieldnames=["nom", "score"])
    writer.writeheader()  # Écrire l'en-tête
    writer.writerows(donnees)
```

## 🎯 Exemple complet : Gestion de scores

```python
import json
from pathlib import Path

FICHIER_SCORES = "scores.json"

def charger_scores():
    """Charge les scores depuis le fichier."""
    fichier = Path(FICHIER_SCORES)
    
    if not fichier.exists():
        return []  # Liste vide si le fichier n'existe pas
    
    try:
        with open(FICHIER_SCORES, "r", encoding="utf-8") as f:
            donnees = json.load(f)
            return donnees.get("scores", [])
    except json.JSONDecodeError:
        print("Erreur : le fichier JSON est invalide.")
        return []

def sauvegarder_scores(scores):
    """Sauvegarde les scores dans le fichier."""
    donnees = {"scores": scores}
    
    with open(FICHIER_SCORES, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2, ensure_ascii=False)
    
    print("Scores sauvegardés !")

# Utilisation
scores = charger_scores()  # Charger au démarrage
print("Scores actuels :", scores)

# Ajouter un score
scores.append(25)

# Sauvegarder
sauvegarder_scores(scores)
```

## ✅ Valider les données

```python
def valider_scores(scores):
    """
    Vérifie que les scores sont valides.
    Retourne True si valide, False sinon.
    """
    if not isinstance(scores, list):
        return False
    
    for score in scores:
        if not isinstance(score, (int, float)):
            return False
        if score < 0 or score > 100:  # Exemple : scores entre 0 et 100
            return False
    
    return True

# Utilisation
scores = charger_scores()
if valider_scores(scores):
    print("Données valides !")
else:
    print("Erreur : données invalides.")
    scores = []  # Réinitialiser
```

## 🐛 Erreurs fréquentes

1. **Oublier de fermer le fichier**
   ```python
   # ❌ Mauvais (fichier reste ouvert)
   fichier = open("test.txt", "r")
   contenu = fichier.read()
   # Oubli de fichier.close()
   
   # ✅ Bon (utilise 'with' qui ferme automatiquement)
   with open("test.txt", "r") as fichier:
       contenu = fichier.read()
   ```

2. **Erreur si le fichier n'existe pas**
   ```python
   # ❌ Erreur si le fichier n'existe pas
   with open("test.txt", "r") as f:
       contenu = f.read()
   
   # ✅ Vérifier d'abord
   from pathlib import Path
   if Path("test.txt").exists():
       with open("test.txt", "r") as f:
           contenu = f.read()
   ```

3. **Problème d'encodage (caractères spéciaux)**
   ```python
   # ✅ Toujours spécifier l'encodage
   with open("fichier.txt", "r", encoding="utf-8") as f:
       contenu = f.read()
   ```

## 💡 Astuce

Pour déboguer, affiche les données après les avoir chargées :
```python
scores = charger_scores()
print("Données chargées :", scores)  # Voir ce qui a été lu
```

