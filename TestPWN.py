import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 7
pin2 = 11

GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

p = GPIO.PWM(pin, 50)
p.start(60)
time.sleep(1)
#GPIO.output(pin, False)
p.start(0)

q= GPIO.PWM(pin2, 50)
q.start(60)
time.sleep(1)



#for  i in range(40, 60, 10): #frequency pulse per second
#    for j in range(40,60,10): #duty cycle
#        p = GPIO.PWM(pin, i)
#        p.start(j)
#        print("duty cycle", j)
#        print("frquency=", i)
#        time.sleep(2)
#'''

GPIO.output(pin,False)
GPIO.output(pin2,False)
GPIO.cleanup()
