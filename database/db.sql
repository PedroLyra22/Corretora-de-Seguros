CREATE DATABASE corretora;

CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT
)

CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    registration INT,
    comission FLOAT
)

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    kind TEXT,
    price FLOAT
)

CREATE TABLE IF NOT EXISTS quotations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    responsable TEXT,
    comission FLOAT

	FOREIGN KEY (customer_id) REFERENCES customers(id)
	FOREIGN KEY (product_id) REFERENCES products(id)
)

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quotation_id INTEGER,
    comission FLOAT,
    final_price FLOAT

    FOREIGN KEY (quotation_id) REFERENCES quotations(id)
)