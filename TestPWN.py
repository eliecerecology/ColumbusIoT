import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 7

GPIO.setup(pin, GPIO.OUT)


for  i in range(40, 60, 10): #frequency pulse per second
    for j in range(40,60,10):
        p = GPIO.PWM(pin, i)
        p.start(j)
        print("duty cycle", j)
        print("frquency=", i)
        time.sleep(2)
        
     
GPIO.output(pin,False)
GPIO.cleanup()
