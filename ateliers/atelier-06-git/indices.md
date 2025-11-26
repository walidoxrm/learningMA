# Indices - Atelier 6

## 📝 Écrire un bon README

### Structure d'un README

```markdown
# Nom de ton projet

Une courte description de ce que fait ton projet.

## 🎯 Fonctionnalités

- Fonctionnalité 1
- Fonctionnalité 2
- Fonctionnalité 3

## 📦 Installation

1. Clone le dépôt (ou télécharge les fichiers)
2. Installe les dépendances : `pip install rich`
3. Lance le programme : `python main.py`

## 🚀 Utilisation

### Exemple basique

```python
python main.py
```

### Ajouter un score

1. Choisis l'option 1 dans le menu
2. Entre un score entre 0 et 100
3. Le score est automatiquement sauvegardé

## 📁 Structure du projet

```
mon-projet/
├── main.py          # Point d'entrée
├── data.py          # Gestion des données
├── ui.py            # Interface utilisateur
├── calculs.py       # Fonctions de calcul
├── scores.json      # Fichier de données
└── README.md        # Ce fichier
```

## 🛠️ Technologies utilisées

- Python 3.x
- rich (pour l'interface)
- JSON (pour les données)

## 📝 Licence

Ce projet est libre d'utilisation pour l'apprentissage.
```

## 🔧 Git - Les bases

### Installation

```bash
# Vérifier si Git est installé
git --version

# Si pas installé, télécharge depuis git-scm.com
```

### Configuration initiale

```bash
# Configurer ton nom et email (une seule fois)
git config --global user.name "Ton Nom"
git config --global user.email "ton.email@example.com"
```

### Commandes essentielles

```bash
# Initialiser un dépôt Git dans ton dossier
git init

# Voir l'état des fichiers (qu'est-ce qui a changé ?)
git status

# Ajouter des fichiers au "staging area"
git add main.py
git add data.py
# Ou ajouter tous les fichiers modifiés
git add .

# Faire un commit (sauvegarder une version)
git commit -m "Ajout du menu principal et des fonctions de calcul"

# Voir l'historique des commits
git log

# Voir les différences avant de commiter
git diff
```

### Workflow typique

```bash
# 1. Modifier tes fichiers
# 2. Voir ce qui a changé
git status

# 3. Ajouter les fichiers modifiés
git add .

# 4. Faire un commit avec un message clair
git commit -m "Description de ce que tu as fait"

# Répéter pour chaque fonctionnalité !
```

## 📤 GitHub (optionnel mais recommandé)

### Créer un compte et un dépôt

1. Va sur [github.com](https://github.com) et crée un compte
2. Clique sur "New repository"
3. Donne un nom à ton dépôt (ex: `mon-premier-projet`)
4. Choisis "Public" ou "Private"
5. Ne coche PAS "Initialize with README" (tu en as déjà un)
6. Clique sur "Create repository"

### Connecter ton dépôt local à GitHub

```bash
# Ajouter le dépôt distant (remplace USERNAME et REPO par tes valeurs)
git remote add origin https://github.com/USERNAME/REPO.git

# Renommer la branche principale (si nécessaire)
git branch -M main

# Envoyer ton code sur GitHub
git push -u origin main
```

### Commandes GitHub

```bash
# Envoyer tes commits sur GitHub
git push

# Récupérer les changements depuis GitHub
git pull

# Voir les dépôts distants
git remote -v
```

## 💡 Messages de commit clairs

### Bonnes pratiques

```bash
# ✅ Bon : message clair et descriptif
git commit -m "Ajout de la fonction calculer_moyenne avec gestion des listes vides"

# ✅ Bon : message en plusieurs parties
git commit -m "Ajout du menu interactif

- Menu avec 5 options
- Gestion des erreurs d'entrée
- Sauvegarde automatique"

# ❌ Mauvais : message trop vague
git commit -m "modifs"

# ❌ Mauvais : message sans verbe
git commit -m "menu"
```

### Format recommandé

```
Type: Description courte (50 caractères max)

Description détaillée si nécessaire
- Point 1
- Point 2
```

Types courants :
- `feat:` nouvelle fonctionnalité
- `fix:` correction de bug
- `docs:` documentation
- `refactor:` réorganisation du code
- `test:` ajout de tests

## 🗂️ Fichier .gitignore

Crée un fichier `.gitignore` pour exclure certains fichiers :

```
# Fichiers Python
__pycache__/
*.py[cod]
*.pyc

# Environnements virtuels
venv/
env/

# Fichiers de données (si tu ne veux pas les versionner)
*.json
# Ou spécifiquement :
# scores.json

# Fichiers de l'éditeur
.vscode/
.idea/
*.swp
```

## 🎯 Checklist avant de "livrer"

- [ ] Tous les tests passent
- [ ] Le code fonctionne sans erreur
- [ ] Les commentaires sont clairs
- [ ] Le README est complet
- [ ] Les dépendances sont listées (requirements.txt)
- [ ] Le code est propre (pas de print() de debug)
- [ ] Les messages d'erreur sont clairs
- [ ] Le projet est sur Git avec des commits clairs

## 📦 Créer requirements.txt

```bash
# Générer automatiquement
pip freeze > requirements.txt

# Ou créer manuellement
```

Contenu de `requirements.txt` :
```
rich>=13.0.0
```

Pour installer : `pip install -r requirements.txt`

## 🐛 Problèmes courants

### "fatal: not a git repository"

```bash
# Solution : initialiser Git d'abord
git init
```

### "Please tell me who you are"

```bash
# Solution : configurer ton identité
git config --global user.name "Ton Nom"
git config --global user.email "ton.email@example.com"
```

### "Everything up-to-date" mais rien ne change

```bash
# Vérifier que tu as bien fait git add avant git commit
git status  # Doit montrer "nothing to commit"
```

## 💡 Astuces

1. **Commite souvent** : fais des commits petits et fréquents plutôt qu'un gros commit à la fin

2. **Messages clairs** : un bon message de commit explique POURQUOI tu as fait le changement, pas seulement QUOI

3. **Branches** (pour plus tard) : tu peux créer des branches pour tester de nouvelles fonctionnalités sans casser le code principal

4. **GitHub comme portfolio** : ton GitHub devient ton portfolio de projets !

