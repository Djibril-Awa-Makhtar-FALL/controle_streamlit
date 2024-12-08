import streamlit as st
import pandas as pd
import joblib

# Charger le modèle
model_path = r"C:\Users\DELL\Desktop\streamlit\model.pkl"
model = joblib.load(model_path)

# Charger les encodeurs
label_encoders_path = r"C:\Users\DELL\Desktop\streamlit\label_encoders.pkl"
label_encoders_path = joblib.load(label_encoders_path)
# Titre de l'application
st.title("Prédiction de Churn")

# Créer un formulaire pour les saisies utilisateur
st.header("Entrez les informations de l'utilisateur")

st.text_input("Entrer votre Nom :")

st.text_input("Entrer votre Prenom :")

st.number_input("Age :")

# Liste des genres
genres = ["Homme", "Femme", "Autre"]

#Sélection pour le genre
genre = st.selectbox("Genre :", genres)

# Créer un formulaire pour les saisies utilisateur
st.header("Entrez les détails de l'utilisateur")

## Champs de saisie pour les caractéristiques
region = st.text_input("Région", placeholder="Exemple : DAKAR")
tenure = st.number_input("Durée d'abonnement (en mois)", min_value=0, placeholder="Exemple : 24")
montant = st.number_input("Montant", placeholder="Exemple : 4250")
frequence_rech = st.number_input("Fréquence de recherche", placeholder="Exemple : 15")
revenue = st.number_input("Revenu", placeholder="Exemple : 4251")
arpu_segment = st.text_input("Segment ARPU", placeholder="Exemple : 1417")
frequence = st.number_input("Fréquence", placeholder="Exemple : 17")
data_volume = st.number_input("Volume de données", placeholder="Exemple : 4")
on_net = st.number_input("Utilisation on-net", placeholder="Exemple : 388")
orange = st.number_input("Utilisation Orange", placeholder="Exemple : 46")
tigo = st.number_input("Utilisation Tigo", placeholder="Exemple : 1")
zone1 = st.number_input("Zone 1", placeholder="Exemple : 2")
zone2 = st.number_input("Zone 2", placeholder="Exemple : 3")
mrg = st.number_input("Marge", placeholder="Exemple : 54")
regularity = st.number_input("Régularité", placeholder="Exemple : 8")
top_pack = st.text_input("Pack principal", placeholder="Exemple : On net 200F=Unlimited_call24H")
freq_top_pack = st.number_input("Fréquence du pack principal", placeholder="Exemple : 0")

# Bouton pour faire la prédiction

if st.button("Prédire"):
    # Créer un DataFrame avec les données saisies
    input_data = pd.DataFrame({
        'REGION': [region],
        'TENURE': [tenure],
        'MONTANT': [montant],
        'FREQUENCE_RECH': [frequence_rech],
        'REVENUE': [revenue],
        'ARPU_SEGMENT': [arpu_segment],
        'FREQUENCE': [frequence],
        'DATA_VOLUME': [data_volume],
        'ON_NET': [on_net],
        'ORANGE': [orange],
        'TIGO': [tigo],
        'ZONE1': [zone1],
        'ZONE2': [zone2],
        'MRG': [mrg],
        'REGULARITY': [regularity],
        'TOP_PACK': [top_pack],
        'FREQ_TOP_PACK': [freq_top_pack]
    })

 #Faire la prédiction
    prediction = model.predict(input_data)

    # Afficher le résultat
    st.write("Résultat de la prédiction : ", "Désabonnement" if prediction[0] == 1 else "Pas de désabonnement")


#st.write("Colonnes attendues par le modèle :", model.feature_names_in_)
