#include <DS3231.h>
#include <dht.h> //Importing lib for DHT11
#include <LiquidCrystal.h> //Importing lib for LCDScreen

//LCD
const int rs = 13, en = 12, d4 = 7, d5 = 6, d6 = 5, d7 = 4; //Pins for LCD on arduino
LiquidCrystal lcd(rs, en, d4, d5, d6, d7); //Object lcd initialize

//Real-Time-Clock
DS3231  rtc(SDA, SCL);

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

void setup() {
  Serial.begin(9600); //Initialize the serial monitor
  lcd.begin(16, 2); //Initialize Colums(16), Initialize Rows(2)
  rtc.begin(); //Initalize Real-Time-Clock object
  //rtc.setDate(11, 02, 2018);
  //rtc.setTime(4, 33, 0);
  Serial.println("GrowSystem vers:1.0 Getting data...");
  Serial.println("-----------------------------------");
}

void loop() {
  if (Serial.available()) {
    Serial.println("Start");
    getM1Value();
    getDhtValue();
    getLightValue();
    getTimeStamp();
    Serial.println("End");
    Serial.println("-----------------------------------");
    Serial.println("    Data got. Finishes the loop    ");
    Serial.println("-----------------------------------");
    M1onLCD();
    DhtonLCD();
    LightonLCD();
    TimeonLCD();
    delay(20000);
  }



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

