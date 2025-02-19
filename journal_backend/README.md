## Journal Entry API
    This project provides a backend for managing journal entries, including AI-based insights and writing prompts. It is built using Django, Django REST Framework, and integrates Hugging Face transformers for AI functionality.

## Features
    User authentication with token-based access.
    Create, read, update, and delete journal entries.
    AI-generated insights for journal entries.
    AI-generated writing prompts based on previous entries.
    Installation
    Prerequisites
    Python 3.8+
    Virtualenv (optional but recommended)
    PostgreSQL (if not using SQLite)
    Setup Instructions
    Clone the Repository
    git clone https://github.com/devid-koch/ai-powered-app
    cd ai-powered-app

## Create and Activate a Virtual Environment

    python3 -m venv venv
    source venv/bin/activate  # On Windows,
    use venv\Scripts\activate

# Install Dependencies

    pip install -r requirements.txt


# Set Up the Database

    Configure the database settings in settings.py.

    Run migrations:

    python manage.py makemigrations
    python manage.py migrate

# Start the Development Server

    python manage.py runserver

# API Endpoints
    Authentication
    Login: /api/token/
    Method: POST
    Payload: { "username": "<username>", "password": "<password>" }
    Response: Returns access and refresh tokens.

    Refresh Token: /api/token/refresh/
    Method: POST
    Payload: { "refresh": "<refresh_token>" }
    Response: Returns a new access token.

    Journal Entry Management
    List/Create Entries: /api/journal/entries/
    Method: GET, POST
    Auth: Required
    Payload:
    For POST: { "content": "Your journal entry content" }

    Retrieve/Update/Delete Entry: /api/journal/entries/<id>/
    Method: GET, PUT, DELETE
    Auth: Required

    AI-Powered Insights
    Analyze Journal Entry: /api/journal/analyze/
    Method: POST
    Auth: Required
    Payload: { "content": "Your journal entry content" }
    Response: Returns AI insights for the entry.
    AI Writing Prompts
    Get Writing Prompt: /api/journal/prompt/
    Method: GET
    Auth: Required
    Response: Returns a writing prompt based on previous entries.

# Environment Variables
    Create a .env file in the project root and define the following:

    SECRET_KEY=your_django_secret_key
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/dbname  # Adjust for PostgreSQL