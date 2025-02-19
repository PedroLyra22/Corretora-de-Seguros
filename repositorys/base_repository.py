import sqlite3

class BaseRepository:
    def __init__(self):
        self.connection = sqlite3.connect('corretora.db')
        self.cursor = self.connection.cursor()

    def initial_database(self):
        self.create_customer()
        self.create_employee()
        self.create_product()
        self.create_quotation()
        self.create_sale()
        self.connection.close()

    def create_customer(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone TEXT
            )
            '''
        )

    def create_employee(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                registration INT,
                comission FLOAT
            )
            '''
        )

    def create_product(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                kind TEXT,
                price FLOAT
            )
            '''
        )

    def create_quotation(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS quotations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                product_id INTEGER,
                responsable TEXT,
                comission FLOAT
            
                FOREIGN KEY (customer_id) REFERENCES customers(id)
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
            '''
        )

    def create_sale(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quotation_id INTEGER,
                comission FLOAT,
                final_price FLOAT
            
                FOREIGN KEY (quotation_id) REFERENCES quotations(id)
            )
            '''
        )





