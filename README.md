📄 DocuMind — Intelligent Document Query Platform
DocuMind is a secure, scalable, full-stack application that enables users to upload, parse, and query documents (PDF, PPT, CSV, etc.) using advanced NLP techniques with a RAG (Retrieval-Augmented Generation) Agent.


🚀 Features :
🧠 Query documents using advanced RAG Agents (Autogen / CrewAI)

🗃️ Upload & manage documents of any format (PDF, PPT, CSV, DOCX, etc.)

🧾 Powerful parsing with unstructured.io

🔎 Semantic search with vector embeddings (Elasticsearch)
🧩 Modular backend built with FastAPI and LangChain
🧑‍💼 JWT-based user authentication and session management
☁️ Cloud storage with AWS S3
🖼️ Clean and user-friendly UI with React.js
🐳 Dockerized for easy deployment


🏗️ Tech Stack:
Layer                	Technology
----------            ----------
Frontend	            React.js, TailwindCSS
Backend	              FastAPI, LangChain, Autogen/CrewAI
Database	            PostgreSQL, Redis
Storage	              AWS S3
Search	              Elasticsearch
Parsing	              unstructured.io
Auth	                JWT (or session-based alternatives)
Deployment	          Docker, Kubernetes



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



📌 Functional Highlights
✅ Document Upload and Management
-Users can upload documents (PDF, CSV, PPT, etc.)
-Files stored on AWS S3
-Metadata stored in PostgreSQL
-Parsing via unstructured.io to extract and chunk content
-Embedding each chunk using LangChain/OpenAI
-Chunks indexed in Elasticsearch for semantic retrieval


🧠 RAG-based Question Answering:]

-User inputs a question
-Query embedding generated via LangChain
-Relevant chunks retrieved from Elasticsearch
-RAG Agent (e.g., CrewAI) generates response from retrieved data

🛡️ Authentication & Authorization:

-Secure JWT-based authentication
-Login / Register functionality
-Protected routes (upload, ask, etc.)



🧪 Setup Instructions:

⚙️ Backend:
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt

# Set environment variables in .env
uvicorn app.main:app --reload

💻 Frontend:
cd frontend
npm install
npm run dev

🐳 Dockerized Setup:
# At project root
docker-compose up --build



Includes:

- FastAPI backend

- React frontend

🧑‍💻 Author
Built by Nooli Sivanji


- PostgreSQL

- Elasticsearch


