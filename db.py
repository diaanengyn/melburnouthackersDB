import sqlite3

connection = sqlite3.connect("/Users/dakshagrawal/PycharmProjects/flask-server/database.db")

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_name TEXT, 
    sku TEXT, 
    description TEXT,
    quantity INTEGER,
    price INTEGER,
    company_id INTEGER
    );
    """
)
