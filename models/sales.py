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
                remaining REAL,
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.update_trigger()


    def update_trigger(self):
        update_trigger_query = """
            CREATE TRIGGER IF NOT EXISTS auto_update_time
            AFTER UPDATE ON sales
            FOR EACH ROW
            BEGIN
                UPDATE sales SET last_updated = datetime('now') WHERE ROWID = NEW.ROWID;
            END;
            """
        self.cursor.execute(update_trigger_query)

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
            SELECT rowid, * FROM sales ORDER BY date_time DESC
        ''')
        return self.cursor.fetchall()


    def update_by_date(self, values):
        self.cursor.execute('''
            UPDATE sales set
                        products = ?,
                        buyer = ?,
                        quantitities = ?,
                        rates = ?,
                        total_amount = ?,
                        paid = ?,
                        remaining = ?
                        WHERE date_time = ?
        ''', (values[1], values[2], values[3], values[4], values[5], values[6], values[7],values[0]))
        self.conn.commit()


    def get_udaro_data(self):
        self.cursor.execute('''
            SELECT rowid, buyer, sum(total_amount), sum(paid), sum(remaining) 
            FROM sales where remaining > 0 GROUP BY buyer ORDER BY sum(remaining) DESC
        ''')
        vals = self.cursor.fetchall()
        cols = ['Buyer Name', 'Total _bought', 'Paid', 'Remaining']
        return cols, vals


    def delete_by_date(self, date):
        self.cursor.execute("DELETE FROM sales WHERE date_time == ?", (date,))

        self.conn.commit()


    def close_connection(self):
        self.conn.close()