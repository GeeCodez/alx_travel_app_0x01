# ALX Travel App

A **Django REST Framework** application to manage travel **listings**, **bookings**, and **reviews**, with **Swagger API documentation** and **PostgreSQL** integration.

---

## Features

- CRUD operations for **Listings** and **Bookings**  
- **Reviews** for bookings  
- **RESTful API** with Swagger docs at `/swagger/`  
- **PostgreSQL** database configured via environment variables  
- **CORS** support for frontend applications  

---

## Installation

```bash
# Clone repository
git clone <repo-url>
cd alx_travel_app

# Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure PostgreSQL in .env file
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Apply migrations and seed databa
