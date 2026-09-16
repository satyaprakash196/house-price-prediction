import os
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "house-price-mysql"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "houseuser"),
        password=os.getenv("DB_PASSWORD", "housepassword"),
        database=os.getenv("DB_NAME", "house_db")
    )
