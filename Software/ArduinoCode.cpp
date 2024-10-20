#include <Arduino_LSM9DS1.h>

const int antalAvläsningar = 10;  
float xAvläsningar[antalAvläsningar];  
float yAvläsningar[antalAvläsningar];  
float totalX = 0, totalY = 0;  
float medelX = 0, medelY = 0;  
float senasteMedelX = 0, senasteMedelY = 0;  
int läsIndex = 0;  
int antalInsamladeProv = 0;  
int potPin3 = A0;  
int knappGripPin = 2;  
bool gripTillstånd = LOW;  
bool senasteKnappTillstånd = HIGH;  
bool knappTryckt = false;  
int senastePotVärde3 = 0;  
unsigned long senasteDebounceTid = 0;  
unsigned long debounceFördröjning = 70;  
int ingångströskel = 50;  
float imuTröskel = 0.1;  

unsigned long föregåendeMillis = 0;
const long intervall = 150;  

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < antalAvläsningar; i++) {
    xAvläsningar[i] = 0;
    yAvläsningar[i] = 0;
  }
  pinMode(potPin3, INPUT);
  pinMode(knappGripPin, INPUT_PULLUP);  

  if (!IMU.begin()) {
    Serial.println("Misslyckades med att initiera IMU!");
    while (1);
  } else {
    Serial.println("IMU initierad framgångsrikt.");
  }
}

void loop() {
  unsigned long nuvarandeMillis = millis();

  if (nuvarandeMillis - föregåendeMillis >= intervall) {
    föregåendeMillis = nuvarandeMillis;
    float x, y, z;

    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(x, y, z);
      totalX -= xAvläsningar[läsIndex];
      totalY -= yAvläsningar[läsIndex];
      xAvläsningar[läsIndex] = x;
      yAvläsningar[läsIndex] = y;
      totalX += xAvläsningar[läsIndex];
      totalY += yAvläsningar[läsIndex];
      läsIndex = (läsIndex + 1) % antalAvläsningar;
      antalInsamladeProv++;

      if (antalInsamladeProv >= antalAvläsningar) {
        medelX = totalX / antalAvläsningar;
        medelY = totalY / antalAvläsningar;
        int potVärde3 = analogRead(potPin3);

        bool imuÄndrad = (abs(medelX - senasteMedelX) > imuTröskel || abs(medelY - senasteMedelY) > imuTröskel);
        bool potÄndrad = (abs(potVärde3 - senastePotVärde3) > ingångströskel);

        if (imuÄndrad || potÄndrad) {
          skrivData(medelY, medelX, potVärde3, gripTillstånd);
          senasteMedelX = medelX;
          senasteMedelY = medelY;
          senastePotVärde3 = potVärde3;
        }

        antalInsamladeProv = 0;
      }
    }
  }

  int knappAvläsning = digitalRead(knappGripPin);

  if (knappAvläsning != senasteKnappTillstånd) {
    if ((millis() - senasteDebounceTid) > debounceFördröjning) {
      senasteDebounceTid = millis();

      if (knappAvläsning == LOW && !knappTryckt) {
        knappTryckt = true;
        gripTillstånd = !gripTillstånd;  
        skrivData(medelY, medelX, senastePotVärde3, gripTillstånd);  
      } else if (knappAvläsning == HIGH) {
        knappTryckt = false;
      }
    }
  }

  senasteKnappTillstånd = knappAvläsning;  
}

void skrivData(float medelY, float medelX, int potVärde, bool gripTillstånd) {
  Serial.print(medelY);  
  Serial.print(',');
  Serial.print(medelX);  
  Serial.print(',');
  Serial.print(potVärde);  
  Serial.print(',');
  Serial.println(gripTillstånd);  
}
