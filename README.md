# server-rack-climate-tracker
Project For Arduino, tracking a temperature and humidity sensor inside of my homelab server rack, to make sure that it isn't getting too hot!

# Hardware
- 1 Arduino Uno R3
- 1 DHT11 Temperature and Humidity Sensor

# docs
The docs folder currently contains the schema for the MySQL Database that will be holding the information gathered by the arduino.

# Plans
One of my server rack computers will host my Database Server along with a simple web-app for viewing my recorded data. 
The data will be visible in tabular form, or a chart can be generated based on a time frame. 
Eventually I would like to have a USB computer fan mounted to the sever rack, and ramp up/down in speed depending on the recorded temperature. 

