import pygame
import time

#basic elements
pygame.init()
#dimensions
width = 800
height = 600
#colors
black = (0,0,0)
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
###this text   
    
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('ARENA..')
clock = pygame.time.Clock() 

def game_loop():
    #vehicle variables
    x = (width/2)
    y = (height/2)

    GameExit = False
    x_change = 0
    i = 0

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
        vehicle(x,y) #object on top of display (always)
        if x > (width-vehicle_width) or x < 0:
             crash()
        elif y >(height-vehicle_height) or y < 0:
             crash()
             #message_display("fun game")
                 
        pygame.display.update()
        clock.tick(60)
    #    print(i)
    #    i += i
#Calling the functions
    
game_loop()
pygame.quit()
quit()
