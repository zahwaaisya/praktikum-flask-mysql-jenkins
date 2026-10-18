
import os
import time
import mysql.connector
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppassword"),
        database=os.getenv("DB_NAME", "praktikum_db")
    )

def init_db():
    for attempt in range(30):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS visitors (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
            print("Database siap.")
            return
        except mysql.connector.Error as error:
            print(f"Menunggu database: {error}")
            time.sleep(2)

    raise RuntimeError("Database tidak dapat dihubungi.")

@app.route("/")
def hello():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors () VALUES ()")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visitors")
        total = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return (
            "<h1>Flask + MySQL + Docker + Jenkins</h1>"
            f"<p>Koneksi database berhasil!</p>"
            f"<p>Total kunjungan tersimpan: {total}</p>"
        )
    except mysql.connector.Error as error:
        app.logger.exception("Database error")
        return "Database belum dapat diakses.", 500

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
