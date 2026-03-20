from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import torch
import torch.nn as nn
import pandas as pd
from io import StringIO

app = FastAPI()

# Device (GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Templates
templates = Jinja2Templates(directory="templates")

# Model
model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid()
).to(device)


# ---------------------------
# Prediction Function
# ---------------------------
def predict(glucose, wbc):
    input_tensor = torch.tensor([[glucose, wbc]], dtype=torch.float32).to(device)
    prediction = model(input_tensor).item()

    if prediction > 0.7:
        explanation = "High risk detected: Elevated glucose and WBC suggest possible infection or metabolic issue."
    elif prediction > 0.4:
        explanation = "Moderate risk: Some lab values are outside normal range."
    else:
        explanation = "Low risk: Lab values appear within normal range."

    return prediction, explanation


# ---------------------------
# API Endpoint
# ---------------------------
@app.get("/analyze")
def analyze(glucose: float, wbc: float):
    score, explanation = predict(glucose, wbc)
    return {
        "risk_score": score,
        "explanation": explanation
    }


# ---------------------------
# Upload + UI Endpoint
# ---------------------------
@app.post("/upload-ui", response_class=HTMLResponse)
async def upload_ui(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode()))

    table_rows = ""
    glucose_values = []
    wbc_values = []

    for _, row in df.iterrows():
        glucose = float(row["Glucose"])
        wbc = float(row["WBC"])

        glucose_values.append(glucose)
        wbc_values.append(wbc)

        input_tensor = torch.tensor([[glucose, wbc]], dtype=torch.float32).to(device)
        prediction = model(input_tensor).item()

        if prediction > 0.7:
            status = "High Risk"
            color = "red"
        elif prediction > 0.4:
            status = "Moderate Risk"
            color = "orange"
        else:
            status = "Low Risk"
            color = "lightgreen"

        table_rows += f"""
        <tr>
            <td>{glucose}</td>
            <td>{wbc}</td>
            <td style="color:{color}; font-weight:bold;">
                {status} ({prediction:.2f})
            </td>
        </tr>
        """

    # Convert Python lists → JS
    glucose_js = str(glucose_values)
    wbc_js = str(wbc_values)
    labels_js = str(list(range(len(glucose_values))))

    return f"""
    <html>
    <head>
    <style>
        body {{
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
            padding: 40px;
        }}

        table {{
            margin: auto;
            border-collapse: collapse;
            width: 70%;
        }}

        th, td {{
            padding: 12px;
            border-bottom: 1px solid #334155;
        }}

        th {{
            color: #38bdf8;
        }}
    </style>
    </head>

    <body>

    <h1>🧬 AI Lab Analysis Results</h1>

    <canvas id="labChart" width="400" height="200"></canvas>

    <table>
    <tr>
        <th>Glucose</th>
        <th>WBC</th>
        <th>Risk Level</th>
    </tr>

    {table_rows}

    </table>

    <br><br>
    <a href="/" style="color:#38bdf8;">⬅ Back</a>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
    const ctx = document.getElementById('labChart');

    new Chart(ctx, {{
        type: 'line',
        data: {{
            labels: {labels_js},
            datasets: [
                {{
                    label: 'Glucose',
                    data: {glucose_js},
                    borderColor: '#38bdf8',
                    fill: false
                }},
                {{
                    label: 'WBC',
                    data: {wbc_js},
                    borderColor: '#f97316',
                    fill: false
                }}
            ]
        }},
        options: {{
            plugins: {{
                legend: {{
                    labels: {{
                        color: 'white'
                    }}
                }}
            }},
            scales: {{
                x: {{
                    ticks: {{ color: 'white' }}
                }},
                y: {{
                    ticks: {{ color: 'white' }}
                }}
            }}
        }}
    }});
    </script>

    </body>
    </html>
    """


# ---------------------------
# Home Page
# ---------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
