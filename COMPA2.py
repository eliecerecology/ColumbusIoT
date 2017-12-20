from i2clibraries import i2c_hmc5883l
import time

hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1) #choosing which i2c port to use, RPi2 model B uses port 1
hmc5883l.setContinuousMode()
hmc5883l.setDeclination(0,6) #in brakets (degrees, minute)
#hmc5883l.getHeading()
for i in range(1,10):
    i = hmc5883l
    print(i)
    time.sleep(0.5)
#print(hmc5883l)

