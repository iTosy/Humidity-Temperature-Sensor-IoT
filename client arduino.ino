/*
    This sketch sends a string to a TCP server, and prints a one-line response.
    You must run a TCP server in your local network.
    For example, on Linux you can use this command: nc -v -l 3000
*/

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

#ifndef STASSID
#define STASSID "your-ssid"
#define STAPSK  "your-password"
#endif

int outputpin= A0;
const char* ssid     = "2C";
const char* password = "12348765";

const char* host = "192.168.43.173";
const uint16_t port = 40404;
  WiFiClient client;

ESP8266WiFiMulti WiFiMulti;

void setup() {
  Serial.begin(9600);

  // We start by connecting to a WiFi network
  WiFi.mode(WIFI_STA);
  WiFiMulti.addAP(ssid, password);

  Serial.println();
  Serial.println();
  Serial.print("Wait for WiFi... ");

  while (WiFiMulti.run() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
while(!client.connect(host, port)){
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  // Use WiFiClient class to create TCP connections

  
    Serial.println("connection failed");
    Serial.println("wait 5 sec...");
    delay(5000);
    
  
}
  delay(500);
}


void loop() {
  

  // This will send the request to the server
  client.println("hello from ESP8266");
  int analogValue = analogRead(outputpin);
  float millivolts = (analogValue/1024.0) * 3300; //3300 is the voltage provided by NodeMCU
  float celsius = millivolts/10;
  Serial.print("in DegreeC=   ");
  Serial.println(celsius);
  client.println(celsius);
 


  delay(5000);
}

