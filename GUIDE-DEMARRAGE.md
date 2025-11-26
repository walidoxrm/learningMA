# 🚀 Guide de Démarrage - Pour l'Apprenant

Ce guide t'explique comment commencer et suivre ton parcours d'apprentissage.

## 📋 Avant de commencer

### 1. Installation (une seule fois)

1. **Installer Python**
   - Télécharge depuis [python.org](https://www.python.org/downloads/)
   - Vérifie l'installation : ouvre un terminal et tape `python3 --version`

2. **Installer VS Code** (optionnel mais recommandé)
   - Télécharge depuis [code.visualstudio.com](https://code.visualstudio.com/)

3. **Récupérer les ateliers**
   - Si tu as le dossier, c'est bon ✅
   - Sinon, demande à ton frère de te le partager

### 2. Initialiser le suivi (une seule fois)

Ouvre un terminal dans le dossier du projet et lance :

```bash
python3 progress_tracker.py init --project "Mon Projet Python"
```

✅ C'est fait ! Le fichier `progress.json` est créé.

## 🎯 Déroulement d'une séance

### Étape 1 : Choisir un atelier

1. Va dans le dossier `ateliers/`
2. Choisis l'atelier suivant (commence par `atelier-01-setup`)
3. Ouvre le fichier `README.md` de l'atelier pour comprendre l'objectif

### Étape 2 : Travailler sur l'atelier

1. **Lis le README.md** de l'atelier
   - Comprends l'objectif
   - Lis les critères de réussite

2. **Essaie de coder toi-même**
   - Ne regarde pas les exemples tout de suite !
   - Utilise les `indices.md` si tu es bloqué

3. **Consulte les indices si besoin**
   - Ouvre `indices.md` pour de l'aide
   - Syntaxe Python, exemples, erreurs courantes

4. **Regarde les exemples en dernier recours**
   - Si tu es vraiment bloqué, regarde `exemple.py`
   - Mais essaie de comprendre, ne copie pas bêtement !

### Étape 3 : Enregistrer ta séance

À la fin de chaque séance, enregistre ce que tu as fait :

```bash
python3 progress_tracker.py log --session 1 --focus "Installation Python et premier script" --note "J'ai réussi à créer mon premier script qui calcule une moyenne !"
```

**Explication :**
- `--session 1` : numéro de la séance (1, 2, 3, etc.)
- `--focus` : ce sur quoi tu as travaillé
- `--note` : ce que tu as réussi, ce qui était difficile, etc.

### Étape 4 : Cocher les notions acquises

Quand tu maîtrises une notion, coche-la :

```bash
python3 progress_tracker.py check --topic "Scripts Python de base"
```

### Étape 5 : Synchroniser avec GitHub (optionnel)

Pour que ton frère puisse voir ton avancement :

```bash
python3 sync_to_github.py
```

Ou utilise l'option `--sync` directement :

```bash
python3 progress_tracker.py log --session 1 --focus "Test" --sync
```

## 📊 Voir ton avancement

### Dans le terminal

```bash
python3 progress_tracker.py report
```

Tu verras :
- Le nombre de séances
- Les notions acquises
- Ta progression

### Sur le dashboard web

1. Ouvre le dashboard : https://walidoxrm.github.io/learningMA/dashboard.html
2. Tu verras ta progression en temps réel
3. Le dashboard se met à jour automatiquement toutes les 30 secondes

## 📝 Exemple de séance complète

Voici un exemple concret :

```bash
# 1. Tu travailles sur l'atelier 1
# Tu lis le README, tu codes, tu testes...

# 2. À la fin, tu enregistres ta séance
python3 progress_tracker.py log --session 1 \
  --focus "Installation et premier script" \
  --note "J'ai installé Python et créé mon premier script qui calcule des moyennes. C'était cool !"

# 3. Tu coches la notion acquise
python3 progress_tracker.py check --topic "Installation environnement"
python3 progress_tracker.py check --topic "Scripts Python de base"

# 4. Tu synchronises (pour que ton frère voie)
python3 sync_to_github.py

# 5. Tu vérifies ton avancement
python3 progress_tracker.py report
```

## 🎯 Checklist d'une séance réussie

- [ ] J'ai lu le README de l'atelier
- [ ] J'ai codé quelque chose qui fonctionne
- [ ] J'ai testé mon code
- [ ] J'ai enregistré ma séance avec `log`
- [ ] J'ai coché les notions acquises avec `check`
- [ ] J'ai synchronisé avec `sync_to_github.py` (optionnel)
- [ ] J'ai vérifié mon avancement avec `report`

## 💡 Conseils

1. **Prends ton temps** : il n'y a pas de course
2. **Fais des erreurs** : c'est comme ça qu'on apprend
3. **Note ce qui est difficile** : ça t'aidera à progresser
4. **Célèbre tes réussites** : chaque petite victoire compte !
5. **Pose des questions** : si tu es bloqué, demande de l'aide

## 🆘 En cas de problème

### Erreur "command not found: python3"
- Python n'est pas installé ou pas dans le PATH
- Vérifie avec `python3 --version`

### Erreur "Aucun projet initialisé"
- Lance d'abord : `python3 progress_tracker.py init --project "Mon Projet"`

### Le dashboard ne se met pas à jour
- Vérifie que tu as bien fait `sync_to_github.py`
- Attends quelques secondes (le dashboard se met à jour toutes les 30 secondes)

## 📚 Ordre des ateliers

1. **Atelier 1** : Mise en place & premier script
2. **Atelier 2** : Fonctions & interaction
3. **Atelier 3** : Données persistantes
4. **Atelier 4** : Expérience utilisateur
5. **Atelier 5** : Tests & débogage
6. **Atelier 6** : Livraison & Git

## 🛠️ Script d'Aide (Optionnel mais Pratique)

Pour faciliter les commandes, tu peux utiliser le script `helper.sh` :

```bash
./helper.sh
```

Ce script te guide étape par étape pour :
- Enregistrer une séance
- Cocher une notion
- Voir l'avancement
- Synchroniser avec GitHub

C'est plus simple que de taper les longues commandes ! 😊

## 🎉 C'est parti !

Tu es prêt à commencer. Bon courage et amuse-toi bien ! 🚀

---

**Rappel** : Ce parcours est fait pour apprendre en faisant. Ne te précipite pas, prends le temps de comprendre chaque concept avant de passer au suivant.

**📚 Guides disponibles :**
- `GUIDE-DEMARRAGE.md` : Guide complet (ce fichier)
- `DEMARRAGE-RAPIDE.md` : Résumé visuel en 5 minutes
- `learn-by-doing.md` : Vue d'ensemble du parcours

