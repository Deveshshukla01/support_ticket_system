# 🎫 Helpdesk Ticketing API

**Authors:** Devesh, Himanshu, Tanish

A FastAPI-based backend system for managing support tickets with features like ticket creation, assignment, status tracking, and filtering.

---

## 🚀 Features

- User Registration & Login (bcrypt authentication)
- Create Support Tickets
- Assign Tickets to Agents
- Update Ticket Status (open, in_progress, closed)
- Filter Tickets by Status
- Get Tickets by User
- RESTful API with FastAPI
- Dockerized Application

---

## 🛠️ Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- SQLite
- Docker

---

## 📂 Project Structure

```bash
support_ticket_system/
│── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── tickets.py
│   │   ├── comments.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── main.py
│
│── Dockerfile
│── requirements.txt
│── README.md

## ⚙️ Installation & Setup

1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/support_ticket_system.git
cd support_ticket_system

2️⃣ Run locally
pip install -r requirements.txt
uvicorn app.main:app --reload


3️⃣ Run with Docker
docker build -t ticket-api .
docker run -d -p 8000:8000 ticket-api
📌 API Docs

Swagger UI available at:

http://localhost:8000/docs
```
