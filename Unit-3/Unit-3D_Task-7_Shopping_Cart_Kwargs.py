def shopping_cart(**products):
    total = 0
    for item, price in products.items():
        print(item, ": Rs.", price)
        total += price
    print("Total: Rs.", total)

shopping_cart(apple=15, orange=12, mango=10)
