import mysql.connector
from mysql.connector import Error

class Config:
    # Pengaturan Database MySQL
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # UBAH SESUAI PASSWORD MYSQL ANDA
    MYSQL_DB = 'db_jurnal_pkl'
    
    # Secret key untuk Flask session (akan digunakan di Tahap 2)
    SECRET_KEY = 'jurnal-pkl-rpl-secret-key-super-aman'
    
    # Pengaturan Upload File
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def get_db_connection():
    """Fungsi pembantu untuk membuka koneksi ke database MySQL."""
    try:
        connection = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error saat membuat koneksi ke MySQL: {e}")
        return None

# Skrip pengujian koneksi saat file diksekusi langsung
if __name__ == '__main__':
    conn = get_db_connection()
    if conn and conn.is_connected():
        print("[SUCCESS] Koneksi database db_jurnal_pkl BERHASIL!")
        conn.close()
    else:
        print("[FAILED] Gagal terhubung ke database. Periksa konfigurasi MySQL Anda.")