# ATS-CV-Scanner

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-18-green?logo=node.js&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-ff0050?logo=fastapi&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646cff?logo=vite&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?logo=ansible&logoColor=white)

> A full-stack ATS CV Scanner with backend (FastAPI), frontend (Vite SPA), Nginx for static serving & reverse proxy, and automated deployment via Ansible.

---

## 🏗 Architecture Overview

```

┌─────────────┐           ┌───────────────┐
│ Frontend    │  <──────> │ Backend       │
│ Vite/SPA    │           │ FastAPI/Uvicorn │
│ /dist       │           │ /app           │
└─────┬───────┘           └──────┬────────┘
│                          │
│ HTTP requests             │ API endpoints
▼                          ▼
┌────────────────────────────────────────┐
│ Nginx (Reverse Proxy + Static Server) │
│ - Serves /dist files                  │
│ - Proxies /api/* requests to backend │
└────────────────────────────────────────┘

````

---

## ⚡ Backend: systemd Service

Ensure the FastAPI backend is **persistent and starts on boot**.

**Unit file**: `/etc/systemd/system/atsscanner-backend.service`

```ini
[Unit]
Description=ATS-CV-Scanner FastAPI backend
After=network.target

[Service]
User=eissa
Group=www-data
WorkingDirectory=/home/eissa/ats-cv-scanner
ExecStart=/home/eissa/ats-cv-scanner/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000

[Install]
WantedBy=multi-user.target
````

**Commands to manage service:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable atsscanner-backend
sudo systemctl start atsscanner-backend
sudo systemctl status atsscanner-backend
```

---

## ⚡ Quickstart

### Prerequisites

* Python 3.11+ & pip
* Node.js >= 18 & npm
* (Optional) Ansible for deployment automation
* Linux environment (tested on Ubuntu 22.04+)

---

### Run Backend Locally (Development)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Run Frontend Locally

```bash
cd frontend
npm install
npm run dev
```

* Local frontend dev URL: `http://localhost:5173` (Vite default)

---

## 📡 API Endpoints

* **Base URL (local dev):** `http://localhost:8000`

### Health Check

```http
GET /health
```

**Response:**

```json
{ "status": "healthy", "message": "ATS CV Scanner API is running" }
```

### Upload CV

```http
POST /upload-cv
```

**Request:** `multipart/form-data` with key `file`
**Example:**

```bash
curl -F "file=@/path/to/your/resume.pdf" http://localhost:8000/upload-cv
```

**Notes:**

* Allowed extensions: `.pdf`, `.docx`
* Max file size: 10 MB (configurable in `config.py`)

### Analyze CV

```http
POST /analyze
```

**Description:** Score an uploaded CV against a job description

---

## 🚀 Production Setup (Nginx + systemd)

### Frontend with Nginx

1. Build frontend:

```bash
cd frontend
npm install
npm run build
```

2. Create Nginx site config: `/etc/nginx/sites-available/atsscanner`

```nginx
server {
    listen 80;
    server_name localhost;

    root /home/eissa/ats-cv-scanner/frontend/dist;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    # Proxy API requests to backend
    location /api/ {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

3. Enable site and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/atsscanner /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

4. Open browser:

```
http://localhost
```

---

## 🔧 Ansible Deployment

Automate setup:

* Update apt cache
* Install Python, pip, Node.js, npm
* Setup backend virtualenv and install dependencies
* Build frontend with npm
* Manage systemd backend service
* Configure Nginx site

> Ensures **repeatable, production-ready deployment**.

---

## ✅ Best Practices

* Use `sites-available` + `sites-enabled` for Nginx.
* Keep `nginx.conf` clean; server blocks go in `sites-available`.
* Use systemd for backend for uptime and reboot persistence.
* Set permissions so `www-data` can read frontend `dist`.
* Build frontend once for production; no `npm run dev`.

Do you want me to do that next?
```
