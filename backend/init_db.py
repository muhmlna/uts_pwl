import sqlite3
from faker import Faker
import faker_commerce
import os


def init_db():
    if os.path.exists("database.sqlite"):
        os.remove("database.sqlite")
    try:
        with sqlite3.connect("database.sqlite") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price INTEGER,
                    stock INTEGER,
                           image_url TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    init_db()
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)

    with sqlite3.connect("database.sqlite") as conn:
        cursor = conn.cursor()
        for i in range(5):
            cursor.execute("INSERT INTO products (name, price, stock, image_url) VALUES (?,?,?,?)", (fake.ecommerce_name(
            ), fake.random_int(min=1000, max=100000), fake.random_int(min=0, max=100), "https://picsum.photos/200"))
        conn.commit()
