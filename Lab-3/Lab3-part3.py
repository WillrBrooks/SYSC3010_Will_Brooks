import sqlite3

#connect to database created in part 2
dbconnect = sqlite3.connect("lab3Test.db")

#row_factory = sqlite3.Row so that wew can fetch a column by its name
dbconnect.row_factory = sqlite3.Row;

#create a cursor to work with the database
cursor = dbconnect.cursor();

#using the cursor defined above we can then enter regular sqlite commands to
#be executed

#according to the documentation by default a begin is automatically sent before data is modified
cursor.execute('''INSERT INTO temps VALUES (date('now', '-2 DAY'), time('now'), "greenhouse", 23.1);''')
#commit the change to the database
dbconnect.commit()



#to fetch something from the database
cursor.execute('''SELECT * FROM temps WHERE zone="kitchen"''')

#to print the fetched data
for row in cursor:
	print(row['tdate'], row['ttime'], row['zone'], row['temperature'])

dbconnect.close()
