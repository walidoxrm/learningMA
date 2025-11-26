# Atelier 5 : Tests & débogage

## 🎯 Objectif
Apprendre à tester ton code et à déboguer efficacement pour créer des applications robustes !

## 📋 Ce que tu vas faire

1. **Identifier les cas limites**
   - Liste les situations où ton code pourrait planter
   - Exemples : liste vide, division par zéro, fichier manquant, données invalides

2. **Écrire des tests simples**
   - Teste tes fonctions une par une
   - Vérifie qu'elles fonctionnent dans les cas normaux ET les cas limites
   - Utilise `pytest` ou écris tes propres fonctions de test

3. **Déboguer efficacement**
   - Utilise `print()` pour voir ce qui se passe
   - Apprends à utiliser le débogueur de VS Code (points d'arrêt)
   - Comprends les messages d'erreur Python

4. **Gérer les erreurs**
   - Utilise `try/except` pour gérer les erreurs gracieusement
   - Affiche des messages d'erreur clairs à l'utilisateur

## 💡 Exemple de projet

Si tu fais un projet de stats de basket :
- Teste `calculer_moyenne()` avec une liste vide, une liste normale, des nombres négatifs
- Teste `charger_scores()` quand le fichier n'existe pas, est vide, ou contient des données invalides
- Gère les erreurs quand l'utilisateur entre un texte au lieu d'un nombre

## ✅ Critères de réussite

- [ ] Tu as identifié au moins 5 cas limites pour ton projet
- [ ] Tu as écrit des tests pour tes principales fonctions
- [ ] Tu sais utiliser le débogueur de VS Code
- [ ] Tu utilises `try/except` pour gérer les erreurs
- [ ] Les messages d'erreur sont clairs et utiles

## 🆘 Besoin d'aide ?

Consulte le fichier `indices.md` pour apprendre à écrire des tests et déboguer.

## 📝 Après l'atelier

Note dans ton journal :
- L'importance des tests pour éviter les bugs
- Les techniques de débogage que tu as apprises
- Comment gérer les erreurs de manière professionnelle

