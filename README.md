# 🧬 AI Lab Risk Analyzer v2 (GPU-Powered)

An AI-powered healthcare analytics web application that analyzes laboratory data (Glucose, WBC) and predicts patient risk levels using a neural network.

---

## 🚀 Demo

### Upload Interface
<img src="assets/upload.png" width="900">

---

### Results Dashboard
<img src="assets/results.png" width="900">

---

## 💡 Why This Matters

In healthcare, early risk detection can significantly improve patient outcomes.

This project demonstrates how machine learning can assist clinical decision-making by analyzing lab values and identifying potential risk patterns in real time.

---

## ⚡ Features

- 📁 CSV upload for batch lab analysis  
- 🤖 AI-powered risk prediction (Low / Moderate / High)  
- 📊 Interactive visualization with Chart.js  
- ⚡ GPU acceleration with PyTorch (CUDA support)  
- 🌐 FastAPI-based web interface  
- 🎯 Clean, responsive UI  

---

## 🔄 Version History

### 🚀 v2 (Current)
- Web-based UI using FastAPI  
- CSV upload + batch processing  
- Real-time predictions  
- Interactive charts (Chart.js)  
- GPU-ready model  

### 🧪 v1
- Basic neural network model  
- No web interface  
- Limited functionality  

---

## 🧠 Tech Stack

- **Backend:** FastAPI  
- **Machine Learning:** PyTorch  
- **Data Processing:** Pandas  
- **Visualization:** Chart.js  
- **Frontend:** HTML / CSS  

---

## 🏃 Run Locally

```bash
git clone https://github.com/medlabtech2013/ai-lab-risk-analyzer.git
cd ai-lab-risk-analyzer

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload

http://127.0.0.1:8000

## 📊 Example Input
Glucose,WBC
90,5.5
150,12
180,15
110,6
200,18

## 📈 Example Output

-Risk classification displayed in table

-Interactive chart showing Glucose & WBC trends

-Real-time predictions for each patient entry

## 🔮 Future Improvements (v3 Roadmap)

-🔗 HL7 / FHIR integration for real lab systems

-☁️ Cloud deployment (AWS / Docker)

-👤 User authentication & dashboard

-📊 Model training with real clinical datasets

-📉 Advanced analytics (trend detection, alerts)


##👨‍💻 Author

Branden Bryant
BSIT (Artificial Intelligence)
Medical Laboratory Technician → AI Engineer

🔗 GitHub: https://github.com/medlabtech2013

🔗 LinkedIn: https://www.linkedin.com/in/brandenbryant1

⭐️ Support

If you found this project useful, feel free to star the repo ⭐
