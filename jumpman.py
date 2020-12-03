import pygame

BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0)
BLUE = (0 , 0, 255)
RED = (255, 0, 0)
#offset = 0
jump = 0
backdrop = BLACK
gubbe_x = 350
gubbe_y = 400
too_close = 25
##### obstacles
o1 = 700
o2 = 750
o3 = 900
o4 = 1000
o5 = 1050
o6 = 1200
o7 = 1300
o8 = 1350
o9 = 1450


#o_high_1 = 275
#o_high_2 = 475


pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                jump = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jump = 120
                
    ######## game logic  #################

    o1 -= 1
    if o1 < 0:
        o1 += 900
    o2 -= 1
    if o2 < 0:
        o2 += 900
    o3 -= 1
    if o3 < 0:
        o3 += 900
    o4 -= 1
    if o4 < 0:
        o4 += 900
    o5 -= 1
    if o5 < 0:
        o5 += 900
    o6 -= 1
    if o6 < 0:
        o6 += 900
    o7 -= 1
    if o7 < 0:
        o7 += 900
    o8 -= 1
    if o8 < 0:
        o8 += 900
    o9 -= 1
    if o9 < 0:
        o9 += 900
       
    
        
    ##### Draw ####################        
    screen.fill(backdrop)

    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 5)

    ### obstacle low

    pygame.draw.polygon(screen, GREEN, [[o1, 250], [o1 -25, 445], [o1 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o2, 250], [o2 - 25, 445], [o2 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o3, 250], [o3 -25, 445], [o3 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o4, 250], [o4 - 25, 445], [o4 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o5, 250], [o5 -25, 445], [o5 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o6, 250], [o6 - 25, 445], [o6 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o7, 250], [o7 -25, 445], [o7 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o8, 250], [o8 - 25, 445], [o8 + 25, 445]])
    pygame.draw.polygon(screen, GREEN, [[o9, 250], [o9 - 25, 445], [o9 + 25, 445]])


    ### obstacle high
    ### 275
#    pygame.draw.polygon(screen, GREEN, [[o_high_1, 300], [o_high_1 - 25 , 100], [o_high_1 + 25, 100]], 5)
    ### 475
#    pygame.draw.polygon(screen, GREEN, [[o_high_2, 300], [o_high_2 - 25, 100], [o_high_2 + 25, 100]], 5)
   
    
    pygame.draw.rect(screen, RED, [gubbe_x, gubbe_y, 20, 25], 5)
    pygame.draw.ellipse(screen, BLUE, [gubbe_x, gubbe_y, 20, 25], 5)

    pygame.display.flip()

    clock.tick(120)

pygame.quit()

