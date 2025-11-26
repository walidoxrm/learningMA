#!/bin/bash
# Script d'aide pour faciliter l'utilisation du tracker

# Couleurs pour l'affichage
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  🚀 Helper - Suivi d'Apprentissage    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Fonction pour enregistrer une séance
log_session() {
    echo -e "${YELLOW}📝 Enregistrement d'une séance${NC}"
    echo ""
    read -p "Numéro de séance : " session
    read -p "Focus (ce sur quoi tu as travaillé) : " focus
    read -p "Note (optionnel) : " note
    
    if [ -z "$note" ]; then
        python3 progress_tracker.py log --session "$session" --focus "$focus"
    else
        python3 progress_tracker.py log --session "$session" --focus "$focus" --note "$note"
    fi
    
    echo ""
    read -p "Synchroniser avec GitHub ? (o/n) : " sync
    if [ "$sync" = "o" ] || [ "$sync" = "O" ]; then
        python3 sync_to_github.py
    fi
}

# Fonction pour cocher une notion
check_topic() {
    echo -e "${YELLOW}✅ Cocher une notion${NC}"
    echo ""
    read -p "Nom de la notion : " topic
    
    python3 progress_tracker.py check --topic "$topic"
    
    echo ""
    read -p "Synchroniser avec GitHub ? (o/n) : " sync
    if [ "$sync" = "o" ] || [ "$sync" = "O" ]; then
        python3 sync_to_github.py
    fi
}

# Menu principal
while true; do
    echo ""
    echo -e "${GREEN}Choisis une action :${NC}"
    echo "  1) Enregistrer une séance"
    echo "  2) Cocher une notion"
    echo "  3) Voir l'avancement"
    echo "  4) Synchroniser avec GitHub"
    echo "  5) Quitter"
    echo ""
    read -p "Ton choix (1-5) : " choice
    
    case $choice in
        1)
            log_session
            ;;
        2)
            check_topic
            ;;
        3)
            echo ""
            python3 progress_tracker.py report
            echo ""
            echo -e "${BLUE}💡 Astuce :${NC} Ouvre aussi le dashboard web pour voir ta progression visuellement !"
            echo "   https://walidoxrm.github.io/learningMA/dashboard.html"
            ;;
        4)
            python3 sync_to_github.py
            ;;
        5)
            echo -e "${GREEN}Au revoir ! 👋${NC}"
            exit 0
            ;;
        *)
            echo -e "${YELLOW}Choix invalide. Réessaie.${NC}"
            ;;
    esac
done

