from src.core.table import print_table
from src.core.inputs import wait
from constant import PEOPLE_FILE_PATH, DRINKS_FILE_PATH, PREFERENCE_FILE_PATH
from src.core.inputs import user_input
from src.core.data_persistence import save_preferences
# from src.core.inputs import get_menu_input, user_input, wait, input_people
# from src.core.data_persistence import save_data, load_data, load_preferences, save_preferences, load_list_from_file

# people = []
# drinks = []
# preference = {}

def output (text):
    print(f"\n{text}")

def print_preferences(data):
    items = []
    for name, drink in data.items():
        items.append(f"{name}: {drink}")
    print_table('Preference', items)

def print_all_people(list_of_people):
    print_table('PEOPLE', list_of_people)
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
