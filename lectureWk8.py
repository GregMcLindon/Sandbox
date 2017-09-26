products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
print(products)

on_sale_products = []

for name, price, sale_indicator in products:
    if sale_indicator:
        print("{:5} costs ${:8.2f} and is on sale".format(name, price))
        on_sale_products.append([name, price, sale_indicator])
    else:
        print("{:5} costs ${:8.2f} and is not on sale".format(name, price))
print(on_sale_products)

on_sale_products = [product for product in products if product[2]]
print(on_sale_products)
