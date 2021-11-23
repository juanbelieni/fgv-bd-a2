# Importting the necessary libraries
import mysql.connector

# Opening a connection to the database
cnx = mysql.connector.connect(user="root", password="M0m0c0f0", autocommit=True)

# Opening pib.sql file and executing the commands
cursor = cnx.cursor()
with open("pib.sql") as sql_file:
    sql_commands = sql_file.read()
    cursor.execute(sql_commands)

# Closing the connection
cnx.close()