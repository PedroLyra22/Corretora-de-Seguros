from repositorys.base_repository import BaseRepository


class QuotationRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create(self, quotation):
        query = 'INSERT INTO quotations (customer_id, product_id, responsable, comission) VALUES (?, ?, ?, ?)'
        self.cursor.execute(query, (quotation.customer_id, quotation.product_id, quotation.responsable, quotation.comission))
        self.connection.commit()

    def delete_by_id(self):
        pass

    def update_by_id(self):
        pass

    def find_by_id(self, id):
        query = 'SELECT * FROM quotations WHERE id = ?'
        result = self.cursor.execute(query, (id,))

        row = result.fetchone()

        if row is None:
            print('empty')

        return row

    def find_all(self, limit = 10):
        pass