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

    def get_colnames(self):
        self.cursor.execute('''
            PRAGMA table_info(purchase)
        ''')
        cols = self.cursor.fetchall()
        cols = [col[1] for col in cols]
        return cols

    def get_allpurchases(self):
        self.cursor.execute('''
            SELECT rowid, * FROM purchase
        ''')
        return self.cursor.fetchall()


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
