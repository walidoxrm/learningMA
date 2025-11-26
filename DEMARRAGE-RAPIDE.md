# ⚡ Démarrage Rapide - En 5 Minutes

## 🎯 Workflow d'une Séance (Répéter à chaque fois)

```
┌─────────────────────────────────────────┐
│  1. TRAVAILLER sur l'atelier            │
│     - Lire le README.md                 │
│     - Coder, tester, apprendre          │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  2. ENREGISTRER la séance               │
│     python3 progress_tracker.py log \   │
│       --session X \                     │
│       --focus "Ce que j'ai fait" \      │
│       --note "Notes personnelles"       │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  3. COCHER les notions acquises        │
│     python3 progress_tracker.py check \ │
│       --topic "Nom de la notion"        │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  4. SYNCHRONISER (optionnel)            │
│     python3 sync_to_github.py           │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  5. VOIR l'avancement                   │
│     python3 progress_tracker.py report │
│     OU ouvrir le dashboard web          │
└─────────────────────────────────────────┘
```

## 📝 Commandes Essentielles

### Première fois seulement
```bash
python3 progress_tracker.py init --project "Mon Projet"
```

### À chaque séance
```bash
# Enregistrer
python3 progress_tracker.py log --session 1 --focus "Installation" --note "Tout fonctionne !"

# Cocher une notion
python3 progress_tracker.py check --topic "Scripts Python de base"

# Synchroniser
python3 sync_to_github.py

# Voir l'avancement
python3 progress_tracker.py report
```

## 🎯 Exemple Concret

**Séance 1 : Installation et premier script**

```bash
# Après avoir travaillé sur l'atelier 1...

# 1. Enregistrer la séance
python3 progress_tracker.py log \
  --session 1 \
  --focus "Installation Python et premier script" \
  --note "J'ai créé un script qui calcule des moyennes. C'était cool !"

# 2. Cocher les notions acquises
python3 progress_tracker.py check --topic "Installation environnement"
python3 progress_tracker.py check --topic "Scripts Python de base"

# 3. Synchroniser
python3 sync_to_github.py

# 4. Voir le résultat
python3 progress_tracker.py report
```

## 📊 Dashboard Web

Ouvre dans ton navigateur :
**https://walidoxrm.github.io/learningMA/dashboard.html**

Le dashboard se met à jour automatiquement toutes les 30 secondes.

## ✅ Checklist Rapide

- [ ] J'ai travaillé sur l'atelier
- [ ] J'ai enregistré ma séance (`log`)
- [ ] J'ai coché les notions (`check`)
- [ ] J'ai synchronisé (`sync_to_github.py`)
- [ ] J'ai vérifié mon avancement (`report` ou dashboard)

## 🆘 Aide Rapide

```bash
# Voir toutes les commandes disponibles
python3 progress_tracker.py --help

# Voir l'aide d'une commande spécifique
python3 progress_tracker.py log --help
python3 progress_tracker.py check --help
```

---

**💡 Astuce** : Crée des alias dans ton terminal pour aller plus vite (voir guide complet).

