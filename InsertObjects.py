import pygame
import time
import random

#basic elements
pygame.init()
#dimensions
width = 800
height = 600
#colors
black = (0,0,0)
blue = (0,255,255)
white = (255, 255, 255)
#vehicle
#These are to set the borders of the game:
#additionally an ultradound estimation of the borders would be good
#to start too:
vehicle_width  = 240
vehicle_height = 240

def vehicle(x,y):
    carImg = pygame.image.load("vehicle.png")
    gameDisplay.blit(carImg, (x,y))

####all this for a text
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 65) #65 font size
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (width/2, height/2)
    gameDisplay.blit(TextSurf, TextRect) #blit place any object

    pygame.display.update()
    time.sleep(3)
    game_loop() #start the game over!

def crash():
    message_display('Obstacle not detected')

###OBSTACLES  
def obstacles(obstaclex, obstacley, obstaclew, obstacleh, color):
    pygame.draw.rect(gameDisplay, color, [obstaclex, obstacley,obstaclew, obstacleh])
    
def fix_obsta(pos_x, pos_y, pos_w, pos_h, color):
    pygame.draw.rect(gameDisplay, color, [pos_x, pos_y,pos_w, pos_h])
        
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('ARENA..')
clock = pygame.time.Clock() 

def game_loop():
    #vehicle variables
    x = (width/2)
    y = (height/2)
    x_change = 0
    i = 0
    
    #POSITION OBSTACLES
    #obstacles coordinates (starting point)
    obstacle_startx = random.randrange(0, width) #from 0 to ancho
    obstacle_starty = -400 #from 0 to ancho
    obstacle_speed = 7
    obsta_width = 100
    obsta_height = 100

    #sensor measure
    pos_x = width/2 
    pos_y = 100
    pos_w = 20
    pos_h= 20
    





    
    GameExit = False
    
    #main loop
    while not GameExit:
    #for i in range(1,100):
        for event in pygame.event.get():
            #to stop the game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #to move the vehicle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or pygame.K_DOWN:
                    y_change = 0
                    
        gameDisplay.fill(black)
        x += x_change
        obstacles(obstacle_startx, obstacle_starty, obsta_width, obsta_height, blue) 
        obstacle_starty += obstacle_speed

        fix_obsta(pos_x, pos_y, pos_w, pos_h, blue)
        fix_obsta(100, 100, 20, 20, white)
        vehicle(x,y) #object on top of display (always)
        if x > (width-vehicle_width) or x < 0:
             crash()
        elif y >(height-vehicle_height) or y < 0:
             crash()
        #message_display("fun game")

        if obstacle_starty > height: #heigh of display)
            obstacle_starty = 0 - obsta_height
            obstacle_startx = random.randrange(0, width)
                 
        pygame.display.update()
        clock.tick(60)
    #    print(i)
    #    i += i
#Calling the functions
    
game_loop()
pygame.quit()
quit()
