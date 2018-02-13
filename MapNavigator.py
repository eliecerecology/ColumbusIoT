import math
import pygame as pg
from pygame.math import Vector2
from i2clibraries import i2c_hmc5883l
import time
import RPi.GPIO as GPIO
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

pin = 7 # forward right wheel
pin2 = 11 #backward right wheel
pin3 = 12 #forward left wheel
pin4 = 13 #backward left wheel

from PWNTestCompleted import init
from PWNTestCompleted import forward
from PWNTestCompleted import backward
from PWNTestCompleted import turn_right
from PWNTestCompleted import turn_left

#HC-SR04 distance
from sensor_distance import distance 

#Magnetometer
hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1) #choosing which i2c port to use, RPi2 model B uses port 1
hmc5883l.setContinuousMode()
hmc5883l.setDeclination(0,6) #in brakets (degrees, minute)

#i = hmc5883l.getHeading() #here we obtain the angle from north
#g = (i*math.pi/180)
#obst = distance()
#print("obstacle at" , obst, "located at", g, "from north")
time.sleep(5)
class Player(pg.sprite.Sprite):

    def __init__(self, pos=(220, 220)):
        super(Player, self).__init__()
        self.image = pg.Surface((70, 50), pg.SRCALPHA)
        pg.draw.polygon(self.image, (50, 120, 180), ((0, 0), (0, 50), (70, 25)))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.position = Vector2(pos)
        self.direction = Vector2(1, 0)  # A unit vector pointing rightward.
        self.speed = 0
        self.angle_speed = 0
        self.angle = 0

    def update(self):
        if self.angle_speed != 0:
            # Rotate the direction vector and then the image.
            self.direction.rotate_ip(self.angle_speed) #esta mierda
            self.angle += self.angle_speed
            self.image = pg.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        # Update the position vector and the rect.
        
        self.position += self.direction*-self.speed #this controls postion ACA HABIA UN MENOS
        self.rect.center = self.position 


def main():
    pg.init()

    myfont = pg.font.SysFont("monospace", 15)
    # render text
    label = myfont.render("ARENA", 1, (255,255,0))
        
    screen = pg.display.set_mode((700, 700)) #arena
    screen.blit(label, (100, 100))
    player = Player((350, 350)) #starting postion
    playersprite = pg.sprite.RenderPlain((player))

    clock = pg.time.Clock()
    done = False
    angle = [hmc5883l.getHeading()*3.14/180]
    dista = []
    t = []
    #j = 0
    #while not done:
    for k in range(0, 2):    
        for j in range(0, 70): 
                clock.tick(60)
                turn_left(0.1)
                player.angle_speed = angle[j]#-0.5
                print(hmc5883l.getHeading(), "angles")
                print(hmc5883l.getHeading()*3.14/180, "radians")
                print(distance(), "distance")
                angle.append(hmc5883l.getHeading()*3.14/180 + 4.4)
                dista.append(distance())
                t.append(j)
                time.sleep(0.2)
                playersprite.update()
                screen.fill((30, 30, 30))
                playersprite.draw(screen)
                pg.display.flip()
                
        
        print(max(dista), " = max distance", max(angle), "=max angle")
        print(dista.index(max(dista)))
        print(dista)
        
        turn_left(0.1*dista.index(max(dista)))
        player.angle_speed = angle[dista.index(max(dista))]#-0.5
        time.sleep(1)
        forward(1)
        player.speed = angle[j]
        time.sleep(5)
        angle = [hmc5883l.getHeading()*3.14/180]
        dista = []
        t = []
        
        playersprite.update()
        screen.fill((30, 30, 30))
        playersprite.draw(screen)
        pg.display.flip()
        
            
        '''MANUAL CONTROL
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        player.speed = 0.3 #SOLO VELOCITY
                        forward(0.2)
                        #i = var
                        #print(int(float(i)))
                    elif event.key == pg.K_DOWN:
                        player.speed = -0.3
                        backward(0.3)
                        #i = var
                        #print(int(float(i)))
                    elif event.key == pg.K_LEFT:
                        player.angle_speed = 0.3
                        turn_left(0.3)
                    elif event.key == pg.K_RIGHT:
                        player.angle_speed = -0.3 # angle speed is anf
                        turn_right(0.3)
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        player.angle_speed = 0
                    elif event.key == pg.K_RIGHT:
                        player.angle_speed = 0
                    elif event.key == pg.K_UP:
                        player.speed = 0
                    elif event.key == pg.K_DOWN:
                        player.speed = 0
            '''            
            
        #plt.plot(t, angle)
        #plt.show()
if __name__ == '__main__':
    main()
    pg.quit()
#
