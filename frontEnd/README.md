# 🎨 Frontend Streamlit - Moteur de Recherche d'Images

Interface utilisateur intuitive et moderne pour rechercher des images similaires dans la base de données vectorielle.

---

## 📋 Prérequis

- Python 3.8+
- Le backend FastAPI doit être en cours d'exécution sur `http://127.0.0.1:8000`

---

## 🚀 Installation et Lancement

### 1. Installer les dépendances du frontend

```bash
# Depuis le dossier frontEnd
pip install -r requirements.txt
```

### 2. Vérifier que le backend est actif

Assurez-vous que le serveur FastAPI est en cours d'exécution :

```bash
# Dans un terminal séparé, depuis la racine du projet
uvicorn main:app --reload
```

Le backend devrait être accessible sur `http://127.0.0.1:8000`

### 3. Lancer l'application Streamlit

```bash
# Depuis le dossier frontEnd
streamlit run app.py
```

L'interface sera accessible sur `http://localhost:8501`

---

## 🎯 Utilisation

1. **Télécharger une image** : Cliquez sur "Choisissez une image" et sélectionnez un fichier JPG ou PNG
2. **Visualiser l'image** : L'image uploadée s'affiche dans la colonne gauche
3. **Rechercher** : Cliquez sur le bouton "🚀 Rechercher des images similaires"
4. **Consulter les résultats** : Les 3 images les plus similaires de la base de données s'affichent avec :
   - Un aperçu de l'image
   - L'ID de l'image
   - Le score de similarité

---

## 🔧 Configuration

Si vous changez l'URL du backend, modifiez cette ligne dans `app.py` :

```python
BACKEND_URL = "http://127.0.0.1:8000"
```

---

## 📁 Structure

```
frontEnd/
├── app.py              # Application Streamlit principale
├── requirements.txt    # Dépendances Python
└── README.md          # Ce fichier
```

---

## 🎨 Fonctionnalités

✅ Upload d'images (JPG, PNG)  
✅ Preview de l'image uploadée  
✅ Loading spinner pendant la recherche  
✅ Affichage des 3 images les plus similaires  
✅ Score de similarité pour chaque résultat  
✅ Vérification du statut du backend  
✅ Interface responsive et moderne  
✅ Gestion des erreurs complète  

---

## 🐛 Dépannage

### "Backend indisponible"
- Vérifiez que le serveur FastAPI est en cours d'exécution
- Assurez-vous qu'il tourne sur le port 8000

### "Aucune image similaire trouvée"
- Vérifiez que la base de données est bien indexée : `python ingest.py`
- Vérifiez que le dossier `dataset/` contient des images

### Erreur de connexion
- Vérifiez l'URL du backend dans `app.py`
- Vérifiez la connectivité réseau

---

## 📚 Dépendances

- **Streamlit** : Framework pour l'interface web
- **Requests** : Client HTTP pour communiquer avec le backend
- **Pillow** : Traitement des images

---

## 📝 Notes

- Le score de similarité est inversé : plus la valeur est **basse**, plus l'image est similaire
- Les images doivent être en format JPG ou PNG
- Le backend utilise le modèle CLIP d'OpenAI pour l'embedding
- La recherche max retourne les 3 résultats les plus similaires

---

**Projet INF468** - Modélisation des grands volumes de données (BigData) 🎓
