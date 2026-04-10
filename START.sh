#!/bin/bash

# Script de démarrage du projet complet (Backend + Frontend)
# Exécutez avec : bash START.sh

echo ""
echo "=========================================="
echo "  Moteur de Recherche d'Images - INF468"
echo "=========================================="
echo ""

# Vérifier que l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "[ERREUR] L'environnement virtuel n'existe pas !"
    echo "Créez-le avec : python3 -m venv venv"
    exit 1
fi

# Activer l'environnement virtuel
source venv/bin/activate

echo "[INFO] Environnement virtuel activé"
echo ""
echo "Démarrage des deux services..."
echo ""
echo "1. Backend (FastAPI) sera lancé sur http://127.0.0.1:8000"
echo "2. Frontend (Streamlit) sera lancé sur http://localhost:8501"
echo ""
echo "Appuyez sur Entrée pour continuer..."
read

# Lancer le backend en arrière-plan
uvicorn main:app --reload &
BACKEND_PID=$!

# Attendre un peu pour que le backend soit prêt
sleep 3

# Lancer le frontend
cd frontEnd
streamlit run app.py &
FRONTEND_PID=$!

echo "[INFO] Démarrage réussi !"
echo "Backend : http://127.0.0.1:8000"
echo "Frontend : http://localhost:8501"
echo ""
echo "Pour arrêter l'application, appuyez sur Ctrl+C"

# Attendre Ctrl+C
wait
