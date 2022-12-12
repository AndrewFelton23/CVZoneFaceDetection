#include <cvzone.h>

SerialData serialData(3, 1);    //(numVlasRecieved, DigitsPerValRec)
int ValsRec[3];                 //Initialize array recieved

int red = 8;                    //Red is connected on pin 8
int green = 9;                  //Green is connected on pin 9
int blue = 10;                  //Blue is connected on pin 10

void setup() {
  // put your setup code here, to run once:
  serialData.begin();
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(ValsRec);      
 
  digitalWrite(red, ValsRec[0]);
  digitalWrite(green, ValsRec[1]);
  digitalWrite(blue, ValsRec[2]);
  
}
