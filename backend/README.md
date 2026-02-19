# AppiaPalan: AI-Powered Plant Disease Detection System

A comprehensive ecosystem for farmers and agronomists to identify, manage, and treat crop diseases.

## 🏗️ Project Structure
- `/backend`: FastAPI core service (Postgres, JWT, RBAC).
- `/ai_service`: Standalone Fast API service for AI inference (EfficientNet-B0).
- `/dashboard`: Next.js web portal for agronomists and admins.
- `/mobile_app`: Flutter application for farmers with camera/AI integration.

## 🚀 Getting Started

### 1. AI Inference Service
Manages the Computer Vision logic.
```bash
cd ai_service
pip install -r requirements.txt
python main.py # Runs on http://localhost:8001
```

### 2. Backend API
The central brain of the system.
```bash
cd backend
py -m pip install -r requirements.txt
# Ensure Postgres is running (Port 5432)
py -m uvicorn app.main:app --reload
```

**Seed initial data & Create Admin:**
```bash
py seed_agri.py
```
- **Default Admin**: `admin@appiapalan.com`
- **Default Password**: `adminpassword123`

### 3. Admin Dashboard
Web interface for content and disease management.
```bash
cd dashboard
npm install
npm run dev
```

### 4. Mobile App
Farmer-facing interface.
```bash
cd mobile_app
flutter pub get
flutter run
```

## 🧠 AI Pipeline
1. **Camera Capture**: Farmer takes a high-res photo of a leaf.
2. **Preprocessing**: App resizes and center-crops the image to 224x224.
3. **Inference**: Image sent to AI service -> Model predicts disease class.
4. **Knowledge Retrieval**: Backend fetches symptoms and treatment (Organic/Chemical).
5. **Farmer Advice**: Simple, localized instructions displayed to the user.

## 💰 Monetization
- **Free**: 3 scans/day.
- **Premium**: Unlimited scans, expert chat, heatmaps.

---
*Created by Antigravity (Advanced Agentic Coding)*
