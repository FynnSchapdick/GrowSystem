#include <LiquidCrystal.h>
const int rs = 13, en = 12, d4 = 7, d5 = 6, d6 = 5, d7 = 4;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int transistor = 52;
long SensorWert = 0;
void setup() {

  Serial.begin(9600); //Initialisiert den Serial-Monitor
  pinMode(transistor, OUTPUT); //Initialisiert den Pin und setzt ihn als OUT
  lcd.begin(16, 2); //Initialisiert die Spalten und Reihen des LCD's
  //lcd.print("Value:");



}

void loop() {
  if (Serial.available()) {
    SensorWert = getAvgSensorWert();
    Serial.print("Feuchtigkeitswert: ");
    Serial.println(SensorWert,DEC);
    showValue();
    delay(5000);//5 Sekunden, nachher 1800000
  }
}
int getAvgSensorWert() {
  digitalWrite(transistor, HIGH); //Sensor an!
  delay(2);

  long avg = 0;
  for (int i = 1; i <= 100; i++) {
    int messwert = analogRead(A0);
    avg = avg + messwert;
  }
  digitalWrite(transistor, LOW); //Sensor aus!
  return avg = avg / 100;


}
void showValue() {
  lcd.clear();
  lcd.print("F-Wert:");
  lcd.setCursor(0, 1); //Setzt den Cursor auf Spalte 0, Zeile 1
  lcd.print(SensorWert);



}

