# Libraries for GeoJSON, MySQL and data visualization
import geopandas as gpd
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt


# Opening a connection to the database
cnx = mysql.connector.connect(user="root", password="M0m0c0f0", database="pib")

with cnx.cursor() as cursor:
    query = "SELECT id, name, state_code, ST_AsText(geom) as geom FROM cities WHERE state_code = 'SP'"
    df = pd.read_sql(query, cnx)


# Closing the connection
cnx.close()