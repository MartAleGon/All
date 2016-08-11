"""
 Pygame base template for opening a window
 Pygame documentation: https://www.pygame.org/docs/genindex.html
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Part 1")

#movement
x_speed=random.randint(-10,10)
y_speed=random.randint(-10,10)
x_speed1=random.randint(-10,10)
y_speed1=random.randint(-10,10)
x_loc=350
y_loc=250
x_loc1=350
y_loc1=250


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
        if event.type==pygame.MOUSEBUTTONDOWN:
            print("Here!")
            position=pygame.mouse.get_pos()

    #mouse
    #print(pygame.mouse.get_pressed())
    


    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)
    
    # --- Drawing code should go here
    pygame.draw.circle(screen,BLUE, (x_loc,y_loc), 30)
    pygame.draw.circle(screen, GREY, (x_loc1,y_loc1),30)
    
    x_loc+=x_speed
    y_loc+=y_speed
    if x_loc>SCREEN_WIDTH-30:
        x_speed=x_speed*-1
        
    if x_loc<30:
        x_speed=x_speed*-1
        color=GREY
    if y_loc>30:
        y_speed=y_speed*-1
        color=BLACK
    if y_loc<SCREEN_HEIGHT-30:
        y_speed=y_speed*-1
        color=WHITE

        #new ball
    x_loc1+=x_speed1
    y_loc1+=y_speed1
    if x_loc1>SCREEN_WIDTH-30:
        x_speed1=x_speed1*-1
        
    if x_loc1<30:
        x_speed1=x_speed1*-1
    if y_loc1>30:
        y_speed1=y_speed1*-1
    if y_loc1<SCREEN_HEIGHT-30:
        y_speed1=y_speed1*-1


    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
