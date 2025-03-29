# ⚽ Previsor de Partidas do Campeonato Brasileiro – Temporada 2024

Este projeto utiliza **Machine Learning e dados reais de partidas** para prever as probabilidades de resultado (vitória do mandante, empate, vitória do visitante) para os jogos do Campeonato Brasileiro Série A de 2024.

Ele conta com uma interface visual desenvolvida com **Streamlit** e um modelo de classificação treinado com **Random Forest + SMOTE** para lidar com o desbalanceamento de classes.

---

## 🧠 O que este modelo faz?

Dado um confronto entre dois times (mandante vs visitante), o modelo retorna a probabilidade prevista de:

- 🏠 Vitória do mandante  
- ⚖️ Empate  
- 🚗 Vitória do visitante  

Os resultados são exibidos interativamente em uma aplicação web.

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
├── app.py                  # Interface Streamlit
├── predictor.py            # Versão por linha de comando
├── requirements.txt        # Dependências do projeto
├── data/
│   └── brasileirao_2024.csv  # Dados reais das partidas
```

---

## 🚀 Como executar o projeto

### 1. Clone ou baixe este repositório

Ou [clique aqui para baixar a versão ZIP](https://github.com/fschaitel/pitaco/archive/refs/heads/main.zip)

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

### 4. Execute a interface web

```bash
streamlit run app.py
```

Abra a URL exibida no terminal (geralmente http://localhost:8501)

---

## 🌐 Acesse online:

👉 [Clique aqui para abrir o PITACO no navegador](https://pitaco-pysaqfjwjkhxncqd43ftmf.streamlit.app/)

> ⚠️ Pode levar alguns segundos para carregar na primeira vez.

---

## 🎯 Exemplo de uso

Selecione dois times e o sistema exibirá algo como:

```
🎯 Probabilidades para Flamengo vs Palmeiras
- 🏠 Mandante vence: 58.4%
- ⚖️ Empate: 23.7%
- 🚗 Visitante vence: 17.9%
```

---

## 🧪 Detalhes do modelo

- **Classificador:** `RandomForestClassifier`  
- **Balanceamento:** `SMOTE` para corrigir a super-representação de empates  
- **Entrada:** Times mandante e visitante  
- **Saída:** Probabilidades com `predict_proba()`

---

## 🖼️ Destaques da interface

A interface é visualmente estilizada com:
- Um **fundo realista de campo de futebol**
- Texto claro e emojis para melhor compreensão

---

## ✍️ Autor

Criado por Felipe Schaitel  
Um projeto de machine learning inspirado no futebol, para iniciantes!

---

## 📌 Licença

Este projeto está licenciado sob a Licença MIT.
