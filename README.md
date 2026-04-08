# 🔍 Moteur de Recherche d'Images par Similarité (IA)
### Projet INF468 - modelisation des grands volume de donnees : bigdata

Ce projet implémente un système de recherche d'images . Il utilise le modèle de Deep Learning **CLIP (OpenAI)** pour transformer des images en vecteurs mathématiques et **ChromaDB** pour le stockage et la recherche haute performance.

---

## 🏗️ Architecture du Projet

Le projet suit une architecture moderne en micro-services :
*   **Backend :** FastAPI (Python) - Gère l'IA, la base de données vectorielle et le service d'images.
*   **Frontend :** Streamlit (Python) - Interface utilisateur intuitive pour l'upload et l'affichage des résultats.
*   **Base de données :** ChromaDB .

---

## 🚀 Guide d'Installation (Équipe)

Suivez ces étapes scrupuleusement pour faire fonctionner le projet sur votre machine.

### 1. Clonage et Environnement
```bash
# Cloner le dépôt
git clone <URL_DE_VOTRE_DEPOT_GITHUB>
cd ImageSearch_project

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate

### 2. Installation des dépendances
pip install -r requirements.txt

### 3. Intialisation de la base de donnees
Avant de lancer l'application, vous devez indexer les images présentes dans le dossier dataset/ :
python ingest.py

### 4. Lancement de l'Application

Vous devez ouvrir deux terminaux distincts (avec l'environnement venv activé dans les deux).

Étape 1 : Lancer le Backend (Serveur API)
Bash
uvicorn main:app --reload
Le backend tourne sur : http://127.0.0.1:8000

Étape 2 : Lancer le Frontend (Interface Web)
Bash
streamlit run app.py
L'interface sera accessible sur : https://www.google.com/search?q=http://127.0.0.1:8501

### 5. Structure des fichiers
dataset/ : Dossier contenant les images sources (JPG/PNG).

ingest.py : Script d'extraction des caractéristiques et peuplement de la DB.

database.py : Configuration de la connexion à ChromaDB.

search.py : Logique de recherche vectorielle.

main.py : Point d'entrée de l'API FastAPI (Routes et CORS).

app.py : Interface utilisateur Streamlit.

requirements.txt : Liste des bibliothèques Python nécessaires.

.gitignore : Protection des fichiers lourds et temporaires.

### 6. Équipe de développement
 Backend : KAMGA KAKEU, NGUEGUANG ULRICH

Frontend : NGUENGANG ULRICH,MICHAEL JACKSON


