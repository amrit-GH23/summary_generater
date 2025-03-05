### **📝 Text Summarization App**  
A web application that summarizes input text using the **Google Gemini API**. Built with **Django** for the backend and a clean HTML/CSS UI for the frontend.

---

## 🚀 **Features**
- Summarizes long text into a concise summary.
- Uses **Google Gemini API** for AI-powered text processing.

---

## 🛠 **Setup Instructions**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/amrit-GH23/summary_generater
cd text-summarizer
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
- Create a **`.env`** file in the root directory.
- Add your **Google API Key** inside:
  ```ini
  api_key="YOUR_GOOGLE_API_KEY"
  ```
  
---

## 🏗 **Run the Django Project**
```bash
python manage.py runserver
```
Visit: **`http://127.0.0.1:8000/`**

---

---

## 📝 **Usage**
1. Enter text in the input box.
2. Click **"Generate"** to get the AI-generated summary.
3. The summarized text appears on the right panel.

---

## 📜 **Tech Stack**
- **Backend:** Django, Google Gemini API  
- **Frontend:** HTML, CSS  
- **Environment Management:** `python-dotenv`  

---

## 📜 **License**
This project is **open-source** under the **MIT License**.

---
