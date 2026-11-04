# Server Climate Project Charter V1.0
## Objective
Continuously keep track of the temperature, and humidity levels inside of a server rack, for monitoring, and ensuring it does not get too hot.
## Deliverables
- Arduino that uses a DHT11 Sensor to read the requireed data, with code that serializes it to a python controller. 
- A python controller that reads the serial input from the arduino, filters out bad output, packages the data and sends it to the MySQL server.
- MySQL server that stores the logged data, with CRUD operations, can be accessed by the contoller.
- Simple Web-App that displays the logged data from the sensor. Accesses the Database using Read-Only Operations.
## Out of Scope (For V1.0)
- Notification System
- More than one sensor / device in the system
- Mobile Application
- Different methods of supported data visualization

## Constraints
- Scheduling: I do not have much time per day to work on this project.

## Stakeholder
- Micah Hurzeler: Project Sponsor, Owner, Project Manager, lead developer.
