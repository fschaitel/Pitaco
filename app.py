import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

# Aplicar estilo de fundo de gramado de verdade e layout limpo
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://wallpapercave.com/wp/wp10634634.jpg');
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

# Começar layout visual limpo e sem caixa solta
st.title("⚽ PITACO! - Brasileirão 2024")
st.markdown("Escolha os times abaixo para ver a **probabilidade de vitória, empate ou derrota** com base no histórico real.")

# Carregar dados
df = pd.read_csv("data/brasileirao_2024.csv")

# Codificar times
le_team = LabelEncoder()
df['home_team_enc'] = le_team.fit_transform(df['home_team'])
df['away_team_enc'] = le_team.transform(df['away_team'])

# Mapear resultado
result_map = {'H': 0, 'D': 1, 'A': 2}
inv_result_map = {0: '🏠 Vitória do mandante', 1: '⚖️ Empate', 2: '🚗 Vitória do visitante'}
df['result_enc'] = df['result'].map(result_map)

# Preparar dados para treino
X = df[['home_team_enc', 'away_team_enc']]
y = df['result_enc']

# Aplicar SMOTE para balanceamento das classes
sm = SMOTE(random_state=42)
X, y = sm.fit_resample(X, y)

# Treinar modelo
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Interface
team_list = sorted(df['home_team'].unique())
home = st.selectbox("🔵 Time mandante:", team_list)
away = st.selectbox("🔴 Time visitante:", team_list)

if home and away:
    if home == away:
        st.warning("Os times devem ser diferentes.")
    else:
        home_enc = le_team.transform([home])[0]
        away_enc = le_team.transform([away])[0]
        input_data = pd.DataFrame([[home_enc, away_enc]], columns=['home_team_enc', 'away_team_enc'])

        probas = model.predict_proba(input_data)[0]

        st.subheader(f"🎯 Probabilidades para {home} x {away}")
        for i, prob in enumerate(probas):
            st.markdown(f"<h4>{inv_result_map[i]}: <strong>{prob * 100:.1f}%</strong></h4>", unsafe_allow_html=True)

