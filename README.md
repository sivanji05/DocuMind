# 🧠 DocuMind — Intelligent Document Query Platform

DocuMind is a secure, scalable, full-stack application that enables users to upload, parse, and query documents (PDF, PPT, CSV, etc.) using advanced NLP techniques with a RAG (Retrieval-Augmented Generation) Agent.

---

## 🧰 Tech Stack

| Layer      | Technology                                                |
|------------|-----------------------------------------------------------|
| Frontend   | React.js, TailwindCSS                                     |
| Backend    | FastAPI, LangChain, Autogen/CrewAI                        |
| Database   | PostgreSQL                                                |
| Storage    | AWS S3                                                    |
| Search     | Elasticsearch                                             |
| Parsing    | [unstructured.io](https://unstructured.io)               |
| Auth       | JWT / Session-Based                            |
| Deployment | Docker                                      |

---

## 📁 Project Structure

<pre>
documind-fullstack/
│
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── api/            # API route handlers
│   │   ├── models/         # SQLAlchemy models
│   │   ├── services/       # S3, ES, Auth, RAG Agent, Parsing
│   │   ├── utils/          # Helpers and configs
│   │   └── main.py         # Entry point
│   └── requirements.txt
│
├── frontend/               # React.js frontend
│   ├── src/
│   ├── public/
│   └── package.json
│
├── docker-compose.yml                   
└── README.md
</pre>

---

## 📌 Functional Highlights

### 📄 Document Upload and Management
- Users can upload documents (PDF, CSV, PPT, etc.).
- Files stored on AWS S3.
- Metadata stored in PostgreSQL.
- Parsing powered by `unstructured.io`.

### 🤖 Advanced NLP with RAG Agent
- Contextual Q&A based on uploaded documents.
- Powered by LangChain.
- Indexed with Elasticsearch and chunked intelligently.

### 🔐 Authentication
- Implemented using JWT or session-based mechanisms.
- Secure routes and user sessions.

---

## 🚀 Deployment

### 🐳 Docker
Run both frontend and backend with:

docker-compose up --build



---

## 📎 Setup Instructions

### 📥 Clone the Repository

git clone https://github.com/your-repo/documind-fullstack.git
- cd documind-fullstack



## ⚙️ Setup Backend

- cd backend
- pip install -r requirements.txt
- uvicorn app.main:app --reload


## 💻 Setup Frontend
- cd frontend
- npm install
- npm start

## Project BY
Nooli Sovanji
