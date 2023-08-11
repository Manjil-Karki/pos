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
                rate REAL,
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP
            )        
        ''')
        self.update_trigger()


    def update_trigger(self):
        update_trigger_query = """
            CREATE TRIGGER IF NOT EXISTS auto_update_time
            AFTER UPDATE ON purchase
            FOR EACH ROW
            BEGIN
                UPDATE purchase SET last_updated = datetime('now') WHERE ROWID = NEW.ROWID;
            END;
            """
        self.cursor.execute(update_trigger_query)


    def get_colnames(self):
        self.cursor.execute('''
            PRAGMA table_info(purchase)
        ''')
        cols = self.cursor.fetchall()
        cols = [col[1] for col in cols]
        return cols

    def get_allpurchases(self):
        self.cursor.execute('''
            SELECT rowid, * FROM purchase ORDER BY date_time DESC
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

    def update_by_date(self, values):
        self.cursor.execute('''
           UPDATE purchase set
                        product = ?,
                        quantity = ?,
                        kgs_per_sack = ?,
                        cost_price_per_sack = ?,
                        rate = ?
                        WHERE date_time = ?
        ''', (values[1], values[2], values[3], values[4], values[5], values[0]))
        self.conn.commit()
        
    def delete_by_date(self, date):
        try:
            self.cursor.execute("DELETE FROM purchase WHERE date_time == ?", (date,))

            self.conn.commit()
            return True
        except:
            return False