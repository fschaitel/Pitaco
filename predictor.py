import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Carregar os dados
df = pd.read_csv("data/brasileirao_2024.csv")

# Codificar os times
le_team = LabelEncoder()
df['home_team_enc'] = le_team.fit_transform(df['home_team'])
df['away_team_enc'] = le_team.transform(df['away_team'])

# Mapear o resultado para valores numéricos
result_map = {'H': 0, 'D': 1, 'A': 2}
inv_result_map = {0: 'Vitória do mandante', 1: 'Empate', 2: 'Vitória do visitante'}
df['result_enc'] = df['result'].map(result_map)

# Definir variáveis independentes e alvo
X = df[['home_team_enc', 'away_team_enc']]
y = df['result_enc']

# Treinar o modelo
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Interação com o usuário
print("Digite os nomes dos times exatamente como aparecem no dataset.
")
home = input("Time mandante: ").strip()
away = input("Time visitante: ").strip()

if home in le_team.classes_ and away in le_team.classes_:
    home_enc = le_team.transform([home])[0]
    away_enc = le_team.transform([away])[0]
    input_data = pd.DataFrame([[home_enc, away_enc]], columns=['home_team_enc', 'away_team_enc'])
    
    probas = model.predict_proba(input_data)[0]
    
    print(f"\nProbabilidades para {home} x {away}:")
    for i, prob in enumerate(probas):
        print(f"- {inv_result_map[i]}: {prob * 100:.1f}%")
else:
    print("\n❌ Um ou ambos os times não foram encontrados no dataset.")
    print("Use times como:", ", ".join(sorted(set(df['home_team'].unique()) | set(df['away_team'].unique()))))
