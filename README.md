# Health-Insurance-Cost-Prediction
This Project aims to predict the individual health insurance charges using demographic and lifestyle feature with a machine learning model. The best-performing model is deployed using Streamlit for interactive use.

# Project Objective

To build a regression model that accurately predicts medical insurance costs based on:
- Age
- Sex
- BMI
- Number of Children
- Smoker Status
- Region

# Tools & Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- GridSearchCV (Hyperparameter Tuning)

---
# Exploratory Data Analysis (EDA)

- Distribution plots of `age`, `bmi`, `charges`
- Correlation heatmap
- Encoding categorical features (sex, smoker, region)

---
# Model Building

Tested the following regressors:
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor (Best)

# Model Evaluation (After Hyperparameter Tuning)
| Metric     | Value     |
|------------|-----------|
| MSE        | 18,524,952.83 |
| RMSE       | 4,304.06 |
| R² Score   | 0.88      |

---

# Streamlit App Features

- Interactive input of features like age, BMI, etc.
- Backend model: Gradient Boosting Regressor
- Real-time cost prediction

