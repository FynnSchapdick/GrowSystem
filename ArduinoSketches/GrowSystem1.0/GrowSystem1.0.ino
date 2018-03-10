#include <DS3231.h>
#include <dht.h> //Importing lib for DHT11
#include <LiquidCrystal.h> //Importing lib for LCDScreen

//Light
int lo1 = 3;
bool lo1_isOn = false;

//LCD
const int rs = 13, en = 12, d4 = 7, d5 = 6, d6 = 5, d7 = 4; //Pins for LCD on arduino
LiquidCrystal lcd(rs, en, d4, d5, d6, d7); //Object lcd initialize

//Real-Time-Clock
DS3231  rtc(SDA, SCL);

//Light Out
int lo1 = 50;
bool lo1_isOn = False;


//Moisture Sensor
int m1_control = 52; //Pin for the transistor on arduino
int m1_sensor = A0; // Pin for the moisture sensor on arduino
int m1_value = 0; //Moisture value

// DHT Sensor
dht DHT; //Object dht initialize
float t_value = 0.0; //Temperature value
float h_value = 0.0; //Humidity value
#define DHT11_PIN 3 //Pin for the dht sensor on arduino

// Light Photoresistor
int l1_sensor = A1; //Pin for the lightphotoresistor on arduino
int l1_value = 0; //Lightphotoresistor value

// Serial Data from Pi
const byte numChars = 32; //Number of Chars, we want to recieve
char receivedChars[numChars]; //Array to store the received data
boolean newData = false;

void setup() {
  Serial.begin(9600); //Initialize the serial monitor
  lcd.begin(16, 2); //Initialize Colums(16), Initialize Rows(2)
  rtc.begin(); //Initalize Real-Time-Clock object
  //rtc.setDate(11, 02, 2018);
  //rtc.setTime(4, 33, 0);
  Serial.println("-------GrowSystem vers:1.0---------");
  Serial.println("-----------------------------------");
}

void loop() {
  recvWithEndMarker();
  showNewData();
  command();



  if (Serial.available()) {
    Serial.println("Start");
<<<<<<< HEAD

=======
    getM1Value();
    getDhtValue();
    getLightValue();
    getTimeStamp();
    setLight();
>>>>>>> branch 'master' of https://github.com/jayjah/growSystem.git
    Serial.println("End");
    Serial.println("-----------------------------------");
    Serial.println("    Data got. Finishes the loop    ");
    Serial.println("-----------------------------------");

    delay(20000);
  }
}
void command() {
  char water1on[] = "water1on";
  char light1on[] = "light1on";
  char water1off[] = "water1off";
  char light1off[] = "light1off";
  char values[] = "values";
  switch (receivedChars) {
    case water1on:
      //turn waterpump1 on
      break;
    case water1off:
      //turn waterpump1 off
      break;
    case light1on:
      //turn light1 on
      break;
    case light1off:
      //turn light1 off
      break;
    case values:
      //get Values
      break;
    default:
    break;
  }


}
void recvWithEndMarker() {
  static byte ndx = 0;
  char endMarker = '\n';
  char rc;

  // if (Serial.available() > 0) {
  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();

    if (rc != endMarker) {
      receivedChars[ndx] = rc;
      ndx++;
      if (ndx >= numChars) {
        ndx = numChars - 1;
      }
    }
    else {
      receivedChars[ndx] = '\0'; // terminate the string
      ndx = 0;
      newData = true;
    }
  }
}
void showNewData() {
  if (newData == true) {
    Serial.print("in process... ");
    Serial.println(receivedChars);
    newData = false;
  }
}
void setLightOn() {
  digitalWrite(lo1, HIGH);
  lo1_isOn = true;

}
void setLightOff() {
  digitalWrite(lo1, LOW);
  lo1_isOn = false;

}
void getM1Value() {
  digitalWrite(m1_control, HIGH); //Sensor on!
  delay(2);
  long avg = 0;
  for (int i = 1; i <= 100; i++) {

    int value = analogRead(m1_sensor);
    avg = avg + value;
  }
  digitalWrite(m1_control, LOW); //Sensor off!
  m1_value = avg / 100;
  Serial.print("m1 ");
  Serial.print(m1_value);
  Serial.print(" ");
}
void getDhtValue() {
  int chk = DHT.read11(DHT11_PIN);
  t_value = DHT.temperature / 100;
  h_value = DHT.humidity / 100;
  Serial.print("t1 ");
  Serial.print(t_value);
  Serial.print(" ");
  Serial.print("h1 ");
  Serial.print(h_value);
  Serial.print(" ");
  delay(2);
}
void getLightValue() {
  l1_value = analogRead(l1_sensor);
  Serial.print("l1 ");
  Serial.print(l1_value);
  Serial.print(" ");
  delay(2);
}
void M1onLCD() {
  lcd.clear();
  lcd.print("M1 ");
  lcd.setCursor(0, 1); //Sets Cursor on colum "0", row "1"
  lcd.print(m1_value);
  delay(5000);
}
void DhtonLCD() {
  lcd.clear();
  lcd.print("T1:");
  lcd.setCursor(3, 0); //Sets the cursor on colum "0" , row "1"
  lcd.print(t_value);
  lcd.setCursor(0, 1);
  lcd.print("H1:");
  lcd.setCursor(3, 1);
  lcd.print(h_value);
  delay(5000);
}
void LightonLCD() {
  lcd.clear();
  lcd.print("L1:");
  lcd.setCursor(7, 0); //Sets the cursor on colum "0", row "1"
  lcd.print(l1_value);
  delay(5000);
}
void getTimeStamp() {
  Serial.print("time ");
  Serial.print(rtc.getTimeStr());
  Serial.print(" ");
  Serial.print("date ");
  Serial.println(rtc.getDateStr());

}
void TimeonLCD() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Time:  ");
  lcd.print(rtc.getTimeStr());
  lcd.setCursor(0, 1);
  lcd.print("Date: ");
  lcd.print(rtc.getDateStr());
  delay(5000);
}
void setLight() {
  digitalWrite(lo1, HIGH); //Sensor on!
  delay(5000);
  digitalWrite(lo1, LOW); //Sensor off!

  
}

