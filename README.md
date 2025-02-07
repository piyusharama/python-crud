# Flask CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) web application built with Flask and SQLAlchemy. The application allows users to manage a list of items in a database.

## Features
- List all items
- Add new items
- Edit existing items
- Delete items
- Flash messages for user feedback

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.9+
- pip (Python package manager)
- Docker (if running with Docker)

## Installation & Setup

### Clone the repository
```sh
git clone https://github.com/yourusername/flask-crud-app.git
cd flask-crud-app
```

### Install dependencies
```sh
pip install -r requirements.txt
```

### Set up environment variables
Create a `.env` file and set the required environment variables:
```sh
FLASK_SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///items.db  # Use a different DB URI if needed
```

### Initialize the database
```sh
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Run the application
```sh
python app.py
```
The application will run on `http://127.0.0.1:5000/`.

## Running with Docker
### Build the Docker image
```sh
docker build -t flask-crud-app .
```

### Run the container
```sh
docker run -p 5000:5000 -e FLASK_SECRET_KEY=your_secret_key -e DATABASE_URL=sqlite:///items.db flask-crud-app
```

## Routes
| Route         | Method | Description |
|--------------|--------|-------------|
| `/`          | GET    | Display all items |
| `/add`       | GET/POST | Add a new item |
| `/edit/<id>` | GET/POST | Edit an existing item |
| `/delete/<id>` | GET    | Delete an item |

## Project Structure
```
flask-crud-app/
│-- app.py                 # Main Flask application
│-- requirements.txt       # Dependencies
│-- Dockerfile             # Docker setup
│-- templates/             # HTML templates
│   │-- index.html
│   │-- add.html
│   │-- edit.html
│-- static/                # Static files (CSS, JS, etc.)
│-- .env                   # Environment variables
```

