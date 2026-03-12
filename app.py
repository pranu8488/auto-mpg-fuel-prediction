from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# 1. Initialize the FastAPI application
app = FastAPI(
    title="Auto MPG AI Prediction Service",
    description="A REST API service operationalizing a Multiple Linear Regression model for AI Agents and n8n workflows.",
    version="1.0.0"
)

# 2. Define the Structured Data (JSON) format using Pydantic
# This demonstrates your "Strong understanding of structured data (JSON)"
class VehicleSpecs(BaseModel):
    weight: float
    horsepower: float

# 3. Root Endpoint (For health checks by n8n or AI Agents)
@app.get("/")
def home():
    return {
        "status": "Online",
        "message": "AI Prediction Tool is ready for n8n/Chatbot requests",
        "endpoints": ["/predict"]
    }

# 4. Prediction Endpoint (The "Logic Engine")
@app.post("/predict")
def predict_efficiency(specs: VehicleSpecs):
    """
    Receives JSON input, executes regression logic, and returns a prediction.
    This demonstrates 'Experience working with APIs and REST integrations'.
    """
    # These coefficients are derived from your MSBA Regression analysis
    intercept = 46.31
    weight_coeff = -0.0076
    horsepower_coeff = -0.045
    
    # Mathematical Model execution (The intelligence layer)
    prediction = intercept + (weight_coeff * specs.weight) + (horsepower_coeff * specs.horsepower)
    
    return {
        "predicted_mpg": round(prediction, 2),
        "input_summary": {
            "weight_lbs": specs.weight,
            "horsepower": specs.horsepower
        },
        "model_metadata": {
            "type": "Multiple Linear Regression",
            "source": "Wichita State University MSBA Technical Project"
        }
    }

# 5. Local Server Configuration
if __name__ == "__main__":
    # Runs the server locally for testing before deployment
    uvicorn.run(app, host="127.0.0.1", port=8000)
