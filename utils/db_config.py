import psycopg2
import os

def create_connection():
    try:
        connection = psycopg2.connect(
            user=os.getenv('DB_USER', 'your_username'),
            password=os.getenv('DB_PASSWORD', 'your_password'),
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432'),
            database=os.getenv('DB_NAME', 'churn_db')
        )
        return connection
    except Exception as error:
        print("Error while connecting to database:", error)
        return None