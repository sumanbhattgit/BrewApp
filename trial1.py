import sys
args = sys.argv

#prints arguments and no. of arguments
GET_PEOPLE_ARG = "get_people"
GET_DRINKS_ARG = "get_drinks"

#Defining the names
people = ["Suman", "Chloe", "Hannah", "Katie", "Fatou"]
drinks = ["Orange juice", "Tea", "Coffee", "Vodka", "Milk"]

#Asked to write the code in a particular format (Task 2)
while True:
    if args[1] == "get_people":
        print("+=====================+")
        print("|PEOPLE               |")
        print("+=====================+")
        for name in people:
            print(f"| {name}"+ "               |")
        print("+=====================+")
   

    elif args[2] == "get_drinks":
        print("+=====================+")
        print("|DRINKS               |")
        print("+=====================+")
        for drink in drinks:
            print(f"| {drink}" + "              |")
        print("+=====================+")
      

    # elif (args[1] == "get_people" and args[2] == "get_drinks") or (args[2] == "get_people" and args[1] == "get_drinks"):
    #     print("+=====================+")
    #     print("|PEOPLE               |")
    #     print("+=====================+")
    #     for name in people:
    #         print(f"| {name}"+ "               |")
    #     print("+=====================+\n")

    #     print("+=====================+")
    #     print("|DRINKS               |")
    #     print("+=====================+")
    #     for drink in drinks:
    #         print(f"| {drink}" +                "|")
    #     print("+=====================+") 


