import RPi.GPIO as GPIO
import time
 


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# motors
pin = 7 # forward right wheel
pin2 = 11 #backward right wheel
pin3 = 12 #forward left wheel
pin4 = 13 #backward left wheel

# Distance sensor HC-SR04
pin5 = 40
pin6 = 26 #Echo receiver, usin resistor 1kOhm



def init():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    GPIO.setup(pin4, GPIO.OUT)

def initDist():
    #Distance sensort pins
    GPIO.setup(pin5, GPIO.OUT)   
    GPIO.setup(pin6, GPIO.IN) #echo

def forward(tf):
    init()
    p = GPIO.PWM(pin, 50)
    p1 = GPIO.PWM(pin3, 50)
    p.start(60)
    p1.start(60)
    time.sleep(tf)
    p.start(0)
    p1.start(0)

def backward(tf):
    init()
    q= GPIO.PWM(pin2, 50)
    q1= GPIO.PWM(pin4, 50)
    q.start(60)
    q1.start(60)
    time.sleep(tf)
    q.start(0)
    q1.start(0)

def turn_right(tf):
    init()
    p = GPIO.PWM(pin, 50)
    q1= GPIO.PWM(pin4, 50)
    p.start(60)
    q1.start(60)
    time.sleep(tf)
    p.start(0)
    q1.start(0)

def turn_left(tf):
    init()
    p1 = GPIO.PWM(pin3, 50)
    q1= GPIO.PWM(pin2, 50)
    p1.start(60)
    q1.start(60)
    time.sleep(tf)
    p1.start(0)
    q1.start(0)

def distance(measure='cm'):
    initDist()
    GPIO.output(pin5, GPIO.OUT)
    while GPIO.input(pin6) == 0:
        nosig = time.time()

    while GPIO.input(pin5) == 1:
        sig = time.time()

    t1 = sig - nosig

    if measure == 'cm':
        distance = t1/0.000058
    elif measure == 'in':
        distance = t1/0.000148
    else:
        print('improper unit choice')
    GPIO.cleanup()
    return distance

print(distance('cm'))











#def key_input(event):

#forward(2)
#backward(2)
#turn_right(2)
#turn_left(2)



#for  i in range(40, 60, 10): #frequency pulse per second
#    for j in range(40,60,10): #duty cycle
#        p = GPIO.PWM(pin, i)
#        p.start(j)
#        print("duty cycle", j)
#        print("frquency=", i)
#        time.sleep(2)
#'''



