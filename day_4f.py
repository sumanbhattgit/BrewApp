#Dictionaries keys has to be unique. Key:Value

GET_PEOPLE = "1"
GET_DRINKS = "2"
EXIT = "3"
Input_People = "4"
Input_Drinks = "5"
Print = "6"
APP_NAME ="BrIW v0.1" 

#Doc string used to print the menu
Menu = f"""
Welcome to {APP_NAME}!
Please, select an option by entering a number: 
[1] Get all people 
[2] Get all drinks 
[3] Exit
[4] Input People/Drinks
[7] Ask for People/Drinks
"""


#assinging values to our variables
#Good practice to assign all the global value at the start of the script

APP_NAME ="BrIW v0.1"
Count_down = 3 # User has 3 tries to enter a correct option before the programme will quit

#define names
people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]
preference = {}

#Check arguments - Except only one command at a time

#Table output
# Define function to call up parameter later on in the script
def print_table(title, data): # title  ("PEOPLE" or "DRINKS") data: (people or drinks) 
    width = get_table_width(title, data) # width of the table depends on the title and data
    print_header(title, width)  # print table which is defined in the (second) def function
    for item in data:   #for the print_table function the item (name or drink) in the data (people or drinks)
        print(f"| {item}" +  (" " *(width-len(item) - 2) + " |")) # this is purely for the formatting. width of the table - the length of a name/drink 
    print_separator(width)   #this is defined in another def function

def print_header(title, width): #this gets called by print_table()
    print_separator(width)  #==========================
    print(f"| {title}" +  (" " *(width-len(title) - 2) + " |")) # | "PEOPLE" or "DRINKS"  |
    print_separator(width)  #==========================
    
def print_separator(width): #this gets called by print_table() and print_header()
    print("=" * (width + 2)) # this is finding the longest width of our table + 2 to make a table

def get_table_width(title, data): # title  ("PEOPLE" or "DRINKS") data: (people or drinks) 
    longest = len(title)          # length of "PEOPLE"  "DRINKS"
    additional_spacing = 2         

    for item in data:           
        if len(item) > longest:     #checking for longest length of item (suman..//tea..) for our table
            longest = len(item)
    return longest + additional_spacing

def print_menu():
    print(Menu)

def user_input(selection_message):
    return input(f"{selection_message} \n") # return function for the def to return the input

def wait():
    input("Press enter to return to the menu \n")

def input_people(input_message):
    return input(f"{selection_message} \n")


print_menu()
while True:
    user_selection = user_input("Enter your selection or press enter to exit:\n")   # the def function input answers are stored in user_selection variable
    if user_selection == "":
        break

    elif user_selection == "GET_PEOPLE":
        print_table("PEOPLE", people)
        Count_down = 3
    

    elif user_selection == "[2]" or user_selection == "2":
        print_table("DRINKS", drinks)
        Count_down = 3
   
    
    elif user_selection == "[4]" or user_selection == "4":
        input_name = user_input("Input your name: \n")
        input_drink = user_input("Enter your favourite drink: \n")
        input_name_title = input_name.title()
        input_drink_title = input_drink.title()
        people.append(input_name_title)
        drinks.append(input_drink_title)
        print_table("PEOPLE", people)
        print_table("DRINKS", drinks)   
    
    elif user_selection == "[3]" or user_selection == "3":
        break

    elif user_selection == "[7]" or user_selection == "7":
        input_find = user_input("Whose favourite drink would like to know? \n")
        if input_find is people:

        for counter, value in enumerate(drinks,1):
            print (counter, value)

        Count_down = 3

    def id_data(data)    
        for counter, value in enumerate(data,1):
            print (counter, value)

    else:
        Count_down -= 1
        print(f"I don't recognise that, you have {Count_down} tries left. Otherwise, the programme will quit.")
        if Count_down == 0:
            break 
print("Thank you for your input.")




