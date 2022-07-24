from datetime import date, datetime
from time import time
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
import hashlib
import pandas as pd
from random import randint, randrange
import sqlite3

app = Flask(__name__)
load_dotenv()

con=sqlite3.connect("crime_mapping.db") #connecting to the database
cursor=con.cursor()

Dataframe = pd.read_csv('static/overall_cases.csv', encoding = "ISO-8859-1")
list_of_columns=list(Dataframe.columns)
for column in list_of_columns:
    final_name=column.lower().replace(" ","_")
    Dataframe.rename(columns={column:final_name}, inplace=True)
Dataframe.to_sql(name='Dataset',con=con,if_exists='replace') # Dataset converted to RDBMS table

con.commit()

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")
