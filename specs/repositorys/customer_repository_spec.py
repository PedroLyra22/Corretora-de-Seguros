from repositorys.base_repository import BaseRepository
from repositorys.customer_repository import CustomerRepository
from models.customer import Customer

def teste_find_by_id():

    repository = CustomerRepository()
    print(repository.find_by_id(2))

base_repository = BaseRepository()
base_repository.initial_database()
repository = CustomerRepository()

customer = Customer('Juca', 'juca@gmail.com', '12344321')
repository.create(customer)

teste_find_by_id()