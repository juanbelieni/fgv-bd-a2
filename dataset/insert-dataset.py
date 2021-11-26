# Importting the necessary libraries
import mysql.connector

# Opening a connection to the database
cnx = mysql.connector.connect(user="root", password="docker", autocommit=True)

# Opening pib.sql file and executing the commands
cursor = cnx.cursor()
with open("dataset/pib.sql") as sql_file:
    sql_commands = sql_file.read()
    cursor.execute(sql_commands)

# Closing the connection
cnx.close()

print("Dataset inserted successfully")
