# from collections import deque

# people = ["Suman","Hemal","Marieme"," Bilal","Osama","Katie","Chloe","Jessica","Susan"]
# people_list = deque(people)
# # people_list.appendleft("Fatou")
# people_list.popleft()
# print(people_list)

# from collections import ChainMap

# people = {"Suman", "Chloe", "Hannah", "Katie", "Fatou"}
# drinks = {"Orange juice", "Tea", "Coffee", "Vodka", "Milk"}
# people_chainmap = ChainMap(people, drinks)
# print(people_chainmap)
# #Output: ChainMap({'Fatou', 'Katie', 'Hannah', 'Suman', 'Chloe'}, {'Milk', 'Coffee', 'Tea', 'Orange juice', 'Vodka'})

# from collections import Counter #To count hashable inputs
# people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou","Suman", "Sally", "Katie", "Hannah", "Suman"]
# people_counter = Counter(people)
# print(people_counter)
# #Counter({'Suman': 3, 'Hannah': 2, 'Katie': 2, 'Chloe': 1, 'Fatou': 1, 'Sally': 1})
# print(list{people_counter.elements()})
# print{people_counter.most_common()}
# sub = ("Suman" : 1 , "Hannah" : 1)
# print(people_counter.subtract(sub))
# print{people_counter.most_common()}

# from collections import OrderedDict
"""
Showing two methods to add number and loop through
"""
# people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
# items = []
# for i, item in enumerate(people, start=1):
#         items.append(f'[{i}] {item}')
# print(items)
# # # output: ['[1] Suman', '[2] Chloe', '[3] Hannah', '[4] Katie', '[5] Fatou']
# print('\n'.join(items), '\n')
# #[1] Suman
# #[2] Chloe
# #[3] Hannah
# #[4] Katie
# #[5] Fatou

#and 

# people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
# items = []
# for i, name in enumerate(people, start=1):
#         items.append(f'[{i}] {name}')
# for item in items:
#     print(item)

# #[1] Suman
# #[2] Chloe
# #[3] Hannah
# #[4] Katie
# #[5] Fatou

"""
Showing how function is incorporated in the above example
"""
# suman_list = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
# def print_menu(title, data):
#     items = []
#     for i, item in enumerate(data, start=1):
#         items.append(f'[{i}] {item}')
#     print(f'{title}\n')
#     print('\n'.join(items), '\n')
# print_menu("SUMAN" , suman_list)
# #Output
# #SUMAN
# # [1] Suman
# # [2] Chloe
# # [3] Hannah
# # [4] Katie
# # [5] Fatou

# people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
# drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]


# name,drink = item.split(":",1)
# if name in people and drink in drinks:
#     preference[name] = drink

# import csv
# ...

# with open('coding.csv', 'w') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])

#Sally, Whittaker
# Belinda, Jameson
# Jeff, Smith
# Sandy, Allen

import csv
class Order:
    def __init__(self, name, drink):
        self.name = name
        self.drink = drink
round = [Order("John", "Coffee"), Order("Sally", "Tea"), Order("Mark", "Coke"), Order("Lisa", "Beer")]
try:
    with open('round.csv', 'w') as csvfile:
        round_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for order in round:
            round_writer.writerow([order.name, order.drink])
except:
    print("Unable to write round")
orders = []
try:
    with open('round.csv', 'r') as csvfile:
        round_reader = csv.reader(csvfile)
        for row in round_reader:
            orders.append(Order(row[0], row[1]))
except:
    print("Unable to read round")
for order in orders:
    print(order.name + " : " + order.drink)


class Order: