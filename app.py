import streamlit as st

# Fonction pour la page d'accueil
def accueil():
    st.title("Bienvenue sur mon Portfolio")
    st.write("Voici quelques-uns de mes projets de Data Analyst.")
    # Ajouter des éléments comme une introduction, des compétences, etc.

# Fonction pour le projet 1
def projet_1():
    st.title("Projet 1 : Analyse Titanic")
    st.write("Détails du projet Titanic, description, objectifs et résultats.")
    # Ajoute ici le code spécifique au projet 1, comme des visualisations, des analyses, etc.

# Fonction pour le projet 2
def projet_2():
    st.title("Projet 2 : Analyse des Films")
    st.write("Détails du projet d'analyse des films, description, objectifs et résultats.")
    # Ajoute ici le code spécifique au projet 2.

# Fonction pour la page de contact
def contact():
    st.title("Contact")
    st.write("Voici mes informations de contact.")
    st.write("Email : tonemail@example.com")
    # Ajoute des informations de contact ou un formulaire.

# Configuration de la barre latérale pour la navigation
pages = {
    "Accueil": accueil,
    "Projet 1": projet_1,
    "Projet 2": projet_2,
    "Contact": contact
}

# Sélection de la page via le widget sidebar
page_selection = st.sidebar.radio("Choisir une page", list(pages.keys()))

# Affichage de la page choisie
pages[page_selection]()
