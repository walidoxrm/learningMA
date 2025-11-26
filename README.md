# 🚀 Learn by Doing - Parcours d'Initiation au Développement

Un parcours complet pour initier quelqu'un au développement Python en construisant un projet concret.

## 📦 Contenu

- **`learn-by-doing.md`** : Guide principal du parcours
- **`ateliers/`** : 6 ateliers progressifs avec instructions et indices
- **`progress_tracker.py`** : Outil de suivi de progression
- **`dashboard.html`** : Dashboard web pour suivre l'avancement en temps réel
- **`sync_to_github.py`** : Script de synchronisation avec GitHub
- **`GUIDE-HEBERGEMENT.md`** : Guide complet pour héberger et partager

## 🎯 Démarrage Rapide

### Pour l'apprenant

1. Lire `learn-by-doing.md` pour comprendre le parcours
2. Suivre les ateliers dans l'ordre (dossier `ateliers/`)
3. Utiliser `progress_tracker.py` pour suivre sa progression

### Pour le tuteur

1. Partager le dossier complet avec l'apprenant
2. Suivre l'avancement via le dashboard (voir `GUIDE-HEBERGEMENT.md`)

## 📊 Suivi d'Avancement

### Initialiser le suivi

```bash
python progress_tracker.py init --project "Mon Projet"
```

### Enregistrer une séance

```bash
python progress_tracker.py log --session 1 --focus "Fonctions" --note "Bien compris les bases"
```

### Cocher une notion

```bash
python progress_tracker.py check --topic "Fonctions et modularisation"
```

### Voir l'avancement

```bash
python progress_tracker.py report
```

### Synchroniser avec GitHub (optionnel)

```bash
# Méthode 1 : Option --sync
python progress_tracker.py log --session 1 --focus "Fonctions" --sync

# Méthode 2 : Script dédié
python sync_to_github.py
```

## 🌐 Dashboard Web

Le fichier `dashboard.html` permet de visualiser l'avancement en temps réel.

**Pour l'activer :**
1. Suis les instructions dans `GUIDE-HEBERGEMENT.md`
2. Déploie sur GitHub Pages (gratuit et simple)
3. Le dashboard se met à jour automatiquement toutes les 30 secondes

## 📚 Structure des Ateliers

Chaque atelier contient :
- **README.md** : Instructions et objectifs
- **indices.md** : Aides et syntaxe Python
- **exemple.py** : Exemples de code commentés

## 🛠️ Technologies

- Python 3.x
- Git/GitHub (pour le suivi)
- HTML/CSS/JavaScript (pour le dashboard)

## 📝 Licence

Libre d'utilisation pour l'apprentissage.

---

**Bon apprentissage ! 🎓**

