# importing libraries
import pygame
import time
import random

playero_speed = 15

# Window size
window_x = 1368
window_y = 712

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('MADDEN 2K25')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

playero_position = [0, 250]
playero_body = [[0, 250]]

compx_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx = random.randint(0,1)
compx_down = 0
compx1_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx1_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx1 = random.randint(0,1)
compx1_down = 0
compx2_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx2_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx2 = random.randint(0,1)
compx2_down = 0
compx3_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx3_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx3 = random.randint(0,1)
compx3_down = 0
compx4_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx4_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx4 = random.randint(0,1)
compx4_down = 0

ball_body = [100, random.randrange(1, (window_y//10)) * 10]
ball_position = [100, random.randrange(1, (window_y//10)) * 10]

field_lines_body = [[120, 60],
               [120, 70],
               [120, 80],
               [120, 90],
               [120, 100],
               [240, 60],
               [240, 70],
               [240, 80],
               [240, 90],
               [240, 100],
               [360, 60],
               [360, 70],
               [360, 80],
               [360, 90],
               [360, 100],
               [480, 60],
               [480, 70],
               [480, 80],
               [480, 90],
               [480, 100],
               [600, 60],
               [600, 70],
               [600, 80],
               [600, 90],
               [600, 100],
               [720, 60],
               [720, 70],
               [720, 80],
               [720, 90],
               [720, 100],
               [840, 60],
               [840, 70],
               [840, 80],
               [840, 90],
               [840, 100],
               [960, 60],
               [960, 70],
               [960, 80],
               [960, 90],
               [960, 100],
               [1080, 60],
               [1080, 70],
               [1080, 80],
               [1080, 90],
               [1080, 100],
               [1200, 60],
               [1200, 70],
               [1200, 80],
               [1200, 90],
               [1200, 100]]


speedmeter1_body = [[160, 13],
                    [160, 23],]
speedmeter2_body = [[160, 13],
                    [170, 13],
                    [160, 23],
                    [170, 23],]
speedmeter3_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],]
speedmeter4_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23]]
speedmeter5_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [200, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23],
                    [200, 23]]
speedmeter6_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [200, 13],
                    [210, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23],
                    [200, 23],
                    [210, 23]]
speedmeter7_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [200, 13],
                    [210, 13],
                    [220, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23],
                    [200, 23],
                    [210, 23],
                    [220, 23]]
speedmeter8_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [200, 13],
                    [210, 13],
                    [220, 13],
                    [230, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23],
                    [200, 23],
                    [210, 23],
                    [220, 23],
                    [230,23]]
speedmeter9_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [200, 13],
                    [210, 13],
                    [220, 13],
                    [230, 13],
                    [240, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23],
                    [200, 23],
                    [210, 23],
                    [220, 23],
                    [230, 23],
                    [240, 23],]
speedmeter10_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [200, 13],
                    [210, 13],
                    [220, 13],
                    [230, 13],
                    [240, 13],
                    [250, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23],
                    [200, 23],
                    [210, 23],
                    [220, 23],
                    [230, 23],
                    [240, 23],
                    [250, 23]]
speedmeter11_body = [[160, 13],
                    [170, 13],
                    [180, 13],
                    [190, 13],
                    [200, 13],
                    [210, 13],
                    [220, 13],
                    [230, 13],
                    [240, 13],
                    [250, 13],
                    [260, 13],
                    [160, 23],
                    [170, 23],
                    [180, 23],
                    [190, 23],
                    [200, 23],
                    [210, 23],
                    [220, 23],
                    [230, 23],
                    [240, 23],
                    [250, 23],
                    [260, 23]]
speedmeterMax_body = [[160, 13],
              [170, 13],
              [180, 13],
              [190, 13],
              [200, 13],
              [210, 13],
              [220, 13],
              [230, 13],
              [240, 13],
              [250, 13],
              [260, 13],
              [270, 13],
              [160, 23],
              [170, 23],
              [180, 23],
              [190, 23],
              [200, 23],
              [210, 23],
              [220, 23],
              [230, 23],
              [240, 23],
              [250, 23],
              [260, 23],
              [270, 23]
              ]

direction = 'RIGHT'
change_to = direction
ball_direction = [1, 2, 3]
score = [0, 0] 
play = '0'
down = 4
yardline = 10
yard = '0'

def show_score(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    score_surface = my_font.render(
        'SCORE: ' + str(score[0]) + ' vs ' + str(score[1]), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (1100, 5)
    game_window.blit(score_surface, score_rect)
    pygame.display.flip()

def show_downs(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    if down == 1:
        down_surface = my_font.render(str(down) + 'ST & ' + yard, True, white)
    elif down == 2:
        down_surface = my_font.render(str(down) + 'ND & ' + yard, True, white)
    elif down == 3:
        down_surface = my_font.render(str(down) + 'RD & ' + yard, True, white)
    elif down == 4:
        down_surface = my_font.render(str(down) + 'TH & ' + yard, True, white)

    down_rect = down_surface.get_rect()
    down_rect.midtop = (600, 5)
    game_window.blit(down_surface, down_rect)
    pygame.display.flip()

def show_speed(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    speed_surface = my_font.render(
        'SPEED:' , True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (100, 5)
    game_window.blit(speed_surface, speed_rect)
    pygame.display.flip()


def show_yardline(choice, color, font, size):
  
    yardline_font = pygame.font.SysFont(font, size)
    yardline_surface = yardline_font.render(str(yardline), True, color)
    yardline_rect = yardline_surface.get_rect()
    yardline_rect.midtop = (140, 300)
    game_window.blit(yardline_surface, yardline_rect)

def show_nextyardline(choice, color, font, size):
  
    if yardline < 90:

        nextyardline_font = pygame.font.SysFont(font, size)
        
        nextyardline_surface = nextyardline_font.render(str(yardline + 10), True, color)
        
    
        nextyardline_rect = nextyardline_surface.get_rect()
        nextyardline_rect.midtop = (1225, 300)

        game_window.blit(nextyardline_surface, nextyardline_rect)
    
    else:
        #G
        goallineg_font = pygame.font.SysFont(font, size)
        goallineg_surface =  goallineg_font.render('G', True, color)
        goallineg_rect =  goallineg_surface.get_rect()
        goallineg_rect.midtop = (1225, 160)
        game_window.blit( goallineg_surface,  goallineg_rect)
        
        #O
        goallineo_font = pygame.font.SysFont(font, size)
        goallineo_surface =  goallineo_font.render('O', True, color)
        goallineo_rect =  goallineo_surface.get_rect()
        goallineo_rect.midtop = (1225, 260)
        game_window.blit( goallineo_surface,  goallineo_rect)
        
        #A
        goallinea_font = pygame.font.SysFont(font, size)
        goallinea_surface =  goallinea_font.render('A', True, color)
        goallinea_rect =  goallinea_surface.get_rect()
        goallinea_rect.midtop = (1225, 360)
        game_window.blit( goallinea_surface,  goallinea_rect)
        
        #L
        goallinel_font = pygame.font.SysFont(font, size)
        goallinel_surface =  goallinel_font.render('L', True, color)
        goallinel_rect =  goallinel_surface.get_rect()
        goallinel_rect.midtop = (1225, 460)
        game_window.blit( goallinel_surface,  goallinel_rect)



def downs():

    my_font = pygame.font.SysFont('Arial', 70)
    if down == 1:
        downs_surface = my_font.render(str(down) + 'ST DOWN', True, red)
    elif down == 2:
         downs_surface = my_font.render(str(down) + 'ND DOWN', True, red)
    elif down == 3:
         downs_surface = my_font.render(str(down) + 'RD DOWN', True, red)
    elif down == 4:
         downs_surface = my_font.render(str(down) + 'TH DOWN', True, red)
       
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (window_x/2, 300)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    playero_position[0] = playero_position[0]
    playero_position[1] = 300

    time.sleep(2)

def game_over():
  
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    playero_position[0] = playero_position[0]
    playero_position[1] = 300
    time.sleep(2)
    pygame.quit()
    quit()

speedmeter = 0
play = 0 

while True:
    
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_SPACE:
                if speedmeter < 10:
                    speedmeter = speedmeter + 1
            if event.key != pygame.K_SPACE:
                if speedmeter > -2:
                    speedmeter = speedmeter - 1

    if change_to == 'UP':
        direction = 'UP'
    if change_to == 'DOWN':
        direction = 'DOWN'
    if change_to == 'LEFT':
        direction = 'LEFT'
    if change_to == 'RIGHT':
        direction = 'RIGHT'

    # Moving the playero
    if direction == 'UP':
        playero_position[1] -= 10 + speedmeter
    if direction == 'DOWN':
        playero_position[1] += 10 + speedmeter
    if direction == 'LEFT':
        playero_position[0] -= 10 + speedmeter
    if direction == 'RIGHT':
        playero_position[0] += 10 + speedmeter

    # if play == '0':
    for pos in ball_body:
        impball = pygame.image.load("madden25_imgs/football.png").convert()
        game_window.blit(impball, pygame.Rect(ball_position[0], ball_position[1], 10, 10))
        pygame.display.flip()

    ball_direction_start = random.choice(ball_direction)
    ball_position[0] += 10 
    if ball_direction_start == 2:
        ball_position[1] += 10 
    elif ball_direction_start == 3:
        ball_position[1] -= 10 




    if playero_position[0] == compx_position[0] and playero_position[1] == compx_position[1]:
        if down <= 4:
            if compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1:
                downs()
                compx_down = 1
                down = down + 1
            change_to ='RIGHT'
        else:
            game_over()     

    if playero_position[0] == compx1_position[0] and playero_position[1] == compx1_position[1]:
        if down <= 4:
            if compx_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1:
                downs()
                compx1_down = 1
                down = down + 1
            change_to ='RIGHT'
        else:
            game_over()   

    if playero_position[0] == compx2_position[0] and playero_position[1] == compx2_position[1]:
        if down <= 4:
            if compx_down != 1 and compx1_down != 1 and compx3_down != 1 and compx4_down != 1:
                downs()
                compx2_down = 1
                down = down + 1
            change_to ='RIGHT'
        else:
            game_over()   

    if playero_position[0] == compx3_position[0] and playero_position[1] == compx3_position[1]:
        if down <= 4:
            if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx4_down != 1:
                downs()
                compx3_down = 1
                down = down + 1
            change_to ='RIGHT'
        else:
            game_over()   

    if playero_position[0] == compx4_position[0] and playero_position[1] == compx4_position[1]:
        if down <= 4:
            if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx3_down != 1:
                downs()
                compx4_down = 1
                down = down + 1
            change_to ='RIGHT'
        else:
            game_over()   


    playero_body.insert(0, list(playero_position))
    playero_body.pop() 
    game_window.fill(black)

    for pos in field_lines_body:
        pygame.draw.rect(game_window, white,
                         pygame.Rect(pos[0] + 20, pos[1], 10, 10))
        
    for pos in field_lines_body:
        pygame.draw.rect(game_window, white,
                         pygame.Rect(pos[0] + 20, pos[1] + 550, 10, 10))
    
    
    for pos in playero_body:
        if direction == 'RIGHT':
            imp = pygame.image.load("madden25_imgs/raider0.png").convert()
        elif direction == 'LEFT':
            imp = pygame.image.load("madden25_imgs/raider0_flip.png").convert()
        game_window.blit(imp, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.display.flip()

    #making the computer follow the player by coordinants 
    if compx_position[0] > playero_position[0]:
        if yardline < 50:
            compx_position[0] -= random.randint(5,8)
        else:
            compx_position[0] -= random.randint(7,10)
        compx_direction = 'LEFT'
    if compx_position[0] < playero_position[0]:
        if yardline < 50:
            compx_position[0] += random.randint(5,8)
        else:
            compx_position[0] += random.randint(7,10)
        compx_direction = 'RIGHT'
    if compx_position[1] > playero_position[1]:
        if yardline < 50:
            compx_position[1] -= random.randint(5,8)
        else:
            compx_position[1] -= random.randint(7,10)
    if compx_position[1] < playero_position[1]:
        if yardline < 50:
            compx_position[1] += random.randint(5,8)
        else:
            compx_position[1] += random.randint(7,10)

    if compx1_position[0] > playero_position[0]:
        if yardline < 50:
            compx1_position[0] -= random.randint(5,8)
        else:
            compx1_position[0] -= random.randint(7,10)
        compx1_direction = 'LEFT'
    if compx1_position[0] < playero_position[0]:
        if yardline < 50:
            compx1_position[0] += random.randint(5,8)
        else:
            compx1_position[0] += random.randint(7,10)
        compx1_direction = 'RIGHT'
    if compx1_position[1] > playero_position[1]:
        if yardline < 50:
            compx1_position[1] -= random.randint(5,8)
        else:
            compx1_position[1] -= random.randint(7,10)
    if compx1_position[1] < playero_position[1]:
        if yardline < 50:
            compx1_position[1] += random.randint(5,8)
        else:
            compx1_position[1] += random.randint(7,10)

    if compx2_position[0] > playero_position[0]:
        if yardline < 50:
            compx2_position[0] -= random.randint(5,8)
        else:
            compx2_position[0] -= random.randint(7,10)
        compx2_direction = 'LEFT'
    if compx2_position[0] < playero_position[0]:
        if yardline < 50:
            compx2_position[0] += random.randint(5,8)
        else:
            compx2_position[0] += random.randint(7,10)
        compx2_direction = 'RIGHT'
    if compx2_position[1] > playero_position[1]:
        if yardline < 50:
            compx2_position[1] -= random.randint(5,8)
        else:
            compx2_position[1] -= random.randint(7,10)
    if compx2_position[1] < playero_position[1]:
        if yardline < 50:
            compx2_position[1] += random.randint(5,8)
        else:
            compx2_position[1] += random.randint(7,10)

    if compx3_position[0] > playero_position[0]:
        if yardline < 50:
            compx3_position[0] -= random.randint(5,8)
        else:
            compx3_position[0] -= random.randint(7,10)
        compx3_direction = 'LEFT'
    if compx3_position[0] < playero_position[0]:
        if yardline < 50:
            compx3_position[0] += random.randint(5,8)
        else:
            compx3_position[0] += random.randint(7,10)
        compx3_direction = 'RIGHT'
    if compx3_position[1] > playero_position[1]:
        if yardline < 50:
            compx3_position[1] -= random.randint(5,8)
        else:
            compx3_position[1] -= random.randint(7,10)
    if compx3_position[1] < playero_position[1]:
        if yardline < 50:
            compx3_position[1] += random.randint(5,8)
        else:
            compx3_position[1] += random.randint(7,10)

    if compx4_position[0] > playero_position[0]:
        if yardline < 50:
            compx4_position[0] -= random.randint(5,8)
        else:
            compx4_position[0] -= random.randint(7,10)
        compx4_direction = 'LEFT'
    if compx4_position[0] < playero_position[0]:
        if yardline < 50:
            compx4_position[0] += random.randint(5,8)
        else:
            compx4_position[0] += random.randint(7,10)
        compx4_direction = 'RIGHT'
    if compx4_position[1] > playero_position[1]:
        if yardline < 50:
            compx4_position[1] -= random.randint(5,8)
        else:
            compx4_position[1] -= random.randint(7,10)
    if compx4_position[1] < playero_position[1]:
        if yardline < 50:
            compx4_position[1] += random.randint(5,8)
        else:
            compx4_position[1] += random.randint(7,10)

    if compx == 1:
        for pos in compx_body:
            if compx_direction == 'RIGHT':
                impx = pygame.image.load("madden25_imgs/ramx.png").convert()
            elif compx_direction == 'LEFT':
                impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()

            game_window.blit(impx, pygame.Rect(compx_position[0], compx_position[1], 10, 10))
            pygame.display.flip()

    if compx1 == 1:
        for pos in compx1_body:
            if compx1_direction == 'RIGHT':
                impx = pygame.image.load("madden25_imgs/ramx.png").convert()
            elif compx1_direction == 'LEFT':
                impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()

            game_window.blit(impx, pygame.Rect(compx1_position[0], compx1_position[1], 10, 10))
            pygame.display.flip()

    if compx2 == 1:
        for pos in compx2_body:
            if compx2_direction == 'RIGHT':
                impx = pygame.image.load("madden25_imgs/ramx.png").convert()
            elif compx2_direction == 'LEFT':
                impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()

            game_window.blit(impx, pygame.Rect(compx2_position[0], compx2_position[1], 10, 10))
            pygame.display.flip()

    if compx3 == 1:
        for pos in compx3_body:
            if compx3_direction == 'RIGHT':
                impx = pygame.image.load("madden25_imgs/ramx.png").convert()
            elif compx3_direction == 'LEFT':
                impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()

            game_window.blit(impx, pygame.Rect(compx3_position[0], compx3_position[1], 10, 10))
            pygame.display.flip()

    if compx == 4:
        for pos in compx4_body:
            if compx4_direction == 'RIGHT':
                impx = pygame.image.load("madden25_imgs/ramx.png").convert()
            elif compx4_direction == 'LEFT':
                impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()

            game_window.blit(impx, pygame.Rect(compx4_position[0], compx4_position[1], 10, 10))
            pygame.display.flip()

    if playero_position[0] < 0:
        playero_position[0] = 0

    if playero_position[0] > 1300:
        speedmeter = 0
        compx = random.randint(0,1)
        compx_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
        compx1 = random.randint(0,1)
        compx1_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
        compx2 = random.randint(0,1)
        compx2_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
        compx3 = random.randint(0,1)
        compx3_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
        compx4 = random.randint(0,1)
        compx4_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

        if yardline > 80:
            playero_position[0] = 1000
            show_score(1, red, 'Arial', 80)

        playero_position[0] = 0
        yardline = yardline + 10
        down = 1

    if playero_position[1] < 0:
        playero_position[1] = 0

    if playero_position[1] > 620:
        playero_position[1] = 620

    if speedmeter > 9:
        for pos in speedmeterMax_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
    
    if speedmeter > -2:
        for pos in speedmeter1_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > -1:
        for pos in speedmeter2_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > 0:
        for pos in speedmeter3_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > 1:
        for pos in speedmeter4_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > 2:
        for pos in speedmeter5_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > 3:
        for pos in speedmeter6_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > 4:
        for pos in speedmeter7_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > 5:
        for pos in speedmeter8_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
            
    if speedmeter > 6:
        for pos in speedmeter9_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
    if speedmeter > 7:
        for pos in speedmeter10_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))
    if speedmeter > 8:
        for pos in speedmeter11_body:
            pygame.draw.rect(game_window, green,
                            pygame.Rect(pos[0], pos[1], 10, 10))

    show_yardline(1, white, 'Arial', 80)
    show_nextyardline(1, white, 'Arial', 80)
    show_speed(1, white, 'Arial', 30)
    show_downs(1, white, 'Arial', 30)
    show_score(1, white, 'Arial', 30)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(playero_speed)
