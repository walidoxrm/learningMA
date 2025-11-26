# Parcours Learn by Doing — Initiation au Développement

Bienvenue ! Ce parcours te permet d'apprendre la programmation en construisant un projet qui te tient à cœur. Tu vas créer une application concrète (statistiques sportives, bot musical, quiz, outil de calcul, etc.) tout en découvrant les bases du développement. Chaque atelier ajoute une fonctionnalité réelle et introduit juste les notions nécessaires au moment où tu en as besoin.

## Vue d'ensemble

- **Ton projet** : choisis un sujet qui te passionne et définis une application simple (outil de stats, mini-jeu, générateur de playlist…). C'est ce projet qui va te guider tout au long de l'apprentissage.
- **Durée** : 6 ateliers de 1h30–2h environ, à adapter selon ton rythme.
- **Comment ça marche** : à la fin de chaque séance, tu notes ce que tu as compris et ce qui reste à approfondir. C'est normal de revenir sur certains points !

## Les 6 ateliers

### 1. Mise en place & premier script
Tu vas installer Python et VS Code, puis créer ton premier script. Tu vas écrire un programme qui manipule des données liées à ton projet (par exemple calculer une moyenne de points, tirer un morceau au hasard, etc.). C'est l'occasion de découvrir comment exécuter du code, utiliser `print`, et comprendre les erreurs les plus courantes.

**Objectif** : avoir un script qui fonctionne et qui fait quelque chose de concret lié à ton projet.

### 2. Fonctions & interaction
Tu vas transformer ton algorithme en code structuré avec des fonctions (`calculer_moyenne`, `afficher_menu`, etc.). Tu vas aussi ajouter des interactions avec l'utilisateur grâce à `input`, pour que ton programme soit personnalisable. On abordera les notions de retour de fonction et de portée des variables.

**Objectif** : avoir un code organisé et interactif.

### 3. Données persistantes
Tu vas travailler avec des fichiers de données (`data.json` ou `stats.csv`) pour que ton application puisse lire et sauvegarder des informations. Tu vas manipuler des listes et des dictionnaires, et apprendre à valider les données (vérifier les types, gérer les valeurs manquantes).

**Objectif** : ton projet peut maintenant stocker et charger des données.

### 4. Expérience utilisateur
Tu vas améliorer l'interface de ton application avec un menu texte ou une mini-interface (librairies `rich`, `typer`, ou `tkinter`). Tu vas aussi organiser ton code en plusieurs fichiers (`main.py`, `services/data.py`, etc.) pour que ce soit plus clair. On travaillera l'affichage : couleurs, tableaux, tri des données.

**Objectif** : une application agréable à utiliser et bien organisée.

### 5. Tests & débogage
Tu vas apprendre à tester ton code et à déboguer efficacement. Tu vas identifier les cas limites de ton projet, écrire des tests simples, et utiliser des outils de débogage (`print` de debug, puis points d'arrêt dans VS Code). On verra comment s'assurer que ton code fonctionne dans tous les cas.

**Objectif** : un code robuste et fiable.

### 6. Livraison & Git
Tu vas finaliser ton projet en créant un dépôt Git, en écrivant un `README` qui explique comment utiliser ton application, et en préparant une petite démo. C'est aussi le moment de faire le point sur tout ce que tu as appris et de réfléchir à la suite (API, web, jeux, etc.).

**Objectif** : un projet complet, documenté et versionné.

## Suivi de progression

À la fin de chaque atelier, prends 5 minutes pour :
1. **Journal de bord** : note 3 lignes sur ce que tu as compris et ce qui t'a semblé difficile.
2. **Checklist** : coche les notions que tu as abordées (fonctions, fichiers, tests…).
3. **Mini-challenge** : définis une petite tâche liée à ton projet pour t'entraîner avant la prochaine séance.

Pour t'aider à suivre ta progression, tu peux utiliser l'outil `progress_tracker.py` (voir section ci-dessous).

## Ressources francophones

- OpenClassrooms : parcours “Apprenez à programmer avec Python”.
- Grafikart : vidéos concises sur Python, Git et outils dev.
- France-IOI / Codingame : exercices courts avec correction.

## Outil de suivi

Pour suivre ta progression facilement, utilise `progress_tracker.py` :

1. **Initialiser ton projet** : `python progress_tracker.py init --project "Stats Basket"` (remplace par le nom de ton projet). Cela crée un fichier `progress.json`.

2. **Enregistrer une séance** : après chaque atelier, lance par exemple :
   ```
   python progress_tracker.py log --session 1 --focus "Fonctions" --note "Calcul moyenne OK, besoin de revoir les listes"
   ```

3. **Voir ton avancement** : `python progress_tracker.py report` pour afficher toutes tes séances et les notions que tu as acquises.

4. **Cocher une notion** : `python progress_tracker.py check --topic "Lecture fichiers"` pour marquer qu'une notion est acquise.

Tout est sauvegardé dans `progress.json`, que tu peux partager pour suivre ta progression ensemble.

## Conseils pour bien progresser

- **Partir de ce que tu sais** : si tu as déjà fait de l'algo, utilise cette base ! Écris d'abord ton algorithme en pseudo-code, puis traduis-le en Python.
- **Coder toi-même** : tape le code, ne copie pas juste. C'est en faisant des erreurs qu'on apprend vraiment.
- **Célébrer les petites victoires** : chaque fonctionnalité qui marche, même petite, est une réussite. Ne minimise pas tes progrès !
- **Poser des questions** : si quelque chose n'est pas clair, demande. Il n'y a pas de question bête.
- **Pratiquer entre les séances** : les mini-challenges te permettent de consolider ce que tu as appris.

Bon apprentissage ! 🚀

