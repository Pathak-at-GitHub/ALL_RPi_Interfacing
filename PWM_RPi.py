import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
PWM_Pin = GPIO.PWM(8, PWM_OUTPUT)
PWM_Pin.start(0)

while True:
    for i in range(0, 10, 1):
        PWM_Pin.changeDutyCycle(i)
        sleep(10)
    sleep(100)
    for i in range(10, 0, -1):
        PWM_Pin.changeDutyCycle(i)
        sleep(10)
    sleep(100)

