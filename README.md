# Device Management

## Introduction
The Device Management is a Django-based web application designed to manage devices, employees, and checkouts within a company. It provides endpoints for CRUD operations via a RESTful API for devices, employees, and checkouts.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/AnikSaha422/REPLIQ-Django-Practical-Challenge.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

## Usage
1. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

2. Access the API documentation at `http://127.0.0.1:8000/api-docs/` to explore available endpoints and their usage.

3. Use tools like Postman or curl to interact with the API endpoints.

## API Endpoints
### Companies
- `GET /companies/companies/`: List all companies.
- `POST /companies/companies/`: Create a new company.
- `GET /companies/companies/<int:pk>/`: Retrieve, update, or delete a specific company.

### Employees
- `GET /employees/employees/`: List all employees.
- `POST /employees/employees/`: Create a new employee.
- `GET /employees/employees/<int:pk>/`: Retrieve, update, or delete a specific employee.

### Devices
- `GET /devices/devices/`: List all devices.
- `POST /devices/devices/`: Create a new device.
- `GET /devices/devices/<int:pk>/`: Retrieve, update, or delete a specific device.

### Checkouts
- `GET /devices/checkouts/`: List all checkouts.
- `POST /devices/checkouts/`: Create a new checkout.
- `GET /devices/checkouts/<int:pk>/`: Retrieve, update, or delete a specific checkout.


