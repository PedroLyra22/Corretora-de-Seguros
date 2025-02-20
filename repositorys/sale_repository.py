from repositorys.base_repository import BaseRepository


class SaleRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create(self, sale):
        query = 'INSERT INTO sales (quotation_id, comission, final_price) VALUES (?, ?, ?)'
        self.cursor.execute(query, (sale.quotation_id, sale.comission, sale.final_price))
        self.connection.commit()

    def delete_by_id(self):
        pass

    def update_by_id(self):
        pass

    def find_by_id(self, id):
        query = 'SELECT * FROM sales WHERE id = ?'
        result = self.cursor.execute(query, (id,))

        row = result.fetchone()

        if row is None:
            print('empty')

        return row

    def find_all(self, limit = 10):
        pass