
# ⚽ Previsor de Resultados do Brasileirão - Temporada 2024

![versão](https://img.shields.io/badge/version-1.1.0-blue)

<p align="center">
  <img src="docs/pitaco.png" alt="PITACO Banner" width="700">
</p>

Este projeto utiliza **Machine Learning e dados reais de partidas** para prever as probabilidades de resultado (vitória do mandante, empate ou vitória do visitante) dos jogos do Campeonato Brasileiro Série A 2024.

Conta com uma interface visual criada com **Streamlit** e um modelo de classificação treinado com **Random Forest + SMOTE** para balancear as classes.

---

## 🧠 O que este modelo faz?

Dado um confronto entre dois times (mandante x visitante), o modelo retorna a probabilidade prevista de:

- 🏠 Vitória do mandante  
- ⚖️ Empate  
- ✈️ Vitória do visitante  

Os resultados são exibidos de forma interativa em uma interface web.

---

## 📊 Tecnologias utilizadas

- Python  
- Pandas  
- Scikit-learn  
- imbalanced-learn (SMOTE)  
- Streamlit  

---

## 📁 Estrutura do projeto

```
brazilian-football-predictor/
├── app.py                          # Interface visual (Streamlit)
├── train_model.py                 # Treinamento do modelo com engenharia de features
├── model.pkl                      # Modelo Random Forest treinado
├── encoder.pkl                    # Codificador de times (LabelEncoder)
├── requirements.txt               # Dependências do projeto
├── data/
│   └── brasileirao_2024_features.csv  # Dados enriquecidos com features históricas
```

---

## 🧠 Engenharia de Features

O dataset foi enriquecido com informações históricas dos times antes de cada jogo:

- `home_points_so_far`: Pontos acumulados pelo mandante até o jogo
- `away_points_so_far`: Pontos acumulados pelo visitante até o jogo
- `home_goal_diff_so_far`: Saldo de gols do mandante até o jogo
- `away_goal_diff_so_far`: Saldo de gols do visitante até o jogo

Essas features fornecem mais contexto e tornam as previsões mais confiáveis.

---

## 🚀 Como executar o projeto

### 1. Clone ou baixe este repositório

Ou [baixe a versão ZIP](https://github.com/fschaitel/pitaco/archive/refs/heads/main.zip)

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # no Windows
# ou
source venv/bin/activate  # no Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Treine o modelo (apenas uma vez)

```bash
python train_model.py
```

### 5. Rode a interface

```bash
streamlit run app.py
```

Abra a URL exibida no terminal (geralmente http://localhost:8501)

---

## 🌐 Teste online

👉 [Clique aqui para acessar o PITACO](https://pitaco-pysaqfjwjkhxncqd43ftmf.streamlit.app/)

> ⚠️ Pode levar alguns segundos para carregar na primeira vez.

---

## 🎯 Exemplo de uso

Selecione dois times e o sistema mostrará algo como:

```
🎯 Probabilidades para Flamengo x Palmeiras
- 🏠 Vitória do mandante: 58.4%
- ⚖️ Empate: 23.7%
- ✈️ Vitória do visitante: 17.9%
```

---

## 🧪 Detalhes do modelo

- **Classificador:** `RandomForestClassifier`
- **Balanceamento:** `SMOTE` para corrigir desbalanceamento de empates
- **Entradas:** Codificações dos times, pontos acumulados e saldo de gols
- **Saída:** Probabilidades calculadas com `predict_proba()`
- **Avaliação:** Acurácia, matriz de confusão e relatório de classificação

---

## 🖼️ Destaques da interface

A interface é visualmente estilizada com:

- Um **campo de futebol real ao fundo**
- Texto leve e emojis para clareza e simpatia

---

## 🆕 Novidades da versão 1.1.0

- ✅ Adição de features históricas (pontos e saldo de gols)
- ✅ Lógica de treinamento aprimorada com engenharia de dados
- ✅ Substituição de previsões genéricas por entradas baseadas em dados reais
- ✅ Dataset enriquecido salvo em CSV
- ✅ App atualizado para usar o novo modelo com contexto histórico

---

## ✍️ Autor

Criado por Felipe Schaitel  
Um projeto acessível e inspirado no futebol, voltado para aprendizado e visualização.

---

## 📌 Licença

Este projeto está licenciado sob a Licença MIT.
