import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/upload-gpx"  # ton endpoint FastAPI

st.title("Analyse GPX 🏃‍♂️")

# Étape 1 : uploader le fichier
uploaded_file = st.file_uploader("Choisis un fichier GPX", type=["gpx"])

# Étape 2 : bouton pour envoyer au backend
if uploaded_file is not None:
    if st.button("Analyser le fichier"):
        # Envoi au backend
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/gpx+xml")}
        with st.spinner("Analyse en cours..."):
            try:
                response = requests.post(API_URL, files=files)
                response.raise_for_status()
                data = response.json()
                st.success("Analyse terminée ✅")

                # Affichage des résultats
                st.subheader("Résultats")
                for k, v in data.items():
                    st.write(f"**{k}** : {v}")

            except requests.RequestException as e:
                st.error(f"Erreur de requête : {e}")
