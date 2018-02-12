import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)

# motors
pin = 7 # forward right wheel
pin2 = 11 #backward right wheel
pin3 = 12 #forward left wheel
pin4 = 13 #backward left wheel

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    GPIO.setup(pin4, GPIO.OUT)

def forward(tf):
    init()
    p = GPIO.PWM(pin, 50)
    p1 = GPIO.PWM(pin3, 50)
    p.start(60)
    p1.start(60)
    time.sleep(tf)
    p.start(0)
    p1.start(0)
    GPIO.cleanup()

def backward(tf):
    init()
    q= GPIO.PWM(pin2, 50)
    q1= GPIO.PWM(pin4, 50)
    q.start(60)
    q1.start(60)
    time.sleep(tf)
    q.start(0)
    q1.start(0)
    GPIO.cleanup()


def turn_right(tf):
    init()
    p = GPIO.PWM(pin, 60)
    q1= GPIO.PWM(pin4, 60)
    p.start(80)
    q1.start(80)
    time.sleep(tf)
    p.start(0)
    q1.start(0)
    GPIO.cleanup()

def turn_left(tf):
    init()
    p1 = GPIO.PWM(pin3, 60)
    q1= GPIO.PWM(pin2, 60)
    p1.start(80)
    q1.start(80)
    time.sleep(tf)
    p1.start(0)
    q1.start(0)
    GPIO.cleanup()



#def key_input(event):




#for  i in range(40, 60, 10): #frequency pulse per second
#    for j in range(40,60,10): #duty cycle
#        p = GPIO.PWM(pin, i)
#        p.start(j)
#        print("duty cycle", j)
#        print("frquency=", i)
#        time.sleep(2)
#'''



