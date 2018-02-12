import RPi.GPIO as GPIO
import time

def distance():
    GPIO.setmode(GPIO.BOARD)

    ECHO = 38
    TRIG = 37

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG, 0)

    GPIO.setup(ECHO, GPIO.IN)

    time.sleep(0.1)

    #print("measuring..")

    GPIO.output(TRIG,1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()

    t = round((stop - start) * 17000, 2)
    #print(t)
    return t
    GPIO.cleanup()
    #return t

distance()


