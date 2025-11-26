# Exemple : Tests et gestion d'erreurs

# ============================================
# FICHIER : calculs.py (à tester)
# ============================================

def calculer_moyenne(scores):
    """
    Calcule la moyenne d'une liste de scores.
    
    Cas limites gérés :
    - Liste vide → retourne 0
    - Liste avec None → ignore les None
    """
    if not scores:
        return 0
    
    # Filtrer les valeurs None
    scores_valides = [s for s in scores if s is not None]
    
    if not scores_valides:
        return 0
    
    try:
        return sum(scores_valides) / len(scores_valides)
    except (TypeError, ZeroDivisionError):
        return 0


def valider_score(score_input):
    """
    Valide et convertit un score entré par l'utilisateur.
    
    Retourne : (succes: bool, score: float ou None, message: str)
    """
    try:
        score = float(score_input)
        
        if score < 0:
            return False, None, "Le score ne peut pas être négatif."
        
        if score > 100:
            return False, None, "Le score ne peut pas dépasser 100."
        
        return True, score, f"Score {score} valide."
        
    except ValueError:
        return False, None, f"'{score_input}' n'est pas un nombre valide."
    except Exception as e:
        return False, None, f"Erreur inattendue : {e}"


# ============================================
# FICHIER : test_calculs.py
# ============================================

def test_calculer_moyenne():
    """Test de la fonction calculer_moyenne."""
    print("\n🧪 Tests de calculer_moyenne()")
    print("=" * 50)
    
    # Test 1 : Liste normale
    scores = [15, 20, 18, 22, 19]
    resultat = calculer_moyenne(scores)
    attendu = (15 + 20 + 18 + 22 + 19) / 5
    assert abs(resultat - attendu) < 0.01, f"Attendu {attendu}, obtenu {resultat}"
    print("✅ Test liste normale : OK")
    
    # Test 2 : Liste vide
    resultat = calculer_moyenne([])
    assert resultat == 0, f"Attendu 0, obtenu {resultat}"
    print("✅ Test liste vide : OK")
    
    # Test 3 : Un seul élément
    resultat = calculer_moyenne([20])
    assert resultat == 20, f"Attendu 20, obtenu {resultat}"
    print("✅ Test un seul élément : OK")
    
    # Test 4 : Avec None (valeurs manquantes)
    resultat = calculer_moyenne([15, None, 20, None, 18])
    attendu = (15 + 20 + 18) / 3
    assert abs(resultat - attendu) < 0.01, f"Attendu {attendu}, obtenu {resultat}"
    print("✅ Test avec None : OK")
    
    print("\n🎉 Tous les tests de calculer_moyenne() passent !")


def test_valider_score():
    """Test de la fonction valider_score."""
    print("\n🧪 Tests de valider_score()")
    print("=" * 50)
    
    # Test 1 : Score valide
    succes, score, message = valider_score("20")
    assert succes == True, "Devrait réussir"
    assert score == 20.0, f"Attendu 20.0, obtenu {score}"
    print("✅ Test score valide : OK")
    
    # Test 2 : Score invalide (texte)
    succes, score, message = valider_score("abc")
    assert succes == False, "Devrait échouer"
    assert score is None, "Score devrait être None"
    print("✅ Test score invalide (texte) : OK")
    
    # Test 3 : Score négatif
    succes, score, message = valider_score("-5")
    assert succes == False, "Devrait échouer"
    print("✅ Test score négatif : OK")
    
    # Test 4 : Score trop grand
    succes, score, message = valider_score("150")
    assert succes == False, "Devrait échouer"
    print("✅ Test score trop grand : OK")
    
    # Test 5 : Score décimal valide
    succes, score, message = valider_score("18.5")
    assert succes == True, "Devrait réussir"
    assert score == 18.5, f"Attendu 18.5, obtenu {score}"
    print("✅ Test score décimal : OK")
    
    print("\n🎉 Tous les tests de valider_score() passent !")


# ============================================
# FICHIER : main.py (démonstration)
# ============================================

def demo_gestion_erreurs():
    """Démonstration de la gestion d'erreurs."""
    print("\n🔍 Démonstration de gestion d'erreurs")
    print("=" * 50)
    
    scores = []
    
    # Tester différents cas
    cas_tests = ["20", "18.5", "abc", "-5", "150", "0", "100"]
    
    for cas in cas_tests:
        succes, score, message = valider_score(cas)
        if succes:
            scores.append(score)
            print(f"✅ {cas} → {message}")
        else:
            print(f"❌ {cas} → {message}")
    
    print(f"\n📊 Scores valides collectés : {scores}")
    if scores:
        moyenne = calculer_moyenne(scores)
        print(f"📈 Moyenne : {moyenne:.2f}")


# ============================================
# Lancer tous les tests
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  SUITE DE TESTS")
    print("=" * 50)
    
    try:
        test_calculer_moyenne()
        test_valider_score()
        demo_gestion_erreurs()
        
        print("\n" + "=" * 50)
        print("  ✅ TOUS LES TESTS PASSENT !")
        print("=" * 50)
        
    except AssertionError as e:
        print(f"\n❌ ÉCHEC : {e}")
    except Exception as e:
        print(f"\n❌ ERREUR INATTENDUE : {e}")

