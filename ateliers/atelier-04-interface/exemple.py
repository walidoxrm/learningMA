# Exemple : Application avec interface améliorée et modules
# Ce fichier montre comment organiser le code en plusieurs modules

# ============================================
# FICHIER 1 : data.py
# ============================================
"""
Module pour la gestion des données (lecture/écriture fichiers).
"""

import json
from pathlib import Path

FICHIER_DONNEES = "scores.json"

def charger_scores():
    """Charge les scores depuis le fichier JSON."""
    fichier = Path(FICHIER_DONNEES)
    
    if not fichier.exists():
        return []
    
    try:
        with open(FICHIER_DONNEES, "r", encoding="utf-8") as f:
            donnees = json.load(f)
            return donnees.get("scores", [])
    except json.JSONDecodeError:
        return []

def sauvegarder_scores(scores):
    """Sauvegarde les scores dans le fichier JSON."""
    donnees = {"scores": scores}
    
    with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2, ensure_ascii=False)
    
    return True


# ============================================
# FICHIER 2 : calculs.py
# ============================================
"""
Module pour les calculs et statistiques.
"""

def calculer_moyenne(scores):
    """Calcule la moyenne d'une liste de scores."""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def trouver_maximum(scores):
    """Trouve le score maximum."""
    if len(scores) == 0:
        return None
    return max(scores)

def trouver_minimum(scores):
    """Trouve le score minimum."""
    if len(scores) == 0:
        return None
    return min(scores)

def trier_scores(scores, ordre="croissant"):
    """Trie les scores par ordre croissant ou décroissant."""
    if ordre == "croissant":
        return sorted(scores)
    else:
        return sorted(scores, reverse=True)


# ============================================
# FICHIER 3 : ui.py
# ============================================
"""
Module pour l'interface utilisateur (affichage).
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

console = Console()

def afficher_menu():
    """Affiche le menu principal."""
    menu = """
[bold cyan]1.[/bold cyan] Ajouter un score
[bold cyan]2.[/bold cyan] Afficher tous les scores
[bold cyan]3.[/bold cyan] Statistiques
[bold cyan]4.[/bold cyan] Trier les scores
[bold cyan]5.[/bold cyan] Quitter
"""
    console.print(Panel(menu, title="[bold blue]Menu Principal[/bold blue]", border_style="blue"))

def afficher_tableau_scores(scores):
    """Affiche les scores dans un tableau formaté."""
    if not scores:
        rprint("[yellow]Aucun score enregistré.[/yellow]")
        return
    
    table = Table(title="[bold]Liste des Scores[/bold]")
    table.add_column("Index", style="cyan", justify="right", width=8)
    table.add_column("Score", style="magenta", justify="right", width=10)
    
    for i, score in enumerate(scores, start=1):
        # Colorier selon la valeur
        if score >= 20:
            style = "bold green"
        elif score >= 15:
            style = "yellow"
        else:
            style = "red"
        
        table.add_row(str(i), f"[{style}]{score}[/{style}]")
    
    console.print(table)

def afficher_statistiques(scores):
    """Affiche les statistiques dans un tableau."""
    if not scores:
        rprint("[yellow]Aucun score pour calculer les statistiques.[/yellow]")
        return
    
    from calculs import calculer_moyenne, trouver_maximum, trouver_minimum
    
    table = Table(title="[bold]Statistiques[/bold]")
    table.add_column("Métrique", style="cyan")
    table.add_column("Valeur", style="magenta", justify="right")
    
    moyenne = calculer_moyenne(scores)
    maximum = trouver_maximum(scores)
    minimum = trouver_minimum(scores)
    
    table.add_row("Nombre de scores", str(len(scores)))
    table.add_row("Moyenne", f"{moyenne:.2f}")
    table.add_row("Maximum", f"[green]{maximum}[/green]")
    table.add_row("Minimum", f"[red]{minimum}[/red]")
    
    console.print(table)

def afficher_message_succes(message):
    """Affiche un message de succès."""
    rprint(f"[green]✅ {message}[/green]")

def afficher_message_erreur(message):
    """Affiche un message d'erreur."""
    rprint(f"[red]❌ {message}[/red]")

def afficher_separateur():
    """Affiche un séparateur visuel."""
    console.print("─" * 50)


# ============================================
# FICHIER 4 : main.py
# ============================================
"""
Point d'entrée principal de l'application.
"""

from data import charger_scores, sauvegarder_scores
from calculs import trier_scores
from ui import (
    afficher_menu, afficher_tableau_scores, afficher_statistiques,
    afficher_message_succes, afficher_message_erreur, afficher_separateur
)

def ajouter_score(scores):
    """Demande à l'utilisateur d'ajouter un score."""
    try:
        score_input = input("\nEntrez un nouveau score : ")
        score = float(score_input)
        
        if 0 <= score <= 100:
            scores.append(score)
            sauvegarder_scores(scores)
            afficher_message_succes(f"Score {score} ajouté et sauvegardé !")
            return True
        else:
            afficher_message_erreur("Le score doit être entre 0 et 100.")
            return False
    except ValueError:
        afficher_message_erreur("Vous devez entrer un nombre valide.")
        return False

def main():
    """Programme principal."""
    # Charger les données au démarrage
    scores = charger_scores()
    
    if scores:
        afficher_message_succes(f"{len(scores)} score(s) chargé(s) depuis le fichier.")
    else:
        rprint("[yellow]Aucun score trouvé. Commence par ajouter des scores ![/yellow]")
    
    while True:
        afficher_separateur()
        afficher_menu()
        
        choix = input("\nChoisis une option (1-5) : ").strip()
        
        if choix == "1":
            ajouter_score(scores)
        elif choix == "2":
            afficher_tableau_scores(scores)
        elif choix == "3":
            afficher_statistiques(scores)
        elif choix == "4":
            if scores:
                ordre = input("Ordre (croissant/décroissant) [croissant] : ").strip().lower()
                if ordre != "décroissant":
                    ordre = "croissant"
                scores = trier_scores(scores, ordre)
                sauvegarder_scores(scores)
                afficher_message_succes("Scores triés et sauvegardés !")
                afficher_tableau_scores(scores)
            else:
                afficher_message_erreur("Aucun score à trier.")
        elif choix == "5":
            sauvegarder_scores(scores)
            rprint("\n[bold blue]Au revoir ! 👋[/bold blue]")
            break
        else:
            afficher_message_erreur("Option invalide. Choisis entre 1 et 5.")

if __name__ == "__main__":
    main()

