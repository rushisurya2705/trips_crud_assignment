import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # MySQL connection details
    MYSQL_HOST = os.getenv('MYSQL_HOST', "localhost")
    MYSQL_USER = os.getenv('MYSQL_USER', "root")
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', "Rishi1718#")
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', "trip_db")
    
    # Ensure the MYSQL_PASSWORD is set
    if not MYSQL_PASSWORD:
        raise ValueError("No MySQL password set. Please define MYSQL_PASSWORD in the .env file.")
    
    # Secret key for session management and security
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
