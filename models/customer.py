class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


    def to_object(self):
        return f'name:{self.name}, email:{self.email}, phone:{self.phone}'
