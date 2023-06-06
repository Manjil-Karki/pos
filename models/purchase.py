import sqlite3

class PurchaseModel:
    def __init__(self):
        self.conn = sqlite3.connect("prami.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchase (
                date_time TEXT,
                product TEXT,
                quantity REAL,
                kgs_per_sack REAL,
                cost_price_per_sack REAL,
                rate REAL
            )        
        ''')

    def add_purchase(self, record):
        self.cursor.execute('''
            INSERT INTO purchase (
                date_time,
                product,
                quantity,
                kgs_per_sack,
                cost_price_per_sack,
                rate
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', record)
        print("Inserted new data")
        self.conn.commit()
