class Quotation:
    def __init__(self, customer, product, responsable):
        self.customer = customer
        self.product = product
        self.responsable = responsable
        self.discount = 0

    def apply_discount(self, value):
        self.discount = value