# CHANGES MADE ON 02.0CT
import os
import csv
from src.core.table import print_table
from src.core.output import save_data, load_preferences, save_preferences, load_list_from_file, print_all_people, print_all_drinks,input_people_to_the_list, input_drinks_to_the_list, set_your_preference, preference_printout, exit_option, print_preferences, output
from src.core.inputs import get_menu_input, user_input, wait, input_people
from src.core.menu import print_main_menu, validate_menu_input, select_option_from_menu
import roundclass

GET_PEOPLE_ARG = 1
GET_DRINKS_ARG = 2
Input_People_ARG = 3
Input_Drinks_ARG = 4
Set_Your_Preference_ARG = 5
Preference_Printout_ARG = 6
EXIT_ARG = 7


#Input helper funcs
#Output helper funcs
## Input helper funcs
#Data persistence helper funcs
#Menu inputs

#Found
def run():
    while True:     
        print_main_menu()
        user_selection = user_input("Enter your selection or press enter to exit:\n")   # the def function input answers are stored in user_selection variable
        if user_selection == "":
            print("You didn't enter anything! Bye")
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

        elif user_selection == "[7]" or user_selection == "7":
            roundclass.round_menu()
                    
        elif user_selection == "[8]" or user_selection == "8":
            exit_option()

        else:
            print(f"I don't recognise that. Please try again later.")
    print(f"Thank you for using {APP_NAME}")

def start():
    load_preferences()
    run()

if __name__ == "__main__":
    start()
