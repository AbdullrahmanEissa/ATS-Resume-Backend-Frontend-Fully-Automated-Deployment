# ATS Resume Scanner & Analyzer 🚀

[![CI/CD](https://img.shields.io/badge/CI%2FCD-Ansible-EE0000?style=for-the-badge&logo=ansible&logoColor=white)](https://github.com/AbdullrahmanEissa/ATS-Resume-Backend-Frontend-Fully-Automated-Deployment)
[![Backend](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Frontend](https://img.shields.io/badge/Frontend-Vite%20%2B%20React-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)
[![Nginx](https://img.shields.io/badge/Nginx-Stable-orange?logo=nginx)](https://www.nginx.com/)

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/be7fbf3a-c9aa-43ba-9a6a-0fd85da0a0c3" />


A **full-stack, fully automated CV scanner** built with Python, FastAPI, Node.js, and Nginx. Designed for modern DevOps workflows using **Docker** and ready for **production deployment**.

---

## Table of Contents

1. [Features](#features)
2. [Architecture](#architecture)
3. [Quick Start](#quick-start)
4. [Backend Setup](#backend-setup)
5. [Frontend Setup](#frontend-setup)
6. [Running the Full Stack](#running-the-full-stack)
7. [Project Structure](#project-structure)
8. [Best Practices & Notes](#best-practices--notes)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features

* **CV parsing & scoring** using machine learning models
* **REST API backend** powered by FastAPI
* **Modern frontend** built with Node.js & Nginx
* **Dockerized environment** for easy deployment
* Supports **multi-file uploads** and bulk processing
* Clean, maintainable project structure

---

## Architecture

```text
          +-------------------+
          |   Frontend (Nginx)|
          +---------+---------+
                    |
                    v
          +-------------------+
          |  Backend (FastAPI)|
          +---------+---------+
                    |
                    v
           +----------------+
           |  ML Models &   |
           |  Database      |
           +----------------+
```

* **Frontend:** Node.js served via Nginx
* **Backend:** Python FastAPI API
* **Data:** CV processing models and storage

---

## Quick Start

### Prerequisites

* Docker >= 29.0
* Docker Compose plugin (optional)
* Linux environment (tested on Debian 13 “Trixie”)

---

## Backend Setup

```bash
# Navigate to project folder
cd ~/ats-cv-scanner

# Build backend Docker image
docker build -t ats-backend .

# Run backend container
docker run -d --name ats-backend -p 8000:8000 ats-backend
```

Test backend:

```bash
curl http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

# Build frontend Docker image
docker build -t ats-frontend .

# Run frontend container
docker run -d --name ats-frontend -p 80:80 ats-frontend
```

Now access the frontend via `http://localhost`.

---

## Running the Full Stack

Optionally, you can use **Docker Compose**:

```yaml
version: "3.9"
services:
  backend:
    image: ats-backend
    container_name: ats-backend
    ports:
      - "8000:8000"
  frontend:
    image: ats-frontend
    container_name: ats-frontend
    ports:
      - "80:80"
```

```bash
docker compose up -d
```

---

## Project Structure

```
ats-cv-scanner/
│
├─ ansible/              # Ansible deployment scripts
├─ frontend/             # Node.js & Nginx frontend
├─ models/               # ML models for CV parsing
├─ routers/              # API routing modules
├─ services/             # Service layer for backend
├─ uploads/              # Uploaded CV storage
├─ main.py               # FastAPI entry point
├─ config.py             # Configuration file
├─ requirements.txt      # Python dependencies
├─ Dockerfile            # Backend Dockerfile
└─ README.md
```

---

## Best Practices & Notes

* **Remove local virtual environments** before building Docker images:

```bash
rm -rf venv __pycache__ node_modules dist
```

* **Docker cleanup tips**:

```bash
docker system prune -f
```

* **Enable Docker for your user**:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

* Backend runs on port `8000`, frontend on port `80`. Configure Nginx or reverse proxy for production.

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/xyz`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to branch (`git push origin feature/xyz`)
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** – see [LICENSE.txt](LICENSE.txt).

**Author:** [Abdullrahman Eissa](https://www.google.com/search?q=https://github.com/AbdullrahmanEissa)
