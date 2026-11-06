import os
import mysql.connector
from mysql.connector import Error


class Config:
    MYSQL_HOST = os.environ.get('MYSQLHOST')
    MYSQL_USER = os.environ.get('MYSQLUSER')
    MYSQL_PASSWORD = os.environ.get('MYSQLPASSWORD')
    MYSQL_DB = os.environ.get('MYSQLDATABASE')
    MYSQL_PORT = int(os.environ.get('MYSQLPORT') or 3306)

    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'jurnal-pkl-rpl-secret-key-super-aman'
    )

    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}


def get_db_connection():
    """Fungsi pembantu untuk membuka koneksi ke database MySQL."""
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT,
            autocommit=True,
            connection_timeout=30
        )
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE()")
        print(cursor.fetchone())
        if connection.is_connected():
            return connection

    except Error as e:
        print(f"Error saat membuat koneksi ke MySQL: {e}")
        return None