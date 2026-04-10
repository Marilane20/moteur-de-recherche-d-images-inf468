import os
from database import collection
from PIL import Image
import numpy as np


DATASET_PATH = "./dataset"

def index_images():
    # Lister les fichiers dans le dossier dataset
    image_files = [f for f in os.listdir(DATASET_PATH) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print(" Le dossier 'dataset' est vide. Ajoute des images dedans !")
        return

    print(f" Début de l'indexation de {len(image_files)} images...")

    for image_name in image_files:
        image_path = os.path.join(DATASET_PATH, image_name)
        
        try:
            img = Image.open(image_path).convert("RGB")

            #  Convertir l'image en tableau de nombres (Numpy Array)
            img_array = np.array(img)

    
            collection.add(
                ids=[image_name],
                images=[img_array], 
                metadatas=[{"path": image_path}]
            )
            print(f" Indexé : {image_name}")
        except Exception as e:
            print(f" Erreur sur {image_name} : {e}")

    print("\n  base vectorielle remplie.")

if __name__ == "__main__":
    index_images()