import RPi.GPIO as GPIO
import time
#from sensor1 import distance
import math
import matplotlib.pyplot as plt
#Detection of obstacles

angles = [0, 45, 90, 135, 180, 225, 270, 315]
angles = [math.radians(x) for x in angles]
distances = [25, 12, 2]

for angle in angles:
    dist = distance('cm')
    print ('distance at', math.degrees(angle), ':', dist)
    distances.append(dist)
    right(torque)
    time.sleep(1)

angles.append(angles[0])
distances.append(distances[0])
    
ax = plt.subplot(111, polar=True)
ax.plot(angles, distances, color='r', linewidth=3)
ax.grid(True)
plot.show()

