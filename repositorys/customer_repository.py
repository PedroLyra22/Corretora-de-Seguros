from repositorys.base_repository import BaseRepository


class CustomerRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create(self):
        pass

    def delete_by_id(self):
        pass

    def update_by_id(self):
        pass

    def find_by_id(self, id):
        query = f'SELECT * FROM customers WHERE id = {id}'
        result = self.cursor.execute(query)
        return result

    def find_all(self, limit = 10):
        pass