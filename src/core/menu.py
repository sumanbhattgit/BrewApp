import os

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

def clear_screen():
    os.system("cls")

def print_main_menu():
    clear_screen()
    print(Menu)

def print_menu(title, data):
    items = []
    for counter, item in enumerate(data, 1): #list number for preference 5
        items.append(f"[{counter}] {item}")
    clear_screen()
    print(f"{title}\n")
    print('\n'.join(items), '\n')

def validate_menu_input(counter_num, data):
    if counter_num < 0 or counter_num > len(data):
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