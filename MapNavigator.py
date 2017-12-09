import math
import pygame as pg
from pygame.math import Vector2

import RPi.GPIO as GPIO
import time
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
            self.direction.rotate_ip(self.angle_speed)
            self.angle += self.angle_speed
            self.image = pg.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        # Update the position vector and the rect.
        self.position += -self.direction*self.speed #this controls postion
        self.rect.center = self.position


def main():
    pg.init()

    myfont = pg.font.SysFont("monospace", 15)
    # render text
    label = myfont.render("Some text!", 1, (255,255,0))
    


    
    screen = pg.display.set_mode((700, 700)) #arena
    screen.blit(label, (100, 100))
    player = Player((120, 120)) #starting postion
    playersprite = pg.sprite.RenderPlain((player))

    clock = pg.time.Clock()
    done = False
    while not done:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    player.speed = 0.3
                    forward(0.1)
                elif event.key == pg.K_DOWN:
                    player.speed = -0.3
                    backward(0.1)
                elif event.key == pg.K_LEFT:
                    player.angle_speed = -0.8
                    turn_left(0.1)
                elif event.key == pg.K_RIGHT:
                    player.angle_speed = 0.8
                    turn_right(0.1)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    player.angle_speed = 0
                elif event.key == pg.K_RIGHT:
                    player.angle_speed = 0
                elif event.key == pg.K_UP:
                    player.speed = 0
                elif event.key == pg.K_DOWN:
                    player.speed = 0
                    
        playersprite.update()

        screen.fill((30, 30, 30))
        playersprite.draw(screen)
        pg.display.flip()

if __name__ == '__main__':
    main()
    pg.quit()

