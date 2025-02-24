from repositorys.base_repository import BaseRepository

class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__(environment='staging')

    def create(self, customer):
        query = 'INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)'
        self.cursor.execute(query, (customer.name, customer.email, customer.phone))
        self.connection.commit()

        return self.cursor.lastrowid

    def delete_by_id(self, id):
        query = 'DELETE FROM customers WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def update_by_id(self, id, customer):
        query = 'UPDATE customers SET name = ?, email = ?, phone = ? WHERE id = ?'
        self.cursor.execute(query, (customer.name, customer.email, customer.phone, id))
        self.connection.commit()

    def find_by_id(self, customer_id):
        self.cursor.execute(
            'SELECT * FROM customers WHERE id = ?',
            (customer_id,)
        )
        return self.cursor.fetchone()

    def find_all(self, limit=10):
        query = 'SELECT * FROM customers LIMIT ?'
        result = self.cursor.execute(query, (limit,))
        rows = result.fetchall()

        if not rows:
            print('No customers found')

        return rows