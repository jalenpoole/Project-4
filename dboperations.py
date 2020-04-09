import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bus443',
                                         user='root',
                                         password='Jmasterp2198')
    
    
    insert_query = """INSERT INTO faculty (firstname, lastname, coursename, courselocation) 
                           VALUES 
                           ('Jalen', 'Poole', 'BUS443', 'Nelson Hall') """

    cursor = connection.cursor()
    cursor.execute(insert_query)
    connection.commit()

    select_Query = "select * from faculty into outfile 'output.csv' FIELDS TERMINATED BY ','  OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' FROM faculty
    cursor = connection.cursor()
    cursor.execute(select_Query)
    records = cursor.fetchall()
    
    
    for row in records:
        print("firstname = ", row[0], )
        print("lastname = ", row[1])
        print("coursename  = ", row[2])
        print("courselocation  = ", row[3], "\n")

except Error as e:
    print("Error reading data from table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("Connection is closed")


