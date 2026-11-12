import json
import time
import mysql.connector

from flask import Flask, jsonify

app = Flask(__name__)

time.sleep(5)

# App endpoint
# Should simply just dump the database records onto a webpage.
@app.route('/')
def rack_data():
    try:
        # connect to the DB
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="PASSWORD", # Password ommited for obvious reasons
            database="climate_monitor"
        )
        cursor = db.cursor(dictionary=True)
		
        cursor.execute("SELECT * FROM Temperature_and_Humidity WHERE DATE(recorded_at) = CURDATE()")
        rows = cursor.fetchall()

        # Free the resources
        cursor.close()
        db.close()

        return jsonify(rows)
    except Exception as e:
        # this error should print to the page instead of crashing
        return jsonify({"error": str(e)}), 500
        
# set host to 0.0.0.0 so I can access it
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
