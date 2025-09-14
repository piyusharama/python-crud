# Python CRUD Application (Flask + PostgreSQL + Docker)

A simple **CRUD (Create, Read, Update, Delete)** web application built with **Flask**, **SQLAlchemy**, and **PostgreSQL**.  
This project is fully containerized using **Docker & Docker Compose**.

---

## 🚀 Features
- RESTful CRUD operations on items (Add, View, Update, Delete).
- Uses **Flask** as backend web framework.
- Database powered by **PostgreSQL**.
- **SQLAlchemy ORM** for database interactions.
- **Bootstrap templates** for UI.
- Containerized with **Docker** and orchestrated via **Docker Compose**.
- Easy local setup.

---

## 📂 Project Structure

```
python-crud/
│── app.py                # Flask application entry point
│── requirements.txt      # Python dependencies
│── Dockerfile            # Docker image for Flask app
│── docker-compose.yml    # Multi-container setup (Flask + PostgreSQL)
│── templates/            # HTML Jinja2 templates
│── items.db              # Local SQLite DB (for fallback/demo use)
│── Jenkinsfile.docker    # Jenkins pipeline (Docker build/deploy)
│── Jenkinsfile.ssh       # Jenkins pipeline (SSH deploy)
│── README.md             # Documentation
│── venv/                 # Virtual environment (local only, ignored in Docker)
```

---

## ⚙️ Prerequisites

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/)  
- Git (to clone repo)

---

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/piyusharama/python-crud.git
cd python-crud
```

### 2. Build & start the containers
```bash
docker compose up --build
```

This will:
- Start a **PostgreSQL** database (`db` container).  
- Build & start the **Flask app** (`web` container).  

---

## 🌍 Access the Application

Once containers are up, visit:

👉 [http://localhost:5000](http://localhost:5000)

---

## 🐳 Docker Services

- **Web (Flask)** → runs on port `5000`  
- **Database (Postgres)** → runs on port `5432`

To check running containers:
```bash
docker ps
```

To see logs:
```bash
docker logs python-crud-web-1
docker logs python-crud-db-1
```

---

## 🔑 Environment Variables

You can configure database credentials via `docker-compose.yml`. Default values:

```yaml
POSTGRES_USER: postgres
POSTGRES_PASSWORD: postgres
POSTGRES_DB: items
```

The Flask app connects using:

```
postgresql+psycopg2://postgres:postgres@db:5432/items
```

---

## 🧪 Running Locally (without Docker)

If you want to run locally:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

App will run at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Screenshots (Optional)

_Add screenshots of UI pages like Item List, Add Item Form, etc._

---

## 🛠️ CI/CD (Optional)

Project includes sample **Jenkinsfiles**:
- `Jenkinsfile.docker` → for Docker-based builds.  
- `Jenkinsfile.ssh` → for SSH-based deployments.  

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

---

## 📜 License
This project is licensed under the MIT License.

