# importing libraries
import pygame
import time
import random
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

player_speed = 15

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

ball_body = [300, random.randrange(1, ((window_y - 50)//10)) * 10]
ball_position = [300, random.randrange(1, ((window_y - 50)//10)) * 10]

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
selection_body = [[325, 360],
                  [330, 360],
                  [340, 360],
                  [350, 360],
                  [360, 360],
                  [370, 360],
                  [380, 360],
                  [390, 360],
                  [400, 360],
                  [410, 360],
                  [420, 360],
                  [430, 360],
                  [440, 360],
                  [450, 360],
                  [460, 360],
                  [470, 360],
                  [480, 360],
                  [490, 360],
                  [500, 360],
                  [510, 360],
                  [520, 360],
                  [530, 360],
                  [540, 360],
                  [550, 360],
                  [560, 360],
                  [570, 360],
                  [580, 360],
                  [590, 360],
                  [600, 360],
                  [610, 360],
                  [615, 360],]
selection_position = [325, 360]

fieldgoal_body = [560, 250]
fieldgoal_position = [560, 250]

fieldgoalball_body = [680, 630]
fieldgoalball_position = [680, 630]

timer_body = [0, 710]
timer_position = [0, 710]

gb_body = [10, 305]
gb_position = [10, 305]

center_body = [80, 305]
center_position = [80, 305]

player_body = [50, 205]
player_position = [50, 205]

snapo1_body = [160, 160]
snapo1_position = [160, 160]
snapo2_body = [160, 230]
snapo2_position = [160, 230]
snapo3_body = [160, 300]
snapo3_position = [160, 300]
snapo4_body = [160, 375]
snapo4_position = [160, 375]
snapo5_body = [160, 450]
snapo5_position = [160, 450]
snapo6_body = [160, 520]
snapo6_position = [160, 520]

snapx1_body = [225, 160]
snapx1_position = [225, 160]
snapx2_body = [225, 230]
snapx2_position = [225, 230]
snapx3_body = [225, 300]
snapx3_position = [225, 300]
snapx4_body = [225, 375]
snapx4_position = [225, 375]
snapx5_body = [225, 450]
snapx5_position = [225, 450]
snapx6_body = [320, 300]
snapx6_position = [320, 300]

direction = ''
key = ''
change_to = direction
ball_direction = [1, 2, 3]
score = [0, 0] 
play = 0
down = 1
yardline = 10
yard = '0'
field_goal = '0'
play_promt = '0'
speedmeter = 0
play = 0 
power = 0
spacebar_count = 0
snap = 0
ballcatch = 0

def show_playoptions(choice, color, font, size):

    my_font = pygame.font.SysFont('Arial', 50)
    score_surface = my_font.render(
        'FIELD GOAL OR PASS/RUN', True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (650, 300)
    game_window.blit(score_surface, score_rect)

def show_score(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    score_surface = my_font.render(
        'SCORE: ' + str(score[0]) + ' vs ' + str(score[1]), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (1100, 5)
    game_window.blit(score_surface, score_rect)


def show_scorefieldgoal(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    score_surface = my_font.render(
        'SCORE: ' + str(score[0]) + ' vs ' + str(score[1]), True, white)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (1200, 655)
    game_window.blit(score_surface, score_rect)

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

def show_downsfieldgoal(choice, color, font, size):
  
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
    down_rect.midtop = (105, 655)
    game_window.blit(down_surface, down_rect)


def show_speed(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    speed_surface = my_font.render(
        'SPEED:' , True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (100, 5)
    game_window.blit(speed_surface, speed_rect)

def show_fieldgoal(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    speed_surface = my_font.render(
        'QUICKLY & REPEATEDLY TAP THE SPACE BAR' , True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (670, 25)
    game_window.blit(speed_surface, speed_rect)

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
    player_position[0] = player_position[0]
    player_position[1] = 300
    time.sleep(2)

def outofbounds():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('OUT', True, red)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (window_x/2, 300)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    player_position[0] = player_position[0]
    player_position[1] = 300
    time.sleep(2)

def incompletion():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('INCOMPLETE PASS', True, red)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (window_x/2, 280)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    time.sleep(2)

def catch():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('NICE CATCH', True, green)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (window_x/2, 300)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    time.sleep(2)


def kickoff():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('KICK OFF', True, white)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (window_x/2, 300)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    time.sleep(2)

def game_over():
  
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    player_position[0] = player_position[0]
    player_position[1] = 300
    time.sleep(2)
    pygame.quit()
    quit()

def goal():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('ITS GOOD', True, green)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (window_x/2, 600)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    time.sleep(2)

def miss():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('NO GOOD', True, red)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (window_x/2, 600)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    time.sleep(2)
   
while True:
    game_window.fill(black)

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                change_to = 'ENTER'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_SPACE:
                change_to = 'SPACE'
                if speedmeter < 10:
                    speedmeter += 1
                    spacebar_count += 1
            if event.key != pygame.K_SPACE:
                if speedmeter > -2:
                    speedmeter -= 1
            if event.key == pygame.K_p:
                play_promt = 'p'

        if change_to == 'UP':
            direction = 'UP'
        if change_to == 'DOWN':
            direction = 'DOWN'
        if change_to == 'LEFT':
            direction = 'LEFT'
        if change_to == 'RIGHT':
            direction = 'RIGHT'
        if change_to == 'ENTER':
            key = 'ENTER'
        if change_to == 'SPACE':
            key = 'SPACE'

    if play_promt == '0':
            
        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1], 10, 10))
        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1] + 550, 10, 10))    
        if direction == 'RIGHT':
            if selection_position[0] <= 624:
                selection_position[0] += 93
        if direction == 'LEFT':
                if selection_position[0] > 325:
                    selection_position[0] -= 93
        
        if key == 'ENTER' and selection_position[0] > 624:
            play_promt = '2'
        if key == 'ENTER' and selection_position[0] < 624:
            play_promt = '1'

        for pos in selection_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(selection_position[0], pos[1], 300, 10))
        show_downs(1, white, 'Arial', 100)    
        show_score(1, white, 'Arial', 100)    
        show_playoptions(1, white, 'Arial', 100)
            
    if play_promt == '1':
            
            for pos in fieldgoal_body:
                impgoal = pygame.image.load("madden25_imgs/fieldgoal.png").convert()
                game_window.blit(impgoal, pygame.Rect(fieldgoal_position[0], fieldgoal_position[1], 10, 10))

            if key == 'SPACE':
                direction = 'RIGHT'

            for pos in fieldgoalball_body:
                if fieldgoalball_position[1] >= 300 and fieldgoalball_position[1] < 355:
                    impball = pygame.image.load("madden25_imgs/fieldgoalball.png").convert()
                if fieldgoalball_position[1] > 355 and fieldgoalball_position[1] < 410:
                    impball = pygame.image.load("madden25_imgs/fieldgoalball1.png").convert()  
                if fieldgoalball_position[1] >= 410 and fieldgoalball_position[1] <= 465:
                    impball = pygame.image.load("madden25_imgs/fieldgoalball2.png").convert()  
                if fieldgoalball_position[1] >= 465 and fieldgoalball_position[1] <= 520:
                    impball = pygame.image.load("madden25_imgs/fieldgoalball3.png").convert()  
                if fieldgoalball_position[1] >= 520 and fieldgoalball_position[1] <= 575:
                    impball = pygame.image.load("madden25_imgs/fieldgoalball4.png").convert()  
                if fieldgoalball_position[1] >= 575 and fieldgoalball_position[1] <= 630:
                    impball = pygame.image.load("madden25_imgs/fieldgoalball5.png").convert()  
                game_window.blit(impball, pygame.Rect(fieldgoalball_position[0], fieldgoalball_position[1], 10, 10))

            if speedmeter > -2:
                for pos in speedmeter1_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))                 
            if speedmeter > -1:
                for pos in speedmeter2_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))                 
            if speedmeter > 0:
                for pos in speedmeter3_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))               
            if speedmeter > 1:
                for pos in speedmeter4_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))
            if speedmeter > 2:
                for pos in speedmeter5_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))
            if speedmeter > 3:
                for pos in speedmeter6_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))
            if speedmeter > 4:
                for pos in speedmeter7_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))
            if speedmeter > 5:
                for pos in speedmeter8_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))
            if speedmeter > 6:
                for pos in speedmeter9_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))
            if speedmeter > 7:
                for pos in speedmeter10_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))
            if speedmeter > 8:
                for pos in speedmeter11_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10)) 
            if speedmeter > 9:
                for pos in speedmeterMax_body:
                    pygame.draw.rect(game_window, green,
                                    pygame.Rect(pos[0] + 465, pos[1] + 100, 10, 10))    
                    
            for pos in timer_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(timer_position[0], timer_position[1], 10, 10))       

            timer_position[0] += 10      
            if timer_position[0] > 1300:
                if spacebar_count >= 7 and fieldgoalball_position[1] > 300:
                    fieldgoalball_position[1] -= 10
                    if fieldgoalball_position[1] <= 300:
                        goal()
                        play_promt = '0'
                        fieldgoalball_position[0] = 680
                        fieldgoalball_position[1] = 630
                        spacebar_count = 0
                        timer_position[0] = 0

                elif spacebar_count < 7 and spacebar_count > 3 and fieldgoalball_position[1] > 250:
                    fieldgoalball_position[0] -= 5
                    fieldgoalball_position[1] -= 10
                    if fieldgoalball_position[1] <= 250:
                        miss()
                        play_promt = '0'
                        fieldgoalball_position[0] = 680
                        fieldgoalball_position[1] = 630
                        spacebar_count = 0
                        timer_position[0] = 0

                elif spacebar_count < 4 and fieldgoalball_position[1] > 270:
                    fieldgoalball_position[0] += 5
                    fieldgoalball_position[1] -= 10
                    if fieldgoalball_position[1] <= 270:
                        miss()  
                        play_promt = '0'
                        fieldgoalball_position[0] = 680
                        fieldgoalball_position[1] = 630
                        spacebar_count = 0
                        timer_position[0] = 0

            power_range = [0,0,1]
            power = random.choice(power_range)

            if power == 1:
                if timer_position[0] < 1300:
                    if speedmeter > -2:
                        speedmeter -=1
                        spacebar_count -= 1

            show_fieldgoal(1, white, 'Arial', 30)
            show_downsfieldgoal(1, white, 'Arial', 30)
            show_scorefieldgoal(1, white, 'Arial', 30)
    
    if play_promt == '2':

        if player_position[0] < 0:
            player_position[0] = 0

        if player_position[0] > 1300:
            player_position[0] = 1200
            if ballcatch == 1:
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
                snap = 2

                if yardline > 80:
                    player_position[0] >= 1000
                    goal()
                    score[0] += 6
                player_position[0] = 0
                yardline = yardline + 10
                down = 1

        if player_position[1] < 0:
            player_position[1] = 0

        if player_position[1] > 620:
            player_position[1] = 620

        if player_position[1] < 50:
            player_position[1] = 50
            if ballcatch == 1:
                outofbounds()
            direction = 'RIGHT'

        if player_position[1] > 600:
            player_position[1] = 600
            if ballcatch == 1:
                outofbounds()
            direction = 'RIGHT'

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

        if snap == 0:
            
            for pos in field_lines_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))   

            for pos in player_body:
                impplayer = pygame.image.load("madden25_imgs/playercenter.png").convert()
                game_window.blit(impplayer, pygame.Rect(player_position[0], player_position[1], 10, 10))
            for pos in gb_body:
                impball = pygame.image.load("madden25_imgs/raidergb0.png").convert()
                game_window.blit(impball, pygame.Rect(gb_position[0], gb_position[1], 10, 10))
            for pos in center_body:
                impball = pygame.image.load("madden25_imgs/raidercenter.png").convert()
                game_window.blit(impball, pygame.Rect(center_position[0], center_position[1], 10, 10))
            for pos in snapo1_body:
                impball = pygame.image.load("madden25_imgs/raidercenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo1_position[0], snapo1_position[1], 10, 10))
            for pos in snapo2_body:
                impball = pygame.image.load("madden25_imgs/raidercenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo2_position[0], snapo2_position[1], 10, 10))
            for pos in snapo3_body:
                impball = pygame.image.load("madden25_imgs/raidercenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo3_position[0], snapo3_position[1], 10, 10))
            for pos in snapo4_body:
                impball = pygame.image.load("madden25_imgs/raidercenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo4_position[0], snapo4_position[1], 10, 10))
            for pos in snapo5_body:
                impball = pygame.image.load("madden25_imgs/raidercenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo5_position[0], snapo5_position[1], 10, 10))
            for pos in snapx1_body:
                impball = pygame.image.load("madden25_imgs/ramcenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx1_position[0], snapx1_position[1], 10, 10))
            for pos in snapx2_body:
                impball = pygame.image.load("madden25_imgs/ramcenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx2_position[0], snapx2_position[1], 10, 10))
            for pos in snapx3_body:
                impball = pygame.image.load("madden25_imgs/ramcenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx3_position[0], snapx3_position[1], 10, 10))
            for pos in snapx4_body:
                impball = pygame.image.load("madden25_imgs/ramcenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx4_position[0], snapx4_position[1], 10, 10))
            for pos in snapx5_body:
                impball = pygame.image.load("madden25_imgs/ramcenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx5_position[0], snapx5_position[1], 10, 10))
            for pos in snapx5_body:
                impball = pygame.image.load("madden25_imgs/ramcenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx6_position[0], snapx6_position[1], 10, 10))
            for pos in timer_body:
                pygame.draw.rect(game_window, black,
                                pygame.Rect(timer_position[0], timer_position[1], 10, 10))       

            timer_position[0] += 40 
            if timer_position[0] > 1300:
                snap = 1

        if snap == 1:

            # Moving the player 
            if direction == 'UP':
                player_position[1] -= 10 + speedmeter
            if direction == 'DOWN':
                player_position[1] += 10 + speedmeter
            if direction == 'LEFT':
                player_position[0] -= 10 + speedmeter
            if direction == 'RIGHT':
                    player_position[0] += 10 + speedmeter

            for pos in field_lines_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))   
   
            compx_dist = pygame.Vector2(player_position).distance_to(compx_position)
            if compx_dist < 10:
                if down <= 5:
                    if compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()        
            compx1_dist = pygame.Vector2(player_position).distance_to(compx1_position)
            if compx1_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx1_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()      
            compx2_dist = pygame.Vector2(player_position).distance_to(compx2_position)
            if compx2_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx2_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()      
            compx3_dist = pygame.Vector2(player_position).distance_to(compx3_position)
            if compx3_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx3_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()      
            compx4_dist = pygame.Vector2(player_position).distance_to(compx4_position)
            if compx_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx4_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    down = 1
                    game_over()   

            player_body.insert(0, list(player_position))
            player_body.pop() 
            
            if compx_position[0] > player_position[0]:
                if yardline < 50:
                    compx_position[0] -= random.randint(5,8)
                else:
                    compx_position[0] -= random.randint(7,10)
                compx_direction = 'LEFT'
            if compx_position[0] < player_position[0]:
                if yardline < 50:
                    compx_position[0] += random.randint(5,8)
                else:
                    compx_position[0] += random.randint(7,10)
                compx_direction = 'RIGHT'
                
            if compx_position[1] > player_position[1]:
                if yardline < 50:
                    compx_position[1] -= random.randint(5,8)
                else:
                    compx_position[1] -= random.randint(7,10)
            if compx_position[1] < player_position[1]:
                if yardline < 50:
                    compx_position[1] += random.randint(5,8)
                else:
                    compx_position[1] += random.randint(7,10)
            if compx1_position[0] > player_position[0]:
                if yardline < 50:
                    compx1_position[0] -= random.randint(5,8)
                else:
                    compx1_position[0] -= random.randint(7,10)
                compx1_direction = 'LEFT'
            if compx1_position[0] < player_position[0]:
                if yardline < 50:
                    compx1_position[0] += random.randint(5,8)
                else:
                    compx1_position[0] += random.randint(7,10)
                compx1_direction = 'RIGHT'
            if compx1_position[1] > player_position[1]:
                if yardline < 50:
                    compx1_position[1] -= random.randint(5,8)
                else:
                    compx1_position[1] -= random.randint(7,10)
            if compx1_position[1] < player_position[1]:
                if yardline < 50:
                    compx1_position[1] += random.randint(5,8)
                else:
                    compx1_position[1] += random.randint(7,10)
            if compx2_position[0] > player_position[0]:
                if yardline < 50:
                    compx2_position[0] -= random.randint(5,8)
                else:
                    compx2_position[0] -= random.randint(7,10)
                compx2_direction = 'LEFT'
            if compx2_position[0] < player_position[0]:
                if yardline < 50:
                    compx2_position[0] += random.randint(5,8)
                else:
                    compx2_position[0] += random.randint(7,10)
                compx2_direction = 'RIGHT'
            if compx2_position[1] > player_position[1]:
                if yardline < 50:
                    compx2_position[1] -= random.randint(5,8)
                else:
                    compx2_position[1] -= random.randint(7,10)
            if compx2_position[1] < player_position[1]:
                if yardline < 50:
                    compx2_position[1] += random.randint(5,8)
                else:
                    compx2_position[1] += random.randint(7,10)
            if compx3_position[0] > player_position[0]:
                if yardline < 50:
                    compx3_position[0] -= random.randint(5,8)
                else:
                    compx3_position[0] -= random.randint(7,10)
                compx3_direction = 'LEFT'
            if compx3_position[0] < player_position[0]:
                if yardline < 50:
                    compx3_position[0] += random.randint(5,8)
                else:
                    compx3_position[0] += random.randint(7,10)
                compx3_direction = 'RIGHT'
            if compx3_position[1] > player_position[1]:
                if yardline < 50:
                    compx3_position[1] -= random.randint(5,8)
                else:
                    compx3_position[1] -= random.randint(7,10)
            if compx3_position[1] < player_position[1]:
                if yardline < 50:
                    compx3_position[1] += random.randint(5,8)
                else:
                    compx3_position[1] += random.randint(7,10)
            if compx4_position[0] > player_position[0]:
                if yardline < 50:
                    compx4_position[0] -= random.randint(5,8)
                else:
                    compx4_position[0] -= random.randint(7,10)
                compx4_direction = 'LEFT'
            if compx4_position[0] < player_position[0]:
                if yardline < 50:
                    compx4_position[0] += random.randint(5,8)
                else:
                    compx4_position[0] += random.randint(7,10)
                compx4_direction = 'RIGHT'
            if compx4_position[1] > player_position[1]:
                if yardline < 50:
                    compx4_position[1] -= random.randint(5,8)
                else:
                    compx4_position[1] -= random.randint(7,10)
            if compx4_position[1] < player_position[1]:
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
            if compx1 == 1:
                for pos in compx1_body:
                    if compx1_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx1_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx1_position[0], compx1_position[1], 10, 10))
            if compx2 == 1:
                for pos in compx2_body:
                    if compx2_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx2_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx2_position[0], compx2_position[1], 10, 10))
            if compx3 == 1:
                for pos in compx3_body:
                    if compx3_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx3_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx3_position[0], compx3_position[1], 10, 10))
            if compx4 == 1:
                for pos in compx4_body:
                    if compx4_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx4_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx4_position[0], compx4_position[1], 10, 10))

            if gb_position[1] < ball_position[1] and play == 0:
                gb_position[1] += 5
            if gb_position[1] > ball_position[1] and play == 0:
                gb_position[1] -= 5
            if gb_position[1] == ball_position[1]:
                play = 1

            for pos in player_body:
                if play == 0 and ballcatch == 0:
                    if direction == 'LEFT':
                        impplayer = pygame.image.load("madden25_imgs/playersnap_flip.png").convert()
                    if direction == 'RIGHT':
                        impplayer = pygame.image.load("madden25_imgs/playersnap.png").convert()
                if play == 1 and ballcatch == 0:
                    if direction == 'LEFT':
                        impplayer = pygame.image.load("madden25_imgs/raider_catch_flip.png").convert()
                    if direction == 'RIGHT':
                        impplayer = pygame.image.load("madden25_imgs/raider_catch.png").convert()
                if ballcatch == 1:
                    if direction == 'LEFT':
                        impplayer = pygame.image.load("madden25_imgs/raider0_flip.png").convert()
                    if direction == 'RIGHT':
                        impplayer = pygame.image.load("madden25_imgs/raider0.png").convert()
                game_window.blit(impplayer, pygame.Rect(player_position[0], player_position[1], 10, 10))
            for pos in gb_body:
                if play == 0:
                    impball = pygame.image.load("madden25_imgs/raidergb.png").convert()
                if play == 1:
                    impball = pygame.image.load("madden25_imgs/raider_catch.png").convert()
                game_window.blit(impball, pygame.Rect(gb_position[0], gb_position[1], 10, 10))
            for pos in center_body:
                impball = pygame.image.load("madden25_imgs/raiderx.png").convert()
                game_window.blit(impball, pygame.Rect(center_position[0], center_position[1], 10, 10))
            for pos in snapo1_body:
                impball = pygame.image.load("madden25_imgs/raiderx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo1_position[0], snapo1_position[1], 10, 10))
            for pos in snapo2_body:
                impball = pygame.image.load("madden25_imgs/raiderx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo2_position[0], snapo2_position[1], 10, 10))
            for pos in snapo3_body:
                impball = pygame.image.load("madden25_imgs/raiderx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo3_position[0], snapo3_position[1], 10, 10))
            for pos in snapo4_body:
                impball = pygame.image.load("madden25_imgs/raiderx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo4_position[0], snapo4_position[1], 10, 10))
            for pos in snapo5_body:
                impball = pygame.image.load("madden25_imgs/raiderx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo5_position[0], snapo5_position[1], 10, 10))
            for pos in snapx1_body:
                impball = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx1_position[0], snapx1_position[1], 10, 10))
            for pos in snapx2_body:
                impball = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx2_position[0], snapx2_position[1], 10, 10))
            for pos in snapx3_body:
                impball = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx3_position[0], snapx3_position[1], 10, 10))
            for pos in snapx4_body:
                impball = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx4_position[0], snapx4_position[1], 10, 10))
            for pos in snapx5_body:
                impball = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx5_position[0], snapx5_position[1], 10, 10))
            for pos in snapx6_body:
                impball = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx6_position[0], snapx6_position[1], 10, 10))
                
            timer_position[0] = 0
            if snapo1_position[0] < 170 and snapo1_position[0] >= 155:
                snapo1_position[0] += 10 
            elif snapo1_position[0] >= 170:
                snapo1_position[0] -= 10
            if snapo2_position[0] < 170 and snapo1_position[0] >= 155:
                snapo2_position[0] += 10 
            elif snapo2_position[0] >= 170:
                snapo2_position[0] -= 10
            if snapo3_position[0] < 170 and snapo1_position[0] >= 155:
                snapo3_position[0] += 10 
            elif snapo3_position[0] >= 170:
                snapo3_position[0] -= 10
            if snapo4_position[0] < 170 and snapo1_position[0] >= 155:
                snapo4_position[0] += 10 
            elif snapo4_position[0] >= 170:
                snapo4_position[0] -= 10
            if snapo5_position[0] < 170 and snapo1_position[0] >= 155:
                snapo5_position[0] += 10 
            elif snapo5_position[0] >= 170:
                snapo5_position[0] -= 10

            if snapx1_position[0] > 200 and snapx1_position[0] <= 225:
                snapx1_position[0] -= 10 
            elif snapx1_position[0] <= 200:
                snapx1_position[0] += 10
            if snapx2_position[0] > 200 and snapx1_position[0] <= 225:
                snapx2_position[0] -= 10 
            elif snapx2_position[0] <= 200:
                snapx2_position[0] += 10
            if snapx3_position[0] > 200 and snapx1_position[0] <= 225:
                snapx3_position[0] -= 10 
            elif snapx3_position[0] <= 200:
                snapx3_position[0] += 10
            if snapx4_position[0] > 200 and snapx1_position[0] <= 225:
                snapx4_position[0] -= 10 
            elif snapx4_position[0] <= 200:
                snapx4_position[0] += 10
            if snapx5_position[0] > 200 and snapx1_position[0] <= 225:
                snapx5_position[0] -= 10 
            elif snapx5_position[0] <= 200:
                snapx5_position[0] += 10
            if snapx6_position[0] > 135 and snapx1_position[0] <= 225:
                snapx6_position[0] -= 10 
            elif snapx6_position[0] <= 135:
                snapx6_position[0] += 10
                if center_position[0] < 100 and snapo1_position[0] >= 135:
                    center_position[0] += 10 
                elif center_position[0] >= 100:
                    center_position[0] -= 10

            if play == 1:

                # Moving the player 
                if direction == 'UP':
                    player_position[1] -= 10 + speedmeter
                if direction == 'DOWN':
                    player_position[1] += 10 + speedmeter
                if direction == 'LEFT':
                    player_position[0] -= 10 + speedmeter
                if direction == 'RIGHT':
                        player_position[0] += 10 + speedmeter

                ball_dist = pygame.Vector2(player_position).distance_to(ball_position)
                if ball_dist < 10:
                    if ball_position[0] >= 200:
                        catch()
                        ballcatch = 1
                        direction = 'RIGHT'
                if ballcatch != 1:
                    for pos in ball_body:
                        impball = pygame.image.load("madden25_imgs/football.png").convert()
                        game_window.blit(impball, pygame.Rect(ball_position[0], ball_position[1], 10, 10))

                ball_direction_start = random.choice(ball_direction)
                ball_position[0] += 5 
                
                if ballcatch != 1:
                    if ball_direction_start == 2:
                        ball_position[1] += 5 
                    elif ball_direction_start == 3:
                        ball_position[1] -= 5 
                    
                    if ball_position[0] > 1300:
                        incompletion()
                        down = down + 1
                        ball_position[0] = 200

                    if ball_position[1] < 50:
                        ball_position[1] = 50

                    if ball_position[1] > 500:
                        ball_position[1] = 500

                if player_position[0] >= 1300:
                    if ballcatch == 0:
                        player_position[0] = 1300
                    else:
                        player_position[0] = 50
                        snap = 2
                        yardline += 10
                    
        if snap == 2 and ballcatch == 1:

            # Moving the player 
            if direction == 'UP':
                player_position[1] -= 10 + speedmeter
            if direction == 'DOWN':
                player_position[1] += 10 + speedmeter
            if direction == 'LEFT':
                player_position[0] -= 10 + speedmeter
            if direction == 'RIGHT':
                    player_position[0] += 10 + speedmeter
            
            for pos in field_lines_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(pos[0] + 20, pos[1], 10, 10))
            for pos in field_lines_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(pos[0] + 20, pos[1] + 550, 10, 10))   

            for pos in player_body:
                if direction == 'LEFT':
                    impplayer = pygame.image.load("madden25_imgs/raider0_flip.png").convert()
                if direction == 'RIGHT':
                    impplayer = pygame.image.load("madden25_imgs/raider0.png").convert()
                game_window.blit(impplayer, pygame.Rect(player_position[0], player_position[1], 10, 10))

            compx_dist = pygame.Vector2(player_position).distance_to(compx_position)
            if compx_dist < 10:
                if down <= 5:
                    if compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()     
            compx1_dist = pygame.Vector2(player_position).distance_to(compx1_position)
            if compx1_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx1_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()      
            compx2_dist = pygame.Vector2(player_position).distance_to(compx2_position)
            if compx2_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx2_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()      
            compx3_dist = pygame.Vector2(player_position).distance_to(compx3_position)
            if compx3_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx4_down != 1 and ballcatch == 1:
                        downs()
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205   
                        gb_position[1] = 305                     
                        compx3_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    game_over()      
            compx4_dist = pygame.Vector2(player_position).distance_to(compx4_position)
            if compx4_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and ballcatch == 1:
                        downs()
                        play = 0 
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx4_down = 1
                        down = down + 1
                    change_to ='RIGHT'
                else:
                    down = 1
                    game_over()   

            player_body.insert(0, list(player_position))
            player_body.pop() 
            
            if compx_position[0] > player_position[0]:
                if yardline < 50:
                    compx_position[0] -= random.randint(5,8)
                else:
                    compx_position[0] -= random.randint(7,10)
                compx_direction = 'LEFT'
            if compx_position[0] < player_position[0]:
                if yardline < 50:
                    compx_position[0] += random.randint(5,8)
                else:
                    compx_position[0] += random.randint(7,10)
                compx_direction = 'RIGHT'
            if compx_position[1] > player_position[1]:
                if yardline < 50:
                    compx_position[1] -= random.randint(5,8)
                else:
                    compx_position[1] -= random.randint(7,10)
            if compx_position[1] < player_position[1]:
                if yardline < 50:
                    compx_position[1] += random.randint(5,8)
                else:
                    compx_position[1] += random.randint(7,10)

            if compx1_position[0] > player_position[0]:
                if yardline < 50:
                    compx1_position[0] -= random.randint(5,8)
                else:
                    compx1_position[0] -= random.randint(7,10)
                compx1_direction = 'LEFT'
            if compx1_position[0] < player_position[0]:
                if yardline < 50:
                    compx1_position[0] += random.randint(5,8)
                else:
                    compx1_position[0] += random.randint(7,10)
                compx1_direction = 'RIGHT'
            if compx1_position[1] > player_position[1]:
                if yardline < 50:
                    compx1_position[1] -= random.randint(5,8)
                else:
                    compx1_position[1] -= random.randint(7,10)
            if compx1_position[1] < player_position[1]:
                if yardline < 50:
                    compx1_position[1] += random.randint(5,8)
                else:
                    compx1_position[1] += random.randint(7,10)
            if compx2_position[0] > player_position[0]:
                if yardline < 50:
                    compx2_position[0] -= random.randint(5,8)
                else:
                    compx2_position[0] -= random.randint(7,10)
                compx2_direction = 'LEFT'
            if compx2_position[0] < player_position[0]:
                if yardline < 50:
                    compx2_position[0] += random.randint(5,8)
                else:
                    compx2_position[0] += random.randint(7,10)
                compx2_direction = 'RIGHT'
            if compx2_position[1] > player_position[1]:
                if yardline < 50:
                    compx2_position[1] -= random.randint(5,8)
                else:
                    compx2_position[1] -= random.randint(7,10)
            if compx2_position[1] < player_position[1]:
                if yardline < 50:
                    compx2_position[1] += random.randint(5,8)
                else:
                    compx2_position[1] += random.randint(7,10)
            if compx3_position[0] > player_position[0]:
                if yardline < 50:
                    compx3_position[0] -= random.randint(5,8)
                else:
                    compx3_position[0] -= random.randint(7,10)
                compx3_direction = 'LEFT'
            if compx3_position[0] < player_position[0]:
                if yardline < 50:
                    compx3_position[0] += random.randint(5,8)
                else:
                    compx3_position[0] += random.randint(7,10)
                compx3_direction = 'RIGHT'
            if compx3_position[1] > player_position[1]:
                if yardline < 50:
                    compx3_position[1] -= random.randint(5,8)
                else:
                    compx3_position[1] -= random.randint(7,10)
            if compx3_position[1] < player_position[1]:
                if yardline < 50:
                    compx3_position[1] += random.randint(5,8)
                else:
                    compx3_position[1] += random.randint(7,10)

            if compx4_position[0] > player_position[0]:
                if yardline < 50:
                    compx4_position[0] -= random.randint(5,8)
                else:
                    compx4_position[0] -= random.randint(7,10)
                compx4_direction = 'LEFT'
            if compx4_position[0] < player_position[0]:
                if yardline < 50:
                    compx4_position[0] += random.randint(5,8)
                else:
                    compx4_position[0] += random.randint(7,10)
                compx4_direction = 'RIGHT'
            if compx4_position[1] > player_position[1]:
                if yardline < 50:
                    compx4_position[1] -= random.randint(5,8)
                else:
                    compx4_position[1] -= random.randint(7,10)
            if compx4_position[1] < player_position[1]:
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

            if compx1 == 1:
                for pos in compx1_body:
                    if compx1_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx1_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx1_position[0], compx1_position[1], 10, 10))
            if compx2 == 1:
                for pos in compx2_body:
                    if compx2_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx2_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx2_position[0], compx2_position[1], 10, 10))
            if compx3 == 1:
                for pos in compx3_body:
                    if compx3_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx3_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx3_position[0], compx3_position[1], 10, 10))
            if compx == 4:
                for pos in compx4_body:
                    if compx4_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx4_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx4_position[0], compx4_position[1], 10, 10))

            show_yardline(1, white, 'Arial', 80)
            show_nextyardline(1, white, 'Arial', 80)

        show_speed(1, white, 'Arial', 30)
        show_downs(1, white, 'Arial', 30)
        show_score(1, white, 'Arial', 30)

    pygame.display.update()

    fps.tick(player_speed)

    
