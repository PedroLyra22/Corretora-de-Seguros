from models.employee import Employee
from models.customer import Customer
from models.product import Product
from models.quotation import Quotation
from models.sale import Sale

from repositorys.base_repository import BaseRepository

employee = Employee(name='Pedro', registration=202092918, comission=0.05)
customer = Customer(name='Luiza', email='luiza@gmail.com', phone=999804008)
product = Product(name='Seguro Automotivo', kind='parcela única', price=200)
quotation = Quotation(customer=customer, product=product, responsable=employee)
sale = Sale(quotation=quotation, comission=0.1)

base = BaseRepository()
base.initial_database()

print(employee.__dict__)
print(customer.to_object())
print(product.__dict__)
print(quotation.__dict__)
print(sale.__dict__)


quotation.apply_discount(0.2)

print(sale.__dict__)

sale.set_final_price()

print(sale.__dict__)
