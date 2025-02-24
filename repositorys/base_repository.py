import os
import sqlite3


class BaseRepository:
    def __init__(self, environment):
        self.environment = environment
        self.connection = sqlite3.connect(self.handler_database_name())
        self.cursor = self.connection.cursor()

    def __del__(self):
        if self.connection:
            self.connection.close()

    def handler_database_name(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if self.environment == 'production':
            return os.path.join(base_dir, '..', 'database', 'database_production.db')
        else:
            return os.path.join(base_dir, '..', 'database', 'database_staging.db')

    def initial_database(self):
        self.create_customer()
        self.create_employee()
        self.create_product()
        self.create_quotation()
        self.create_sale()

    def clean_database(self):
        self.cursor.execute('DELETE FROM sales')
        self.cursor.execute('DELETE FROM quotations')
        self.cursor.execute('DELETE FROM products')
        self.cursor.execute('DELETE FROM employees')
        self.cursor.execute('DELETE FROM customers')

        self.connection.commit()

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
                comission FLOAT,

                FOREIGN KEY (customer_id) REFERENCES customers(id),
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
                final_price FLOAT,

                FOREIGN KEY (quotation_id) REFERENCES quotations(id)
            )
            '''
        )
