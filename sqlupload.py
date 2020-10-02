# import pymysql
# def read_database():
# 	connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app")
# 	cursor = connection.cursor()
    
# 	# args = ("Hannah", "Mocha")
# 	cursor.execute("SELECT first_name, surname, age, favourite_drink from PERSON") 
# 	# connection.commit()
# 	rows = cursor.fetchall()

# 	for row in rows:
# 		print(row)

# 	cursor.close()
# 	connection.close()

# if __name__ == "__main__":

# 	read_database()

import csv
File_Path = 'C:/Users/suman/Desktop/BrewApp/user_sample.csv'

def load_csv_file(path):
    data = []
    try:
        with open(path, "r") as file:
            file_reader = csv.reader(file, delimiter = ",", quoting=csv.QUOTE_ALL)
            for line in file_reader:
                if not line and line == "":
                    continue
                if line == "\n":
                    continue
                data.append(line[1])
        print(data)
        for i in data:
            print(i.title())
            return(i.title())
    except FileNotFoundError:
        print(f"No file an be found at path : {path}")
        exit()
    except Exception as e:
        print(f"Unable to load data from {path} with error: {str(e)}")
    except ValueError as ve:
        print(f"Unable to load data from {path} with error: {str(ve)}")

load_csv_file(File_Path)
