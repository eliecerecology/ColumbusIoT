import RPi.GPIO as GPIO
import time
import Tkinter as tk 


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pin = 7 # forward right wheel
pin2 = 11 #backward right wheel
pin3 = 12 #forward left wheel
pin4 = 13 #backward left wheel

def init():
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

#def key_input(event):

forward(2)
backward(2)
turn_right(2)
turn_left(2)

def key_input(event):
	init()
	print 'Key:', event.char
	key_press = event.char
	sleep.time = 0.030
	
	if key_press.lower() == "K_UP":
	    forward(tf)
	elif key_press.lower() == "K_DOWN":
		backward(tf)
	elif key_press.lower() == "K_RIGHT":
		turn_right(tf)
	elif key_press.lower() == "K_LEFT":
		turn_left(tf)
		
command = tk.TK
command.blind('<KeyPress>'>, key_input)
command.mainloop

print("test completed!")

#for  i in range(40, 60, 10): #frequency pulse per second
#    for j in range(40,60,10): #duty cycle
#        p = GPIO.PWM(pin, i)
#        p.start(j)
#        print("duty cycle", j)
#        print("frquency=", i)
#        time.sleep(2)
#'''



