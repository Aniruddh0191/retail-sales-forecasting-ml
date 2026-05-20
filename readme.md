# 📊 Retail Sales Forecasting & Analytics ML Pipeline

A complete Machine Learning pipeline project for retail and warehouse sales analytics built using:

- **Python**
- **Pandas & NumPy**
- **Scikit-learn**
- **Joblib**
- **Feature Engineering Pipelines**
- **Power BI**

This project focuses on:

- Data preprocessing
- Feature engineering
- Sales forecasting
- ML model training
- Data pipeline automation
- Business analytics visualization

---

# 🚀 Project Overview

The project processes retail sales data, cleans and transforms it, engineers meaningful business features, and trains a machine learning model to predict total sales.

The repository also includes a Power BI dashboard for business analytics and reporting.

Main pipeline execution starts from:

- `main.py`

---

# 📂 Project Structure

```bash
project/
│
├── main.py
├── requirements.txt
├── config.py
├── data_preprocessing.py
├── feature_engineering.py
├── train_model.py
├── model.pkl
├── HR Analytics Dashboard.pbix
│
├── data/
│   ├── raw/
│   │   └── data.csv
│   │
│   └── processed/
│       └── cleaned_data.csv
│
└── models/
    └── model.pkl
```

---

# ⚙️ Core Workflow

The ML workflow is divided into 4 stages:

1. Load raw retail sales data
2. Clean and preprocess dataset
3. Engineer advanced business features
4. Train ML forecasting model

Pipeline execution:

```python
run_pipeline()
```

Defined in:

- `main.py`

---

# 🧹 Data Preprocessing

The preprocessing pipeline:

- Loads CSV data
- Standardizes column names
- Handles missing values
- Converts numeric columns
- Creates datetime features

Implemented inside:

- `data_preprocessing.py`

---

## Preprocessing Steps

### Column Standardization

```python
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
```

### Missing Value Handling

```python
df = df.fillna(0)
```

### Numeric Conversion

The following columns are converted into numeric format:

- retail_sales
- retail_transfers
- warehouse_sales

### Datetime Feature Creation

```python
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
```

---

# 🧠 Feature Engineering

Custom business features are generated for improving model performance.

Implemented in:

- `feature_engineering.py`

---

## Engineered Features

### Month Name

```python
df['month_name'] = df['date'].dt.month_name()
```

### Quarter Extraction

```python
df['quarter'] = df['date'].dt.quarter
```

### Seasonal Categorization

Seasons are classified as:

- Winter
- Spring
- Summer
- Fall

### Total Sales Feature

```python
df['total_sales'] = df['retail_sales'] + df['warehouse_sales']
```

This becomes the prediction target for the ML model.

---

# 🤖 Machine Learning Model

The project uses:

- `RandomForestRegressor`

Implemented inside:

- `train_model.py`

---

## Model Training Workflow

### Features Used

```python
X = df[['month', 'retail_transfers']]
```

### Target Variable

```python
y = df['total_sales']
```

### Train/Test Split

```python
train_test_split(test_size=0.2, random_state=42)
```

### Model Initialization

```python
RandomForestRegressor(random_state=42)
```

### Model Saving

```python
joblib.dump(model, MODEL_PATH)
```

The trained model is stored as:

```bash
models/model.pkl
```

---

# ⚙️ Configuration Management

All project paths are centrally managed through:

- `config.py`

---

## Configured Paths

```python
DATA_RAW
DATA_PROCESSED
MODEL_PATH
```

This helps maintain scalability and cleaner project structure.

---

# 📦 Requirements

Dependencies used:

```txt
pandas
numpy
scikit-learn
joblib
```

---

# ▶️ How to Run the Project

## 1. Clone Repository

```bash
git clone <repository-url>
cd project-folder
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Pipeline

```bash
python main.py
```

Pipeline automatically:

- Cleans data
- Saves processed dataset
- Trains model
- Saves trained model

---

# 📊 Dataset Information

The dataset appears to include:

- Retail sales
- Retail transfers
- Warehouse sales
- Monthly business data
- Yearly sales records

Files included:

- `data.csv`
- `cleaned_data.csv`

---

# 📈 Business Intelligence Dashboard

The project includes a Power BI dashboard:

- `HR Analytics Dashboard.pbix`

This can be used for:

- Executive reporting
- KPI visualization
- Sales trend analysis
- Business analytics dashboards

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Storage | Joblib |
| Visualization | Power BI |
| ML Algorithm | Random Forest Regressor |

---

# 🔮 Future Improvements

Potential enhancements:

- Add API deployment with FastAPI
- Add Streamlit dashboard
- Add hyperparameter tuning
- Add model evaluation metrics
- Add MLflow experiment tracking
- Add Docker support
- Add CI/CD pipelines
- Add automated retraining
- Add time-series forecasting models
- Deploy on cloud platforms

---

# 📌 Key Highlights

✅ End-to-end ML pipeline

✅ Automated preprocessing

✅ Feature engineering workflow

✅ Machine learning forecasting

✅ Centralized configuration management

✅ Power BI integration

✅ Modular project structure

---

# 👨‍💻 Author

Built as a Data Analytics & Machine Learning project focused on:

- Retail sales forecasting
- Business intelligence
- Automated ML pipelines
- Scalable project architecture

---

# 📜 License

This project is open-source and can be modified for educational, research, and production purposes.

