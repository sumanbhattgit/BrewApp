#Python Object-Oriented Programming

# Method is a function associated with a class
import table
class Round: #Class is a blueprint for creating instances. Each person we create in my round class will be an istance of that class
    def _init__(self, owner_name):
        self.owner_name = name
        self.orders = {}

    def add_an_order(self, preferences, name, drink = None):
        if drink:
            self.orders[name] = drink
            return
        else:
            self.orders[name] = preferences[name]
    def print_order(self):
        items =[]
        for name, drink in self.orders.items():
            items.append(f'{name} ordered {drink}')
        table.print_table(f"{self.owner}'s round",items)

round = Round(input("Enter the brewer name:\n"))



     