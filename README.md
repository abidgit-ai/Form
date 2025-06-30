# Form Builder

This project provides a minimal dynamic form builder using Flask for the backend and plain HTML/Tailwind for the frontend.

## Features

- Create forms with dynamic fields.
- Submit form responses which are stored in the database.
- Optional parent-child submissions for subforms.
- Export submissions as CSV.

## Running locally

1. Create a Python virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Start the server:

```bash
python backend/app.py
```

The app will be available at `http://localhost:5000`.

## Database

The default configuration uses SQLite for convenience, but you can set the `SQLALCHEMY_DATABASE_URI` environment variable to a PostgreSQL URI if desired.
