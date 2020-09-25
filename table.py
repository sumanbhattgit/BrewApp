def print_table(title, data): # title  ("PEOPLE" or "DRINKS") data: (people or drinks) 
    width = get_table_width(title, data) # width of the table depends on the title and data
    print_header(title, width)  # print table which is defined in the (second) def function
    for item in data:   #for the print_table function the item (name or drink) in the data (people or drinks)
        print(f"| {item}" +  (" " *(width-len(item) - 2) + " |")) # this is purely for the formatting. width of the table - the length of a name/drink 
    print_separator(width)   #this is defined in another def function

def print_header(title, width): #this gets called by print_table()
    print_separator(width)  #==============================
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