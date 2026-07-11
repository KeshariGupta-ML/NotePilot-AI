# 🚀 NotePilot AI

### An Agent-Based Generative AI Learning Assistant that transforms course transcripts into intelligent notes, summaries, quizzes, and downloadable PDFs.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Web_Framework-green)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent_Workflow-purple)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

# 📌 Overview

**NotePilot AI** is an authentication-based Generative AI application that helps students and professionals convert course lectures into structured learning material.

The application accepts lecture transcripts from videos or educational content and uses multiple AI agents powered by Google Gemini to:

* Understand lecture content
* Generate structured notes
* Create summaries
* Prepare quizzes
* Export professional PDF study material

Unlike traditional note-taking applications, NotePilot AI does not permanently store user lecture content. The lecture data is processed only during the active user session, and users can export the generated notes as PDF whenever required.

---

# 🎯 Problem Statement

Learning from long technical lectures is time-consuming because users need to:

* Watch hours of video content
* Manually prepare notes
* Extract important concepts
* Create revision material

NotePilot AI automates this workflow using Agentic AI.

---

# ✨ Features

## 🔐 Secure User Authentication

* User registration
* Login/logout
* JWT-based authentication
* Protected application dashboard
* Secure password hashing

---

## 🎥 Lecture Transcript Processing Agent

Processes uploaded lecture content:

* Text cleaning
* Content understanding
* Topic identification
* Chapter segmentation

---

## 🧠 AI Notes Generation Agent

Creates structured learning notes:

* Topic explanation
* Key concepts
* Important definitions
* Examples
* Practical applications
* Interview preparation points

---

## 📝 Quiz Generation Agent

Generates:

* Multiple choice questions
* Concept evaluation questions
* Answers with explanations
* Self-learning assessments

---

## 📄 PDF Export Agent

Users can save generated content as:

* Professional study notes
* Course summaries
* Revision documents

PDF generation happens only when requested by the user.

---

# 🏗️ System Architecture

```
                         User
                          |
                          |
                   Authentication
                          |
                          |
                    FastAPI Backend
                          |
        ---------------------------------
        |                               |
 User Database                  Session Manager
        |                               |
        |                               |
 User Profile                 Current Lecture Data
                                    |
                                    |
                            Agent Workflow
                                    |
        ------------------------------------------------
        |                  |                 |
 Transcript Agent    Notes Agent      Quiz Agent
        |                  |                 |
        ------------------------------------------------
                          |
                          |
                    Gemini API
                          |
                          |
                    PDF Generator
                          |
                          |
                  User Downloads PDF

```

---

# 🤖 Agent Workflow

```
START

 |
 |
Transcript Agent

 |
 |
Summary Agent

 |
 |
Notes Generation Agent

 |
 |
Quiz Generation Agent

 |
 |
PDF Export Agent

 |
 |
END
```

Each AI agent performs a dedicated task, creating a modular and scalable Agentic AI architecture.

---

# 🔐 Privacy-First Data Design

NotePilot AI follows a privacy-focused architecture.

### Stored Permanently:

✅ User account information only

### Temporary Session Data:

* Uploaded transcript
* Generated summary
* Generated notes
* Generated quizzes

### Not Stored:

❌ Lecture transcripts
❌ Generated notes history
❌ Course content database

Session data is removed after logout or session expiration.

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

## Authentication

* JWT Authentication
* OAuth2 Password Flow
* Passlib / bcrypt

## Frontend

* HTML
* Bootstrap 5
* Jinja2 Templates

## Generative AI

* Google Gemini API
* LangGraph
* LangChain

## Document Processing

* PDF parsing
* Text processing
* Document generation

## Storage

User Data:

* SQLite (Development)
* PostgreSQL (Production)

Session Data:

* In-memory session storage
* Redis (Future Production Upgrade)

---

# 📂 Project Structure

```
notepilot-ai/

│
├── app/
│
│   ├── auth/
│   │   ├── models.py
│   │   ├── security.py
│   │   ├── jwt.py
│   │   └── router.py
│   │
│   ├── agents/
│   │   ├── transcript_agent.py
│   │   ├── summary_agent.py
│   │   ├── notes_agent.py
│   │   ├── quiz_agent.py
│   │   └── pdf_agent.py
│   │
│   ├── sessions/
│   │   └── session_manager.py
│   │
│   ├── services/
│   │   ├── gemini_service.py
│   │   └── pdf_service.py
│   │
│   ├── routers/
│   │
│   ├── templates/
│   │
│   ├── static/
│   │
│   └── main.py
│
├── uploads/
│
├── generated_pdf/
│
├── requirements.txt
│
├── .env.example
│
└── README.md

```

---

# 🚀 Application Workflow

## Step 1

User creates an account and logs in.

## Step 2

User uploads lecture transcript.

## Step 3

AI agents process the lecture:

```
Transcript
    ↓
Summary
    ↓
Notes
    ↓
Quiz
```

## Step 4

User reviews generated content.

## Step 5

User optionally exports notes as PDF.

---

# 🔮 Future Enhancements

## AI Learning Assistant

* Chat with lecture content
* RAG-based question answering
* Semantic search

## Learning Features

* Flashcards
* Progress tracking
* Personalized learning paths
* Voice tutor

## Platform Improvements

* Cloud deployment
* Redis session management
* Multiple AI model support
* Team collaboration

---

# 🔧 Environment Variables

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key

DATABASE_URL=sqlite:///./users.db

SECRET_KEY=your_secret_key
```

---

# ▶️ Run Locally

Clone repository:

```bash
git clone <repository-url>

cd notepilot-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000
```

---

# 🎓 Learning Objectives Demonstrated

This project demonstrates:

✅ Agentic AI Application Development
✅ LLM Workflow Orchestration
✅ Gemini API Integration
✅ LangGraph Multi-Agent Architecture
✅ FastAPI Backend Engineering
✅ JWT Authentication
✅ Document Intelligence
✅ AI Product Development

---

# 👨‍💻 Author

**Keshari**

Data Scientist | Generative AI Engineer

Building practical AI systems using LLMs, Agents, and RAG.
