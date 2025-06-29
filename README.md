# Courses API - Backend (Django)

This is the backend for the Courses API application, built with Django and Django REST Framework.

## Features

- REST API for managing Courses and their Instances.
- PostgreSQL database integration.
- Dockerized for easy setup and deployment.

## API Endpoints

Refer to the main project README or Postman collection for detailed API documentation.
Briefly:

**Courses**
- `POST /api/courses` – Create a new course
- `GET /api/courses` – List all courses
- `GET /api/courses/<id>` – View a course by ID
- `DELETE /api/courses/<id>` – Delete a course

**Instances**
- `POST /api/instances` – Create a new course instance
- `GET /api/instances/<year>/<semester>` – List all course instances in that year/semester
- `GET /api/instances/<year>/<semester>/<id>` – View a specific course instance
- `DELETE /api/instances/<year>/<semester>/<id>` – Delete a course instance

## Running Locally with Docker

This backend service is designed to be run as part of the `docker-compose.yml` setup in the project root.

1.  **Ensure Docker and Docker Compose are installed.**
2.  **Navigate to the project root directory** (where `docker-compose.yml` is located).
3.  **Environment Variables (Optional but Recommended for Customization):**
    You can create a `.env` file in the project root to customize database credentials or other settings. Example `.env` file:
    ```env
    DB_NAME=my_courses_db
    DB_USER=my_user
    DB_PASSWORD=my_secret_password
    ```
    If no `.env` file is present, `docker-compose.yml` uses default values.

4.  **Build and run the services:**
    ```bash
    docker-compose up --build
    ```
    The `--build` flag ensures images are rebuilt if there are changes (e.g., in `Dockerfile` or `requirements.txt`).

5.  **Database Migrations:**
    The first time you run the application, or after model changes, migrations need to be applied. The `backend` service in `docker-compose.yml` uses a `command` that should ideally be wrapped in a script that waits for the DB and runs migrations. For now, if you encounter DB errors, run migrations manually while services are up:
    ```bash
    docker-compose exec backend python manage.py makemigrations api
    docker-compose exec backend python manage.py migrate
    ```

6.  **Accessing the API:**
    The API will be available at `http://localhost:8000/api/`.

## Design & Architecture Justification

- **Django & Django REST Framework (DRF):** Chosen for rapid development, robust ORM, built-in admin panel (useful for debugging), and excellent support for building REST APIs. DRF provides serializers, generic views, and authentication/permission classes that significantly speed up development.
- **PostgreSQL:** A powerful, open-source relational database suitable for production workloads.
- **Docker:** For containerization, ensuring consistent environments across development, testing, and production. It simplifies dependency management and deployment.
- **Layered Architecture:**
    - `models.py`: Defines the database schema (Courses, Instances).
    - `serializers.py`: Handles conversion of complex data types (like model instances) to JSON and vice-versa, and includes validation.
    - `views.py`: Contains the API logic, using DRF's generic views for common CRUD operations.
    - `urls.py`: Maps API endpoints to their respective views.
- **RESTful Principles:** Endpoints are designed to be resource-oriented and use standard HTTP methods (GET, POST, DELETE). #   a s c - b a c k e n d  
 #   a s c - b a c k e n d  
 #   a s c - b a c k e n d  
 