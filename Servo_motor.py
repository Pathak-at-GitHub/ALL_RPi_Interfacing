import RPi.GPIO as GPIO
from time import sleep
control = [5,5.5,6,6.5,7]
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
pwm = GPIO.PWM(8, 1000)
pwm.start(0)

try:
    while True:
        for i in range(len(control)):
            pwm.changeDutyCycle(control[i])
            print("servo moving")
            sleep(10)
        sleep(10)
        for i in range(10, 0, -1):
            pwm.changeDutyCycle(control[i])
            print("reverse Direction")
            sleep(10)
        sleep(10)