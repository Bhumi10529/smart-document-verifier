# 🧠 Smart Document AI Verifier

Smart Document AI Verifier is a hackathon project that automatically analyzes uploaded documents and performs basic AI-style verification.  
The system allows users to upload documents and get a quick verification result with document type detection and a verification score.

The goal of this project is to demonstrate how AI-powered document verification systems can help automate document validation processes used in government services, recruitment systems, and digital identity platforms.

---

# 🚀 Project Overview

This system provides a simple pipeline:

Upload Document  
↓  
Store File on Server  
↓  
Analyze Document Information  
↓  
Detect Document Type  
↓  
Generate Verification Score  
↓  
Display Results in Web Interface  

The project is built using **Python Flask for backend** and **HTML/CSS/JavaScript for frontend**.

---

# 🧩 Features

### 📤 Document Upload
Users can upload documents through a simple web interface.

### 📂 File Storage
Uploaded files are stored in a backend uploads folder.

### 📄 Document Type Detection
The system detects document types such as:

- Aadhaar Card
- PAN Card
- Resume
- Unknown Document

### 🧠 AI-Style Verification Logic
The system generates a verification score based on extracted document information.

Example output:

Document Type: Resume  
Verification Status: Verified  
Verification Score: 92%

### 🌐 Frontend + Backend Integration
The frontend communicates with the backend using REST API.


---


# 🏗 Projecsmart-doc-ai
│
├── backend
│ ├── app.py
│ ├── requirements.txt
│ └── uploads
│
└── frontend
├── index.html
├── script.js
└── style.css 

---

# ⚙️ Technologies Used

## Backend
- Python
- Flask
- Flask-CORS

## Frontend
- HTML
- CSS
- JavaScript

## Tools
- VS Code
- Live Server
- REST API

---

# 🔌 API Endpoints

## Upload Document

**POST /upload**

Uploads a document to the server.

Example Response:

---
{
"document_type": "Resume",
"verification_status": "Verified",
"verification_score": 92
}

---

# ▶️ How to Run the Project

## 1️⃣ Clone or Download the Project

Open the project folder in VS Code.

---

## 2️⃣ Install Backend Dependencies

Go to the backend folder and run:

---

## 3️⃣ Start Backend Server

---

python app.py


Server will run at:

http://127.0.0.1:5000

---

## 4️⃣ Run Frontend

Open `frontend/index.html` using **Live Server** in VS Code.


---

# 🧪 How to Use

1. Open the web interface  
2. Upload a document  
3. Click **Upload / Analyze**  
4. View verification result  

The system will display:

- Document Type
- Verification Status
- Verification Score

---

# 📊 Example Output


---
Document Type: Resume
Verification Status: Verified
Verification Score: 92%


---

# 🔮 Future Improvements

To make the system more intelligent, the following features can be added:

- OCR based text extraction
- Aadhaar / PAN field detection
- Document fraud detection
- Image quality analysis
- Duplicate document detection
- Machine learning verification model
- Advanced dashboard UI

---

# 🏆 Hackathon Value

This project demonstrates how AI can automate document verification tasks that are usually manual and time-consuming.

Potential use cases:

- Government document verification
- Recruitment document validation
- Digital KYC systems
- University certificate verification

---

# 👨‍💻 Author

Developed as a hackathon prototype demonstrating AI-based document verification.

