import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from imblearn.over_sampling import SMOTE

# Carregar os dados
df = pd.read_csv("data/brasileirao_2024.csv")

# Codificar times
le_team = LabelEncoder()
df['home_team_enc'] = le_team.fit_transform(df['home_team'])
df['away_team_enc'] = le_team.transform(df['away_team'])

# Mapear resultado
result_map = {'H': 0, 'D': 1, 'A': 2}
df['result_enc'] = df['result'].map(result_map)

# Inicializar features acumuladas
df['home_points_so_far'] = 0
df['away_points_so_far'] = 0
df['home_goal_diff_so_far'] = 0
df['away_goal_diff_so_far'] = 0

def calc_points(res, team, is_home):
    if res == 'H' and is_home:
        return 3
    elif res == 'A' and not is_home:
        return 3
    elif res == 'D':
        return 1
    return 0

# Atualizar features com base no histórico anterior
team_stats = {}
rows = []

for _, row in df.iterrows():
    home = row['home_team']
    away = row['away_team']

    # Pontos e saldo anteriores
    h_pts = team_stats.get(home, {}).get('points', 0)
    a_pts = team_stats.get(away, {}).get('points', 0)
    h_diff = team_stats.get(home, {}).get('goal_diff', 0)
    a_diff = team_stats.get(away, {}).get('goal_diff', 0)

    row['home_points_so_far'] = h_pts
    row['away_points_so_far'] = a_pts
    row['home_goal_diff_so_far'] = h_diff
    row['away_goal_diff_so_far'] = a_diff

    # Atualizar stats após o jogo
    home_score = row.get('home_score', 0)
    away_score = row.get('away_score', 0)
    result = row['result']

    h_points = calc_points(result, home, True)
    a_points = calc_points(result, away, False)

    team_stats.setdefault(home, {'points': 0, 'goal_diff': 0})
    team_stats.setdefault(away, {'points': 0, 'goal_diff': 0})

    team_stats[home]['points'] += h_points
    team_stats[away]['points'] += a_points
    team_stats[home]['goal_diff'] += home_score - away_score
    team_stats[away]['goal_diff'] += away_score - home_score

    rows.append(row)

# Atualizar o dataframe
full_df = pd.DataFrame(rows)
full_df.to_csv("data/brasileirao_2024_features.csv", index=False)

# Features finais para o modelo
X = full_df[['home_team_enc', 'away_team_enc', 'home_points_so_far', 'away_points_so_far', 'home_goal_diff_so_far', 'away_goal_diff_so_far']]
y = full_df['result_enc']

# Balanceamento com SMOTE
sm = SMOTE(random_state=42)
X, y = sm.fit_resample(X, y)

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
print("=== Avaliação do Modelo ===")
print("Acurácia:", accuracy_score(y_test, y_pred))
print("Matriz de Confusão:\n", confusion_matrix(y_test, y_pred))
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))

# Salvar modelo e codificador
joblib.dump(model, "model.pkl")
joblib.dump(le_team, "encoder.pkl")
print("\n✅ Modelo, codificador e CSV com features salvos com sucesso!")