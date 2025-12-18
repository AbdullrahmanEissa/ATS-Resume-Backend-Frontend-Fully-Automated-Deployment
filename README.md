# ATS CV Scanner ⚡️

A simple, lightweight **ATS (Applicant Tracking System) CV scanner** that extracts text from uploaded CVs (PDF/DOCX) and scores them against a job description using keyword matching. Includes a **FastAPI backend**, a **React + Vite frontend**, and an **Ansible playbook** for automated deployment.

---

## Table of Contents
- [Features](#features-)
- [Architecture](#architecture-)
- [Tech Stack](#tech-stack-)
- [Quickstart](#quickstart)
  - [Prerequisites](#prerequisites)
  - [Run Backend Locally](#run-backend-locally-development)
  - [Run Frontend Locally](#run-frontend-locally)
- [API](#api-)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Security & Notes](#security--notes)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features ✅
- Upload CVs in PDF or DOCX format
- Extract text from CVs using `PyPDF2` / `python-docx`
- Score CVs against job descriptions via keyword matching
- Minimal, easy-to-run API and lightweight React frontend
- Ansible playbook for automating server setup and deployment
- **Systemd service** setup for backend for production-ready reliability

---

## Architecture 🔧
- **Backend:** FastAPI app exposing endpoints for health, upload, and analyze operations
- **Parser:** `cv_parser.py` parses PDFs/DOCX
- **Scoring:** `scorer.py` extracts keywords and computes a score (percentage)
- **Frontend:** React + Vite app in `frontend/`
- **Deployment:** Automated using `deploy.yml` (shout out to Ansible! 🎉)

---

## Tech Stack 🧰
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)

---

## Quickstart

### Prerequisites
- Python 3.11+ and `pip`
- Node.js (recommended >= 18) and `npm`
- (Optional) Ansible for deployment automation

---

### Run Backend Locally (Development)
```bash
# 1. Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
````

---

### Run Frontend Locally

```bash
cd frontend
npm install
npm run dev
```

---

## API 📡

**Base URL (local dev):** `http://localhost:8000`

### GET `/health`

* **Response:**

```json
{ "status": "healthy", "message": "ATS CV Scanner API is running" }
```

### POST `/upload-cv`

* **Description:** Upload a CV file (PDF or DOCX)
* **Request:** `multipart/form-data` with key `file`
* **Example:**

```bash
curl -F "file=@/path/to/your/resume.pdf" http://localhost:8000/upload-cv
```

* **Notes:**

  * Allowed extensions: `.pdf`, `.docx`
  * Max file size: 10 MB (configurable in `config.py`)

### POST `/analyze`

* **Description:** Score an uploaded CV against a job description

---

## Deployment 🚀

### Systemd Service for Backend (Professional Setup)

To run your backend as a **production service**, create a `ats-cv-scanner.service` file:

```ini
[Unit]
Description=ATS CV Scanner Backend
After=network.target

[Service]
User=eissa
Group=eissa
WorkingDirectory=/home/eissa/ats-cv-scanner
Environment="PATH=/home/eissa/ats-cv-scanner/venv/bin"
ExecStart=/home/eissa/ats-cv-scanner/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

**Commands to enable & start:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable ats-cv-scanner
sudo systemctl start ats-cv-scanner
sudo systemctl status ats-cv-scanner
```

💡 *Pro tip: Ansible makes deploying this service to multiple servers effortless.*

---

## Project Structure

```
ats-cv-scanner/
├── backend/
│   ├── main.py
│   ├── cv_parser.py
│   ├── scorer.py
│   └── requirements.txt
├── frontend/
│   ├── package.json
│   └── src/
├── deploy.yml
├── README.md
└── config.py
```

---

## Security & Notes

* Only accept files from trusted sources in production
* Limit file size to prevent DoS
* Configure CORS for frontend/backend in production
* Run behind a reverse proxy like Nginx for HTTPS

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## License

MIT License © 2025

---

## Contact

Eissa – [GitHub](https://github.com/AbdullrahmanEissa/)| [Email]
