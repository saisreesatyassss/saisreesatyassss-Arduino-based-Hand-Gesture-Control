import serial
import time
import pyautogui
ArduinoSerial=serial.Serial('COM5', 9600, timeout=0.05) 
time.sleep(2)
while 1:
 
         incoming = str (ArduinoSerial.readline())  
         print (incoming)
         if 'Play/Pause' in incoming: pyautogui.typewrite(['space'], 0.2)
         if 'Rewind' in incoming:pyautogui.hotkey('ctrl', 'left')  
         if 'Forward' in incoming: pyautogui.hotkey('ctrl', 'right') 
         if 'Vup' in incoming:pyautogui.hotkey('ctrl', 'down')
         if 'Vdown' in incoming: pyautogui.hotkey('ctrl', 'up')
 


         incoming = "";        
