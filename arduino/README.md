# Arduino Code
The Arduino Code is connected to a DHT11 Sensor, reading temperature and humidity data. The responsibility of the arduino is to read the data, and send it over serial. It does not need to know what is reading the output. The data gets packaged into a JSON format. The arduino also has an indicator light on the breadboard, that changes color based on the comfort level in the server rack.


## JSON
{
    "temp" : float,
    "humidity" : float
}

## LED Color
- `>= 75` is orange, for hot
- `>= 64` is green, for comfortable
- `< 64` is light blue, for cold