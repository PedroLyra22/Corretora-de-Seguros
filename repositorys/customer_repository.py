from main import employee
from repositorys.base_repository import BaseRepository


class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create(self, customer):
        query = 'INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)'
        self.cursor.execute(query, (customer.name, customer.email, customer.phone))
        self.connection.commit()

    def delete_by_id(self):
        pass

    def update_by_id(self):
        pass

    def find_by_id(self, id):
        query = 'SELECT * FROM customers WHERE id = ?'
        result = self.cursor.execute(query, (id,))

        row = result.fetchone()

        if row is None:
            print('empty')

        return row

    def find_all(self, limit = 10):
        pass