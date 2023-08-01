import sqlite3

class InventoryModel:
    def __init__(self):
        self.conn = sqlite3.connect("prami.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                product TEXT UNIQUE,
                rate REAL,
                remaining_quantity REAL,
                last_updated TEXT DEFAULT CURRENT_TIMESTAMP
            )        
        ''')

        self.update_trigger()


    def update_trigger(self):
        update_trigger_query = """
            CREATE TRIGGER IF NOT EXISTS auto_update_time
            AFTER UPDATE ON inventory
            FOR EACH ROW
            BEGIN
                UPDATE inventory SET last_updated = datetime('now') WHERE ROWID = NEW.ROWID;
            END;
            """
        self.cursor.execute(update_trigger_query)
    
    def get_product_names(self):
        self.cursor.execute('''
            SELECT product FROM inventory
        ''')
        products = self.cursor.fetchall()
        products = [product[0] for product in products]        
        return products


    def get_product_rate(self, product):
        self.cursor.execute('''
            SELECT rate FROM inventory WHERE product = ?
        ''', (product, ))
        rate = self.cursor.fetchone()
        return rate[0]
    
    def get_product_details(self, product):
        self.cursor.execute('''
            SELECT rowid, * FROM inventory WHERE product = ?
        ''', (product, ))
        record = self.cursor.fetchone()
        return record

    def update_product_details(self, data, rowid):
        self.cursor.execute('''
           UPDATE inventory set rate = ?, remaining_quantity = ? WHERE rowid = ?
        ''', (data[0], data[1], rowid))
        self.conn.commit()

    def update_product_quantity(self, quanttity, rowid):
        self.cursor.execute('''
           UPDATE inventory set remaining_quantity = ? WHERE rowid = ?
        ''', (quanttity, rowid))
        self.conn.commit()

    def get_colnames(self):
        self.cursor.execute('''
            PRAGMA table_info(inventory)
        ''')
        cols = self.cursor.fetchall()
        cols = [col[1] for col in cols]
        return cols

    def get_allproducts(self):
        self.cursor.execute('''
            SELECT rowid, * FROM inventory
        ''')
        return self.cursor.fetchall()

    def add_produt_details(self, record):
        self.cursor.execute('''
            INSERT INTO inventory (
                product,
                rate,
                remaining_quantity
            ) VALUES (?, ?, ?)
        ''', record)
        print("Inserted Inventory new data")
        self.conn.commit()


    def update_by_name(self, values):
        self.cursor.execute('''
           UPDATE inventory set rate = ?, remaining_quantity = ? WHERE product = ?
        ''', (values[1], values[2], values[0]))
        self.conn.commit()