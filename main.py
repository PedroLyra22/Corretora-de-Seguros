from models.employee import Employee
from models.customer import Customer
from models.product import Product
from models.quotation import Quotation

employee = Employee(name='Pedro', registration=202092918, comission=0.1)
customer = Customer(name='Luiza', email='luiza@gmail.com', phone=999804008)
product = Product(name='Seguro Automotivo', kind='parcela única', price=200)
quotation = Quotation(customer=customer, product=product, responsable=employee)

print(employee.__dict__)
print(customer.to_object())
print(product.__dict__)
print(quotation.__dict__)