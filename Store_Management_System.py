import csv

# Creating a class
class Item:
    pay_rate = 0.8 # pay rate after 20% of discount (class attribute)
    all = []

    # __init__ initialises instances
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"

        # Assign attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # defining methods within the class, that can be called from all instances lateron
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # overwrites an items attribute
                                                # should the attribute not be defined itemwise, it takes the classwise definition
    @classmethod
    def instantiate_from_csv(cls): # Class method, because it cannot be called from an instance, since it is for initiating the instances
        with open('/home/stefanie/Python/OOP_for_Store_Management_System/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
                )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): # defines how instances are represented
        return f"Item('{self.name}', {self.price}, {self.quantity})" # best praxis is to display these the same way as we define instances


# Creating instances (manually)
'''
item1 = Item("Phone", 100, 1)

item2 = Item("Laptop", 1000, 3)
item2.has_numpad = False # attribute that's only existing on that particular item
item2.pay_rate = 0.7

item3 = Item("Cable", 10, 5)

item4 = Item("Mouse", 50, 5)

item5 = Item("Keyboard", 75, 5)


# Detecting functionality by outputs
#print(item1.pay_rate) # searches for attributes first on instance-level, and if there isn't any, then looks up the class attributes

#print(Item.__dict__) # creates a dictionary of all active attributes
#print(item1.__dict__) # creates a dictionary of all active attributes

item1.apply_discount() # applying the account on items
#print(item1.price)
item2.apply_discount() # applying the account on items
#print(item2.price)

print(Item.all) # lists all instances and where they are saved
for instance in Item.all:
    print(instance.name)
'''

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.0))