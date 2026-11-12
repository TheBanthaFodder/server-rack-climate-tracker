import json
import mysql.connector

from flask import Flask

app = Flask(__name__)

time.sleep(5)

# connect to the DB
db = mysql.connector.connect(
	host="db",
	user="root",
	password="PASSWORD", # Password ommited for obvious reasons
	database="climate_monitor"
)
cursor = db.cursor(dictionary=True)

# App endpoint
# Should simply just dump the database records onto a webpage.
@app.route('/')
def rack_data():
	cursor.execute("SELECT * FROM TEMPERATURE_and_Humidity")
    rows = cursor.fetchall()
    json_data = json.dumps(rows, indent=4, default=str)
    return json_data

if __name__ == '__main__':
	app.run()