# import pyinputplus as pyip
# response = pyip.inputInt('Enter your age: ', min=1)
# print(response)

# input_name_title = "Suman"
# input_last_name_title = " Bhatt"
# print(f"{input_name_title}{input_last_name_title} has been added to the list.")


# def user_input(selection_message):
#     return input(f"{selection_message} \n") # return function for the def to return the input

# input_drink = user_input("Enter a drink: \n")
# input_drink_title = input_drink.title()
# if input_drink == "":
#     print("No name entered")
#     wait()

# input_category = user_input("Enter a category: Coffee or Cocktails or Wine or Soft Drinks \n")
# input_category_title = input_category.title()
# if input_category == "":
#     print("No name entered")
#     wait()

# input_age_limit = user_input("Does it have alcohol: Yes or No \n")
# if input_age_limit == "":
#     print("Enter Yes or No")
#     wait()
#     if input_age_limit.lower() in {"y","yes"}:
#         age_limit = 0 
#     if input_age_limit.lower() in {"n","no"}:
#         age_limit = 1 

a = input('How much is 1 share in that company? ')

while a == None:
    print ("You need to write a number!\n")
    a = input('How much is 1 share in that company? ')