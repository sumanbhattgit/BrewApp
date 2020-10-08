import pymysql
from drinkclass import Drink as drink

def read_drink_database():
	connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
	cursor = connection.cursor()

	cursor.execute('SELECT Drink_Name from Drinks') 
	rows = cursor.fetchall()

	drink_list = []

	for row in rows:
		d_name = row[0]
		drink_list.append(d_name)

		# person_dict = {"id": row[0],"fname": row[1], "lname": row[2]}
		# people_list.append(person_dict)
	
	return drink_list

	cursor.close()
	connection.close()

	
    
# if __name__ == "__main__":
	read_drink_database()

	# d_list = read_drink_database()

	# print(d_list)

        
def uploading_drink_to_the_database(Drink_Name, Category, Age_limit, Price):
    connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
    cursor = connection.cursor()

    mysql = "INSERT INTO Drinks (Drink_Name, Category, Age_limit, Price) VALUES ('{}', '{}', {}, {})". format(Drink_Name, Category, Age_limit, Price)
    cursor.execute(mysql)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
	uploading_drink_to_the_database()