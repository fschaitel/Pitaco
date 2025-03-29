# ⚽ Brazilian Football Match Predictor - 2024 Season

This project uses **Machine Learning and real match data** to predict the outcome probabilities (home win, draw, away win) for matches in the 2024 Brazilian football league (Campeonato Brasileiro Série A).

It features a visual interface built with **Streamlit** and a classification model trained using **Random Forest + SMOTE** to address class imbalance.

---

## 🧠 What does this model do?

Given a match between two teams (home vs away), the model returns the predicted probability of:

- 🏠 Home team win  
- ⚖️ Draw  
- 🚗 Away team win  

These results are displayed interactively in a web app.

---

## 📊 Technologies used

- Python
- Pandas
- Scikit-learn
- imbalanced-learn (SMOTE)
- Streamlit

---

## 📁 Project structure

```
brazilian-football-predictor/
├── app.py                  # Streamlit interface
├── predictor.py            # Command-line version
├── requirements.txt        # Required dependencies
├── data/
│   └── brasileirao_2024.csv  # Real match data
```

---

## 🚀 How to run the project

### 1. Clone or download this repository

Or [download the ZIP version](https://github.com/fschaitel/pitaco/archive/refs/heads/main.zip)

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
# or
source venv/bin/activate  # on Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the web interface

```bash
streamlit run app.py
```

Open the URL displayed in the terminal (usually http://localhost:8501)

---

## 🌐 Try it online:

👉 [Click here to open PITACO in your browser]([https://your-app.streamlit.app](https://pitaco-pysaqfjwjkhxncqd43ftmf.streamlit.app/))

> ⚠️ It might take a few seconds to load on the first visit.

---

## 🎯 Example usage

Select two teams and the system will output something like:

```
🎯 Probabilities for Flamengo vs Palmeiras
- 🏠 Home win: 58.4%
- ⚖️ Draw: 23.7%
- 🚗 Away win: 17.9%
```

---

## 🧪 Model details

- **Classifier:** `RandomForestClassifier`
- **Balancing:** `SMOTE` to fix draw over-representation
- **Input:** Home and away teams
- **Output:** Probabilities using `predict_proba()`

---

## 🖼️ Interface highlights

The interface is visually styled with:
- A **real football field background**
- Light text and emojis for clarity and friendliness

---

## ✍️ Author

Created by Felipe Schaitel  
A beginner-friendly, football-inspired machine learning project, designed for both learning and visual appeal.

---

## 📌 License

This project is licensed under the MIT License.
