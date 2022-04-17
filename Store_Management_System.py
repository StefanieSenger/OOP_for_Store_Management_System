from cgi import print_exception


class Item:

    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)

item2 = Item("Laptop", 1000, 3)
item2.has_numpad = False

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.has_numpad)
print(item2.calculate_total_price())