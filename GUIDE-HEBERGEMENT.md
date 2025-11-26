# 📍 Guide d'Hébergement et Suivi en Temps Réel

Ce guide t'explique comment mettre les ateliers à disposition et suivre l'avancement en temps réel.

## 🎯 Solutions Recommandées

### Option 1 : GitHub (Recommandé - Gratuit et Simple) ⭐

**Avantages :**
- ✅ Gratuit
- ✅ Professionnel
- ✅ Versioning automatique
- ✅ Dashboard accessible partout
- ✅ Facile à mettre en place

**Étapes :**

1. **Créer un dépôt GitHub**
   - Va sur [github.com](https://github.com) et crée un compte
   - Clique sur "New repository"
   - Nomme-le (ex: `learn-by-doing`)
   - Choisis "Public" (pour que le dashboard fonctionne)
   - Crée le dépôt

2. **Initialiser Git localement**
   ```bash
   cd /Users/walid/mohamed_amine
   git init
   git add .
   git commit -m "Initial commit: ateliers learn by doing"
   git branch -M main
   git remote add origin https://github.com/TON_USERNAME/learn-by-doing.git
   git push -u origin main
   ```

3. **Configurer le dashboard**
   - Modifie `dashboard.html` ligne 108 :
     ```javascript
     const PROGRESS_URL = 'https://raw.githubusercontent.com/TON_USERNAME/learn-by-doing/main/progress.json';
     ```
   - Remplace `TON_USERNAME` et `learn-by-doing` par tes valeurs

4. **Activer GitHub Pages**
   - Va dans Settings → Pages
   - Source : "Deploy from a branch"
   - Branch : `main` / `/ (root)`
   - Sauvegarde
   - Ton dashboard sera accessible à : `https://TON_USERNAME.github.io/learn-by-doing/dashboard.html`

5. **Synchronisation automatique**
   - Après chaque `progress_tracker.py log` ou `check`, lance :
     ```bash
     python sync_to_github.py
     ```
   - Ou crée un alias pour automatiser (voir ci-dessous)

### Option 2 : Netlify/Vercel (Plus Avancé)

**Avantages :**
- ✅ Déploiement automatique
- ✅ HTTPS automatique
- ✅ URL personnalisée possible

**Étapes :**

1. **Préparer les fichiers**
   - Assure-toi que `dashboard.html` et `progress.json` sont dans le repo

2. **Déployer sur Netlify**
   - Va sur [netlify.com](https://netlify.com)
   - Connecte ton compte GitHub
   - Sélectionne le dépôt
   - Netlify détectera automatiquement et déploiera

3. **Configurer l'URL du JSON**
   - Modifie `dashboard.html` pour pointer vers l'URL Netlify :
     ```javascript
     const PROGRESS_URL = 'https://ton-site.netlify.app/progress.json';
     ```

### Option 3 : Google Drive / Dropbox (Simple mais Limité)

**Avantages :**
- ✅ Très simple
- ✅ Pas besoin de Git

**Inconvénients :**
- ❌ Pas de suivi automatique
- ❌ Dashboard moins pratique

**Étapes :**
1. Partage le dossier `ateliers/` via Google Drive
2. Partage le `dashboard.html` (mais il faudra héberger le JSON ailleurs)

## 🔄 Automatisation de la Synchronisation

### Méthode 1 : Alias Git (Simple)

Ajoute dans ton `~/.zshrc` ou `~/.bashrc` :

```bash
alias track-sync='python /Users/walid/mohamed_amine/sync_to_github.py'
```

Puis après chaque modification :
```bash
track-sync
```

### Méthode 2 : Hook Git (Automatique)

Crée `.git/hooks/post-commit` :

```bash
#!/bin/bash
# Synchronise automatiquement après chaque commit
python /Users/walid/mohamed_amine/sync_to_github.py
```

Rends-le exécutable :
```bash
chmod +x .git/hooks/post-commit
```

### Méthode 3 : Wrapper Script (Recommandé)

Modifie `progress_tracker.py` pour auto-sync après chaque commande (optionnel).

## 📊 Accéder au Dashboard

Une fois déployé :

1. **URL du dashboard** : `https://TON_USERNAME.github.io/learn-by-doing/dashboard.html`
2. **Actualisation automatique** : Le dashboard se met à jour toutes les 30 secondes
3. **Actualisation manuelle** : Bouton "🔄 Actualiser"

## 🔐 Sécurité (Optionnel)

Si tu veux garder le repo privé mais partager le dashboard :

1. Crée un repo **public** juste pour le dashboard
2. Utilise GitHub Actions pour copier `progress.json` automatiquement
3. Ou utilise un service comme [JSONBin.io](https://jsonbin.io) pour héberger le JSON

## 📱 Partage avec ton Frère

**Pour lui donner accès aux ateliers :**
- Partage le lien GitHub : `https://github.com/TON_USERNAME/learn-by-doing`
- Il peut cloner : `git clone https://github.com/TON_USERNAME/learn-by-doing.git`

**Pour qu'il voie son avancement :**
- Partage le lien du dashboard : `https://TON_USERNAME.github.io/learn-by-doing/dashboard.html`
- Il peut l'ajouter en favori sur son téléphone/ordinateur

**Pour toi suivre son avancement :**
- Ouvre le dashboard dans ton navigateur
- Il se met à jour automatiquement quand il fait `python sync_to_github.py`

## 🛠️ Dépannage

### Le dashboard ne se met pas à jour
- Vérifie que `progress.json` est bien dans le repo
- Vérifie l'URL dans `dashboard.html`
- Vérifie que le repo est public (pour raw.githubusercontent.com)

### Erreur CORS
- Si tu héberges le dashboard ailleurs que GitHub Pages, tu devras configurer CORS
- Ou utilise un proxy CORS comme `https://cors-anywhere.herokuapp.com/`

### Git push ne fonctionne pas
- Vérifie tes identifiants : `git config --global user.name` et `user.email`
- Pour GitHub, utilise un Personal Access Token au lieu du mot de passe

## 💡 Astuce Pro

Crée un raccourci sur le bureau de ton frère qui ouvre directement le dashboard. Comme ça, il peut voir sa progression d'un coup d'œil !

