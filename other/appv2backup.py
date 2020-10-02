import os
import csv
from src.core.table import print_table 

GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2
Input_People_ARG = 3
Input_Drinks_ARG = 4
Set_Your_Preference_ARG = 5
Preference_Printout_ARG = 6
EXIT_ARG = 7

APP_NAME ="BrIW" 
VERSION  = "0.1"

Menu = f"""
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number: 
[1] Get all people 
[2] Get all drinks 
[3] Input People
[4] Input Drinks
[5] Set_Your_Preference
[6] Preference_Printout
[7] Round
[8] Exit
"""
PEOPLE_FILE_PATH = 'C:/Users/suman/Desktop/BrewApp/data/p.csv'
DRINKS_FILE_PATH = 'C:/Users/suman/Desktop/BrewApp/data/d.csv'
PREFERENCE_FILE_PATH = 'C:/Users/suman/Desktop/BrewApp/data/preference_list.csv'

people = []
drinks = []
preference = {}

def clear_screen():
    os.system("cls")

def print_main_menu():
    clear_screen()
    print(Menu)

#Input helper funcs

def get_menu_input(message):
    try:
        return int(input(f"{message} "))
    except ValueError:
        output("Menu items - numbers are the only input I understand")
        wait()
        return False

def user_input(selection_message):
    return input(f"{selection_message} \n") # return function for the def to return the input

def wait():
    input("Press enter to continue \n")

def input_people(input_message):
    return input(f"{selection_message} \n")

#Output helper funcs

def output (text):
    print(f"\n{text}")

def print_preferences(data):
    items = []
    for name, drink in data.items():
        items.append(f"{name}: {drink}")
    print_table('Preference', items)


## Input helper funcs
def print_menu(title, data):
    items = []
    for counter, item in enumerate(data, 1): #list number for preference 5
        items.append(f"[{counter}] {item}")
    clear_screen()
    print(f"{title}\n")
    print('\n'.join(items), '\n')

def validate_menu_input(counter_num, data):
    if counter_num < 0 or counter_num >= len(data):
        print(f'"{counter_num}" is not a valid option from that menu\n')
        wait()
        return False
    return True

    
def select_option_from_menu(message, data):
    print_menu(message, data)
    counter_num = get_menu_input('Enter your selection:')
    if not validate_menu_input(counter_num, data):
        return False
    return data[counter_num - 1]



#Data persistence helper funcs
def load_list_from_file(path):
    data = []
    try:
        with open(path, "r") as file:
            file_reader = csv.reader(file, delimiter = ",", quoting=csv.QUOTE_ALL)
            for line in file_reader:
                if not line and line == "":
                    continue
                if line == "\n":
                    continue
                data.append(line[0])
        print(data)
        return data
    except FileNotFoundError:
        print(f"No file an be found at path : {path}")
        exit()
    except Exception as e:
        print(f"Unable to load data from {path} with error: {str(e)}")
    except ValueError as ve:
        print(f"Unable to load data from {path} with error: {str(ve)}")

def load_preferences(people,drinks):
    try:
        items = load_list_from_file(PREFERENCE_FILE_PATH)
        print(items)
        for item in items:
            print(item)
            person,drink = item.split(":", 1) #### fix this
            if person in people and drink in drinks:
                preference[person] = drink
            else:
                print("Unexpected data returned when loading favourites.")
                print(f"Drink is known: {drink in drinks}")
                print(f"Name is known: {name in people}")
    except ValueError:
        print(f"Unable to load preference list with error")
        
def load_data():    
    for person in load_list_from_file(PEOPLE_FILE_PATH):
        people.append(person)
    for drink in load_list_from_file(DRINKS_FILE_PATH):
        drinks.append(drink)
    load_preferences(people,drinks)

def save_data(path, data):
    try:
        with open(path, 'w', newline = "") as file:
            writer = csv.writer(file,delimiter = ",", quoting=csv.QUOTE_ALL)
            for element in data:
                writer.writerow([element])
    except FileNotFoundError as e:
        print(f'File "{path}" cannot be found')
    except Exception as e:
        print(f'Unable to open file "{path}". Error is "{e}".')

def save_preferences(path,data):
    items = []
    for item in data.items():
        name, drink = item
        items.append(f'{name}:{drink}')
        save_data(PREFERENCE_FILE_PATH, items) 

#Menu inputs
def print_all_people():
    print_table('PEOPLE', people)
    wait() 

def print_all_drinks():
    print_table('DRINKS', drinks)
    wait()

def input_people_to_the_list():
    input_name = user_input("Enter a name: \n")
    if input_name == "":
        print("No name entered")
        wait()
    else:
        input_name_title = input_name.title()
        if input_name_title not in people:
            people.append(input_name_title)
            print(f"{input_name_title} has been added to the list.")
            print_table("PEOPLE", people)
            save_data(PEOPLE_FILE_PATH, people)      
            wait()

def input_drinks_to_the_list():
    input_drink = user_input("Enter a drink: \n")
    if input_drink == "":
        print("No name entered")
        wait()
    else:
        input_drink_title = input_drink.title()
        if input_drink not in drinks:
            drinks.append(input_drink_title)
            print(f"{input_drink_title} has been added.")
            print_table("DRINKS", drinks)
            COUNT_DOWN = 3  
            wait()

def set_your_preference():        
    person = select_option_from_menu('Choose a person', people)
    if not person:
        output(f'{person} is not in the list')
        wait()
    drink = select_option_from_menu(f'Choose a drink for {person}', drinks)
    if not drink:
        wait()
    preference[person] = drink
    print(f"\nThank you - {person}'s favourite drink is now {drink}")
    wait()

def preference_printout():
    print_preferences(preference)
    save_preferences(PREFERENCE_FILE_PATH, preference)
    wait()

def exit_option():
    print('Saving data...')
    save_data(PEOPLE_FILE_PATH, people)
    save_data(DRINKS_FILE_PATH, drinks)
    save_data(PREFERENCE_FILE_PATH, preference)
    save_preferences(PREFERENCE_FILE_PATH, preference)

    print(f"Thank you for using {APP_NAME}")
    exit()
def run():
    while True:
        print_main_menu()
        user_selection = user_input("Enter your selection or press enter to exit:\n")   # the def function input answers are stored in user_selection variable
        if user_selection == "":
            save_data(PEOPLE_FILE_PATH, people)
            save_data(DRINKS_FILE_PATH, drinks)
            save_data(PREFERENCE_FILE_PATH, preference)
            save_preferences(PREFERENCE_FILE_PATH, preference)
            exit()

        elif user_selection == "[1]" or user_selection == "1":
            print_all_people()  

        elif user_selection == "[2]" or user_selection == "2":
            print_all_drinks()

        elif user_selection == "[3]" or user_selection == "3":
            input_people_to_the_list()

        elif user_selection == "[4]" or user_selection == "4":
            input_drinks_to_the_list()

        elif user_selection == "[5]" or user_selection == "5":
            set_your_preference()

        elif user_selection == "[6]" or user_selection == "6":
            preference_printout()

        # elif user_selection == "[7]" or user_selection == "7":
        #     round_printout()
        
    
        elif user_selection == "[8]" or user_selection == "8":
            exit_option()

        else:
            print(f"I don't recognise that. Please try again later.")
    print(f"Thank you for using {APP_NAME}")

def start():
    load_data()
    run()

if __name__ == "__main__":
    start()