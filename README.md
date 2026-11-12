# server-rack-climate-tracker
Project For Arduino, tracking a temperature and humidity sensor inside of my homelab server rack, to make sure that it isn't getting too hot!

# Hardware
- 1 Arduino Uno R3
- 1 DHT11 Temperature and Humidity Sensor

# docs
- The docs folder currently contains the schema for the MySQL Database that will be holding the information gathered by the arduino.
- The final MySQL dump is available for copy `finalizedSchema.sql`
- Initial Project Charter
- DataFlow diagram for webserver, data-controller, and MySQL database

# arduino
Contains a `README.md` and a .ino file to be uploaded to an arduino

# services
- Contains Docker Files: `docker-compose.yml`, `Dockerfile`, `entrypoint.sh`, `requirements.txt`
- Make sure the entrypoint file is executable!
- Contains main.py (data controller) and webapp.py (the web app)
- All of these files are being run in the web app container in the same directory

# Plans
One of my server rack computers will host my Database Server along with a simple web-app for viewing my recorded data. 
The data will be visible in tabular form, or a chart can be generated based on a time frame. 
Eventually I would like to have a USB computer fan mounted to the sever rack, and ramp up/down in speed depending on the recorded temperature. 

# Note
If you wish to replicate this project, make sure you set a common password for the database! These should be in the files:
- `docker-compose.yml`
- `web-app.py`
- `main.py`
