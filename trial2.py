#Use of function and loop
import sys
args = sys.argv
#prints arguments and no. of arguments
print(args)
print(len(args), "\n")


#Defining the names
people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]

#defines expected commands
GET_PEOPLE = "get-people"
GET_DRINKS = "get-drinks"

title = "people"
#Asked to write the code in a particular format

separator = "+================================+"

def banner(x):
    print(separator)
    print(f"| {x.upper()}" + " " *(len(separator) - len(x))+ "|")
    print(separator)
def table(y):
    for item in y:
        print(f"| {item}" + (" " *(len(separator) - len(item)))+ "|")
    print(separator)    
#prints lists if expected command put in, exception if IndexError comes up due to lack of command
try:
    command = args[1]
    #makes sure user only puts in 1 command at a time
    if len(args[1]) < 2:
        print("I can only do one thing at a time")
        exit()
    elif command == GET_PEOPLE:
        banner("names")
        table(people)              
    elif command == GET_DRINKS:
        banner("drinks")
        table(drinks)
    elif command == GET_PEOPLE and command == GET_DRINKS:
        banner("names")
        table(people)
        banner("drinks")
        table(drinks)
    else:
        print(f"{command} is not a valid command.")
except IndexError:
    print("Give me something to work with")

















# def print_outline():
#     print("=" *22 )
# def print_header(title):
#     print("| " + title.upper() + "  |")
# def print_outline():
#     print("=" *22 )
# if args[1] == "get_people":
#     for name in people:
#         print("| " + name + "               |")    
# print("=" *22 )

# def print_row(row):
#     print("| " + row)+ "  |") 
# def print_outline():
#     print("+==============") 





 

# people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
# drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"] 

# print_online()
# print header("people")





# if len(args) > 2:
#     print("Far too many command!")
#     exit()
# elif len(args) < 2: 
#     print("Don't know!")   
# elif len(args) == 2:
#     command = args[1]
#     for names in people:
#         print(person)

#     command = args[2]
#     for drink in drinks:
#         print(drink)    
# else:
#     print("I am struggling to understand you!")


