import numpy as np
from database import collection
from PIL import Image

# On définit la fonction qu'on pourra appeler n'importe où
def search_similar_image(image_file):
    """
    Prend une image (objet PIL) et cherche dans la base.
    """
    query_array = np.array(image_file.convert("RGB"))
    
    results = collection.query(
        query_images=[query_array],
        n_results=3
    )
    return results