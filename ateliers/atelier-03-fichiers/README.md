# Atelier 3 : Données persistantes

## 🎯 Objectif
Faire en sorte que ton application puisse sauvegarder et charger des données depuis des fichiers !

## 📋 Ce que tu vas faire

1. **Créer un fichier de données**
   - Crée un fichier JSON ou CSV avec des données liées à ton projet
   - Exemple : `scores.json` avec une liste de scores, ou `joueurs.csv` avec des informations

2. **Lire des données depuis un fichier**
   - Écris une fonction qui lit le fichier
   - Charge les données dans ton programme

3. **Sauvegarder des données dans un fichier**
   - Quand l'utilisateur ajoute/modifie des données, sauvegarde-les
   - Les modifications doivent persister après la fermeture du programme

4. **Valider les données**
   - Vérifie que les données lues sont valides
   - Gère les cas où le fichier n'existe pas encore

## 💡 Exemple de projet

Si tu fais un projet de stats de basket :
- Fichier `scores.json` : `[15, 20, 18, 22, 19]`
- Au démarrage : charger les scores depuis le fichier
- Quand on ajoute un score : sauvegarder dans le fichier
- Si le fichier n'existe pas : créer une liste vide

## ✅ Critères de réussite

- [ ] Tu as créé un fichier de données (JSON ou CSV)
- [ ] Ton programme lit les données au démarrage
- [ ] Les modifications sont sauvegardées automatiquement
- [ ] Tu gères le cas où le fichier n'existe pas
- [ ] Tu valides que les données sont correctes

## 🆘 Besoin d'aide ?

Consulte le fichier `indices.md` pour la syntaxe de lecture/écriture de fichiers en Python.

## 📝 Après l'atelier

Note dans ton journal :
- La différence entre données en mémoire et données dans un fichier
- Comment tu as structuré tes données
- Les difficultés rencontrées avec les fichiers

