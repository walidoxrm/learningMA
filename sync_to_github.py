#!/usr/bin/env python3
"""
Script pour synchroniser automatiquement progress.json sur GitHub.
À exécuter après chaque modification du suivi.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, check=True):
    """Exécute une commande shell."""
    try:
        result = subprocess.run(cmd, shell=True, check=check, 
                              capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur: {e.stderr}", file=sys.stderr)
        return None

def sync_to_github():
    """Synchronise progress.json sur GitHub."""
    progress_file = Path("progress.json")
    
    if not progress_file.exists():
        print("❌ Fichier progress.json introuvable.")
        print("   Lance d'abord: python progress_tracker.py init --project ...")
        return False
    
    # Vérifier si Git est initialisé
    if not Path(".git").exists():
        print("⚠️  Git n'est pas initialisé dans ce dossier.")
        print("   Initialise Git avec: git init")
        return False
    
    # Vérifier si un remote est configuré
    remote = run_command("git remote get-url origin", check=False)
    if not remote:
        print("⚠️  Aucun dépôt distant configuré.")
        print("   Configure avec: git remote add origin https://github.com/walidoxrm/learningMA.git")
        return False
    
    # Ajouter progress.json
    print("📝 Ajout de progress.json...")
    run_command("git add progress.json")
    
    # Commit
    print("💾 Création du commit...")
    result = run_command('git commit -m "Mise à jour du suivi d\'avancement"', check=False)
    if result is None:
        print("ℹ️  Aucun changement à commiter.")
        return True
    
    # Push
    print("🚀 Envoi sur GitHub...")
    result = run_command("git push origin main", check=False)
    if result is None:
        # Essayer avec 'master' si 'main' ne fonctionne pas
        result = run_command("git push origin master", check=False)
    
    if result is None:
        print("❌ Erreur lors du push. Vérifie ta configuration Git.")
        return False
    
    print("✅ Synchronisation réussie !")
    print(f"   Le dashboard se mettra à jour automatiquement.")
    return True

if __name__ == "__main__":
    success = sync_to_github()
    sys.exit(0 if success else 1)

