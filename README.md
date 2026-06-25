# Chocolate_Demand_Analysis

# 🍫 Chocolate Demand Forecasting & Sales Analysis
An end-to-end data science and machine learning project that builds regression pipelines to predict chocolate box shipment demands and provides a premium-themed interactive deployment dashboard using **Streamlit**.
---
## 🚀 Live Interactive Dashboard
Experience the live application deployed with a custom artisan chocolate aesthetic:
👉 [Chocolate Demand Dashboard Live Link](https://chocolatesalesanalysis-s6zbs8rmjyx5uhytnfrymd.streamlit.app/)
---
## 📊 Project Workflow & Key Stages
### 1. Data Exploration & Preparation
* Processed a comprehensive international sales dataset tracking over 200,000 distinct orders.
* Standardized target values and handled complex formatting anomalies across categorical values.
### 2. Feature Engineering & Preprocessing Pipelines
* Built automated pipelines using `ColumnTransformer` to seamlessly handle feature sets.
* Categorical features (`Product`, `Country`, `Channel`, `Salesperson`) were processed using robust `OneHotEncoder` schemes with unseen-label guardrails.
* Numerical vectors were handled via statistical imputation approaches (`KNNImputer`).
### 3. Model Evaluation & Regression Tuning
Evaluated multiple robust ensemble structures and gradient boosting frameworks based on Mean Absolute Error (MAE) and $R^2$ scores:

| Model Structure | MAE | $R^2$ Score |
| :--- | :--- | :--- |
| **CatBoost Regressor** | **12.52** | **0.8371** |
| **LightGBM Regressor** | **12.14** | **0.8368** |
| **XGBoost Regressor** | **18.23** | **0.8132** |
| **Random Forest** | **12.38** | **0.0538** |
| **Decision Tree** | **14.79** | **0.0298** |

---
## ✨ Web App UI Features
* **Artisan Visual Theme:** Bypassed standard configurations to implement a smooth, deep cocoa and caramel theme layout using custom configuration maps (`.streamlit/config.toml`).
* **Dynamic Control Array:** Built multi-select filter controls allowing live queries across targeted geographical regions and supply methods.
* **Responsive Visualizations:** Integrated clean, high-contrast Seaborn aggregations tracking total shipments.
---
## 📁 Repository Map
```text
├── .streamlit/
│   └── config.toml      # Artisan chocolate theme parameter mappings
├── app.py               # Live dashboard core engine script
├── Chocolate_Sales.csv  # Main shipment transactions ledger (200k entries)
├── requirements.txt     # Locked production library environment variables
└── README.md            # Comprehensive documentation manual

Let's connect! Feel free to reach out for collaborations or inquiries:
Email: englandengland271@gmail.com
LinkedIn: [https://www.linkedin.com/in/mohammed-nafay-ali-16519138a?utm_source=share_via&utm_content=profile&utm_medium=member_android]
