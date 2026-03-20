# 🧬 AI Lab Risk Analyzer (GPU-Powered)

## 📸 Demo

### Upload Interface
![Upload](assets/upload.png)

### Results Dashboard
![Results](assets/results.png)

An AI-powered healthcare analytics app that analyzes lab data (Glucose, WBC) and predicts patient risk levels using a neural network.

## 🚀 Features
- CSV upload for batch lab analysis
- GPU acceleration (CUDA)
- Risk classification (Low / Moderate / High)
- Interactive visualization with Chart.js

## 🧠 Tech Stack
- FastAPI
- PyTorch (GPU)
- Pandas
- Chart.js

## 🔧 Run Locally

pip install -r requirements.txt
uvicorn main:app --reload
