# Trip Management System

This project is a **Flask-based web application** designed to manage trips. It provides an API to retrieve trip details from a **MySQL** database and serves an HTML page as the front-end interface. The project uses `.env` files to manage sensitive configuration like database credentials.

## Features

- Displays a homepage with trip details.
- API to manage trip data (`GET` requests).
- Integration with a MySQL database.
- Flask Blueprint architecture for API routes.
- Secure and configurable using environment variables.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Project Structure

Here’s the overall structure of the project:

```bash
trip_crud_assignment/
│
├── app.py                 # Main entry point for the Flask application
├── routes/
│   └── trip_routes.py      # Flask Blueprint for trip-related API routes
├── static/
│   └── js
│       └── trip_crud.js
├── templates/
│   └── index.html          # HTML file rendered for the home page
├── config.py               # Configuration file for Flask and MySQL
├── .env                    # Environment file for sensitive variables
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation (this file)
```

---

## Installation

To run this project locally, follow the steps below:

### 1. Clone the repository:

```bash
git clone https://github.com/rushisurya2705/trips_crud_assignment.git
cd trip-management
```

### 2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables:

You need to create a `.env` file in the root directory with the following variables:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=trip_db
SECRET_KEY=your_secret_key
```

This file will be used to manage sensitive configurations securely.

---

## Environment Variables

The project uses the following environment variables from the `.env` file:

- `MYSQL_HOST`: The host address for the MySQL database (usually `localhost` for local development).
- `MYSQL_USER`: The MySQL username.
- `MYSQL_PASSWORD`: The MySQL password.
- `MYSQL_DATABASE`: The name of the database.
- `SECRET_KEY`: A secret key for Flask’s session management and security features.

**Important:** Do not commit the `.env` file to source control to avoid exposing sensitive information.

---

## Running the Application

Once you have set up the environment and installed the dependencies, run the application using the following command:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`.

---

## API Documentation

The project includes API endpoints to manage trip information.

### Base URL

```
http://127.0.0.1:5000/api/trips
```

### **GET /api/trips**

Fetches the list of all trips.

**Response:**

```json
[
  {
    "id": 1,
    "location": "Location A",
    "name": "Trip A",
    "price": "100.00"
  },
  {
    "id": 2,
    "location": "Location B",
    "name": "Trip B",
    "price": "200.00"
  }
]
```

#### Usage:

You can access this API endpoint using an HTTP client like **Postman** or through a browser.

### **Home Route**

- **URL:** `/`
- **Method:** `GET`
- **Description:** Serves the main HTML page (`index.html`) for the web application.

---

## Configuration

The database connection is handled in `config.py` and relies on environment variables. Here's a simplified explanation of the configuration:

```python
class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    SECRET_KEY = os.getenv('SECRET_KEY')
```

The environment variables are loaded using **python-dotenv**.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or issues, please feel free to reach out.

---

By following the above instructions, you should be able to set up, run, and contribute to the Trip Management System.
