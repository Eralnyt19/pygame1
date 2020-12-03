import pygame

BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0)
BLUE = (0 , 0, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
backdrop = BLACK
gubbe_x = 350
gubbe_y = 400
obstacles = [700, 750, 900, 1000, 1050, 1200, 1300, 1350, 1500, 1600, 1700, 1750, 1850]

pygame.init()
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False

def draw_obstacle(x):
    pygame.draw.polygon(screen, ORANGE, [[x, 250], [x -25, 445], [x + 25, 445]])    

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True        
              
    screen.fill(backdrop)
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 5)

    
    for i in range(len(obstacles)):
        draw_obstacle(obstacles[i])    
        obstacles[i] -= 1
        if obstacles[i] < 0:
            obstacles[i] += 1300
       
    pygame.draw.rect(screen, RED, [gubbe_x, gubbe_y, 20, 25], 5)
    pygame.draw.ellipse(screen, BLUE, [gubbe_x, gubbe_y, 20, 25])
    pygame.display.flip()
    clock.tick(120)

pygame.quit()

