import sqlite3

class SalesModel:
    def __init__(self):
        self.conn = sqlite3.connect("prami.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                date_time TEXT,
                products TEXT,
                buyer TEXT,
                quantitities TEXT,
                rates TEXT,
                total_amount REAL,
                paid REAL,
                remaining REAL
            )
        ''')

    def add_sale(self, record):
        self.cursor.execute('''
            INSERT INTO sales (
                date_time,
                products,
                buyer,
                quantitities,
                rates,
                total_amount,
                paid,
                remaining
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', record)
        print("Inserted new data")
        self.conn.commit()

    def update_sale():
        pass

    
    def get_sales(self):
        self.cursor.execute('''
            SELECT * FROM sales
        ''')
        return self.cursor.fetchall()


    def close_connection(self):
        self.conn.close()