#include <SoftwareSerial.h>

const int rx = 2;
const int tx = 3;
const int IN1 = 7;
const int IN2 = 8;
const int EN1 = 6;
const int servo1 = 9;
const int servo2 = 10;

String rx_data = "";
String tx_data = "";
int state_flag = 0;

SoftwareSerial swSerial(rx, tx);

void setup() 
{
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(EN1, OUTPUT);

  pinMode(servo1, OUTPUT);
  pinMode(servo2, OUTPUT);

  digitalWrite(IN1, 0);
  digitalWrite(IN2, 0);
  analogWrite(EN1, 0);
  
  Serial.begin(9600);
  swSerial.begin(9600);
}

void loop() 
{  
   if(swSerial.available())
   {
      rx_data = Rec_data();
      
      if (rx_data == "go")
          Serial.println("go");
       
      else if(rx_data == "stop")
         Serial.println("stop");
      
      if(rx_data == "rgrab")
      {
        Serial.println("rgrab");
        swSerial.write("complete\n");  
      }

      else if(rx_data == "fgrab")
      {
        Serial.println("fgrab");
        swSerial.write("complete\n");  
      }
   }
}

String Rec_data()
{
  String data = "";
  data = swSerial.readStringUntil('\n');
  return data;
    
}