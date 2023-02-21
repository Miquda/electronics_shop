from classes import Product

item1 = Product('Iphone', 1200, 15)
item2 = Product('Google Pixel', 1000, 10)

print(item1.get_total_amount())
print(item2.get_total_amount())

Product.discount_price = 0.8

print(item1.set_discount())
print(item2.set_discount())

print(Product.product_list)
