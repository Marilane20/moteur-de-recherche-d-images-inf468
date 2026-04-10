import streamlit as st
import requests
from PIL import Image
import io
import os

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="VisualMatch — Recherche par similarité",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. STYLE CSS PERSONNALISÉ ( Look Premium Dark )
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stImage { border-radius: 8px; border: 1px solid #2a2a2a; }
    .tag-success { 
        background-color: #0d2b1f; padding: 0.75rem 1rem; border-radius: 4px;
        border-left: 3px solid #1db954; color: #a8f0c6; font-size: 0.875rem; font-weight: 500;
    }
    .tag-error {
        background-color: #2b0d0d; padding: 0.75rem 1rem; border-radius: 4px;
        border-left: 3px solid #e53e3e; color: #f4a8a8; font-size: 0.875rem; font-weight: 500;
    }
    .divider { border: none; border-top: 1px solid #1f1f1f; margin: 1.5rem 0; }
    </style>
""", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

# 3. EN-TÊTE
st.markdown("## ◈ VisualMatch")
st.markdown("<p style='color:#ffff; font-size:0.9rem; margin-top:-0.5rem;'>Moteur de recherche d'images vectoriel — CLIP + ChromaDB</p>", unsafe_allow_html=True)

# 4. BARRE LATÉRALE (Sidebar)
with st.sidebar:
    st.markdown("### Configuration")
    st.markdown("---")
    st.markdown("**Statut du Backend**")
    try:
        r = requests.get(f"{BACKEND_URL}/", timeout=2)
        st.success("Connecté au serveur")
    except:
        st.error("Serveur hors ligne")
        st.info("Lancez : uvicorn main:app --reload")
    
    st.markdown("---")
    st.caption("Projet INF468 - Big Data")
    st.caption("Modèle : CLIP ViT-B/32")

# 5. ZONE DE CHARGEMENT
col_upload, col_results = st.columns([1, 1])

with col_upload:
    st.markdown("#### Image source")
    uploaded_file = st.file_uploader("Fichier image (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with col_upload:
        st.image(uploaded_file, caption="Recherche en cours...", use_container_width=True)

    with col_results:
        st.markdown("#### Correspondances")
        if st.button("Lancer la recherche →", use_container_width=True):
            with st.spinner("Analyse des vecteurs..."):
                try:
                    # Envoi de l'image au Backend FastAPI
                    files = {'file': ('query.jpg', uploaded_file.getvalue(), 'image/jpeg')}
                    response = requests.post(f"{BACKEND_URL}/search", files=files, timeout=30)

                    if response.status_code == 200:
                        data = response.json()
                        st.markdown('<div class="tag-success">Analyse terminée avec succès</div>', unsafe_allow_html=True)
                        st.markdown("<hr class='divider'>", unsafe_allow_html=True)

                        if data['results']:
                            for idx, res in enumerate(data['results'], 1):
                                with st.container():
                                    st.markdown(f"**Résultat #{idx}**")
                                    c_img, c_meta = st.columns([2, 1])
                                    
                                    with c_img:
                                        try:
                                            # LOGIQUE DE CHEMIN DYNAMIQUE (Fix pour Windows/Linux)
                                            file_name = os.path.basename(res['metadata']['path'])
                                            
                                            # On cherche le dossier dataset à la racine du projet
                                            # On remonte d'un niveau si on est dans /frontend
                                            current_dir = os.path.dirname(os.path.abspath(__file__))
                                            root_dir = os.path.abspath(os.path.join(current_dir, ".."))
                                            full_path = os.path.join(root_dir, "dataset", file_name)
                                            
                                            img = Image.open(full_path)
                                            st.image(img, use_container_width=True)
                                        except Exception as e:
                                            st.error("Fichier introuvable")
                                            st.caption(f"Nom : {file_name}")

                                    with c_meta:
                                        st.metric("Score L2", f"{res['score']:.4f}")
                                        st.caption(f"ID: {res['id']}")
                                    
                                    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
                        else:
                            st.warning("Aucune image similaire trouvée.")
                    else:
                        st.error(f"Erreur Backend ({response.status_code})")
                except Exception as e:
                    st.error(f"Erreur de connexion : {e}")
else:
    with col_results:
        st.info("Veuillez charger une image pour lancer la comparaison vectorielle.")

# 6. FOOTER
st.markdown("<p style='font-size:0.75rem; color:#444; text-align:center; margin-top:2rem;'>University of Yaoundé I — Master SIGL</p>", unsafe_allow_html=True)