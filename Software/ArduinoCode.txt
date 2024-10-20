#include <Arduino_LSM9DS1.h>  // Include the library for the IMU

const int numReadings = 10;  // Number of samples to average
float xReadings[numReadings];  // Array to store X readings
float yReadings[numReadings];  // Array to store Y readings
float totalX = 0, totalY = 0;  // Totals for X and Y readings
float averageX = 0, averageY = 0;  // Averages for X and Y
float lastAverageX = 0, lastAverageY = 0;  // Previous averages
int readIndex = 0;  // Index for reading array
int numSamplesCollected = 0;  // Counter for collected samples
int potPin3 = A0;  // Pin for potentiometer controlling Joint 3
int buttonGripperPin = 2;  // Button pin for gripper control
bool gripperState = LOW;  // Gripper state, LOW for closed, HIGH for open
bool lastButtonState = HIGH;  // Stores the previous state of the button
bool buttonPressed = false;  // Flag to detect when the button is pressed
int lastPotValue3 = 0;  // Store last potentiometer value for Joint 3
unsigned long lastDebounceTime = 0;  // Last time the output pin was toggled
unsigned long debounceDelay = 70;  // The debounce time; increase if the output flickers
int inputThreshold = 50;  // Threshold for filtering input (for potentiometer)
float imuThreshold = 0.1;  // Threshold for IMU filtering

// Timing variables for non-blocking delay
unsigned long previousMillis = 0;
const long interval = 150;  // 50ms delay for sampling

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < numReadings; i++) {
    xReadings[i] = 0;
    yReadings[i] = 0;
  }
  pinMode(potPin3, INPUT);
  pinMode(buttonGripperPin, INPUT_PULLUP);  // Use internal pull-up resistor

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  } else {
    Serial.println("IMU initialized successfully.");
  }
}

void loop() {
  unsigned long currentMillis = millis();

  // Handle IMU and potentiometer updates
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    float x, y, z;

    // IMU data and potentiometer reading
    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(x, y, z);
      totalX -= xReadings[readIndex];
      totalY -= yReadings[readIndex];
      xReadings[readIndex] = x;
      yReadings[readIndex] = y;
      totalX += xReadings[readIndex];
      totalY += yReadings[readIndex];
      readIndex = (readIndex + 1) % numReadings;
      numSamplesCollected++;

      if (numSamplesCollected >= numReadings) {
        averageX = totalX / numReadings;
        averageY = totalY / numReadings;
        int potValue3 = analogRead(potPin3);

        // Apply filtering
        bool imuChanged = (abs(averageX - lastAverageX) > imuThreshold || abs(averageY - lastAverageY) > imuThreshold);
        bool potChanged = (abs(potValue3 - lastPotValue3) > inputThreshold);

        // Only print if IMU or potentiometer values change
        if (imuChanged || potChanged) {
          printData(averageY, averageX, potValue3, gripperState);
          lastAverageX = averageX;
          lastAverageY = averageY;
          lastPotValue3 = potValue3;
        }

        numSamplesCollected = 0;
      }
    }
  }

  // Gripper button handling, independent of IMU and potentiometer
  int buttonReading = digitalRead(buttonGripperPin);

  // Check if the button state has changed (debounced)
  if (buttonReading != lastButtonState) {
    if ((millis() - lastDebounceTime) > debounceDelay) {
      lastDebounceTime = millis();

      if (buttonReading == LOW && !buttonPressed) {
        // Button is pressed, but wasn't pressed before
        buttonPressed = true;
        gripperState = !gripperState;  // Toggle gripper state
        
        // Print the updated gripper state immediately
        printData(averageY, averageX, lastPotValue3, gripperState);  // Use the most recent IMU and potentiometer values
      } else if (buttonReading == HIGH) {
        // Button is released, reset the pressed flag
        buttonPressed = false;
      }
    }
  }

  lastButtonState = buttonReading;  // Update last button state
}

// Function to print the IMU, potentiometer, and gripper state data
void printData(float avgY, float avgX, int potVal, bool gripState) {
  Serial.print(avgY);  // Y-axis for Joint 1
  Serial.print(',');
  Serial.print(avgX);  // X-axis for Joint 2
  Serial.print(',');
  Serial.print(potVal);  // Potentiometer for Joint 3
  Serial.print(',');
  Serial.println(gripState);  // Include gripper state in the same line
}
