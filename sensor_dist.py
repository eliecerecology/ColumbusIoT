import RPi.GPIO as GPIO
import time

def distance():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.OUT) # 0 is output
    GPIO.setup(38, GPIO.IN) # 1 input

    GPIO.output(37, False)
    while GPIO.input(38) == 0:
        nosig = time.time()

    while GPIO.input(38) == 1:
        sig = time.time()

    tl = sig - nosig

    distance = tl / 0.000058
   
        
    return distance

print(distance())
GPIO.cleanup()
