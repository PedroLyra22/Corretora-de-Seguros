from repositorys.base_repository import BaseRepository


class ProductRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create(self, product):
        query = 'INSERT INTO employees (name, kind, price) VALUES (?, ?, ?)'
        self.cursor.execute(query, (product.name, product.kind, product.price))
        self.connection.commit()

    def delete_by_id(self):
        pass

    def update_by_id(self):
        pass

    def find_by_id(self, id):
        query = 'SELECT * FROM products WHERE id = ?'
        result = self.cursor.execute(query, (id,))

        row = result.fetchone()

        if row is None:
            print('empty')

        return row

    def find_all(self, limit = 10):
        pass