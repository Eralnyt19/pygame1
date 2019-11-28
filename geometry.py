"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0 , 0, 255)
RED = (255, 0, 0)
PI = 3.14
line_s = 0
line_e = 100

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
offset = 0.0 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    offset += 1
    if offset == 400:
        offset = 0

    if   120 < offset < 220:
        red = BLACK
        blue = BLACK
        green = WHITE
        line_s = 0
        line_e = 200

    elif offset > 220:    
        red = RED
        blue = BLUE
        green = GREEN
        line_s = 320
        line_e = 100 + offset

    else:
        red = RED
        blue = BLUE
        green = GREEN
        line_s = 0
        line_e = 100 + offset

    
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    # ---- coordinates for upper left, hight, width
    pygame.draw.rect(screen, red, [100 + offset, 100 + offset, 20, 25], 5)
    pygame.draw.ellipse(screen, blue, [100 + offset, 100 + offset, 20, 25], 5)
    pygame.draw.line(screen, green, [line_s,line_s], [line_e, line_e], 5)
    pygame.draw.arc(screen, WHITE, [300, 300, 100, 100], 0, PI, 5)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
