class Product:
    discount_price = 0.85
    product_list = []

    def __init__(self, product_name, price, amount):
        self.product_name = product_name
        self.price = price
        self.amount = amount
        self.product_list.append(self)

    def get_total_amount(self):
        return self.price * self.amount

    def set_discount(self):
        return self.price * self.discount_price

    def __repr__(self):
        return (f'Product - {self.product_name}, price - {self.price}, amount - {self.amount}')

