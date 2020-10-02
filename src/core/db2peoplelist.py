import pymysql
from personclass import Person as Person

def read_people_database():
	connection = pymysql.connect(host = "localhost", port = 33066, user = "root", password = "password", db = "brew_app", autocommit = True)
	cursor = connection.cursor()
	
	# args = ("Hannah", "Mocha")
	cursor.execute('SELECT PersonID, First_Name, Last_Name from People') 
	rows = cursor.fetchall()

	people_list = []

	for row in rows:
		# print(row)
		# print(row[1])
		first_name = row[1]
		# print(first_name)
		last_name = row[2]
		# print(last_name)

		fullname = " ".join((first_name, last_name))
		people_list.append(fullname)
	
		ID = row[0]
		# person_dict = {"id": row[0],"fname": row[1], "lname": row[2]}
		# people_list.append(person_dict)
	# print(people_list)	
	return people_list

	cursor.close()
	connection.close()


# if __name__ == "__main__":
# 	read_people_database()

	# p_list = read_people_database()

	# print(p_list)
