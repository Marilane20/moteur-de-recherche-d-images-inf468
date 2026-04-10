import streamlit as st
import requests
from PIL import Image
import io
import time

st.set_page_config(
    page_title="VisualMatch — Recherche par similarité",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background-color: #0f0f0f;
        padding: 2rem;
    }

    .block-container {
        background-color: #0f0f0f;
    }

    .stImage {
        border-radius: 4px;
        border: 1px solid #2a2a2a;
    }

    .tag-success {
        background-color: #0d2b1f;
        padding: 0.75rem 1rem;
        border-radius: 4px;
        border-left: 3px solid #1db954;
        color: #a8f0c6;
        font-size: 0.875rem;
        font-weight: 500;
    }

    .tag-error {
        background-color: #2b0d0d;
        padding: 0.75rem 1rem;
        border-radius: 4px;
        border-left: 3px solid #e53e3e;
        color: #f4a8a8;
        font-size: 0.875rem;
        font-weight: 500;
    }

    .divider {
        border: none;
        border-top: 1px solid #1f1f1f;
        margin: 1.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

st.markdown("## ◈ VisualMatch")
st.markdown(
    "<p style='color:#ffff; font-size:0.9rem; margin-top:-0.5rem;'>"
    "Recherche d'images par similarité vectorielle — CLIP + ChromaDB"
    "</p>",
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown("### Panneau de configuration")
    st.markdown("---")
    st.markdown("**État du serveur**")

    try:
        r = requests.get(f"{BACKEND_URL}/", timeout=2)
        st.success("Serveur opérationnel")
    except:
        st.error("Serveur inaccessible")
        st.warning("Le backend FastAPI doit être lancé.")
        st.code("uvicorn main:app --reload", language="bash")

    st.markdown("---")
    st.markdown(
        "<p style='font-size:0.78rem; color:#fff;'>v1.0 · CLIP ViT-B/32 · L2 distance</p>",
        unsafe_allow_html=True
    )

col_upload, col_results = st.columns([1, 1])

with col_upload:
    st.markdown("#### Image source")
    uploaded_file = st.file_uploader(
        "Formats acceptés : JPG, PNG",
        type=["jpg", "jpeg", "png"],
        help="L'image sera encodée et comparée aux vecteurs de la base"
    )

if uploaded_file is not None:
    with col_upload:
        st.image(uploaded_file, caption="Image chargée", use_column_width=True)

    with col_results:
        st.markdown("#### Correspondances")

        if st.button("Lancer la recherche →", key="search_btn", use_container_width=True):
            with st.spinner("Encodage et recherche en cours..."):
                try:
                    files = {
                        'file': ('image.jpg', uploaded_file, 'image/jpeg')
                    }

                    response = requests.post(
                        f"{BACKEND_URL}/search",
                        files=files,
                        timeout=30
                    )

                    if response.status_code == 200:
                        results = response.json()

                        st.markdown(
                            '<div class="tag-success">Requête traitée — résultats disponibles</div>',
                            unsafe_allow_html=True
                        )

                        st.markdown("<hr class='divider'>", unsafe_allow_html=True)

                        if results['results']:
                            st.markdown("**Images correspondantes :**")

                            for idx, result in enumerate(results['results'], 1):
                                with st.container():
                                    st.markdown(f"**#{idx}**")

                                    col_img, col_meta = st.columns([2, 1])

                                    with col_img:
                                        try:
                                            image_path = result['metadata']['path']
                                            img = Image.open(image_path)
                                            st.image(img, caption=f"Identifiant : {result['id']}", use_column_width=True)
                                        except Exception as e:
                                            st.warning(f"Fichier non accessible : {e}")

                                    with col_meta:
                                        st.metric("Identifiant", result['id'])
                                        st.metric("Score L2", f"{result['score']:.4f}")

                                    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
                        else:
                            st.warning("Aucune correspondance trouvée dans la base.")

                    else:
                        st.markdown(
                            f'<div class="tag-error">Erreur HTTP {response.status_code}</div>',
                            unsafe_allow_html=True
                        )
                        st.error(response.text)

                except requests.exceptions.ConnectionError:
                    st.markdown(
                        '<div class="tag-error">Connexion refusée — le backend est injoignable.</div>',
                        unsafe_allow_html=True
                    )
                except requests.exceptions.Timeout:
                    st.markdown(
                        '<div class="tag-error">Délai dépassé — la requête a expiré. Réessayez.</div>',
                        unsafe_allow_html=True
                    )
                except Exception as e:
                    st.markdown(
                        f'<div class="tag-error">Erreur inattendue : {str(e)}</div>',
                        unsafe_allow_html=True
                    )

else:
    with col_results:
        st.markdown("#### Correspondances")
        st.info("Chargez une image pour démarrer la recherche.")

st.markdown("---")

st.markdown(
    "<p style='font-size:0.75rem; color:#444; text-align:center; margin-top:2rem;'>"
    "INF468 — Modélisation des grands volumes de données"
    "</p>",
    unsafe_allow_html=True
)