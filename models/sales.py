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

    def get_colnames(self):
        self.cursor.execute('''
            PRAGMA table_info(sales)
        ''')
        cols = self.cursor.fetchall()
        cols = [col[1] for col in cols]
        return cols

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

    def get_allsales(self):
        self.cursor.execute('''
            SELECT rowid, * FROM sales
        ''')
        return self.cursor.fetchall()



    def close_connection(self):
        self.conn.close()