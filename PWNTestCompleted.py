import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 7 # forward right wheel
pin2 = 11 #backward right wheel
pin3 = 12 #forward left wheel
pin4 = 13 #backward left wheel

GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

#forward
p = GPIO.PWM(pin, 50)
p1 = GPIO.PWM(pin3, 50)
p.start(60)
p1.start(60)
time.sleep(1)

# Stopping the GPIOs == GPIO.output(pin, False)
p.start(0)
p1.start(0)

#Backwards
q= GPIO.PWM(pin2, 50)
q1= GPIO.PWM(pin4, 50)
q.start(60)
q1.start(60)
time.sleep(1)

q.start(0)
q1.start(0)

print("test completed!")

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
