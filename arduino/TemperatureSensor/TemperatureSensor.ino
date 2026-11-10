#include <Wire.h>
#include <DHT11.h>

#include <string.h>

#define DHTPIN 2

DHT11 dht11(DHTPIN);

//rgb pins
const int PIN_RED = 5;
const int PIN_GREEN = 6; 
const int PIN_BLUE  = 9;

void setup() {
  //serial
  Serial.begin(9600); // 9600 is the baud rate

  //light
  pinMode(PIN_RED, OUTPUT);
  pinMode(PIN_GREEN, OUTPUT);
  pinMode(PIN_BLUE, OUTPUT);

  delay(1000);

}

void loop() {
  int tempc = 0;
  int hum = 0;

  // Attempt to read temperature and humidity together with error checking
  int result = dht11.readTemperatureHumidity(tempc, hum);

  delay(50);

  if (result == 0) {
    // Success! Convert to Fahrenheit and display
    decideLightColor(tempc);

    //serial print
    sendSerialJSONData(tempc, hum);

    } else {

    changeLightColor(255, 255, 255);

    //serial print
    Serial.print("Sensor Read Failed:");
    Serial.println(DHT11::getErrorString(result));

  }

  // DHT11 needs at least 2 seconds between reads
  delay(30000);
}

void decideLightColor(int tempc){
  if(tempc > 24.0){ //orange for hot About 75f
    changeLightColor(255, 50, 0);
  }
  else if(tempc > 17.5){ //Green for comfortable about 64f
    changeLightColor(0, 255, 0);
  }
  else { //Light blue for cold
    changeLightColor(0, 231, 255);
  }
}

void changeLightColor(int r, int g, int b){
  analogWrite(PIN_RED, r);
  analogWrite(PIN_GREEN, g);
  analogWrite(PIN_BLUE, b);
}


void sendSerialJSONData(int tempc, float humidity){
  Serial.print("{\"temp\" : ");
  Serial.print(tempc);
  Serial.print(", \"humidity\" : ");
  Serial.print(humidity);
  Serial.print("}");
  //Carraige return here?
  Serial.println();
}