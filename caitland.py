import csv 
#import receipts
#import orders
#import favourites

"""
Menu = f"""
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number: 
[1] Make an order
[2] Favourite drinks list
[3] Customer receipts
[4] Exit
"""

​def load_from_csv():
    with open('orders.csv', 'w') as csvfile:
  #      orders_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
   #     for order in orders:
    #        orders_writer.writerow([order.name, order.drink])
​
#except:
 #   print("Unable to write orders")
​
​


#data
​
  #  favourites = {'Janet' : 'Coffee', 'Joe' : 'Tea', 'Jane' : 'Green Tea', 'Jack' : 'Water'}
​
​
#for key, value in enumerate(people):
#   dict()
#for key, value in enumerate(drinks):
 #   dict()
#favourites = dict(zip(people, drinks))
​
prices = {'Coffee' : '£2.50', 'Tea' : '£2.00', 'Green Tea' : "£2.00", 'Water' : '£1.00'}
​
​
​
​
#Order definitions 
​
def wait():
    input('Press ENTER to return to the menu')
​
def if_wrong_drink(user_input):
    while user_input not in prices:
        user_input = input(f'Sorry we don\'t sell that here.\nPlease type a drink from the price list:{prices}:\n').title()
        if user_input in prices:
            order.append(user_input)
            user_input = input(f'Your order is \'{order}\'\nWould you like to add to this order?\nYES or NO\n').lower()
            while user_input == "yes":
                user_input = input(f'Please type a drink from the price list: {prices} \n').title()
                if user_input in prices:
                    order.append(user_input)
                    user_input = input(f'Your order is \'{order}\'\nWould you like to add to this order?\nYES or NO\n').lower()
                    if user_input == "no":
                        print(f'Thank you! \nYour order is: {order}.\n\nWe hope to see you again, {name}!')
                        wait()
      
                            
          #  if user_input == 'no':
           #     print(f'Thank you! \nYour order is: {order}.\n\nWe hope to see you again, {name}!')
            #    wait()
      
def thank_you_message():
    print(f'\n\nThank you, {input_name}! \nYour order is: {order}.\n\nWe look forward to seeing you again!')
    wait()
​
​
#def name_search(user_input):
   # try: 
 #       print(f'{people_search}\'s favourite drink is: {favourites[user_input.title()]}') 
    #except:
     #   print('This name does not exist')
​
#drink orders
    order = []
    for i in range(10):
        list()
#new names for reciepts
 #   new_name = []
  #  for i in range (40):
   #     list()
​
​
   
​
    
    
​
# Handle arguments
​
#start app 
while True:
    print(MENU)
    try: 
        user_selection = int(input('Enter your selection: '))
        print(user_selection)
​
    except ValueError:
        print('Not an option.')
        wait()
        continue
#load data from csv
    try:
        with open('favourites.csv', 'r') as favouritesfile:
            reader = csv.DictReader(favouritesfile)
​
    except:
        print("Unable to handle favourites")
​
    if user_selection == ORDER_ARG:
        input_name = (input('\nWhat is your name?:\n').title())
        if input_name in favouritesfile:
            user_input = input(f'\nWelcome back {input_name}!\nWould you like to order a {favouritesfile[name]}?\n\nYES or NO\n').lower()
            if user_input == 'yes':
                order = (favouritesfile[name])
                user_input = input(f'\nWe have your order down as a {order}.\n\nWould you like to add to this?\n YES or NO\n').lower()
                while user_input == "yes":
                    user_input = input(f'Please type a drink from the price list: {prices} \n').title()
                    if_wrong_drink(user_input)
                    if user_input in prices:
                        #    order.append(user_input)
                        user_input = input(f'Your order is \'{order}\'\nWould you like to add to this order?\nYES or NO\n').lower()
                           # if name in prices:
                            #    orders[name].append(order)  
                        if user_input == "no":
                            thank_you_message()
​
               # if user_input == "no":
                #   thank_you_message()
             
   
            elif user_input == "no":
                user_input = input(f'Please type a drink from the price list:{prices}:\n').title()
                if_wrong_drink(user_input)
                if user_input in prices:
                    order.append(user_input)
                    user_input = input(f'Your order is \'{order}\'\nWould you like to add to this order?\nYES or NO\n').lower()
                    while user_input == 'yes':
                        user_input = input(f'Please type a drink from the price list: {prices} \n').title()
                        if_wrong_drink(user_input)
                      #  if user_input == 'no':
                       #     thank_you_message()  
                   
            else: 
                wait()
#favourites is a new dict was once two lists
            if input_name not in favouritesfile:
                name.favouritesfile.append(input_name)
                user_input = input(f'\nWelcome {input_name}!\n Please type a drink from the price list: {prices} \n').title() 
                if_wrong_drink(user_input)
                if user_input in prices:
                    order.append(user_input)
                    user_input = input(f'Your order is \'{order}\'\nWould you like to add to this order?\nYES or NO\n').lower()
                    while user_input == 'yes':
                        user_input = input(f'Please type a drink from the price list: {prices} \n').title() 
                        if_wrong_drink(user_input)  
                    #if user_input == 'no':
                     #   thank_you_message()
                #else:
                  #  wait()
                    
​
#TODO: Save and refresh order variable after each order
          
​
    #favourites section
    
    if user_selection == FAVE_DRINK_ARG:
        print(favouritesfile)
        answer = input('\nWould you like to add to this? \nYES or NO: \n')
        if answer.lower() == 'yes':
            new_name = input('\nType in a name: \n').title()
​
            while new_name in favouritesfile:
                print(f'\'{new_name}\' already exists on our system')
                new_name = input('Press ENTER to return to menu page \n    OR\nType in name: \n').title()
#write cvsfile
            try:
                with open ('favourites.csv', 'w') as csvfile:
                    favourites_reader = csv.reader(csvfile)
                for favourite in favourites_reader:
                    favourites_reader.writerow([name, drink]) 
            except:
                print('Unable to print favourites')
​
            if new_name not in favouritesfile:
              #  favouritesfile['name'].append(new_name)
                print(f'\'{new_name}\' has been added...')
                new_drink = input(f'Now type {new_name}\'s favourite drink from the price list: {prices} \n').title()
                if new_drink in prices:
                    favouritesfile['favourite drink'].append(new_drink)
                    print(f'{new_name}\'s order is now saved as \'{new_drink.lower()}\'.')
                    wait()
                else: 
                    print('Sorry, we don\'t sell that here.')
                    while new_drink not in prices:
                        new_drink = input(f'Choose a drink: {prices} \n').title()
                        if new_drink in prices:
                            drinks.append(new_drink)
                            print(f'{new_name}\'s order is now saved as \'{new_drink.lower()}\'.')
                            wait()     
    
   # elif user_selection == RECEIPTS_ARG:
       # customer_receipt = input("Type in a name: ").title()
       # print(people(customer_receipt)
      #  wait()
​
    
​
#TODO: save lists before exit
​
    if user_selection == EXIT_ARG:
        print("Goodbye!")
        exit()
​
    else: 
        print(f'"{user_selection}" is not an option.')