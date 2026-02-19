# 🚀 AppiaPalan API Documentation & Integration Guide

Welcome to the **AppiaPalan API**. This guide provides everything you need to connect your Mobile App or Website to our backend services, including user management, disease diagnosis, content management, and the new LLM (Large Language Model) integration.

## 📌 Base URL
- **Production**: `https://appiapalanbackebd.onrender.com/api/v1`
- **Development**: `http://localhost:8000/api/v1`

---

## 🔐 Authentication
The API uses **OAuth2 with Password Grant** and **JWT Tokens**.

### 1. Login (Get Token)
- **Endpoint**: `POST /auth/login/access-token`
- **Body (Form Data)**:
  - `username`: your-email
  - `password`: your-password
- **Response**:
  ```json
  {
    "access_token": "eyJhbG...",
    "token_type": "bearer"
  }
  ```
- **Usage**: Include this token in the header of all protected requests:
  `Authorization: Bearer <your_token>`

### 2. Register User
- **Endpoint**: `POST /auth/register`
- **Body (JSON)**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword",
    "full_name": "John Doe"
  }
  ```

---

## 🍃 Agriculture & Diagnosis
### 1. List Plants
- **Endpoint**: `GET /agri/plants`
- **Description**: Returns all supported plants (Tomato, Potato, etc.).

### 2. Predict Disease (AI Diagnosis)
- **Endpoint**: `POST /agri/predict`
- **Body (Multipart/Form-Data)**:
  - `file`: (The image file of the plant leaf)
- **Description**: Analyzes the image and returns the disease name, confidence score, and treatment advice.

---

## 🤖 LLM Management (New)
Manage multiple AI models and API keys directly from the backend.

### 1. List LLM Providers
- **Endpoint**: `GET /ai/` (Superuser only)
- **Description**: Returns all configured AI models (OpenAI, Gemini, etc.).

### 2. Create LLM Configuration
- **Endpoint**: `POST /ai/`
- **Body (JSON)**:
  ```json
  {
    "name": "My ChatGPT-4",
    "provider_type": "openai",
    "api_key": "sk-...",
    "model_id": "gpt-4"
  }
  ```

---

## 📦 Content Management (CMS)
Dynamic content for your app (Articles, Feature Flags, etc.).

### 1. Get Content by Type
- **Endpoint**: `GET /content/type/{type_key}`
- **Example**: `GET /content/type/monetization_settings`

---

## 💡 Integration Tips
### 1. Connecting Flutter/React
- Use a persistent HTTP client (like `dio` in Flutter or `axios` in React).
- Create a base service that automatically attaches the `Bearer` token from local storage.
- **Handling JSON Schemas**: The CMS endpoints return dynamic JSON. In your app, use a flexible Map or dynamic object to parse the `data` field.

### 2. Automatic Admin Credentials
- **Admin**: `admin`
- **Password**: `admin`
*(Created automatically via `seed_system.py` on deployment).*

---

## 🛠 Troubleshooting
- **Docs**: Access the interactive Swagger UI at `/docs` (e.g., `https://appiapalanbackebd.onrender.com/docs`).
- **Issues**: Contact `support@appiapalan.com`.
