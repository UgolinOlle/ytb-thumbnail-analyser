# YouTube Thumbnail Analyzer

This project is a web application that analyzes YouTube thumbnail images using AI to provide scores and improvement suggestions. It consists of a FastAPI backend and a React frontend.

## Features

- Upload YouTube thumbnail images
- Analyze thumbnails using AI (powered by Groq API)
- Provide scores and improvement suggestions for thumbnails
- Store analysis results in a database

## Project Structure

The project is divided into two main parts:

1. Backend (FastAPI)
2. Frontend (React + TypeScript + Vite)

### Backend

The backend is a FastAPI application that handles image uploads, analysis, and database operations.

Key components:
- FastAPI application
- SQLAlchemy for database operations
- Groq API integration for image analysis
- Error handling and environment configuration

### Frontend

The frontend is a React application built with TypeScript and Vite, providing a user interface for thumbnail uploads and result display.

Key components:
- React with TypeScript
- Vite for build and development
- Tailwind CSS for styling
- Various UI components and utilities

## Installation

### Prerequisites

- Docker and Docker Compose
- Node.js (for local frontend development)
- Python 3.11+ (for local backend development)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/UgolinOlle/ytb-thumbnail-analyser.git
   cd ytb-thumbnail-analyser
   ```

2. Move the `.env.local` file in the `root` directory to `.env` and complete it with your own credentials
    ```
    mv .env.local .env
    ```

3. Move the `.env.local` file in the `backend` directory to `.env` and complete it with your own credentials
   ```
   cd backend
   mv .env.local .env
   ```

4. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

4. The application should now be running:
   - Backend: http://localhost:8000
   - Frontend: http://localhost:3000

## Development

### Backend

To run the backend locally for development:

1. Navigate to the `backend` directory
    ```
    cd backend
    ```
2. Create a virtual environment and activate it
    ```
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies: `pip install -r requirements.txt`
4. Run the FastAPI server: `uvicorn app.main:app --reload`

### Frontend

To run the frontend locally for development:

1. Navigate to the `frontend` directory
    ```
    cd frontend
    ```
2. Install dependencies: `yarn`
3. Start the development server: `yarn dev`

## API Documentation

Once the backend is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

This project is licensed under the [MIT License](LICENSE).
