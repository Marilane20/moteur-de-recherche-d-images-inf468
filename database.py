import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
import os

#  Initialisation du client ChromaDB (il va créer un dossier pour stocker les données)
client = chromadb.PersistentClient(path="./chromadb_storage")

# Choisir le "cerveau" (Embedding Function)

embedding_function = OpenCLIPEmbeddingFunction()

#  Créer ou récupérer la collection d'images(tables)
collection = client.get_or_create_collection(
    name="my_images",
    embedding_function=embedding_function
)

print(" Base de données vectorielle initialisée avec succès !")