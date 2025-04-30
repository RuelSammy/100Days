#Raspberry pi code
from machine import Pin
import time

led = Pin(15, Pin.OUT)  # Use GPIO 15

while True:
    led.toggle()       # Switch LED on/off
    time.sleep(1)      # Wait 1 second
