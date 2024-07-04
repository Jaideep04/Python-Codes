import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

db = '/content/drive/MyDrive/Datasets/movies.sqlite'
conn = sqlite3.connect(db)
cur = conn.cursor()
# Fetching the data of the Movies table from the Database
cur.execute("SELECT * FROM movies")
# Creating the cursor object
movies = cur.fetchall()
# Displaying the database data
print(movies)