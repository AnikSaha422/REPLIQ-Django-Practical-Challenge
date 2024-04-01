# Device Management System

## Introduction
The Device Management System is a Django-based web application designed to manage devices, employees, and checkouts within a company. It provides endpoints for CRUD operations via a RESTful API for devices, employees, and checkouts.

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

2. Access the API documentation at `http://localhost:8000/api-docs/` to explore available endpoints and their usage.

3. Use tools like Postman or curl to interact with the API endpoints.

## API Endpoints
### Companies
- `GET /companies/`: List all companies or create a new company.
- `GET /companies/<int:pk>/`: Retrieve, update, or delete a specific company.

### Employees
- `GET /employees/`: List all employees or create a new employee.
- `GET /employees/<int:pk>/`: Retrieve, update, or delete a specific employee.

### Devices
- `GET /devices/`: List all devices or create a new device.
- `GET /devices/<int:pk>/`: Retrieve, update, or delete a specific device.

### Checkouts
- `GET /checkouts/`: List all checkouts or create a new checkout.
- `GET /checkouts/<int:pk>/`: Retrieve, update, or delete a specific checkout.

## Contributing
Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) for details on how to contribute to this project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
