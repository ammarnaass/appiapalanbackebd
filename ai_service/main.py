from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import time
import random

app = FastAPI(title="AppiaPalan AI Inference Service")

# Supported classes (Mapping to PlantVillage labels)
DISEASE_CLASSES = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust", "Apple___healthy",
    "Blueberry___healthy", "Cherry___Powdery_mildew", "Cherry___healthy",
    "Corn___Cercospora_leaf_spot Gray_leaf_spot", "Corn___Common_rust", 
    "Corn___Northern_Leaf_Blight", "Corn___healthy",
    "Grape___Black_rot", "Grape___Esca_(Black_Measles)", "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
    "Peach___Bacterial_spot", "Peach___healthy", "Pepper,_bell___Bacterial_spot", "Pepper,_bell___healthy",
    "Potato___Early_blight", "Potato___Late_blight", "Potato___healthy", "Raspberry___healthy",
    "Soybean___healthy", "Squash___Powdery_mildew", "Strawberry___Leaf_scorch", "Strawberry___healthy",
    "Tomato___Bacterial_spot", "Tomato___Early_blight", "Tomato___Late_blight", "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot", "Tomato___Spider_mites Two-spotted_spider_mite", 
    "Tomato___Target_Spot", "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

@app.post("/v1/predict")
async def predict(file: UploadFile = File(...)):
    # In a real implementation:
    # 1. Read file bytes
    # 2. Preprocess image (Resize to 224x224, Normalize)
    # 3. Load TFLite/PyTorch model
    # 4. Run inference
    
    # Simulating heavy computation
    time.sleep(0.5) 
    
    # Mock result
    predicted_class = random.choice(DISEASE_CLASSES)
    confidence = random.uniform(0.85, 0.99)
    
    return {
        "status": "success",
        "prediction": predicted_class,
        "confidence": confidence,
        "inference_time_ms": 500
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
