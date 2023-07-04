
#include <SPI.h>
#include <SD.h>
#include <dht11.h>
//#include <DFRobot_DHT11.h>
dht11 DHT;

//humidity and temp sens pin
#define DHTPIN 3
//mositure sens pin
int M0 =0;
int M1 =1;
int M2 =2;


//declare file variables
//moisture sensor
File myFile0;
//humidity and temp
File myFile1;
 //Time increment in milliseconds to be used later in delay
  int increment = 5000;

void setup() {
  //HT.begin();
  // Open serial communications and wait for port to open:
Serial.begin(115200);
  pinMode(M0, INPUT);
  pinMode(M1, INPUT);
  pinMode(M2, INPUT);
  pinMode(DHTPIN,INPUT);
  ///SETUP SD CARD FRO WRITING

while (!Serial) {
  ;  // wait for serial port to connect. Needed for native USB port only
}
Serial.print("Initializing SD card...");
if (!SD.begin(10)) {
  Serial.println("initialization failed!");
  //while (1)
    ;
}
Serial.println("initialization done.");
// open the file. note that only one file can be open at a time,
// so you have to close this one before opening another.
myFile0 = SD.open("Moist.csv", FILE_WRITE);
myFile1 = SD.open("HumTemp.csv", FILE_WRITE);
// if the file opened okay, write to it:
if (myFile0) {
  Serial.print("Writing to file 0...");
   myFile0.println("M0,M1,M2");
   myFile0.flush();
} else {
  // if the file didn't open, print an error:
  Serial.println("error opening file 0");
}
if (myFile1) {
  Serial.print("Writing to file 1...");
  //print headings for temp and humidity
  myFile1.println("Humidity,Temperature");
  myFile1.flush();
} else {
  // if the file didn't open, print an error:
  Serial.println("error opening file 1");
}
}

void loop() {
  //Moisture sensore readings
//intitiate variable TO STORE reading
  float val0;
  float val1;
  float val2;
val0 = analogRead(M0); //connect sensor to Analog 0
val1 = analogRead(M1); //connect sensor to Analog 1
val2 = analogRead(M2); //connect sensor to Analog 2
Serial.print("Moisture Sensor 0 Value :");
Serial.println(val0);
Serial.print("Moisture Sensor 1 Value :");
Serial.println(val1);
Serial.print("Moisture Sensor 2 Value :");
Serial.println(val2);
//print to file
myFile0.print(val0);
myFile0.print(",");
myFile0.print(val1);
myFile0.print(",");
myFile0.print(val2);
myFile0.println();
//ensure data is saved w/o closing
myFile0.flush();
//Humidity and temp readings
int chk;
Serial.print("DHT being read, \t");
chk = DHT.read(DHTPIN);    // READ DATA
switch (chk){
  case DHTLIB_OK:  
              Serial.print("OK,\t"); 
              break;
  case DHTLIB_ERROR_CHECKSUM: 
              Serial.print("Checksum error,\t"); 
              break;
  case DHTLIB_ERROR_TIMEOUT: 
              Serial.print("Time out error,\t"); 
              break;
  default: 
              Serial.print("Unknown error,\t"); 
              break;
}

//Print to serial
Serial.print("Humidity Value :");
Serial.println(DHT.humidity);
Serial.print("Temperature Value :");
Serial.println(DHT.temperature);
// Write DATA
//print to file
myFile1.print(DHT.humidity);
myFile1.print(",");
myFile1.print(DHT.temperature);
myFile1.println();
//ensure data is saved w/o closing
myFile1.flush();
delay(increment);
}