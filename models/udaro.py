import sqlite3

class UdaroModel:
    def __init__(self):
        self.conn = sqlite3.connect("prami.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS udaro (
                date_time TEXT,
                buyer TEXT,
                total_amount REAL,
                discount REAL,
                paid REAL,
                remaining REAL,
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.update_trigger()


    def update_trigger(self):
        update_trigger_query = """
            CREATE TRIGGER IF NOT EXISTS auto_update_time
            AFTER UPDATE ON udaro
            FOR EACH ROW
            BEGIN
                UPDATE udaro SET last_updated = datetime('now') WHERE ROWID = NEW.ROWID;
            END;
            """
        self.cursor.execute(update_trigger_query)

    def check_name(self, buyer):
        check_query = '''
            SELECT * FROM udaro WHERE buyer = ?
        '''
        self.cursor.execute(check_query, (buyer,))

        result = self.cursor.fetchone()
        return result



    def add_to_udaro(self, record):
        self.cursor.execute('''
            INSERT INTO udaro (
                date_time,
                buyer,
                total_amount,
                discount,
                paid,
                remaining
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', record)
        print("Inserted new data")
        self.conn.commit()

    def get_colnames(self):
        self.cursor.execute('''
            PRAGMA table_info(udaro)
        ''')
        cols = self.cursor.fetchall()
        cols = [col[1] for col in cols]
        return cols


    def get_alludaro(self):
        self.cursor.execute('''
            SELECT rowid, * FROM udaro ORDER BY date_time DESC
        ''')
        return self.cursor.fetchall()


    def update_by_name(self, values):
        self.cursor.execute('''
            UPDATE udaro set
                        total_amount = ?,
                        discount = ?,
                        paid = ?,
                        remaining = ?
                        WHERE buyer = ?
        ''', (values[1], values[2], values[3], values[4], values[0]))
        self.conn.commit()

    def update_by_date(self, values):
        self.cursor.execute('''
            UPDATE udaro set
                        buyer = ?,
                        total_amount = ?,
                        discount = ?,
                        paid = ?,
                        remaining = ?
                        WHERE date_time = ?
        ''', (values[1], values[2], values[3], values[4], values[5], values[0]))
        self.conn.commit()


    def delete_by_date(self, date):
        self.cursor.execute("DELETE FROM udaro WHERE date_time == ?", (date,))

        self.conn.commit()


    def close_connection(self):
        self.conn.close()