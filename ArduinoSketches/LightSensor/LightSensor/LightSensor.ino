#include <LiquidCrystal.h>

const int rs = 13, en = 12, d4 = 7, d5 = 6, d6 = 5, d7 = 4;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int Pin = A1;
int l = 0;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2); //Initialisiert die Spalten und Reihen des LCD's

}

void loop() {
  if (Serial.available()) {
    l = analogRead(Pin);
    Serial.print("Wert:");
    Serial.println(l);
    showValues();
    delay(3000);
  }
}
void showValues() {
  lcd.clear();
  lcd.print("Wert:");
  lcd.setCursor(5, 0); //Setzt den Cursor auf Spalte 0, Zeile 1
  lcd.print(l);
}
