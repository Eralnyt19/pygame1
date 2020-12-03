import pygame

BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0)
BLUE = (0 , 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
backdrop = BLACK
gubbe_x = 350
gubbe_y = 425
jump_counter = 0
obstacles_org = [700, 750, 900, 1000, 1050, 1200, 1300, 1350, 1500, 1600, 1700, 1750, 1850]
crash = True


pygame.init()
obstacles = obstacles_org.copy() 
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False

def draw_obstacle(x):
    pygame.draw.polygon(screen, GREEN, [[x, 250], [x -25, 445], [x + 25, 445]])    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                 jump_counter = 120    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                jump_counter = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                crash = False
                obstacles = obstacles_org.copy()
               
                
    ######## game logic  #################
                                
    if jump_counter:
        jump = 250
        jump_counter -= 1
    else:
        jump = 0
        
    if not crash:
        for x in range(len(obstacles)):
            obstacles[x] -= 1
            if obstacles[x] < 0:
                obstacles[x] += 1300
            if (abs(obstacles[x] -  gubbe_x ) < 15) and not jump:
                crash = True
                    
        
        
    ##### Draw ####################        
    screen.fill(backdrop)
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 5)

    
    for x in range(len(obstacles)):
        draw_obstacle(obstacles[x])              
    pygame.draw.rect(screen, RED, [gubbe_x, gubbe_y - jump, 20, 25], 5)           
    pygame.draw.ellipse(screen, BLUE, [gubbe_x, gubbe_y - jump, 20, 25], 5)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()

