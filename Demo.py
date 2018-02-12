import RPi.GPIO as GPIO
import time
import math
import pygame as pg
from pygame.math import Vector2
from i2clibraries import i2c_hmc5883l
 
#HC-SR04 distance
from sensor_distance import distance 
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




#Start
hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1) #choosing which i2c port to use, RPi2 model B uses port 1
hmc5883l.setContinuousMode()
hmc5883l.setDeclination(0,6) #in brakets (degrees, minute)
i = hmc5883l.getHeading() #here we obtain the angle from north
g = (i*math.pi/180)
obst = distance()
print("obstacle at" , obst, "located at", g, "from north")

turn_right(3)
i = hmc5883l.getHeading() #here we obtain the angle from north
g = (i*math.pi/180)
obst = distance()
print("obstacle at" , obst, "located at", g, "from north")

'''
forward(1)
i = hmc5883l.getHeading() #here we obtain the angle from north
g = (i*math.pi/180)
obst = distance()
print("obstacle at" , obst, "located at", g, "from north")
backward(1)
i = hmc5883l.getHeading() #here we obtain the angle from north
g = (i*math.pi/180)
obst = distance()
print("obstacle at" , obst, "located at", g, "from north")

turn_right(1)
turn_left(1)



#for  i in range(40, 60, 10): #frequency pulse per second
#    for j in range(40,60,10): #duty cycle
#        p = GPIO.PWM(pin, i)
#        p.start(j)
#        print("duty cycle", j)
#        print("frquency=", i)
#        time.sleep(2)
#'''


