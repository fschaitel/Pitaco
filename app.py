import pandas as pd
import streamlit as st
import joblib

# Aplicar estilo de fundo de gramado de verdade e layout limpo
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=2448,h=1632,fit=crop/mnlqpZaW31i8aBMn/chatgpt-image-4-de-abr.-de-2025-00_30_59-ALpeBe3QOGSl2rPA.png');
        background-size: cover;
        background-position: center;
    }
    .content-box {
        background-color: rgba(255, 255, 255, 0.94);
        padding: 2rem;
        border-radius: 10px;
        max-width: 750px;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚽ PITACO! - Brasileirão 2024")
st.markdown("Escolha os times abaixo para ver a **probabilidade de vitória, empate ou derrota** com base no histórico real.")

# Carregar modelo e encoder
model = joblib.load("model.pkl")
le_team = joblib.load("encoder.pkl")

# Carregar dados com features
df = pd.read_csv("data/brasileirao_2024_features.csv")
team_list = sorted(df['home_team'].unique())

# Interface de seleção
home = st.selectbox("🔵 Time mandante:", team_list)
away = st.selectbox("🔴 Time visitante:", team_list)

if home and away:
    if home == away:
        st.warning("Os times devem ser diferentes.")
    else:
        # Pega a última linha que contém esse confronto (ou o mais recente)
        filtro = df[(df['home_team'] == home) & (df['away_team'] == away)]
        if filtro.empty:
            st.error("❌ Este confronto não está registrado no dataset.")
        else:
            exemplo = filtro.iloc[-1]
            home_enc = le_team.transform([home])[0]
            away_enc = le_team.transform([away])[0]

            input_data = pd.DataFrame([[home_enc, away_enc,
                                        exemplo['home_points_so_far'],
                                        exemplo['away_points_so_far'],
                                        exemplo['home_goal_diff_so_far'],
                                        exemplo['away_goal_diff_so_far']]],
                                      columns=['home_team_enc', 'away_team_enc',
                                               'home_points_so_far', 'away_points_so_far',
                                               'home_goal_diff_so_far', 'away_goal_diff_so_far'])

            probas = model.predict_proba(input_data)[0]

            inv_result_map = {0: '🏠 Vitória do mandante', 1: '⚖️ Empate', 2: '✈️ Vitória do visitante'}

            st.subheader(f"🎯 Probabilidades para {home} x {away}")
            for i, prob in enumerate(probas):
                st.markdown(f"<h4>{inv_result_map[i]}: <strong>{prob * 100:.1f}%</strong></h4>", unsafe_allow_html=True)
