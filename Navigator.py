import pygame

pygame.init()
display_width = 800
display_height = 600
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render("Some text!", 1, (255,255,0))
screen.blit(label, (100, 100))


#colors
black = (0,0,0)
white = (255,255,255)
red = (255, 0,0)


#size display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("ARENA..")

clock = pygame.time.Clock()

#main loop

carImg = pygame.image.load("ROV.jpg")

x = display_width*0.45   
y = display_height*0.45

def car(x, y ):
    gameDisplay.blit(carImg, (x, y)) #blit put it on
    
direction = "right"


x_change = 0
y_change = 0



crashed = False


#MAIN LOOP and MOVEMENTS: where car it is
while not crashed:
    
    for event in pygame.event.get(): # create a list of events per second
        if event.type == pygame.QUIT: #press ESC
            crahed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = +5
            

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

        
                
            
        #print(event)
    
    
    gameDisplay.fill(white)
    #UPdate position
    
    x += x_change
    y += y_change
    car(x, y)
    pygame.display.update() #update
    clock.tick(60) #60 frames per second

pygame.quit()

quit()

    
            
            
    
