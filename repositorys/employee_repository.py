from repositorys.base_repository import BaseRepository


class EmployeeRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create(self, employee):
        query = 'INSERT INTO customers (name, registration, comission) VALUES (?, ?, ?)'
        self.cursor.execute(query, (employee.name, employee.registration, employee.comission))
        self.connection.commit()

    def delete_by_id(self):
        pass

    def update_by_id(self):
        pass

    def find_by_id(self, id):
        query = 'SELECT * FROM employees WHERE id = ?'
        result = self.cursor.execute(query, (id,))

        row = result.fetchone()

        if row is None:
            print('empty')

        return row

    def find_all(self, limit = 10):
        pass