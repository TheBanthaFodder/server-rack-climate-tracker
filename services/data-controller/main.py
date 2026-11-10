import time
import json
import serial
import mysql.connector

# Helper functions
def getStatus(temp):
	if temp > 24.0:
		return "HOT"
	if temp > 17.5:
		return "COMFORTABLE"
	if temp > 0.0:
		return "COLD"
	return "ERR" # Unlikely to be below freezing

def printLog(temp, humidity, status):
	print(f"Logged: Temp={temp}C, Humidity={humidity}%, Status={status}")


# Main code
time.sleep(5)

# connect to the DB
db = mysql.connector.connect(
	host="db",
	user="root",
	password="PASSWORD", # Password ommited for obvious reasons
	database="climate_monitor"
)
cursor = db.cursor()

ser = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
time.sleep(2)

print("Connected to the Device, and the database!")

while True:
	try:
		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').strip()
			
			data = json.loads(line)
			
			temp = float(data['temp'])
			humidity = float(data['humidity'])
			status = getStatus(temp)

			# TEST 
			print(status)
			sql = "INSERT INTO Temperature_and_Humidity (sensor_id, tempc, humidity, status) VALUES (%s, %s, %s, %s)"
			val = ("Center_HL_Sensor", temp, humidity, status)

			cursor.execute(sql, val)
			db.commit()
			
			printLog(temp, humidity, status)
		
	except Exception as e:
		print(f"Error reading serial or writing to DB {e}")
		time.sleep(2)
