🏠 California House Price Prediction — End-to-End ML Deployment
A complete machine learning project that predicts California house prices using the classic California Housing dataset. The project covers the full AI lifecycle: data analysis, model training, evaluation, and production deployment via both Streamlit and Flask REST API.
---
🚀 Live Demos
Deployment	Link
🎯 Streamlit App	cal-house-price1.streamlit.app
⚙️ Flask REST API	calhouseprice-production.up.railway.app
---
📌 Project Overview
	
Type	Regression
Dataset	California Housing (Scikit-learn built-in)
Best Model	XGBoost
Deployment	Streamlit Cloud + Flask API on Railway
---
🧠 Models Evaluated
Model	Notes
Linear Regression	Baseline
SVR	Support Vector Regression
Decision Tree	Simple tree-based model
Gradient Boosting	Ensemble boosting
XGBoost	✅ Best performer — selected for deployment
---
🗂️ Project Structure
```
cal_house_price/
│
├── streamlit_app.py       # Interactive prediction UI
├── Flask_app.py           # REST API for backend deployment
├── index.html             # Simple frontend to consume the API
├── xgb_model.pkl          # Trained XGBoost model
├── features.pkl           # Feature names for input validation
├── full_housing_data.csv  # Dataset
├── requirements.txt       # Dependencies
└── README.md
```
---
⚙️ Deployment Architecture
```
User Input
    │
    ▼
Streamlit App ──────────────────► Streamlit Cloud
    │
    ▼
Flask REST API  ─────────────────► Railway (Live)
    │
    ▼
index.html (Local Frontend) ────► Consumes Flask API
```
---
🔌 API Usage
Endpoint: `POST /predict`
Request Body:
```json
{
  "features": [8.3, 41, 6.9, 1.0, 322, 2.5, 37.88, -122.23]
}
```
Feature Order:
`MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude`
Example with curl:
```bash
curl -X POST https://calhouseprice-production.up.railway.app/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [8.3, 41, 6.9, 1.0, 322, 2.5, 37.88, -122.23]}'
```
---
🛠️ Run Locally
1. Clone the repo
```bash
git clone https://github.com/ayasaberw2024-lang/cal_house_price.git
cd cal_house_price
```
2. Create and activate environment
```bash
conda create -n cal_env python=3.10 -y
conda activate cal_env
pip install -r requirements.txt
```
3. Run Streamlit
```bash
streamlit run streamlit_app.py
```
4. Run Flask API
```bash
python Flask_app.py
```
---
🧰 Tech Stack
ML: Python, Scikit-learn, XGBoost
Deployment: Streamlit, Flask, Railway
Frontend: HTML, JavaScript
Tools: Pandas, NumPy, Matplotlib, Jupyter Notebook
---
👩‍💻 Author
Aya Saber Omran — Data Scientist & ML Engineer
![LinkedIn](www.linkedin.com/in/aya-saber-omran)
