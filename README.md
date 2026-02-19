# 🚀 AppiaPalan API Documentation | توثيق برمجية أبيا بالان

Welcome to the **AppiaPalan API**. This guide provided in both **English** and **Arabic** helps you connect your Mobile App or Website to our services.
أهلاً بك في **برمجية أبيا بالان**. هذا الدليل متوفر باللغتين **الإنجليزية** و**العربية** لمساعدتك في ربط تطبيق الجوال أو الموقع الإلكتروني بخدماتنا.

---

## 📌 Base URL | الرابط الأساسي
- **Production (الإنتاج)**: `https://appiapalanbackebd.onrender.com/api/v1`
- **Development (التطوير)**: `http://localhost:8000/api/v1`

---

## 🔐 Authentication | التوثيق والأمان
The API uses **OAuth2 with Password Grant**. | تستخدم البرمجية نظام **OAuth2** لتسجيل الدخول.

### 1. Login (Get Token) | تسجيل الدخول (الحصول على الرمز)
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

### 2. Register User | تسجيل مستخدم جديد
- **Endpoint**: `POST /users/register`
- **Body**: `email, password, full_name, phone_number, country`

### 3. Social & Phone Login | تسجيل الدخول الاجتماعي وعبر الهاتف
- **Google Login**: `POST /auth/login/google`
- **Phone Login**: `POST /auth/login/phone`

---

## 🍃 Agriculture & Diagnosis | الزراعة والتشخيص

### 1. Predict Disease (AI) | تشخيص الأمراض (ذكاء اصطناعي)
- **Endpoint**: `POST /agri/predict`
- **Description**: Basic classification of plant diseases.
- **الوصف**: تصنيف أساسي لأمراض النباتات.

### 2. High-Accuracy Analysis (LLM Vision) | التحليل الدقيق (الرؤية بالذكاء الاصطناعي)
- **Endpoint**: `POST /ai/analyze-image`
- **Description**: Deep, natural language analysis using GPT-4o or Gemini.
- **الوصف**: تحليل عميق ومفصل باستخدام لغة طبيعية عبر موديلات متطورة.

---

## 💳 Subscriptions & Payments | الاشتراكات والمدفوعات
Manage your monetization and payment gateways. | إدارة 수익 والاشتراكات وبوابات الدفع.

### 1. List Payment Gateways | عرض بوابات الدفع
- **Endpoint**: `GET /payments/gateways`
- **Description**: Returns active gateways (Stripe, PayPal, etc.)

### 2. Set Preferred Currency | تحديد العملة المفضلة
- **Endpoint**: `POST /payments/currency?currency=USD`

---

## 🤖 AI & LLM Management | إدارة الذكاء الاصطناعي
Manage your API keys and models. | إدارة مفاتيح الـ API والنماذج الخاصة بك.

### 1. Configure Provider | إعدا المزود
- **Endpoint**: `POST /ai/`
- **Fields**: `name, provider_type (openai/google), api_key, model_id`

---

## 👥 User Management | إدارة المستخدمين
For administrators only. | مخصص للمسؤولين فقط.

### 1. List & Update Users | عرض وتحديث المستخدمين
- **Endpoint**: `GET /users/` | `PUT /users/{id}`
- **Description**: Manage subscription tiers, countries, and roles.
- **الوصف**: إدارة فئات الاشتراك والدول والأدوار.

---

## 💡 Integration Tips | نصائح للربط البرمجي

1. **Headers**: Always include `Authorization: Bearer <token>`.
   **العناوين**: يجب دائماً تضمين رمز الدخول في العنوان.
2. **Swagger UI**: Access interactive docs at `/docs`.
   **واجهة Swagger**: الوصول للتوثيق التفاعلي عبر المسار `/docs`.

---

## 🛠 Support | الدعم الفني
Contact us at | تواصل معنا عبر: `support@appiapalan.com`
