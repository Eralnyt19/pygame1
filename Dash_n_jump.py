import pygame
import time
import copy
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255) 
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255,100,10)

background = BLACK
dash_y = 325
jump_y = 345


offset = 0
obstacles_org = [[700, jump_y], [750, jump_y], [900,dash_y], [1000,jump_y], [1050,jump_y], [1200,dash_y],
                 [1300,jump_y], [1350,jump_y], [1500,jump_y], [1650,jump_y], [1700,jump_y] , [1850,dash_y], [1900,dash_y]]
obstacles = []
coldis_jump = 30
coldis_dash = 20

score = 0
speed = 100
pygame.init()
obstacles = copy.deepcopy(obstacles_org)
size = (800, 500)
screen = pygame.display.set_mode(size)

x = 350
y = 420
height = 25
wide = 20
pygame.display.set_caption("Dash n Jump")

clock = pygame.time.Clock()

is_jump = False
is_dash = False
isCrash = False
jumpCount = 7
font_color = WHITE

done = False
pygame.mixer.music.load('MassiveEdge.wav')
pygame.mixer.music.play(-1)



def draw_obstacle_n_check(coord):
    if coord[1] == jump_y:
        pygame.draw.polygon(screen, ORANGE, [[coord[0], coord[1]], [coord[0] -25, coord[1] + 100], [coord[0] + 25, coord[1] + 100]])
    else:
        pygame.draw.polygon(screen, ORANGE, [[coord[0], coord[1] + 100], [coord[0] -25, coord[1]], [coord[0] + 25, coord[1]]])
        
    if not is_jump and abs(coord[0] - 350) < coldis_jump and coord[1] == jump_y :
        return True
    elif not is_dash and abs(coord[0] - 350) < coldis_dash and coord[1] == dash_y:
        return True

    else:
        return False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #Game logic

    
    keys = pygame.key.get_pressed()

    
        

      
    if keys[pygame.K_SPACE] and isCrash:
        score = 0
        isCrash = False
        background = BLACK
        pygame.mixer.music.play(-1)
        obstacles = copy.deepcopy(obstacles_org)
    
     
    if not(is_jump):        
        if keys[pygame.K_UP]:
            isJump = True
            is_jump = True
        
        elif keys[pygame.K_DOWN]:
            height = 15
            wide =25
            y = 430
            is_dash = True
        else: 
            height = 25
            wide = 20
            y = 420
            is_dash = False

    else:
        if jumpCount >= -7:
            y -= (jumpCount * abs(jumpCount)) * 0.1
            jumpCount -= 0.1
        else: 
            jumpCount = 7
            is_jump = False

    
    if not isCrash:
        for i in range(len(obstacles)):
            obstacles[i][0] -= 1
            if obstacles[i][0] < 0:
                obstacles[i][0] += 1300
        
    
    #Draw
    screen.fill(background)
     
    pygame.draw.line(screen, WHITE, [0, 450], [3000, 450], 10)
    pygame.draw.rect(screen, RED, [x, y, wide, height], 5) 
    

    for i in range(len(obstacles)):
        if draw_obstacle_n_check(obstacles[i]):
            background = RED
            pygame.mixer.music.stop()
            isCrash = True


    font75 = pygame.font.SysFont('Calibri', 75, True, False)
    font40 = pygame.font.SysFont('Calibri', 40, True, False)
    font15 = pygame.font.SysFont('Calibri', 15, True, False)

    text1 = font75.render("LET'S JUMP", True, WHITE)
    text2 = font40.render(str(score) + " M", True, WHITE)
    text3 = font15.render("Press Keyup = Jump", True, font_color)
    text4 = font15.render("Press Keydown = Dash", True, font_color)
    text5 = font15.render("Press Space = Play Again", True, font_color)    
 
    screen.blit(text1, [200, 100])
    screen.blit(text2, [60, 30])
    
    if score > 500:
        font_color = BLACK
    else:
        font_color = WHITE
        
    screen.blit(text3, [20, 70])
    screen.blit(text4, [20, 87])
    screen.blit(text5, [20, 104])
       

    

    pygame.display.flip()
    if not isCrash:
        score += 1
        
    clock.tick(speed)

pygame.quit()
