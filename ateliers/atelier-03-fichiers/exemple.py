# Exemple : Gestion de données avec fichiers JSON

import json
from pathlib import Path

FICHIER_DONNEES = "scores.json"

def charger_donnees():
    """
    Charge les données depuis le fichier JSON.
    Retourne un dictionnaire avec les données.
    """
    fichier = Path(FICHIER_DONNEES)
    
    # Si le fichier n'existe pas, retourner des données par défaut
    if not fichier.exists():
        print("Fichier non trouvé. Création de données par défaut.")
        return {
            "scores": [],
            "joueur": "Joueur",
            "derniere_mise_a_jour": None
        }
    
    # Lire le fichier
    try:
        with open(FICHIER_DONNEES, "r", encoding="utf-8") as f:
            donnees = json.load(f)
            print("Données chargées avec succès !")
            return donnees
    except json.JSONDecodeError:
        print("Erreur : le fichier JSON est invalide.")
        return {
            "scores": [],
            "joueur": "Joueur",
            "derniere_mise_a_jour": None
        }


def sauvegarder_donnees(donnees):
    """
    Sauvegarde les données dans le fichier JSON.
    """
    try:
        with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
            json.dump(donnees, f, indent=2, ensure_ascii=False)
        print("✅ Données sauvegardées !")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
        return False


def valider_score(score):
    """
    Vérifie qu'un score est valide (entre 0 et 100 par exemple).
    """
    try:
        score_num = float(score)
        if 0 <= score_num <= 100:
            return True, score_num
        else:
            return False, None
    except ValueError:
        return False, None


def ajouter_score(donnees):
    """
    Demande à l'utilisateur d'ajouter un nouveau score.
    """
    score_input = input("Entrez un nouveau score (0-100) : ")
    est_valide, score = valider_score(score_input)
    
    if est_valide:
        donnees["scores"].append(score)
        print(f"Score {score} ajouté !")
        return True
    else:
        print("❌ Score invalide. Doit être un nombre entre 0 et 100.")
        return False


def afficher_statistiques(donnees):
    """
    Affiche les statistiques des scores.
    """
    scores = donnees["scores"]
    
    if len(scores) == 0:
        print("Aucun score enregistré.")
        return
    
    print("\n=== Statistiques ===")
    print(f"Nombre de scores : {len(scores)}")
    print(f"Scores : {scores}")
    
    # Calculer la moyenne
    moyenne = sum(scores) / len(scores)
    print(f"Moyenne : {moyenne:.2f}")
    
    # Trouver min et max
    print(f"Minimum : {min(scores)}")
    print(f"Maximum : {max(scores)}")


def main():
    """
    Programme principal.
    """
    # Charger les données au démarrage
    donnees = charger_donnees()
    
    print(f"\nBienvenue, {donnees['joueur']} !")
    print(f"Scores actuels : {donnees['scores']}")
    
    while True:
        print("\n" + "="*30)
        print("1. Ajouter un score")
        print("2. Afficher les statistiques")
        print("3. Sauvegarder et quitter")
        print("="*30)
        
        choix = input("Choisis une option (1-3) : ")
        
        if choix == "1":
            if ajouter_score(donnees):
                # Sauvegarder automatiquement après ajout
                sauvegarder_donnees(donnees)
        elif choix == "2":
            afficher_statistiques(donnees)
        elif choix == "3":
            sauvegarder_donnees(donnees)
            print("Au revoir ! 👋")
            break
        else:
            print("❌ Option invalide.")


if __name__ == "__main__":
    main()

