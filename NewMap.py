import pygame as pg
import math
from pygame.math import Vector2
import time

pg.init()
screen = pg.display.set_mode((640, 480))
screen_rect = screen.get_rect()

FONT = pg.font.Font(None, 24)
#bullet images NOT NEEDED
#BULLET_IMAGE = pg.Surface((20, 11), pg.SRCALPHA)
#pg.draw.polygon(BULLET_IMAGE, pg.Color('aquamarine1'),
#                [(0, 0), (20, 5), (0, 11)])


class Bullet(pg.sprite.Sprite):

    def __init__(self, pos, angle):
        super().__init__()
        #1 set the angle of the image!
        self.image = pg.transform.rotate(BULLET_IMAGE, -angle)
        #2. get_rect gives the position
        self.rect = self.image.get_rect(center=pos) #(center=pos)

        angle_rad = math.radians(angle)
        self.velocity_x = speed * math.cos(angle_rad)
        self.velocity_y = speed * math.sin(angle_rad)

        # To apply an offset to the start position,
        # create another vector and rotate it as well.
        offset = Vector2(40, 0).rotate(angle)

        # Then add the offset vector to the position vector.
        self.pos = Vector2(pos) + offset  # pos not defined yet

        # Rotate the direction vector (1, 0) by the angle.
        # Multiply by desired speed.
        self.velocity = Vector2(1, 0).rotate(angle) * 9
        
    def update(self): #siempre update the position
        self.pos += self.velocity  # Add velocity to pos to move the sprite. (2 components of this vector)
        self.rect.center = self.pos  # Update rect coords.

        

        if not screen_rect.contains(self.rect):
            self.kill()


def main():
    clock = pg.time.Clock() #siempre
    #SPRITE!!
    #cannon_img = pg.Surface((20, 11), pg.SRCALPHA) # para dibujar1
    #cannon_img.fill(pg.Color('aquamarine3'))       #para dibujar 2
    cannon_img = pg.Surface((40, 22), pg.SRCALPHA)
    pg.draw.polygon(cannon_img, pg.Color('red'),
                    [(0, 0), (20, 5), (0, 11)])

    cannon = cannon_img.get_rect(center=(320, 240))
    angle = 0
    bullet_group = pg.sprite.Group()  # Add bullets to this group.

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                 #Left button fires a bullet from center with
                 #current angle. Add the bullet to the bullet_group.
                if event.button == 1:
                    bullet_group.add(Bullet(cannon.center, angle))

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            angle -= 3
        elif keys[pg.K_d]:
            angle += 3
        elif keys[pg.K_w]:
            #velocity_x += 3
            #velocity_y += 3
        #if keys[pg.K_SPACE]:
            #bullet_group.add(Bullet(cannon.center, angle))

        # Rotate the cannon image.
        #angulos = list(range(0,45))
        #for idx, angle in enumerate(angulos):
        #print(angle)
        rotated_cannon_img = pg.transform.rotate(cannon_img, -angle) #-val, -angle
        cannon = rotated_cannon_img.get_rect(center=cannon.center)
        #time.sleep(0.3)
        bullet_group.update()

                # Draw
        screen.fill((3, 6, 8))
        screen.blit(rotated_cannon_img, cannon)
        bullet_group.draw(screen)

        txt = FONT.render('angle rotation {:.1f}'.format(angle), True, (150, 150, 170))
        screen.blit(txt, (10, 10))
        pg.display.update()

        clock.tick(30)    

if __name__ == '__main__':
    main()
    pg.quit()
