# Exemple : Programme avec fonctions et menu interactif

def calculer_moyenne(scores):
    """
    Calcule la moyenne d'une liste de scores.
    
    Paramètres:
    - scores: liste de nombres
    
    Retourne:
    - la moyenne (float)
    """
    if len(scores) == 0:
        return 0
    
    somme = 0
    for score in scores:
        somme = somme + score
    
    moyenne = somme / len(scores)
    return moyenne


def trouver_maximum(scores):
    """
    Trouve le score maximum.
    """
    if len(scores) == 0:
        return None
    
    maximum = scores[0]
    for score in scores:
        if score > maximum:
            maximum = score
    return maximum


def afficher_scores(scores):
    """
    Affiche tous les scores de manière lisible.
    """
    if len(scores) == 0:
        print("Aucun score enregistré.")
        return
    
    print("\n=== Liste des scores ===")
    for i, score in enumerate(scores, start=1):
        print(f"  {i}. {score}")


def ajouter_score(scores):
    """
    Demande à l'utilisateur d'ajouter un nouveau score.
    """
    try:
        nouveau_score = input("Entrez un nouveau score : ")
        score = float(nouveau_score)  # Convertir en nombre
        scores.append(score)
        print(f"Score {score} ajouté !")
    except ValueError:
        print("Erreur : vous devez entrer un nombre valide.")


def afficher_menu():
    """
    Affiche le menu principal.
    """
    print("\n" + "="*30)
    print("  MENU PRINCIPAL")
    print("="*30)
    print("1. Ajouter un score")
    print("2. Afficher tous les scores")
    print("3. Calculer la moyenne")
    print("4. Trouver le score maximum")
    print("5. Quitter")
    print("="*30)


# Programme principal
def main():
    scores = []  # Liste vide pour stocker les scores
    
    while True:
        afficher_menu()
        choix = input("\nChoisis une option (1-5) : ")
        
        if choix == "1":
            ajouter_score(scores)
        elif choix == "2":
            afficher_scores(scores)
        elif choix == "3":
            if len(scores) > 0:
                moyenne = calculer_moyenne(scores)
                print(f"\nLa moyenne est : {moyenne:.2f}")
            else:
                print("Aucun score à calculer.")
        elif choix == "4":
            if len(scores) > 0:
                maximum = trouver_maximum(scores)
                print(f"\nLe score maximum est : {maximum}")
            else:
                print("Aucun score à analyser.")
        elif choix == "5":
            print("\nAu revoir ! 👋")
            break
        else:
            print("\n❌ Option invalide. Choisis entre 1 et 5.")


# Lancer le programme
if __name__ == "__main__":
    main()

