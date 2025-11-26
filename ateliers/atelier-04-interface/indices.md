# Indices - Atelier 4

## 🎨 Améliorer l'affichage avec `rich`

### Installation

```bash
pip install rich
```

### Utilisation de base

```python
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

console = Console()

# Afficher du texte avec des couleurs
console.print("Hello", style="bold red")
console.print("World", style="green")

# Ou utiliser print() amélioré
rprint("[bold red]Erreur[/bold red] : fichier non trouvé")
rprint("[green]✅[/green] Opération réussie !")
```

### Créer un tableau

```python
from rich.table import Table

table = Table(title="Scores des joueurs")

table.add_column("Nom", style="cyan")
table.add_column("Score", style="magenta", justify="right")
table.add_column("Moyenne", style="green", justify="right")

table.add_row("Mohamed", "20", "18.5")
table.add_row("Ahmed", "18", "17.2")

console.print(table)
```

### Créer un panneau

```python
from rich.panel import Panel

contenu = """
Bienvenue dans l'application de stats !
Choisis une option dans le menu.
"""

console.print(Panel(contenu, title="[bold]Menu Principal[/bold]", border_style="blue"))
```

### Séparateurs et règles

```python
from rich.rule import Rule

console.print(Rule("[bold blue]Section Statistiques[/bold blue]"))
```

## 📦 Organiser le code en modules

### Structure de dossiers

```
mon-projet/
├── main.py          # Point d'entrée
├── data.py          # Gestion des données
├── ui.py            # Affichage et interface
├── calculs.py       # Fonctions de calcul
└── scores.json      # Fichier de données
```

### Créer un module (`data.py`)

```python
# data.py
import json
from pathlib import Path

FICHIER_DONNEES = "scores.json"

def charger_scores():
    """Charge les scores depuis le fichier."""
    # Code ici...
    pass

def sauvegarder_scores(scores):
    """Sauvegarde les scores."""
    # Code ici...
    pass
```

### Utiliser un module (`main.py`)

```python
# main.py
from data import charger_scores, sauvegarder_scores
from ui import afficher_menu, afficher_tableau
from calculs import calculer_moyenne

# Utiliser les fonctions importées
scores = charger_scores()
moyenne = calculer_moyenne(scores)
afficher_tableau(scores)
```

### Module pour l'interface (`ui.py`)

```python
# ui.py
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def afficher_menu():
    """Affiche le menu principal."""
    menu = """
1. Ajouter un score
2. Afficher les statistiques
3. Trier les scores
4. Quitter
"""
    console.print(Panel(menu, title="[bold]Menu[/bold]"))

def afficher_tableau_scores(scores):
    """Affiche les scores dans un tableau."""
    table = Table(title="Scores")
    table.add_column("Index", style="cyan")
    table.add_column("Score", style="magenta", justify="right")
    
    for i, score in enumerate(scores, start=1):
        table.add_row(str(i), str(score))
    
    console.print(table)
```

## 🔄 Trier et filtrer

### Trier une liste

```python
# Trier par ordre croissant
scores = [20, 15, 18, 22, 19]
scores_tries = sorted(scores)  # [15, 18, 19, 20, 22]

# Trier par ordre décroissant
scores_tries = sorted(scores, reverse=True)  # [22, 20, 19, 18, 15]

# Trier sur place (modifie la liste originale)
scores.sort()  # scores devient [15, 18, 19, 20, 22]
```

### Filtrer une liste

```python
# Filtrer les scores supérieurs à 18
scores = [20, 15, 18, 22, 19]
scores_eleves = [s for s in scores if s > 18]  # [20, 22, 19]

# Avec une fonction
def est_eleve(score):
    return score > 18

scores_eleves = list(filter(est_eleve, scores))
```

## 🎯 Exemple complet : Menu amélioré

```python
# ui.py
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

console = Console()

def afficher_menu():
    menu = """
[bold cyan]1.[/bold cyan] Ajouter un score
[bold cyan]2.[/bold cyan] Afficher les statistiques
[bold cyan]3.[/bold cyan] Trier les scores
[bold cyan]4.[/bold cyan] Rechercher un score
[bold cyan]5.[/bold cyan] Quitter
"""
    console.print(Panel(menu, title="[bold blue]Menu Principal[/bold blue]"))

def afficher_scores(scores):
    if not scores:
        rprint("[yellow]Aucun score enregistré.[/yellow]")
        return
    
    table = Table(title="[bold]Scores[/bold]")
    table.add_column("Index", style="cyan", justify="right")
    table.add_column("Score", style="magenta", justify="right")
    
    for i, score in enumerate(scores, start=1):
        # Colorier selon la valeur
        style = "green" if score >= 20 else "yellow" if score >= 15 else "red"
        table.add_row(str(i), f"[{style}]{score}[/{style}]")
    
    console.print(table)

def afficher_message_succes(message):
    rprint(f"[green]✅ {message}[/green]")

def afficher_message_erreur(message):
    rprint(f"[red]❌ {message}[/red]")
```

## 🐛 Erreurs fréquentes

1. **Oublier d'importer le module**
   ```python
   # ❌ Erreur : NameError
   scores = charger_scores()
   
   # ✅ Correct
   from data import charger_scores
   scores = charger_scores()
   ```

2. **Problème de chemin de fichier**
   ```python
   # Si les modules sont dans des dossiers différents
   # Utilise des chemins relatifs ou absolus
   from pathlib import Path
   FICHIER = Path(__file__).parent / "scores.json"
   ```

3. **Import circulaire**
   ```python
   # ❌ Évite : main.py importe data.py qui importe main.py
   # Organise mieux tes modules pour éviter ça
   ```

## 💡 Bonnes pratiques

1. **Un fichier = une responsabilité**
   - `data.py` : seulement la gestion des fichiers
   - `ui.py` : seulement l'affichage
   - `calculs.py` : seulement les calculs

2. **Nommer clairement les fonctions**
   ```python
   # ✅ Bon
   def afficher_tableau_scores(scores):
   
   # ❌ Moins clair
   def afficher(s):
   ```

3. **Documenter tes modules**
   ```python
   # ui.py
   """
   Module pour l'interface utilisateur.
   Contient toutes les fonctions d'affichage.
   """
   ```

