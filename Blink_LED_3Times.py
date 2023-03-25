import RPi.GPIO as GPIO 
from Time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.Low)
counter = 3

while counter < 3:
    GPIO.output(8, GPIO.HIGH)
    sleep(100)
    GPIO.output(8, GPIO.Low)
    counter = counter + 1

