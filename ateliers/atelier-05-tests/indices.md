# Indices - Atelier 5

## 🧪 Écrire des tests simples

### Tests manuels (sans librairie)

```python
# test_calculs.py

def test_calculer_moyenne():
    """Test de la fonction calculer_moyenne."""
    from calculs import calculer_moyenne
    
    # Test cas normal
    scores = [15, 20, 18]
    resultat = calculer_moyenne(scores)
    assert resultat == (15 + 20 + 18) / 3, "La moyenne devrait être 17.67"
    print("✅ Test cas normal : OK")
    
    # Test cas limite : liste vide
    resultat = calculer_moyenne([])
    assert resultat == 0, "La moyenne d'une liste vide devrait être 0"
    print("✅ Test liste vide : OK")
    
    # Test avec un seul élément
    resultat = calculer_moyenne([20])
    assert resultat == 20, "La moyenne d'un seul élément devrait être l'élément"
    print("✅ Test un seul élément : OK")

# Lancer les tests
if __name__ == "__main__":
    test_calculer_moyenne()
    print("\n🎉 Tous les tests passent !")
```

### Utiliser pytest (recommandé)

```bash
# Installer pytest
pip install pytest
```

```python
# test_calculs.py
import pytest
from calculs import calculer_moyenne

def test_moyenne_liste_normale():
    """Test avec une liste normale."""
    scores = [15, 20, 18]
    assert calculer_moyenne(scores) == pytest.approx(17.67, rel=0.01)

def test_moyenne_liste_vide():
    """Test avec une liste vide."""
    assert calculer_moyenne([]) == 0

def test_moyenne_un_element():
    """Test avec un seul élément."""
    assert calculer_moyenne([20]) == 20
```

Lancer avec : `pytest test_calculs.py`

## 🐛 Déboguer avec print()

```python
def calculer_moyenne(scores):
    print(f"DEBUG: scores reçus = {scores}")  # Voir ce qui est passé
    print(f"DEBUG: type = {type(scores)}")     # Vérifier le type
    
    somme = 0
    for score in scores:
        print(f"DEBUG: ajout de {score}")      # Voir chaque itération
        somme = somme + score
    
    print(f"DEBUG: somme = {summe}")           # Vérifier la somme
    print(f"DEBUG: longueur = {len(scores)}")  # Vérifier la longueur
    
    moyenne = somme / len(scores)
    print(f"DEBUG: moyenne = {moyenne}")      # Voir le résultat
    
    return moyenne
```

## 🔍 Utiliser le débogueur de VS Code

1. **Placer un point d'arrêt** : clique à gauche du numéro de ligne (un point rouge apparaît)

2. **Lancer en mode débogage** : appuie sur F5 ou clique sur "Run and Debug"

3. **Contrôles** :
   - **F10** : exécuter ligne par ligne (step over)
   - **F11** : entrer dans les fonctions (step into)
   - **F5** : continuer jusqu'au prochain point d'arrêt

4. **Inspecter les variables** : dans le panneau de gauche, tu vois toutes les variables et leurs valeurs

## ⚠️ Gérer les erreurs avec try/except

### Syntaxe de base

```python
try:
    # Code qui peut planter
    score = int(input("Entrez un score : "))
    print(f"Score : {score}")
except ValueError:
    # Ce qui se passe si une erreur ValueError se produit
    print("Erreur : vous devez entrer un nombre entier.")
except Exception as e:
    # Gérer toutes les autres erreurs
    print(f"Une erreur s'est produite : {e}")
```

### Exemples pratiques

```python
# Gérer la division par zéro
def calculer_moyenne(scores):
    try:
        if len(scores) == 0:
            return 0
        return sum(scores) / len(scores)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("Erreur : les scores doivent être des nombres.")
        return None

# Gérer les erreurs de fichier
def charger_scores():
    try:
        with open("scores.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Fichier non trouvé. Création d'une nouvelle liste.")
        return []
    except json.JSONDecodeError:
        print("Erreur : le fichier JSON est invalide.")
        return []
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return []
```

### Lever des erreurs personnalisées

```python
def valider_score(score):
    """Valide un score et lève une erreur si invalide."""
    if not isinstance(score, (int, float)):
        raise ValueError("Le score doit être un nombre.")
    if score < 0:
        raise ValueError("Le score ne peut pas être négatif.")
    if score > 100:
        raise ValueError("Le score ne peut pas dépasser 100.")
    return True

# Utilisation
try:
    valider_score(150)
except ValueError as e:
    print(f"Erreur de validation : {e}")
```

## 🎯 Identifier les cas limites

Pour chaque fonction, demande-toi :

1. **Que se passe-t-il si...**
   - La liste est vide ?
   - La liste contient un seul élément ?
   - Les données sont du mauvais type ?
   - Les valeurs sont négatives ou trop grandes ?
   - Le fichier n'existe pas ?
   - Le fichier est vide ?
   - Le fichier contient des données invalides ?

2. **Exemples de cas limites**

```python
# Fonction calculer_moyenne()
# Cas limites :
# - Liste vide → retourner 0 ou None ?
# - Liste avec None → comment gérer ?
# - Liste avec des strings → erreur ou conversion ?

# Fonction charger_scores()
# Cas limites :
# - Fichier n'existe pas → créer par défaut
# - Fichier vide → retourner liste vide
# - Fichier corrompu → gérer l'erreur JSON
# - Fichier avec mauvais format → valider les données
```

## 📝 Exemple complet : Fonction robuste

```python
def ajouter_score(scores, score_input):
    """
    Ajoute un score à la liste après validation.
    Gère toutes les erreurs possibles.
    """
    try:
        # Convertir en nombre
        score = float(score_input)
        
        # Valider la plage
        if score < 0:
            raise ValueError("Le score ne peut pas être négatif.")
        if score > 100:
            raise ValueError("Le score ne peut pas dépasser 100.")
        
        # Ajouter le score
        scores.append(score)
        return True, f"Score {score} ajouté avec succès !"
        
    except ValueError as e:
        # Erreur de conversion ou validation
        return False, f"Erreur : {e}"
    except Exception as e:
        # Erreur inattendue
        return False, f"Erreur inattendue : {e}"

# Utilisation
scores = []
succes, message = ajouter_score(scores, "20")
if succes:
    print(f"✅ {message}")
else:
    print(f"❌ {message}")
```

## 🐛 Messages d'erreur utiles

```python
# ❌ Mauvais message d'erreur
print("Erreur")

# ✅ Bon message d'erreur
print("Erreur : impossible de charger les scores. Le fichier 'scores.json' est introuvable ou corrompu.")
print("Solution : le fichier sera créé automatiquement avec une liste vide.")
```

## 💡 Bonnes pratiques

1. **Tester d'abord, coder après** (TDD - Test Driven Development)
   - Écris d'abord un test qui échoue
   - Puis écris le code pour que le test passe

2. **Un test = une chose**
   - Chaque test vérifie une seule fonctionnalité
   - Nomme clairement tes tests : `test_moyenne_liste_vide()`

3. **Gérer les erreurs gracieusement**
   - N'affiche jamais de messages d'erreur techniques à l'utilisateur
   - Explique ce qui s'est passé et comment résoudre

4. **Documenter les cas limites**
   - Dans les commentaires, liste les cas que ta fonction gère

