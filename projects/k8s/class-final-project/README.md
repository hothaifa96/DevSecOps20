# Tiny AutoScan Lab

A minimal full-stack playground that demonstrates a “cool automation scanning” concept:

- `frontend/` — Vite + React UI that lets you launch simulated scans and browse the backend environment.
- `backend/` — Flask API with CORS enabled, persisting scan history to SQLite.

## Prerequisites

- Node.js 18+ for the React dev server (Vite needs modern Node).
- Python 3.11+ recommended (any 3.9+ with SQLite works).

## Running the backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API listens on `http://127.0.0.1:5000` and creates `backend/autoscan.db` automatically.

## Running the frontend

```bash
cd frontend
npm install
npm run dev -- --host
```

Set `VITE_API_URL` if your backend runs elsewhere:

```bash
echo "VITE_API_URL=http://127.0.0.1:5000" > .env.local
```

## Available endpoints

- `GET /api/health` basic status.
- `GET /api/scans` returns the latest 20 scan runs.
- `POST /api/scans` creates a simulated scan and records it in SQLite.
- `GET /api/env` exposes a safe snapshot of selected backend environment data for the frontend “Env” page.

## Frontend routes

- `/` automation dashboard with a scan launcher + history table.
- `/env` environment view that renders the data returned by `GET /api/env`.

Feel free to extend the mock scan engine or wire the UI to real tooling. The project stays intentionally tiny so it’s easy to hack on inside the `frontend` and `backend` folders.

## Container builds

Both apps ship with multi-stage Dockerfiles. Example build & push commands (replace the image names with your own registry path):

```bash
# Backend (Python + SQLite)
docker buildx build \
  -f backend/Dockerfile backend \
  -t ghcr.io/you/autoscan-backend:latest \
  --platform linux/amd64,linux/arm64 \
  --push

# Frontend (Vite build served by nginx)
docker buildx build \
  -f frontend/Dockerfile frontend \
  -t ghcr.io/you/autoscan-frontend:latest \
  --platform linux/amd64,linux/arm64 \
  --push
```

If you only need local images, drop the `--platform` and `--push` flags and use `docker run` normally:

```bash
docker build -f backend/Dockerfile -t autoscan-backend:dev backend
docker run --rm -p 5000:5000 autoscan-backend:dev

docker build -f frontend/Dockerfile -t autoscan-frontend:dev frontend
docker run --rm -p 8080:80 autoscan-frontend:dev
```

