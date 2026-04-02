# 🚌 Public Transport Delay Prediction Project

<p align="center">
  <img src="thumbline.png" alt="Public transport delay project thumbnail" width="760"/>
</p>

<p align="center">
  📊 Data Analysis + 🤖 Machine Learning + 📈 Power BI + 🌐 Streamlit
</p>

---

## ✨ What this project does

This project predicts **`DELAY_MINUTES`** (how many minutes a public transport trip is late).

It combines:
- 🧹 data cleaning (messy real-world transport data),
- 🧠 ML models (Linear Regression + Random Forest),
- 📊 dashboard reporting (Power BI),
- 🌐 interactive prediction app (Streamlit).

---

## 📋 Problem statement

### Background

Public transport systems often run late because of **weather**, **traffic congestion**, **rush hours**, **public events**, and differences between **routes**, **cities**, and **vehicle types**. Passengers cannot plan trips well when delay risk is unknown, and operators lose efficiency when delays are not understood or forecasted.

### What we need to solve

| Question | Why it matters |
|----------|----------------|
| **How many minutes** will a trip be delayed? | Helps riders and planners set realistic expectations. |
| **Which factors** push delay up the most? | Supports scheduling, staffing, and route planning. |
| **Can we trust messy real-world data?** | Raw feeds often have wrong symbols, mixed units, and bad categories — we must clean before modeling. |

### Project goal (formal)

Build an end-to-end pipeline that **analyzes** delay drivers and **predicts** the target:

- **Target variable:** `delay_minutes` (or `DELAY_MINUTES` in engineered data) — the number of minutes a trip is delayed.

### Project objectives

- 🧹 Clean **messy** transport data (symbols, units, categories).
- 📊 Explore relationships: weather, traffic, events, time vs delay (**EDA**).
- 🤖 Train **regression** models to predict delay time.
- 📈 Compare models and report **MAE**, **RMSE**, and **R²**.
- 🔍 Explain drivers of delay with **SHAP**.
- 📉 Turn insights into a **Power BI** dashboard and a **Streamlit** demo app.

### Dataset features (inputs used in the project)

Typical columns in the dataset include:

| Feature | Meaning |
|---------|---------|
| `trip_id` | Unique trip identifier |
| `city` | City / service area |
| `route_id` | Route or line |
| `hour` | Time of day |
| `rainfall_mm`, `temperature`, `humidity`, `wind_speed` | Weather |
| `rush_hour`, `traffic_level` | Congestion and peak time |
| `event_today`, `event_type` | Special events |
| `is_weekend` | Weekend vs weekday |
| `vehicle_type` | Mode of transport |
| **`delay_minutes`** | **Target** — minutes delayed |

Engineered features also include ideas such as **`rush_hour`**, **`heavy_rain`**, and **`is_weekend`** (see `feature_engineering/` and notebooks).

### Scope note

This project is focused on a **specific set of cities and routes** (as in the dashboard filters and `problem_statement/`). Results are **illustrative** for that scope, not a global claim for every city worldwide.

---

## 💡 Our solution (what we built)

We treat delay prediction as a **supervised regression** problem and deliver **data**, **models**, **reports**, and **an app** in one repo.

### Solution in one picture

```text
Messy CSV  →  ETL + preprocessing  →  feature engineering  →  EDA
                    ↓
            ML models (Linear + Random Forest) + metrics + SHAP
                    ↓
    Power BI dashboard + Streamlit app + SQL analytics + saved models (.pkl)
```

### How each part answers the problem

| Layer | What we deliver | How it helps |
|-------|-----------------|--------------|
| **ETL** (`ETL/`) | Extract, transform, load; messy → cleaned CSV | Reliable input for analysis and ML |
| **Preprocessing** (`perprocessing/`) | Imputation, scaling, encoding-ready pipelines | Models see consistent numeric/categorical inputs |
| **Feature engineering** (`feature_engineering/`) | `feature_engineering.csv` + richer signals | Better prediction than raw columns alone |
| **EDA** (`EDA/`) | Histograms, correlations, rainfall/traffic vs delay | Validates patterns before modeling |
| **Model** (`Model/`) | Pipelines, Linear Regression, Random Forest, MAE/RMSE/R², SHAP, `joblib` export | **Answers “how many minutes?”** and **“why?”** |
| **SQL** (`SQL/`) | Aggregations by city, traffic, rush hour, events, routes | Repeatable analytics for DB-backed workflows |
| **Power BI** (`power bi/`) | `public_transport_delay.pbix` | Executive-friendly KPIs and slices (see `Result pic/`) |
| **App** (`app/`) | Streamlit UI + model choice + quick charts | **Interactive** delay estimate for demos |

### Expected outcomes (what you get at the end)

- ✅ A **trained regression model** that outputs predicted delay minutes.
- ✅ **Evaluation metrics** and **SHAP**-based insight into important features.
- ✅ A **clean ETL path** from messy strings to modeling-ready tables.
- ✅ **Dashboard** and **app** screenshots documented under **`Result pic/`**.

---

## 🧭 Full project flow (step by step)

1. **Extract** raw/messy transport data  
2. **Transform** data (fix text, numbers, units, categories)  
3. **Load** cleaned data  
4. **Preprocess** for ML (imputation, scaling, encoding)  
5. **Feature engineer** better predictor columns  
6. **EDA** to understand patterns  
7. **Train models** and compare metrics  
8. **Explain model** with SHAP  
9. **Build dashboard** in Power BI  
10. **Deploy prediction app** using Streamlit

---

## 📁 Every folder and file explained clearly

### Root files

| File / Folder | Why it is in project |
|---|---|
| `README.md` | Main documentation file (this file). |
| `thumbline.png` | 🖼️ Main thumbnail/hero image for README and portfolio preview. |
| `feature_engineering.csv` | Final engineered dataset used by modeling/app visual parts. |
| `public_transport_delay_cleaned.csv` | Cleaned dataset copy available at project root. |
| `EDA/` | EDA notebook and charts to understand data behavior. |
| `ETL/` | Full ETL pipeline notebooks + raw and cleaned files. |
| `Model/` | Model training/evaluation notebook with metrics and SHAP. |
| `SQL/` | SQL analysis queries for city/traffic/rush-hour/event insights. |
| `app/` | Streamlit app code and app images/model files (if present). |
| `feature_engineering/` | Notebook/csv artifacts related to engineered features. |
| `perprocessing/` | Preprocessing notebook artifacts. |
| `power bi/` | `.pbix` dashboard file. |
| `problem_statement/` | project objective and base cleaned file copy. |
| `Result pic/` | 📸 all screenshots of outputs/results used in README. |

---

### `ETL/` (Extract → Transform → Load)

| File | Purpose |
|---|---|
| `ETL/Extract.ipynb` | Reads source raw data and initial checks. |
| `ETL/Transform.ipynb` | Cleans symbols/noise, fixes datatypes, standardizes values. |
| `ETL/Load.ipynb` | Saves cleaned output for analysis/modeling. |
| `ETL/public_transport_delay_messy_45000.csv` | Raw messy dataset (input). |
| `ETL/public_transport_delay_cleaned.csv` | Cleaned ETL output. |

---

### `Model/` (training notebook)

| File | Purpose |
|---|---|
| `Model/full_model_code.ipynb` | End-to-end ML: split, preprocess pipeline, train models, evaluate MAE/RMSE/R², SHAP, model export with `joblib`. |

Model types used:
- `LinearRegression`
- `RandomForestRegressor`

---

### `app/` (Streamlit app)

| File | Purpose |
|---|---|
| `app/delay_app.py` | Streamlit UI with tabs: Welcome, About, User Input, Visualization, Developer section. |

App behavior:
- user enters rainfall/temp/humidity/wind/city/weekend/vehicle info,
- app loads saved model,
- app predicts delay minutes,
- app shows quick charts.

---

### `SQL/`

| File | Purpose |
|---|---|
| `SQL/transport_delay_queries.sql` | SQL questions like avg delay by city, traffic level, rush hour, events, routes, etc. |

---

### `power bi/`

| File | Purpose |
|---|---|
| `power bi/public_transport_delay.pbix` | Main Power BI dashboard/report file. |

---

## 🛠️ Tools and technologies used

- 🐍 **Python**
- 🧮 **NumPy**
- 🐼 **Pandas**
- 🤖 **scikit-learn**
- 🔍 **SHAP**
- 📉 **Matplotlib**
- 🎨 **Seaborn**
- 🗄️ **MySQL (SQL analysis)**
- 📊 **Power BI**
- 🌐 **Streamlit**
- 💾 **joblib**

---

## 📸 Result pictures (from `Result pic/`)

These are project proof screenshots: dashboard, app, and model outputs.

### Main highlighted outputs

| Image | What it shows |
|---|---|
| ![Power BI Bus Dashboard](Result%20pic/Screenshot%202026-04-01%20215913.png) | Power BI KPI/dashboard page (delay by city, traffic, route, rainfall, rush hour). |
| ![Power BI Data View](Result%20pic/Screenshot%202026-04-01%20215935.png) | Table/schema view showing fields used for analysis. |
| ![Streamlit Welcome](Result%20pic/Screenshot%202026-04-01%20221023.png) | Streamlit app landing page with model selector. |
| ![Streamlit Prediction](Result%20pic/Screenshot%202026-04-01%20221109.png) | User input + prediction output screen. |
| ![Model Evaluation](Result%20pic/Screenshot%202026-04-01%20221309.png) | Actual vs predicted plot for Random Forest result. |

### All result files in this project

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

## 🖼️ How to add thumbnail and result images in README

### 1) Add thumbnail (`thumbline.png`)

```markdown
<p align="center">
  <img src="thumbline.png" alt="Project thumbnail" width="760"/>
</p>
```

### 2) Add any result image from `Result pic/`

Because folder name has space, use `%20` in path:

```markdown
![My Result](Result%20pic/Screenshot%202026-04-01%20215913.png)
```

### 3) If image is too big, use HTML size control

```markdown
<img src="Result%20pic/Screenshot%202026-04-01%20215913.png" alt="Result" width="800"/>
```

---

## ▶️ How to run project (clear)

### Step 1: Open project
- Open folder `Public_Transport_Delay` in VS Code/Cursor/Jupyter.

### Step 2: Install Python libraries
Run:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn shap joblib streamlit
```

### Step 3: Run notebooks in order
- Run `ETL/Extract.ipynb`
- Run `ETL/Transform.ipynb`
- Run `ETL/Load.ipynb`
- Run preprocessing/feature files in `perprocessing/` and `feature_engineering/`
- Run `EDA/eda.ipynb`
- Run `Model/full_model_code.ipynb`

This generates cleaned data and model artifacts.

### Step 4: Run Streamlit app

```bash
cd app
streamlit run delay_app.py
```

Then open the local URL shown in terminal.

### Step 5: Open Power BI dashboard
- Open `power bi/public_transport_delay.pbix` in Power BI Desktop.
- Click **Refresh** if data does not appear.

---

## ⚠️ Important note for running on another system

Some scripts currently use **absolute Windows paths** (example: `C:\Users\...`).  
If files do not load, change them to your local path or relative project paths.

---

## 👤 Author

**Induri Avinash Reddy**

- GitHub: [avinashreddy0](https://github.com/avinashreddy0)
- LinkedIn: [Avinash Reddy Induri](https://www.linkedin.com/in/avinash-reddy-induri-4662b832a/)

---

<p align="center">
  🚍 Thanks for visiting this project! 📚
</p>
