import streamlit as st
import pandas as pd
import gpxpy

st.set_page_config(page_title="Visualisation GPX", layout="wide")

st.title("Visualisation d'un fichier GPX sur une carte 🗺️")

# Étape 1 : uploader le fichier
uploaded_file = st.file_uploader("Charge un fichier .gpx", type=["gpx"])

# Étape 2 : bouton pour envoyer au backend
if uploaded_file is not None:
    # Lecture du contenu
    content = uploaded_file.read()
    gpx = gpxpy.parse(content.decode("utf-8"))

    # Extraction des points
    points = []
    for track in gpx.tracks:
        # les points seront certainement stockés en base, il faudra :
        #   - trouver un moyen pour les stocker
        #   - les récupérer ici avec la DAO
        for segment in track.segments:
            for point in segment.points:
                points.append({
                    "lat": point.latitude,
                    "lon": point.longitude,
                    "elev": point.elevation,
                })

    if not points:
        st.error("Aucun point trouvé dans ce fichier GPX.")
    else:
        df = pd.DataFrame(points)

        st.subheader("Carte")
        # st.map attend les colonnes lat / lon
        st.map(df[["lat", "lon"]])

        st.subheader("Stats de base")
        st.write(f"Nombre de points : {len(df)}")
        st.write(f"Altitude min : {df['elev'].min():.1f} m")
        st.write(f"Altitude max : {df['elev'].max():.1f} m")
