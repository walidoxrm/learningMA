# 📊 Gestionnaire de Scores

Une application Python simple pour gérer et analyser des scores de manière interactive.

## 🎯 Fonctionnalités

- ✅ Ajouter et sauvegarder des scores
- ✅ Calculer des statistiques (moyenne, min, max)
- ✅ Afficher les scores dans un tableau formaté
- ✅ Trier les scores par ordre croissant ou décroissant
- ✅ Interface colorée et intuitive avec `rich`
- ✅ Sauvegarde automatique dans un fichier JSON

## 📦 Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes

1. **Cloner ou télécharger le projet**
   ```bash
   git clone https://github.com/ton-username/mon-projet.git
   cd mon-projet
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
   
   Ou installer manuellement :
   ```bash
   pip install rich
   ```

3. **Lancer l'application**
   ```bash
   python main.py
   ```

## 🚀 Utilisation

### Menu principal

L'application affiche un menu avec 5 options :

```
1. Ajouter un score
2. Afficher tous les scores
3. Statistiques
4. Trier les scores
5. Quitter
```

### Exemple d'utilisation

1. **Ajouter un score**
   - Choisis l'option `1`
   - Entre un score entre 0 et 100
   - Le score est automatiquement sauvegardé

2. **Voir les statistiques**
   - Choisis l'option `3`
   - L'application affiche :
     - Nombre de scores
     - Moyenne
     - Score maximum
     - Score minimum

3. **Trier les scores**
   - Choisis l'option `4`
   - Choisis l'ordre (croissant ou décroissant)
   - Les scores triés sont sauvegardés

## 📁 Structure du projet

```
mon-projet/
├── main.py              # Point d'entrée de l'application
├── data.py              # Gestion des données (lecture/écriture JSON)
├── calculs.py           # Fonctions de calcul et statistiques
├── ui.py                # Interface utilisateur (affichage avec rich)
├── scores.json          # Fichier de données (créé automatiquement)
├── requirements.txt     # Dépendances Python
└── README.md            # Ce fichier
```

## 🛠️ Technologies utilisées

- **Python 3.x** : Langage de programmation
- **rich** : Bibliothèque pour une interface en ligne de commande améliorée
- **JSON** : Format de stockage des données

## 📝 Format des données

Les scores sont sauvegardés dans `scores.json` :

```json
{
  "scores": [15, 20, 18, 22, 19]
}
```

## 🧪 Tests

Pour lancer les tests :

```bash
python test_calculs.py
```

## 🐛 Problèmes connus

- Les scores doivent être entre 0 et 100
- Le fichier `scores.json` est créé automatiquement s'il n'existe pas

## 🔮 Améliorations futures

- [ ] Graphiques des scores
- [ ] Export en CSV
- [ ] Historique des modifications
- [ ] Comparaison entre plusieurs sessions

## 📄 Licence

Ce projet est libre d'utilisation pour l'apprentissage.

## 👤 Auteur

Créé dans le cadre d'un parcours d'apprentissage du développement Python.

## 🙏 Remerciements

- Merci à la communauté Python
- Documentation de la bibliothèque `rich`

---

**Note** : Ce projet a été créé pour apprendre les bases du développement Python. N'hésite pas à le modifier et l'améliorer !

