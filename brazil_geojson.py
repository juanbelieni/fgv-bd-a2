# Libraries for GeoJSON, MySQL and data visualization
import geopandas as gpd
import mysql.connector

# Importing Brazil GeoJSON file
brazil = gpd.read_file("brazil_geojson.json")

# Brazil states
states = {
    # North
    "12": "AC",
    "13": "AM",
    "16": "AP",
    "15": "PA",
    "11": "RO",
    "14": "RR",
    "17": "TO",
    # Northeast
    "27": "AL",
    "29": "BA",
    "23": "CE",
    "21": "MA",
    "25": "PB",
    "26": "PE",
    "22": "PI",
    "24": "RN",
    "28": "SE",
    # Southeast
    "32": "ES",
    "31": "MG",
    "33": "RJ",
    "35": "SP",
    # South
    "41": "PR",
    "43": "RS",
    "42": "SC",
    # Center-West
    "53": "DF",
    "52": "GO",
    "51": "MT",
    "50": "MS",
}

# Creating a new column with the state code, based on the first two digits of the id
brazil["state_code"] = brazil["id"].apply(lambda id: states[id[:2]])

# Printing the head of the dataframe
print(brazil.head())

# Opening a connection to the database
cnx = mysql.connector.connect(user="root", password="docker", database="brazil")

# SQL query to insert the dataframe into the database
sql = """
    INSERT INTO cities (id, name, geom, state_code)
    VALUES (%s, %s, ST_GeomFromText(%s), %s)
"""

# Iterating over the dataframe
for index, row in brazil.iterrows():
    # Showing the progress
    print(f"{index}/{brazil.shape[0]}")

    # Creating a tuple with the data
    data = (row["id"], row["name"], row["geometry"].wkt, row["state_code"])

    # Executing the query
    with cnx.cursor() as cursor:
        cursor.execute(sql, data)

# Committing the changes
cnx.commit()

# Closing the connection
cnx.close()
