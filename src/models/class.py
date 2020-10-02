from src.core.table import print_table
preferences = {"Suman": "Water", "Katie" : "Tea"}
class Round: #Class is a blueprint for creating instances. Each person we create in my round class will be an istance of that class
    def __init__(self, owner, time, order_number):
        self.owner = owner
        self.time = time
        self.order_number = order_number
        
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
        print_table(f"{self.owner}'s round",items)

def round_menu():
    input_round_owner = input("Enter round owner name: \n")
    input_round_time = input("Enter time and date: \n")
    input_order_number = input("Enter order number: \n")
    round = Round(input_round_owner, input_round_time,input_order_number)

    # for name, drink in preference:
    #     drink = drink 
    #     if name in preference:
    #         drink = None
    
    # while 
    for name in preferences:
        round.add_an_order(preferences, name)
    round.print_order()

round_menu()