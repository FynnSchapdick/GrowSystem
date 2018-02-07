#include <LiquidCrystal.h>

const int rs = 13, en = 12, d4 = 7, d5 = 6, d6 = 5, d7 = 4;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int transistor = 52;
long fWert = 0;

void setup() {
  Serial.begin(9600); //Initialisiert den Serial-Monitor
  lcd.begin(16, 2); //Initialisiert die Spalten und Reihen des LCD's

}

void loop() {
  if (Serial.available()) {
    fWert = getAvgSensorWert();
    Serial.print("Feuchtigkeitswert:");
    Serial.println(fWert, DEC);
    showValues();
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
void showValues() {
  lcd.clear();
  lcd.print("F-Wert:");
  lcd.setCursor(0, 1); //Setzt den Cursor auf Spalte 0, Zeile 1
  lcd.print(fWert);
}
