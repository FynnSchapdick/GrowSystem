#include <dht.h>
#include <LiquidCrystal.h>


const int rs = 13, en = 12, d4 = 7, d5 = 6, d6 = 5, d7 = 4;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
dht DHT;
float t = 0.0;
float h = 0.0;

#define DHT11_PIN 3

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2); //Initialisiert die Spalten und Reihen des LCD's
}

void loop()
{
  if (Serial.available()) {
    int chk = DHT.read11(DHT11_PIN);
    t = DHT.temperature / 100;
    h = DHT.humidity / 100;
    Serial.print("Temperatur: ");
    Serial.println(t, DEC);
    Serial.print("L-Feuchtigkeit: ");
    Serial.println(h, DEC);
    showValues();
    delay(10000);
  }
}
void showValues() {
  lcd.clear();
  lcd.print("T:");
  lcd.setCursor(3, 0); //Setzt den Cursor auf Spalte 0, Zeile 1
  lcd.print(t);
  lcd.setCursor(0, 1);
  lcd.print("H:");
  lcd.setCursor(3, 1);
  lcd.print(h);
}

