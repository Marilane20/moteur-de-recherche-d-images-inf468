from fastapi import FastAPI, UploadFile, File
from database import collection
from PIL import Image
import numpy as np
import io

app = FastAPI(title="Moteur de Recherche d'Images - INF468")

@app.get("/")
def home():
    return {"message": "Le serveur de recherche d'images est en ligne !"}

@app.post("/search")
async def search(file: UploadFile = File(...)):
    # Lire l'image envoyée par l'utilisateur
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content)).convert("RGB")
    
    # Convertir en Numpy pour ChromaDB
    query_array = np.array(img)
    
    # Interroger la base de données
    results = collection.query(
        query_images=[query_array],
        n_results=3
    )
    
    # Retourner les résultats proprement
    formatted_results = []
    for i in range(len(results['ids'][0])):
        formatted_results.append({
            "id": results['ids'][0][i],
            "score": results['distances'][0][i],
            "metadata": results['metadatas'][0][i]
        })
        
    return {"results": formatted_results}