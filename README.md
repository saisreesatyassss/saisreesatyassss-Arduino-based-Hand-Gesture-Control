# saisreesatyassss-Arduino-based-Hand-Gesture-Control
# Arduino-Based Hand Gesture Control of Computer

This project aims to control computer functions, such as media playback and volume, using hand gestures. It utilizes an Arduino Uno, ultrasonic sensors, and a laptop to enable gesture-based interaction with the computer.

## Abstract
The project explores the concept of Human Machine Interface (HMI) using hand gestures as a means of communication between the user and the computer. Instead of traditional input devices like keyboards and mice, hand gestures are used to control various functions of the computer. The Arduino Uno captures the hand gestures through ultrasonic sensors, which are then interpreted by the Arduino code. The information is sent to the computer running Python code, which generates virtual keystrokes to control applications like VLC Media Player.

## Introduction
In this era of increasing automation, the interaction between humans and machines has become crucial. Hand gestures have been a significant means of communication since ancient times, even predating language. This project focuses on using hand gestures to control a computer or laptop. Various methods can be employed to capture and recognize human gestures, such as distance measurement, cameras, data gloves, and motion detection.

The project utilizes an Arduino Uno, ultrasonic sensors, and a laptop to enable hand gesture control. Ultrasonic sensors detect the hand gestures and the distance of the hand from the sensors. The Arduino code processes the sensor data and sends relevant keywords to the Windows operating system. In the background, Python code recognizes these keywords and generates virtual keystrokes to control the VLC Media Player application.

## Hardware and Software Used
### Hardware:
- Arduino Uno
- Ultrasonic sensors
- Laptop

### Software:
- Arduino IDE for programming the Arduino Uno
- Python 2.7 for running the Python code
- PyAutoGUI module for generating virtual keystrokes

## Circuit Layout
The ultrasonic sensors are connected to the Arduino Uno, which is then connected to the laptop via USB. The ultrasonic sensors consist of a transmitter and a receiver. The transmitter emits ultrasonic waves, which hit a surface and are then picked up by the receiver. Based on the intensity of the reflected waves, the distance of the object from the sensor is determined. The Arduino code processes this data and sends specific keywords to the Python code running on the laptop.

## Execution of the Program
After setting up the hardware and installing the required software, the Python code is executed. The Python code establishes a serial connection with the Arduino and receives the data. The received data is then processed to generate virtual keystrokes using PyAutoGUI. These keystrokes control the hotkeys of the VLC Media Player, enabling media playback and volume control through hand gestures.

## Algorithms Used
1. The ultrasonic sensors capture the hand gestures and distance.
2. The captured gestures are compared with stored gestures.
3. If a match is found, a specific action is executed by the system.
4. If no match is found, no action is performed.

## Arduino Code
```C++

const int trigger1 = 2; // Trigger pin of the 1st sensor
const int echo1 = 3; // Echo pin of the 1st sensor
const int trigger2 = 4; // Trigger pin of the 2nd sensor
const int echo2 = 5; // Echo pin of the 2nd sensor
long time_taken;
int dist, distL, distR;

void setup() {
  Serial.begin(9600);

  pinMode(trigger1, OUTPUT);
  pinMode(echo1, INPUT);
  pinMode(trigger2, OUTPUT);
  pinMode(echo2, INPUT);
}

void calculate_distance(int trigger, int echo) {
  digitalWrite(trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  time_taken = pulseIn(echo, HIGH);
  dist = time_taken * 0.034 / 2;
  
  if (dist > 50) {
    dist = 50;
  }
}

void loop() {
  calculate_distance(trigger1, echo1);
  distL = dist; // Get distance of left sensor

  calculate_distance(trigger2, echo2);
  distR = dist; // Get distance of right sensor

  // Uncomment for debugging
  /*
  Serial.print("L=");
  Serial.println(distL);
  Serial.print("R=");
  Serial.println(distR);
  */

  // Pause Modes - Hold
  if ((distL > 40 && distR > 40) && (distL < 50 && distR < 50)) {
    Serial.println("Play/Pause");
    delay(500);
  }

  calculate_distance(trigger1, echo1);
  distL = dist;

  calculate_distance(trigger2, echo2);
  distR = dist;

  // Control Modes
  // Lock Left - Control Mode
  if (distL >= 13 && distL <= 17) {
    delay(100); // Hand Hold Time
    calculate_distance(trigger1, echo1);
    distL = dist;

    if (distL >= 13 && distL <= 17) {
      Serial.println("Left Locked");

      while (distL <= 40) {
        calculate_distance(trigger1, echo1);
        distL = dist;

        if (distL < 10) { // Hand pushed in
          Serial.println("Vup");
          delay(300);
        }
        
        if (distL > 20) { // Hand pulled out
          Serial.println("Vdown");
          delay(300);
        }
      }
    }
  }

  // Lock Right - Control Mode
  if (distR >= 13 && distR <= 17) {
    delay(100); // Hand Hold Time
    calculate_distance(trigger2, echo2);
    distR = dist;

    if (distR >= 13 && distR <= 17) {
      Serial.println("Right Locked");

      while (distR <= 40) {
        calculate_distance(trigger2, echo2);
        distR = dist;

        if (distR < 10) { // Right hand pushed in
          Serial.println("Rewind");
          delay(300);
        }
        
        if (distR > 20) { // Right hand pulled out
          Serial.println("Forward");
          delay(300);
        }
      }
    }
  }
  
  delay(200);
}
```

## Python Code
```python
# Python Code for Gesture Control VLC Player

import serial
import time
import pyautogui

ArduinoSerial = serial.Serial('com18', 9600)
time.sleep(2)

while 1:
    incoming = str(ArduinoSerial.readline())
    print(incoming)

    if 'Play/Pause' in incoming:
        pyautogui.typewrite(['space'], 0.2)

    if 'Rewind' in incoming:
        pyautogui

.hotkey('ctrl', 'left')

    if 'Forward' in incoming:
        pyautogui.hotkey('ctrl', 'right')

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    if 'Vdown' in incoming:
        pyautogui.hotkey('ctrl', 'up')

    incoming = ""
```

## Conclusion
The Arduino-based hand gesture control of a computer provides an alternative way to interact with computers using simple hand gestures. It reduces the reliance on traditional input devices and increases interactivity. By capturing and interpreting hand gestures, the system can control media playback and volume. This project demonstrates the potential of gesture-based interfaces for human-machine interaction.

## References
- [Instructables: PC Apps Control Using Arduino](https://www.instructables.com/PC-Apps-Control-Using-Arduino/)
- [Circuit Digest: Control Your Computer with Hand Gestures](https://circuitdigest.com/microcontroller-projects/control-your-computer-with-hand-gestures)
