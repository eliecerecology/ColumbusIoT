import Adafruit_DHT
import time
als = True
while als: 
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 40) #on gpio pin 4 or pin 7
    if humidity is not None and temperature is not None:
      humidity = round(humidity, 2)
      temperature = round(temperature, 2)
      print 'Temperature = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity)
    else:
      print 'can not connect to the sensor!'
    time.sleep(20) # read data every minute
