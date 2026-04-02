# 🚌 Public Transport Delay — Analysis & Prediction

<p align="center">
  <img src="thumbline.png" alt="Public transport delay project thumbnail" width="760"/>
</p>

<p align="center">
  📊 Data Analysis + 🤖 Machine Learning + 📈 Power BI + 🌐 Streamlit
</p>

---

## 📌 Project overview

Public transport delays are influenced by **weather**, **traffic**, **rush hour**, and **events**.  
This project predicts the **delay time in minutes** and explains the key reasons behind delays.

- 🎯 **Target variable:** `delay_minutes` / `DELAY_MINUTES`
- 🧠 **Models:** Linear Regression, Random Forest Regression
- 📊 **Dashboard:** Power BI (`power bi/public_transport_delay.pbix`)
- 🌐 **App:** Streamlit (`app/delay_app.py`)

---

## 🧭 Table of contents

- [🧩 Problem statement](#-problem-statement)
- [💡 Our solution](#-our-solution)
- [✅ What we did (work done)](#-what-we-did-work-done)
- [🛠️ Tools & tech used](#️-tools--tech-used)
- [🗂️ Folder structure (tree)](#️-folder-structure-tree)
- [⚡ Quick start (run this project)](#-quick-start-run-this-project)
- [📁 Repository structure (every file explained)](#-repository-structure-every-file-explained)
- [🖼️ Results (images shown from-result-pic)](#️-results-images-shown-from-result-pic)
- [🖼️ How to show images in README (important)](#️-how-to-show-images-in-readme-important)
- [👤 Author](#-author)

---

## 🧩 Problem statement

Public transport systems often experience delays due to:
- 🌧️ weather (rainfall, temperature, humidity, wind)
- 🚦 traffic congestion
- 🕒 peak hours / rush hour
- 🎉 public events
- 🚌 route and vehicle type

These delays affect passenger planning and reduce system efficiency.  
So we need a system that can:
- ✅ predict **how many minutes** a trip will be delayed
- ✅ identify **which factors** are most responsible for delays

---

## 💡 Our solution

We built an end-to-end pipeline:

```text
Raw messy dataset → ETL cleaning → preprocessing + feature engineering → EDA
                                  ↓
                   ML training + evaluation (MAE/RMSE/R²) + SHAP
                                  ↓
         Power BI dashboard + Streamlit prediction app + SQL analytics
```

---

## ✅ What we did (work done)

- 🧹 **ETL pipeline**: extracted raw data, cleaned messy values, and saved a clean dataset (`ETL/` + `public_transport_delay_cleaned.csv`).
- 🧼 **Preprocessing**: prepared data for ML (missing values, scaling, encoding) (`perprocessing/` + pipelines in `Model/`).
- 🧠 **Feature engineering**: created model-friendly features and exported `feature_engineering.csv`.
- 📊 **EDA**: explored distributions, correlations, outliers, and relationships like rainfall vs delay (`EDA/eda.ipynb`).
- 🤖 **Model training**: trained regression models (Linear Regression, Random Forest) and compared performance.
- 📏 **Evaluation**: used **MAE**, **RMSE**, and **R²** to measure accuracy.
- 🔍 **Explainability**: used **SHAP** to understand the most important delay drivers (`model_explainability/SHAP.ipynb`).
- ✅ **Cross validation**: experimented with cross-validation (`cross_validation/`).
- 🎛️ **Hyperparameter tuning**: experimented with tuning (`hyperparameter tuning/`).
- 🗄️ **SQL analysis**: wrote queries for avg delay by city/traffic/rush hour/events/routes (`SQL/transport_delay_queries.sql`).
- 📈 **Power BI dashboard**: built an interactive report (`power bi/public_transport_delay.pbix`).
- 🌐 **Streamlit app**: created an app to input trip conditions and predict delay (`app/delay_app.py`).
- 📸 **Results screenshots**: saved proof images in `Result pic/` and embedded them in this README.

---

## 🛠️ Tools & tech used

### Python (data + ML)

- 🐍 Python
- 🐼 pandas, 🧮 numpy
- 🤖 scikit-learn (pipelines, preprocessing, regression models, metrics)
- 📉 matplotlib, 🎨 seaborn
- 🔍 SHAP (model explainability)
- 💾 joblib (saving/loading models)
- 🌐 Streamlit (web app)

### Database (SQL)

- 🗄️ **MySQL Server + MySQL Workbench** (installed separately; not via `pip`)
- 🧩 **SQLAlchemy + PyMySQL** (Python connectors used in `ETL/Load.ipynb`)

### BI / Reporting

- 📊 **Power BI Desktop** (installed separately; not via `pip`)

---

## 🗂️ Folder structure (tree)

```text
Public_Transport_Delay/
├── README.md
├── requirements.txt
├── .gitignore
├── thumbline.png
├── public_transport_delay_cleaned.csv
├── feature_engineering.csv
│
├── problem_statement/
│   ├── .txt
│   └── public_transport_delay_cleaned.csv
│
├── ETL/
│   ├── Extract.ipynb
│   ├── Transform.ipynb
│   ├── Load.ipynb
│   ├── public_transport_delay_messy_45000.csv
│   ├── public_transport_delay_cleaned.csv
│   └── public_transport_delay_cleaned.xlsx
│
├── EDA/
│   └── eda.ipynb
│
├── perprocessing/
│   └── .ipynb
│
├── feature_engineering/
│   ├── .ipynb
│   └── feature_engineering.csv
│
├── Model/
│   ├── full_model_code.ipynb
│   └── linear_model.pkl
│
├── model_pipelines/
│   └── pipelines.ipynb
│
├── model_explainability/
│   └── SHAP.ipynb
│
├── cross_validation/
│   └── .ipynb
│
├── hyperparameter tuning/
│   └── .ipynb
│
├── SQL/
│   └── transport_delay_queries.sql
│
├── power bi/
│   └── public_transport_delay.pbix
│
├── app/
│   ├── delay_app.py
│   ├── linear_model.pkl
│   ├── Gemini_Generated_Image_joezrjjoezrjjoez.png
│   └── Gemini_Generated_Image_9i4rke9i4rke9i4r.png
│
└── Result pic/
    ├── Screenshot 2026-04-01 215913.png
    ├── Screenshot 2026-04-01 215935.png
    └── ... more screenshots ...
```

---

## ⚡ Quick start (run this project)

### 1) Install Python requirements 📦

```bash
pip install -r requirements.txt
```

### 2) Run notebooks (recommended order) 📒

- `ETL/Extract.ipynb`
- `ETL/Transform.ipynb`
- `ETL/Load.ipynb` (loads into **MySQL Workbench** using `SQLAlchemy` + `PyMySQL`)
- `perprocessing/.ipynb`
- `feature_engineering/.ipynb`
- `EDA/eda.ipynb`
- `Model/full_model_code.ipynb`

✅ After this, you will have:
- cleaned dataset (`public_transport_delay_cleaned.csv`)
- engineered dataset (`feature_engineering.csv`)
- saved model(s) (`linear_model.pkl`, and optionally Random Forest if exported)

### 3) Run the Streamlit app 🌐

```bash
cd app
streamlit run delay_app.py
```

⚠️ **Important:** `app/delay_app.py` expects **two model files**:
- `app/linear_model.pkl` ✅ (present)
- `app/random_forest_model.pkl` ❌ (currently missing in repo)

To fix: export/save the Random Forest model from your notebook and place it as `app/random_forest_model.pkl` (or update the app code to match your filename).

### 4) Open the Power BI dashboard 📈

- Open `power bi/public_transport_delay.pbix` in **Power BI Desktop**
- Refresh the dataset if required

### 5) Run SQL queries in MySQL Workbench 🗄️

- Open `SQL/transport_delay_queries.sql`
- Make sure your database/table names match your environment (the file uses `transport`)
- Run queries to reproduce dashboard-style insights (avg delay by city, traffic, rush hour, events, routes)

---

## 📁 Repository structure (every file explained)

### Root files

| Path | What it is | Why it exists |
|---|---|---|
| `README.md` | Documentation | Explains project, structure, and results. |
| `requirements.txt` | Python deps | Install packages for notebooks + Streamlit. |
| `.gitignore` | Git ignore rules | Ignores `*.pkl` (model files) by default. |
| `thumbline.png` | Thumbnail image | Displayed at top of README. |
| `public_transport_delay_cleaned.csv` | Clean dataset | Cleaned output copy at root. |
| `feature_engineering.csv` | Engineered dataset | Used for modeling and app charts. |

### `problem_statement/`

| Path | What it is | Why it exists |
|---|---|---|
| `problem_statement/.txt` | Full problem statement | Objectives, features, workflow description. |
| `problem_statement/public_transport_delay_cleaned.csv` | Clean dataset copy | Reference dataset for statement section. |

### `ETL/` (Extract → Transform → Load) 🧹

| Path | What it is | Why it exists |
|---|---|---|
| `ETL/Extract.ipynb` | Extract notebook | Reads raw file and prepares for cleaning. |
| `ETL/Transform.ipynb` | Transform notebook | Cleans messy values, fixes types, standardizes categories. |
| `ETL/Load.ipynb` | Load notebook | Loads cleaned data to MySQL using `SQLAlchemy` + `PyMySQL`. |
| `ETL/public_transport_delay_messy_45000.csv` | Raw messy dataset | Input (contains symbols / mixed formats). |
| `ETL/public_transport_delay_cleaned.csv` | Cleaned CSV | Output after transformation. |
| `ETL/public_transport_delay_cleaned.xlsx` | Cleaned Excel | Alternate output format. |

### `EDA/` 📊

| Path | What it is | Why it exists |
|---|---|---|
| `EDA/eda.ipynb` | EDA notebook | Visual analysis: patterns, distributions, correlations, outliers. |

### `perprocessing/` 🔧

| Path | What it is | Why it exists |
|---|---|---|
| `perprocessing/.ipynb` | Preprocessing notebook | Imputation/encoding/scaling experiments (file name is `.ipynb`). |

### `feature_engineering/` 🧠

| Path | What it is | Why it exists |
|---|---|---|
| `feature_engineering/.ipynb` | Feature notebook | Creates new features for prediction. |
| `feature_engineering/feature_engineering.csv` | Engineered dataset | Local copy used for modeling/visuals. |

### `Model/` 🤖

| Path | What it is | Why it exists |
|---|---|---|
| `Model/full_model_code.ipynb` | Full ML notebook | Pipelines, training, evaluation, SHAP, model saving. |
| `Model/linear_model.pkl` | Saved model | Linear Regression model exported by notebook. |

### `model_pipelines/` 🧩

| Path | What it is | Why it exists |
|---|---|---|
| `model_pipelines/pipelines.ipynb` | Pipeline notebook | Focused notebook for preprocessing + model pipelines. |

### `model_explainability/` 🔍

| Path | What it is | Why it exists |
|---|---|---|
| `model_explainability/SHAP.ipynb` | SHAP notebook | Explainability: which features drive delays. |

### `cross_validation/` ✅

| Path | What it is | Why it exists |
|---|---|---|
| `cross_validation/.ipynb` | CV notebook | Cross-validation experiments (file name is `.ipynb`). |

### `hyperparameter tuning/` 🎛️

| Path | What it is | Why it exists |
|---|---|---|
| `hyperparameter tuning/.ipynb` | Tuning notebook | Hyperparameter tuning experiments (file name is `.ipynb`). |

### `SQL/` 🗄️

| Path | What it is | Why it exists |
|---|---|---|
| `SQL/transport_delay_queries.sql` | SQL queries | Average delay by city/traffic/rush hour, events, routes, etc. |

### `power bi/` 📈

| Path | What it is | Why it exists |
|---|---|---|
| `power bi/public_transport_delay.pbix` | Power BI report | Interactive dashboard for KPIs and insights. |

### `app/` 🌐

| Path | What it is | Why it exists |
|---|---|---|
| `app/delay_app.py` | Streamlit app | UI for model selection + prediction + charts. |
| `app/linear_model.pkl` | Model file | Used by Streamlit for Linear Regression predictions. |
| `app/Gemini_Generated_Image_joezrjjoezrjjoez.png` | App image | Welcome page image. |
| `app/Gemini_Generated_Image_9i4rke9i4rke9i4r.png` | App image | Image shown after prediction. |

---

## 🖼️ Results (images shown from `Result pic/`)

### ⭐ Main highlights

| Preview | Description |
|---|---|
| ![Power BI dashboard](Result%20pic/Screenshot%202026-04-01%20215913.png) | **Power BI dashboard:** KPIs, delay by city, traffic, route, rainfall, rush hour. |
| ![Power BI data view](Result%20pic/Screenshot%202026-04-01%20215935.png) | **Power BI data view:** dataset fields and table view. |
| ![Streamlit welcome](Result%20pic/Screenshot%202026-04-01%20221023.png) | **Streamlit welcome page** with model selector. |
| ![Streamlit prediction](Result%20pic/Screenshot%202026-04-01%20221109.png) | **Streamlit prediction** page with input-to-model preview and output. |
| ![Model evaluation](Result%20pic/Screenshot%202026-04-01%20221309.png) | **Random Forest evaluation** (actual vs prediction plot). |

### 🗂️ All result screenshots

- `Result pic/Screenshot 2026-04-01 215913.png`
- `Result pic/Screenshot 2026-04-01 215935.png`
- `Result pic/Screenshot 2026-04-01 215948.png`
- `Result pic/Screenshot 2026-04-01 220118.png`
- `Result pic/Screenshot 2026-04-01 220158.png`
- `Result pic/Screenshot 2026-04-01 220210.png`
- `Result pic/Screenshot 2026-04-01 220236.png`
- `Result pic/Screenshot 2026-04-01 220243.png`
- `Result pic/Screenshot 2026-04-01 221023.png`
- `Result pic/Screenshot 2026-04-01 221109.png`
- `Result pic/Screenshot 2026-04-01 221128.png`
- `Result pic/Screenshot 2026-04-01 221158.png`
- `Result pic/Screenshot 2026-04-01 221212.png`
- `Result pic/Screenshot 2026-04-01 221224.png`
- `Result pic/Screenshot 2026-04-01 221243.png`
- `Result pic/Screenshot 2026-04-01 221309.png`
- `Result pic/Screenshot 2026-04-01 221339.png`

---

## 🖼️ How to show images in README (important)

Because folder name has a space (**`Result pic`**), use `%20` in markdown paths:

```markdown
![Dashboard](Result%20pic/Screenshot%202026-04-01%20215913.png)
```

---

## 👤 Author

**Induri Avinash Reddy**

- GitHub: [avinashreddy0](https://github.com/avinashreddy0)
- LinkedIn: [Avinash Reddy Induri](https://www.linkedin.com/in/avinash-reddy-induri-4662b832a/)

---

<p align="center">
  🚌 📊 🤖 — <em>Thanks for reading.</em>
</p>
