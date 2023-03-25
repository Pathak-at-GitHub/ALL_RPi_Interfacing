import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.semode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(20, GPIO.OUT)
try:
    while True:
        Button_state = GPIO.input(8)
        if Button_state == False:
            print("Buttom pressed")
            sleep(100)
            GPIO.output(20, GPIO.HIGH)
        else:
            print("Buttom not Pressed")
            GPIO.output(20, GPIO.LOW)
            
except:
    GPIO.clesnup()
    
