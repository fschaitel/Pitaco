# ⚽ Brazilian Football Match Predictor - 2024 Season

![version](https://img.shields.io/badge/version-1.1.0-blue)

<p align="center">
  <img src="docs/pitaco.png" alt="PITACO Banner" width="700">
</p>

This project uses **Machine Learning and real match data** to predict the outcome probabilities (home win, draw, away win) for matches in the 2024 Brazilian football league (Campeonato Brasileiro Série A).

It features a visual interface built with **Streamlit** and a classification model trained using **Random Forest + SMOTE** to address class imbalance.

---

## 🧠 What does this model do?

Given a match between two teams (home vs away), the model returns the predicted probability of:

- 🏠 Home team win  
- ⚖️ Draw  
- ✈️ Away team win  

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
├── app.py                          # Streamlit interface
├── train_model.py                 # Model training with feature engineering
├── model.pkl                      # Trained Random Forest model
├── encoder.pkl                    # Team LabelEncoder
├── requirements.txt              # Required dependencies
├── data/
│   └── brasileirao_2024_features.csv  # Enriched match data with features
```

---

## 🧠 Feature Engineering

The dataset now includes historically-informed features for each team before each match:

- `home_points_so_far`: Points accumulated by the home team before the match
- `away_points_so_far`: Points accumulated by the away team before the match
- `home_goal_diff_so_far`: Goal difference for the home team so far
- `away_goal_diff_so_far`: Goal difference for the away team so far

These features provide better context and improve the model’s predictive capabilities.

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

### 4. Train the model (once)
```bash
python train_model.py
```

### 5. Run the web interface

```bash
streamlit run app.py
```

Open the URL displayed in the terminal (usually http://localhost:8501)

---

## 🌐 Try it online:

👉 [Click here to open PITACO in your browser](https://pitaco-pysaqfjwjkhxncqd43ftmf.streamlit.app/)

> ⚠️ It might take a few seconds to load on the first visit.

---

## 🎯 Example usage

Select two teams and the system will output something like:

```
🎯 Probabilities for Flamengo vs Palmeiras
- 🏠 Home win: 58.4%
- ⚖️ Draw: 23.7%
- ✈️ Away win: 17.9%
```

---

## 🧪 Model details

- **Classifier:** `RandomForestClassifier`
- **Balancing:** `SMOTE` to fix draw over-representation
- **Input:** Historical features: team encodings, points, goal difference
- **Output:** Probabilities using `predict_proba()`
- **Evaluation:** Accuracy, confusion matrix, and classification report

---

## 🖼️ Interface highlights

The interface is visually styled with:
- A **real football field background**
- Light text and emojis for clarity and friendliness

---

## 📌 What's new in v1.1.0

- ✅ Added historically-informed match features (points and goal difference)
- ✅ Improved training logic with feature engineering
- ✅ Replaced placeholder input with real data-driven predictions
- ✅ Exported enriched dataset to CSV
- ✅ Updated web app to use enhanced model and features

---

## ✍️ Author

Created by Felipe Schaitel  
A beginner-friendly, football-inspired machine learning project.

---

## 📌 License

This project is licensed under the MIT License.
