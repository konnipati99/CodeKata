class Store:
    def __init__(self):
        self.actual_prices = {
            'A' : 50,
            'B' : 30,
            'C' : 20,
            'D' : 15
            }
        self.offer_prices = {
            'A':(3,130),
            'B':(2,45)
        }
    def total_price(self,user_input):
        total_price = 0
        product_counts = {}
        for product in user_input:
            if product in self.actual_prices:
               product_counts[product] = product_counts.get(product,0) + 1
            else:
                print(f"{product} is not availble in the store")
        for product, count in product_counts.items():
            if product in self.offer_prices:
                offer_quantity, offer_price = self.offer_prices[product]
                no_of_offers = count // offer_quantity
                remaining_products = count % offer_quantity
                total_price += no_of_offers * offer_price + remaining_products * self.actual_prices[product]
            else:
                total_price += count * self.actual_prices[product]

        return total_price
s = Store()
user_input = input("Enter the products:")
result= s.total_price(user_input)
print(f"The total price is:{result}")