# Task-Management-App
FastAPI, ReactJS, Postgres App

## Stack
- **Backend:** FastAPI, SQLAlchemy 2, Alembic, psycopg 3 (Python 3.12), in `backend/`
- **Frontend:** React + Vite, Axios, in `frontend/`
- **Database:** PostgreSQL 16 (Homebrew)

## Database
Postgres runs as a Homebrew service:
```bash
brew services start postgresql@16   # start (it auto-starts on login)
brew services stop postgresql@16
psql -h localhost -U taskapp -d taskapp   # password: taskapp
```
Databases are `taskapp` (dev) and `taskapp_test` (tests), both owned by the user `taskapp`.

## Backend
```bash
cd backend
cp .env.example .env
source .venv/bin/activate
pip install -r requirements.txt     # only needed on a fresh clone (after python3.12 -m venv .venv)
fastapi dev app/main.py             # http://localhost:8000, docs at /docs
```

## Frontend
```bash
cd frontend
cp .env.example .env
npm install                         # only needed on a fresh clone
npm run dev                         # http://localhost:5173
```
