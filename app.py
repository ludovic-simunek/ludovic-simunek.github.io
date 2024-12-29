import streamlit as st

# Titre
st.title('Mon Portfolio Data Science')

# Introduction
st.write("""
Bienvenue sur mon portfolio de projets en Data Science !  
Vous trouverez ici des exemples de projets que j'ai réalisés dans différents domaines de la data science.
""")

# Section Projets
st.header('Projets')

st.subheader('Projet 1: Analyse du Titanic')
st.write("""
Description du projet Titanic, ce que j'ai appris et réalisé avec les données du Titanic.
""")
st.image('image_titanic.png', caption='Graphique du projet Titanic')

st.subheader('Projet 2: Analyse de données financières')
st.write("""
Description d'un projet d'analyse des données financières où j'ai utilisé Python et Pandas pour extraire des insights.
""")
st.image('image_finances.png', caption='Graphique du projet financier')

# Ajouter des liens vers des projets GitHub ou autres
st.write("[Voir le code source sur GitHub](https://github.com/moncompte/monrepo)")
