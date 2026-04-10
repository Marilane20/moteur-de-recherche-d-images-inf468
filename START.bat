@REM Script de démarrage du projet complet (Backend + Frontend)
@REM Exécutez ce fichier pour lancer l'application

@echo off
echo.
echo ==========================================
echo  Moteur de Recherche d'Images - INF468
echo ==========================================
echo.

REM Vérifier que l'environnement virtuel existe
if not exist "venv\Scripts\activate.bat" (
    echo [ERREUR] L'environnement virtuel n'existe pas !
    echo Créez-le avec : python -m venv venv
    pause
    exit /b 1
)

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

echo [INFO] Environnement virtuel activé
echo.
echo Démarrage des deux services...
echo.
echo 1. Backend (FastAPI) sera lancé sur http://127.0.0.1:8000
echo 2. Frontend (Streamlit) sera lancé sur http://localhost:8501
echo.
echo Appuyez sur une touche pour continuer...
pause

REM Lancer le backend dans une nouvelle fenêtre
start cmd /k "cd /d %cd% && uvicorn main:app --reload"

REM Attendre un peu pour que le backend soit prêt
timeout /t 3 /nobreak

REM Lancer le frontend dans une nouvelle fenêtre
start cmd /k "cd /d %cd%\frontEnd && streamlit run app.py"

echo [INFO] Démarrage réussi !
echo Backend : http://127.0.0.1:8000
echo Frontend : http://localhost:8501
echo.
pause
