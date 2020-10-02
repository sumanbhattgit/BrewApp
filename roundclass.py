#Python Object-Oriented Programming

# Method is a function associated with a class
UPDATED ON 01/10/2020  01:00 AM

from src.core.table import print_table, print_footer, print_footer2
import datetime

preferences = {"Suman":"Orange juice", "Chloe":"Tea" , "Hannah":"Coffee", "Katie":"Vodka", "Fatou":"Milk"}

class Round: #Class is a blueprint for creating instances. Each person we create in my round class will be an istance of that class
    def __init__(self, owner_name, round_time, order_number):
        self.name = owner_name
        self.time = round_time
        self.ordernum = order_number
        self.orders = {}

    def add_an_order(self, name, drink):
        if drink:
            self.orders[name] = drink
    def print_order(self):
        items =[]
        for name, drink in self.orders.items():
            items.append(f'{name} ordered {drink}')
        print_table(f"{self.name}'s round",items)
        # print(f"{self.input_round_time}")
        # print(f"{self.input_order_number}")



def round_menu():
    print("Print1")
    input_round_owner = input("Enter round owner name: \n")
    input_round_time = datetime.datetime.now
    print(input_round_time)
    input_order_number = 5
    round = Round(input_round_owner, input_round_time,input_order_number) 
    while True:
        order_name = input("Enter a name: \n")
        if order_name not in preferences:
            userin = input("Enter your drink :\n")
            round.add_an_order(order_name, userin)
         
            userinputexit = input("Press enter to add more drinks or type exit to quit: \n")
            if userinputexit.lower() in {"e", "exit"}:
                print("checking 1 2 3")
                round.print_order()      
                exit()
            else:
                continue

        if order_name in preferences:
            print("Do you want your favourite drink? \n")
            userinput = input("Enter yes or no \n")
            if userinput.lower() in {"y","yes"}: 
                round.add_an_order(order_name, preferences[order_name])
 
                print("it will prob print something")
                round.print_order()  
                exit()
            else:
                continuee
            if userinput.lower() in {"n","no"}: 
                userin = input("Enter your drink :\n")
                print("userin")
                round.add_an_order(order_name, userin)
  
            userinputexit = input("Press enter to add more drinks or type exit to quit: \n")
            if userinputexit.lower() in {"e", "exit"}:
                print("checking 1 2 3")
                round.print_order()  
                exit()
            else:
                continue

    for name in preferences:
        round.add_an_order(preferences, name)
    round.print_order()
round_menu()

# r1 = Round("Vovo","b","c")
# r1.add_an_order({}, "Suman", "Water")

# r1.print_order()

# class Person:
#     def__init__(self,name ,age):
#         self.name = name
#         self.age = age

#     def drink_age(self):
#         return self.age >= 18

# class Drink:
#     def__init__(self, name, drinks):
#         self.name = name
#         self.drinks = drinks





     