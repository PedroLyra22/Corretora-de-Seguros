class Sale:
    def __init__(self, quotation, comission):
        self.quotation = quotation
        self.comission = comission
        self.final_price = None

    def set_final_price(self):
        self.final_price = self.quotation.product.price - (self.quotation.product.price * self.quotation.discount)


