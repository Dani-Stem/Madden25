# importing libraries
import pygame
import time
import random
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


# Window size
window_x = 1368
window_y = 712

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 71, 171)
yellow = pygame.Color(255, 215, 0)

#window and fps settings 
pygame.init()
pygame.display.set_caption('MADDEN 2K25')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

#defining all coordanates 
compx_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx_down = 0
compx1_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx1_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx1_down = 0
compx2_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx2_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx2_down = 0
compx3_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx3_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx3_down = 0
compx4_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx4_body = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
compx4_down = 0

ball_body = [300, random.randrange(1, ((window_y - 50)//10)) * 10]
ball_position = [300, random.randrange(1, ((window_y - 50)//10)) * 10]

field_lines_blue_body = [[120, 60],
                        [120, 70],
                        [120, 80],
                        [120, 90],
                        [120, 100]]

field_lines_yellow_body = [[1200, 60],
                        [1200, 70],
                        [1200, 80],
                        [1200, 90],
                        [1200, 100]]
field_line_10 = 120
field_line_9 = 240
field_line_8 = 360
field_line_7 = 480
field_line_6 = 600
field_line_5 = 720
field_line_4 = 840
field_line_3 = 960
field_line_2 = 1080
field_line_1 = 1200

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
timergo_body = [0, 710]
timergo_position = [0, 710]
timerpc_body = [0, 710]
timerpc_position = [0, 710]
timerfg_body = [0, 710]
timerfg_position = [0, 710]
timergoal_body = [0, 710]
timergoal_position = [0, 710]
timersnap_body = [0, 710]
timersnap_position = [0, 710]
timerpo_body = [0, 710]
timerpo_position = [0, 710]
timersack_body = [0, 710]
timersack_position = [0, 710]
timeroppsgoal_body = [0, 710]
timeroppsgoal_position = [0, 710]

gb_body = [10, 305]
gb_position = [10, 305]

pc_body = [380, 200]
pc_position = [380, 200]

urball_body = [80, 305]
urball_position = [80, 305]

center_body = [80, 305]
center_position = [80, 305]

player_body = [50, 205]
player_position = [50, 205]

oppsgoal_body = [380, 200]
oppsgoal_position = [380, 200]

gameover_body = [380, 200]
gameover_position = [380, 200]

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

logo_body = [195, 200]
logo_position = [195, 200]

howto_body = [675, 180]
howto_position = [675, 180]

quarter_body = [975, 225]
quarter_position = [975, 225]

cfi_body = [100, 200]
cfi_position = [100, 200]

callchoice_body = [380, 300]
callchoice_position = [380, 300]


#decalring all variables
player_speed = 15
direction = ''
key = ''
change_to = direction
ball_direction = [1, 2, 3]
score = [0, 0] 
play = 0
down = 1
yardline = 10
yard = 10
field_goal = '0'
play_promt = '0'
speedmeter = 0
play = 0 
power = 0
spacebar_count = 0
snap = 0
ballcatch = 0
down_yard = 10
start_screen = 0
quarter = 'HEADS'
teamquarter = ''
rand0oppscallball = [0, 1]
oppscallball = 3
oppssnap = 0
rand0oppgoall = [1, 2]
oppsgoal = 1
randpc = [1, 4]
pc = 1
yard1_position = 120
yard2_position = 240
yard3_position = 360
yard4_position = 480
yard5_position = 600
yard6_position = 720
yard7_position = 840
yard8_position = 960
yard9_position = 1080
yard10_position = 1225

#functions
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
        down_surface = my_font.render(str(down) + 'ST & ' + str(yard), True, white)
    elif down == 2:
        down_surface = my_font.render(str(down) + 'ND & ' + str(yard), True, white)
    elif down == 3:
        down_surface = my_font.render(str(down) + 'RD & ' + str(yard), True, white)
    elif down == 4:
        down_surface = my_font.render(str(down) + 'TH & ' + str(yard), True, white)
    elif down > 4:
        down_surface = my_font.render('1ST & 10' , True, white)

    down_rect = down_surface.get_rect()
    down_rect.midtop = (600, 5)
    game_window.blit(down_surface, down_rect)

def show_downsfieldgoal(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    if down == 1:
        down_surface = my_font.render(str(down) + 'ST & ' + str(yard), True, white)
    elif down == 2:
        down_surface = my_font.render(str(down) + 'ND & ' + str(yard), True, white)
    elif down == 3:
        down_surface = my_font.render(str(down) + 'RD & ' + str(yard), True, white)
    elif down == 4:
        down_surface = my_font.render(str(down) + 'TH & ' + str(yard), True, white)
    elif down > 4:
        down_surface = my_font.render('1ST & 10' , True, white)


    down_rect = down_surface.get_rect()
    down_rect.midtop = (105, 655)
    game_window.blit(down_surface, down_rect)

def show_yardonstart(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    speed_surface = my_font.render(
        'YARD: ' + str(yardline), True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (100, 5)
    game_window.blit(speed_surface, speed_rect)

def show_speed(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    speed_surface = my_font.render(
        'SPEED:' , True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (100, 5)
    game_window.blit(speed_surface, speed_rect)

def show_quarter(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 50)
    speed_surface = my_font.render(
        quarter, True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (1070, 475)
    game_window.blit(speed_surface, speed_rect)

def show_teamquarter(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 40)
    speed_surface = my_font.render(
        "YOUR TEAM CHOOSES " + teamquarter, True, yellow)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (430, 475)
    game_window.blit(speed_surface, speed_rect)

def show_fieldgoal(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    speed_surface = my_font.render(
        'QUICKLY & REPEATEDLY TAP THE SPACE BAR' , True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (670, 25)
    game_window.blit(speed_surface, speed_rect)

def show_startscreen(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 30)
    speed_surface = my_font.render(
        'MADDEN25' , True, yellow)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (310, 480)
    game_window.blit(speed_surface, speed_rect)

def show_startscreensub(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 15)
    speed_surface = my_font.render(
        'A DN INDUSTRIES PRODUCT' , True, yellow)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (306, 515)
    game_window.blit(speed_surface, speed_rect)

def show_startscreensub1(choice, color, font, size):
  
    my_font = pygame.font.SysFont('Arial', 35)
    speed_surface = my_font.render(
        'PRESS S TO START THE GAME', True, white)
    speed_rect = speed_surface.get_rect()
    speed_rect.midtop = (906, 525)
    game_window.blit(speed_surface, speed_rect)

def show_nextyardline(choice, color, font, size):
  
    if yardline < 90:

        nextyardline_font = pygame.font.SysFont(font, size)
        nextyardline_surface = nextyardline_font.render(str(yardline + 10), True, color)
        nextyardline_rect = nextyardline_surface.get_rect()
        if yard == 1:
            nextyardline_rect.midtop = (120, 300)
        if yard == 2:
            nextyardline_rect.midtop = (240, 300)
        if yard == 3:
            nextyardline_rect.midtop = (360, 300)
        if yard == 4:
            nextyardline_rect.midtop = (480, 300)
        if yard == 5:
            nextyardline_rect.midtop = (600, 300)
        if yard == 6:
            nextyardline_rect.midtop = (720, 300)
        if yard == 7:
            nextyardline_rect.midtop = (840, 300)
        if yard == 8:
            nextyardline_rect.midtop = (960, 300)
        if yard == 9:
            nextyardline_rect.midtop = (1080, 300)
        if yard == 10:
            nextyardline_rect.midtop = (1225, 300)
        game_window.blit(nextyardline_surface, nextyardline_rect)
    
    else:
        #G
        goallineg_font = pygame.font.SysFont(font, size)
        goallineg_surface =  goallineg_font.render('G', True, color)
        goallineg_rect =  goallineg_surface.get_rect()
        if yard == 1:
            goallineg_rect.midtop = (120, 160)
        if yard == 2:
            goallineg_rect.midtop = (240, 160)
        if yard == 3:
            goallineg_rect.midtop = (360, 160)
        if yard == 4:
            goallineg_rect.midtop = (480, 160)
        if yard == 5:
            goallineg_rect.midtop = (600, 160)
        if yard == 6:
            goallineg_rect.midtop = (720, 160)
        if yard == 7:
            goallineg_rect.midtop = (840, 160)
        if yard == 8:
            goallineg_rect.midtop = (960, 160)
        if yard == 9:
            goallineg_rect.midtop = (1080, 160)
        if yard == 10:
            goallineg_rect.midtop = (1225, 160)
        game_window.blit( goallineg_surface,  goallineg_rect)
        
        #O
        goallineo_font = pygame.font.SysFont(font, size)
        goallineo_surface =  goallineo_font.render('O', True, color)
        goallineo_rect =  goallineo_surface.get_rect()
        if yard == 1:
            goallineo_rect.midtop = (120, 260)
        if yard == 2:
            goallineo_rect.midtop = (240, 260)
        if yard == 3:
            goallineo_rect.midtop = (360, 260)
        if yard == 4:
            goallineo_rect.midtop = (480, 260)
        if yard == 5:
            goallineo_rect.midtop = (600, 260)
        if yard == 6:
            goallineo_rect.midtop = (720, 260)
        if yard == 7:
            goallineo_rect.midtop = (840, 260)
        if yard == 8:
            goallineo_rect.midtop = (960, 260)
        if yard == 9:
            goallineo_rect.midtop = (1080, 260)
        if yard == 10:
            goallineo_rect.midtop = (1225, 260)
        game_window.blit( goallineo_surface,  goallineo_rect)
        
        #A
        goallinea_font = pygame.font.SysFont(font, size)
        goallinea_surface =  goallinea_font.render('A', True, color)
        goallinea_rect =  goallinea_surface.get_rect()
        if yard == 1:
            goallinea_rect.midtop = (120, 360)
        if yard == 2:
            goallinea_rect.midtop = (240, 360)
        if yard == 3:
            goallinea_rect.midtop = (360, 360)
        if yard == 4:
            goallinea_rect.midtop = (480, 360)
        if yard == 5:
            goallinea_rect.midtop = (600, 360)
        if yard == 6:
            goallinea_rect.midtop = (720, 360)
        if yard == 7:
            goallinea_rect.midtop = (840, 360)
        if yard == 8:
            goallinea_rect.midtop = (960, 360)
        if yard == 9:
            goallinea_rect.midtop = (1080, 360)
        if yard == 10:
            goallinea_rect.midtop = (1225, 360)
        game_window.blit( goallinea_surface,  goallinea_rect)
        
        #L
        goallinel_font = pygame.font.SysFont(font, size)
        goallinel_surface =  goallinel_font.render('L', True, color)
        goallinel_rect =  goallinel_surface.get_rect()
        if yard == 1:
            goallinel_rect.midtop = (120, 460)
        if yard == 2:
            goallinel_rect.midtop = (240, 460)
        if yard == 3:
            goallinel_rect.midtop = (360, 460)
        if yard == 4:
            goallinel_rect.midtop = (480, 460)
        if yard == 5:
            goallinel_rect.midtop = (600, 460)
        if yard == 6:
            goallinel_rect.midtop = (720, 460)
        if yard == 7:
            goallinel_rect.midtop = (840, 460)
        if yard == 8:
            goallinel_rect.midtop = (960, 460)
        if yard == 9:
            goallinel_rect.midtop = (1080, 460)
        if yard == 10:
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
    print("DOWN")
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
    downs_surface = my_font.render('NO GOOD. OPPS BALL', True, red)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = ((window_x/2) - 70, 600)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()
    time.sleep(2)

def urcall():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('YOUR CALL', True, green)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (700, 100)
    game_window.blit(downs_surface, downs_rect)
    pygame.display.flip()

def oppscall():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('OPPONENTS CALL', True, red)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (700, 200)
    game_window.blit(downs_surface, downs_rect)

def oppscall1():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('THEIR BALL', True, yellow)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (700, 300)
    game_window.blit(downs_surface, downs_rect)

def oppscall2():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('YOUR BALL', True, yellow)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (700, 300)
    game_window.blit(downs_surface, downs_rect)

def defend():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('STOP THE', True, yellow)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (700, 200)
    game_window.blit(downs_surface, downs_rect)

def defend1():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('RECIEVER', True, yellow)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (700, 300)
    game_window.blit(downs_surface, downs_rect)


def sack():

    my_font = pygame.font.SysFont('Arial', 70)
    downs_surface = my_font.render('HE DOWN', True, green)
    downs_rect = downs_surface.get_rect()
    downs_rect.midtop = (700, 300)
    game_window.blit(downs_surface, downs_rect)   
    pygame.display.update()
    time.sleep(2) 

def show_urball(choice, color, font, size):

    my_font = pygame.font.SysFont('Arial', 50)
    score_surface = my_font.render(
        'YOUR BALL', True, green)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (6500, 300)
    game_window.blit(score_surface, score_rect)
   
#game start  
while True:

    game_window.fill(black)

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                change_to = 's'
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
                    if yardline < 50:
                        speedmeter -= 3
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
        if change_to == 's':
            key = 's'

    #start the game screen
    if play_promt == '0' and start_screen == 0:

        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1], 10, 10))
        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1] + 550, 10, 10)) 
              
        show_startscreen(1, white, 'Arial', 80)
        show_startscreensub(1, white, 'Arial', 70)
        timer_position[0] += 75
        if timer_position[0] > 1300:
            timer_position[0] = 0
        if timer_position[0] > 750:
            show_startscreensub1(1, white, 'Arial', 70)

        for pos in logo_body:   
            implogo = pygame.image.load("madden25_imgs/logo.png").convert()
            game_window.blit(implogo, pygame.Rect(logo_position[0], logo_position[1], 10, 10))

        for pos in howto_body:   
            impht = pygame.image.load("madden25_imgs/howtoplay.png").convert()
            game_window.blit(impht, pygame.Rect(howto_position[0], howto_position[1], 10, 10))

        if key == 's':
            start_screen = 1
            play_promt = 'coinflip'
            teamquarteroptions = ['HEADS', 'TAILS']
            teamquarter = random.choice(teamquarteroptions)

   #coin flip game play
    if play_promt == 'coinflip' and start_screen == 1:

        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1], 10, 10))
        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1] + 550, 10, 10))
            
        timer_position[0] += 225
        if timer_position[0] > 1300  and key != 'SPACE':
            timer_position[0] = 0
            quarter = 'HEADS'
        if timer_position[0] > 975 and timer_position[0] < 1300  and key != 'SPACE':
            quarter = 'edge'
        if timer_position[0] > 650 and timer_position[0] < 975  and key != 'SPACE':
            quarter = 'TAILS'
        if timer_position[0] > 325 and timer_position[0] < 650 and key != 'SPACE':
            quarter = 'edge'

        if key == 'SPACE':
            if quarter == 'edge':
                quarteroptions = ['HEADS', 'TAILS']
                quarter = random.choice(quarteroptions)
                timer_position[0] = 0
            if teamquarter != quarter:
                play_promt = 'lose'
                timer_position[0] = 0
            elif teamquarter == quarter:
                timer_position[0] = 0
                play_promt = 'win'
            start_screen = 1

        for pos in quarter_body:   
            if quarter == 'HEADS':
                impquarter = pygame.image.load("madden25_imgs/HEADS.jpg").convert()
                game_window.blit(impquarter, pygame.Rect(quarter_position[0], quarter_position[1], 10, 10))
            if quarter == 'edge':
                impquarter = pygame.image.load("madden25_imgs/edge.jpg").convert()
                game_window.blit(impquarter, pygame.Rect(quarter_position[0]+100, quarter_position[1], 10, 10))
            if quarter == 'TAILS':
                impquarter = pygame.image.load("madden25_imgs/TAILS.jpg").convert()
                game_window.blit(impquarter, pygame.Rect(quarter_position[0], quarter_position[1], 10, 10))

        for pos in cfi_body:
                impcfi = pygame.image.load("madden25_imgs/constructions.png").convert()
                game_window.blit(impcfi, pygame.Rect(cfi_position[0], cfi_position[1], 10, 10))
        
        if key == 'SPACE' and quarter != 'edge':
            show_teamquarter(1, white, 'Arial', 100)
            pygame.display.update()
            time.sleep(2)

        show_teamquarter(1, white, 'Arial', 100)
        print("quarter: " + str(quarter))
        print("teamquarter: " + str(teamquarter))
        print("playprompt: " + play_promt)

    #if you lose the coin flip screen
    if play_promt == 'lose' and start_screen == 1:
        for pos in timer_body:
            pygame.draw.rect(game_window, white, pygame.Rect(timer_position[0], timer_position[1], 10, 10))   

        if timer_position[0] < 1300:
            timer_position[0] += 50

        if oppscallball == 3:
            oppscallball = random.choice(rand0oppscallball)
        oppscall()
        if oppscallball == 0:
            oppscall1()
            if timer_position[0] >= 1300:
                play_promt = '3'
                timeroppsgoal_position[0] = 0
                start_screen = 1
        if oppscallball == 1:
            oppscall2()
            if timer_position[0] >= 1300:
                play_promt = '0'
                start_screen = 1

    #if you win the coin flip screen
    if play_promt == 'win' and start_screen == 1:

        if direction == 'RIGHT':
            if selection_position[0] <= 704:
                selection_position[0] += 93
            if selection_position[0] > 740:
                selection_position[0] = 740
        if direction == 'LEFT':
                if selection_position[0] > 325:
                    selection_position[0] -= 93
                if selection_position[0] < 325:
                    selection_position[0] = 325
            
        for pos in callchoice_body:
            impcc = pygame.image.load("madden25_imgs/callchoice.png").convert()
            game_window.blit(impcc, pygame.Rect(callchoice_position[0]-35, callchoice_position[1], 10, 10))

        for pos in selection_body:
            pygame.draw.rect(game_window, white, pygame.Rect(selection_position[0], pos[1], 300, 10))

        for pos in timer_body:
            pygame.draw.rect(game_window, white, pygame.Rect(timer_position[0], timer_position[1], 10, 10))   

        if key == 'ENTER':    
            if timer_position[0] < 1300:
                timer_position[0] += 100

        if key == 'ENTER' and selection_position[0] > 624:
            if timer_position[0] >= 1300:
                play_promt = '3'
                timeroppsgoal_position[0] = 0
                start_screen = 1
                key = ''
        if key == 'ENTER' and  selection_position[0] < 624:
            if timer_position[0] >= 1300:
                play_promt = '0'
                start_screen = 1
                key = ''

        urcall()

    #your ball choose to kick or run screen
    if play_promt == '0' and start_screen == 1:

        if yard == 10:
            down

        if yard == 1:
            yard = 10

        compx_down = 0
        compx_down1 = 0
        compx_down2 = 0
        compx_down3 = 0
        compx_down4 = 0

        if score[0] >= 30 or score[1] >= 30:
            start_screen = 0
            play_promt = 'gameover'
            
        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1], 10, 10))
        for pos in field_lines_body:
            pygame.draw.rect(game_window, white,
                            pygame.Rect(pos[0] + 20, pos[1] + 550, 10, 10))  
            
        for pos in urball_body:
            impgoal = pygame.image.load("madden25_imgs/urball.png").convert()
            game_window.blit(impgoal, pygame.Rect(fieldgoal_position[0], fieldgoal_position[1], 10, 10))

        for pos in timerpo_body:
            pygame.draw.rect(game_window, white, pygame.Rect(timerpo_position[0], timerpo_position[1], 10, 10))   

        if key == 'ENTER':    
            if timerpo_position[0] < 1300:
                timerpo_position[0] += 100

        if direction == 'RIGHT':
            if selection_position[0] <= 624:
                selection_position[0] += 93
        if direction == 'LEFT':
                if selection_position[0] > 325:
                    selection_position[0] -= 93

        if key == 'ENTER' and selection_position[0] < 624 and timerpo_position[0] >= 1300:
            play_promt = '1'
            key = ''
        if key == 'ENTER' and  selection_position[0] > 325 and timerpo_position[0] >= 1300:
            play_promt = '2'
            key = ''

        for pos in selection_body:
            pygame.draw.rect(game_window, white, pygame.Rect(selection_position[0], pos[1], 300, 10))
            
        show_downs(1, white, 'Arial', 100)    
        show_score(1, white, 'Arial', 100)    
        show_yardonstart(1, white, 'Arial', 100)  
        show_playoptions(1, white, 'Arial', 100)
        show_urball(1, green, 'Arial', 100)
            
    #if kick was chosen game play 
    if play_promt == '1':

            for pos in fieldgoal_body:
                impgoal = pygame.image.load("madden25_imgs/fieldgoal.png").convert()
                game_window.blit(impgoal, pygame.Rect(fieldgoal_position[0], fieldgoal_position[1], 10, 10))

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

            for pos in timerfg_body:
                pygame.draw.rect(game_window, white,
                                pygame.Rect(timerfg_position[0], timerfg_position[1], 10, 10))       

            timerfg_position[0] += 10    

            if key == 'SPACE' and timerfg_position[0] < 1300:
                direction = 'RIGHT'
            elif key == 'SPACE' and timerfg_position[0] >= 1300:
                direction = ''

            if timerfg_position[0] < 1300:
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

            if timerfg_position[0] >= 1300:
                if spacebar_count >= 8 and fieldgoalball_position[1] > 300 and yardline >= 70:
                    fieldgoalball_position[1] -= 10
                    if fieldgoalball_position[1] <= 300:
                        goal()
                        key = ''
                        if score[0] >= 30 or score[1] >= 30:
                            play_promt = 'gameover'
                        else:
                            snap = 0
                            start_screen = 1  
                            play_promt = '3'  
                            yard = 10
                            yardline = 10
                            timeroppsgoal_position[0] = 0
                        fieldgoalball_position[0] = 680
                        fieldgoalball_position[1] = 630
                        spacebar_count = 0
                        timerfg_position[0] = 0
                        score[0] += 3

                elif spacebar_count >= 8 and fieldgoalball_position[1] > 300 and yardline < 70:
                    fieldgoalball_position[0] -= 5
                    fieldgoalball_position[1] -= 10
                    if fieldgoalball_position[1] <= 300:
                        miss()
                        play_promt = '3'
                        timeroppsgoal_position[0] = 0 
                        yard = 10
                        yardline = 10
                        print(play_promt)
                        fieldgoalball_position[0] = 680
                        fieldgoalball_position[1] = 630
                        spacebar_count = 0
                        timerfg_position[0] = 0

                elif spacebar_count < 8 and spacebar_count > 3 and fieldgoalball_position[1] > 250:
                    fieldgoalball_position[0] -= 5
                    fieldgoalball_position[1] -= 10
                    if fieldgoalball_position[1] <= 250:
                        miss()
                        play_promt = '3'
                        timeroppsgoal_position[0] = 0 
                        yard = 10
                        yardline = 10
                        print(play_promt)
                        fieldgoalball_position[0] = 680
                        fieldgoalball_position[1] = 630
                        spacebar_count = 0
                        timerfg_position[0] = 0

                elif spacebar_count < 4 and fieldgoalball_position[1] > 270:
                    fieldgoalball_position[0] += 5
                    fieldgoalball_position[1] -= 10
                    if fieldgoalball_position[1] <= 270:
                        miss()  
                        play_promt = '3'
                        timeroppsgoal_position[0] = 0 
                        yard = 10
                        yardline = 10
                        print(play_promt)
                        fieldgoalball_position[0] = 680
                        fieldgoalball_position[1] = 630
                        spacebar_count = 0
                        timerfg_position[0] = 0

            power_range = [0,0,1]
            power = random.choice(power_range)

            if power == 1:
                if timerfg_position[0] < 1300:
                    if speedmeter > -2:
                        speedmeter -=1
                        spacebar_count -= 1

            show_fieldgoal(1, white, 'Arial', 30)
            show_downsfieldgoal(1, white, 'Arial', 30)
            show_scorefieldgoal(1, white, 'Arial', 30)
    
    #if run was chosen game play
    if play_promt == '2':

        if player_position[0] < 0:
            player_position[0] = 0

        if player_position[0] > 1300:
            if ballcatch == 1:
                speedmeter = 0
                compx_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
                compx1_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
                compx2_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
                compx3_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
                compx4_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
                snap = 2

                player_position[0] = 0
                yardline = yardline + 10
                down = 1

    
        if yardline > 80:
            if yard == 1 and player_position[0] >= yard1_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('1')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 2 and player_position[0] >= yard2_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('2')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 3 and player_position[0] >= yard3_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('3')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 4 and player_position[0] >= yard4_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('4')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 5 and player_position[0] >= yard5_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('5')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 6 and player_position[0] >= yard6_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('6')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 7 and player_position[0] >= yard7_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('7')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 8 and player_position[0] >= yard8_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('8')
                play_promt = 'pc' 
                player_position[0] = 0
                down = 1
            if yard == 9 and player_position[0] >= yard9_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('9')
                play_promt = 'pc' 
                pc = random.choice(randpc)
                player_position[0] = 0
                down = 1
            if yard == 10 and player_position[0] >= yard10_position:
                goal()
                yard = 10
                yardline = 10
                key = ''
                score[0] += 6 
                print('10')
                play_promt = 'pc' 
                player_position[0] = 0
                down = 1

        if player_position[1] < 0:
            player_position[1] = 0

        if player_position[1] > 620:
            player_position[1] = 620

        if player_position[1] < 50:
            player_position[1] = 50
            if ballcatch == 1:
                down_yard = player_position[0]
                outofbounds()
                play_promt = '0'
                play = 0 
                snap = 0  
                ballcatch = 0
                player_position[0] = 50
                player_position[1] = 205
                gb_position[1] = 305
                down += 1
            direction = 'RIGHT'

        if player_position[1] > 600:
            player_position[1] = 600
            if ballcatch == 1:
                down_yard = player_position[0]
                outofbounds()
                play_promt = '0'
                play = 0 
                snap = 0  
                ballcatch = 0
                player_position[0] = 50
                player_position[1] = 205
                gb_position[1] = 305
                down += 1
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
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))    
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
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

            for pos in timersnap_body:
                pygame.draw.rect(game_window, black,
                                pygame.Rect(timersnap_position[0], timersnap_position[1], 10, 10))       

            timersnap_position[0] += 40 
            if timersnap_position[0] > 1300:
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
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))  
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))  

            compx_dist = pygame.Vector2(player_position).distance_to(compx_position)
            if compx_dist < 10:
                if down <= 5:
                    if compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        print('down 1596')
                        downs()
                        key = ''
                        play_promt = '0'
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx_down = 1
                        down += 1
                    change_to ='RIGHT'
                else:
                    play_promt = 'gameover'        
            compx1_dist = pygame.Vector2(player_position).distance_to(compx1_position)
            if compx1_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 1617')
                        key = ''
                        play_promt = '0'
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx1_down = 1
                        down += 1
                    change_to ='RIGHT'
                else:
                    play_promt = 'gameover'    
            compx2_dist = pygame.Vector2(player_position).distance_to(compx2_position)
            if compx2_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 1637')
                        key = ''
                        play_promt = '0'
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
                    play_promt = 'gameover'   
            compx3_dist = pygame.Vector2(player_position).distance_to(compx3_position)
            if compx3_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx4_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 1657')
                        key = ''
                        play_promt = '0'
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx3_down = 1
                        down += 1
                    change_to ='RIGHT'
                else:
                    play_promt = 'gameover'  
            compx4_dist = pygame.Vector2(player_position).distance_to(compx4_position)
            if compx4_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 1677')
                        key = ''
                        play_promt = '0'
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx4_down = 1
                        down += 1
                    change_to ='RIGHT'
                else:
                    play_promt = 'gameover'  

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

            for pos in compx_body:
                if compx_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx_position[0], compx_position[1], 10, 10))
            for pos in compx1_body:
                if compx1_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx1_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx1_position[0], compx1_position[1], 10, 10))
            for pos in compx2_body:
                if compx2_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx2_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx2_position[0], compx2_position[1], 10, 10))
            for pos in compx3_body:
                if compx3_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx3_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx3_position[0], compx3_position[1], 10, 10))
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
                
            timersnap_position[0] = 0
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

            if down_yard <= field_line_10:
                yard = 10
            if down_yard <= field_line_9 and down_yard >= field_line_10:
                yard = 9
            if down_yard <= field_line_8 and down_yard >= field_line_9:
                yard = 8
            if down_yard <= field_line_7 and down_yard >= field_line_8:
                yard = 7
            if down_yard <= field_line_6 and down_yard >= field_line_7:
                yard = 6
            if down_yard <= field_line_5 and down_yard >= field_line_6:
                yard = 5
            if down_yard <= field_line_4 and down_yard >= field_line_5:
                yard = 4
            if down_yard <= field_line_3 and down_yard >= field_line_4:
                yard = 3
            if down_yard <= field_line_2 and down_yard >= field_line_3:
                yard = 2
            if down_yard <= field_line_1 and down_yard >= field_line_2:
                yard = 1
            
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
                if ball_dist < 50 and ballcatch != 1:
                    if ball_position[0] >= 200:
                        catch()
                        ballcatch = 1
                        direction = 'RIGHT'
                        speedmeter = 0
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
                        play_promt = '0'
                        play = 0
                        snap = 0
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        down = down + 1
                        ball_position[0] = 0

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
                        down = 1
                        compx_down = 0
                        compx1_down = 0
                        compx2_down = 0
                        compx3_down = 0
                        compx4_down = 0
                    
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
                        down_yard = player_position[0]
                        downs()
                        print('down 2074')
                        key = ''
                        play_promt = '0'
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
                    play_promt = 'gameover'    
            compx1_dist = pygame.Vector2(player_position).distance_to(compx1_position)
            if compx1_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx2_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 2094')
                        key = ''
                        play_promt = '0'
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
                    play_promt = 'gameover'  
            compx2_dist = pygame.Vector2(player_position).distance_to(compx2_position)
            if compx2_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx3_down != 1 and compx4_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 2114')
                        key = ''
                        play_promt = '0'
                        play = 0
                        snap = 0
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        compx2_down = 1
                        down += 1
                    change_to ='RIGHT'
                else:
                    play_promt = 'gameover'    
            compx3_dist = pygame.Vector2(player_position).distance_to(compx3_position)
            if compx3_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx4_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 2134')
                        key = ''
                        play_promt = '0'
                        play = 0
                        snap = 0  
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205   
                        gb_position[1] = 305                     
                        compx3_down = 1
                        down += 1
                    change_to ='RIGHT'
                else:
                    play_promt = 'gameover'  
            compx4_dist = pygame.Vector2(player_position).distance_to(compx4_position)
            if compx4_dist < 10:
                if down <= 5:
                    if compx_down != 1 and compx1_down != 1 and compx2_down != 1 and compx3_down != 1 and ballcatch == 1:
                        down_yard = player_position[0]
                        downs()
                        print('down 2154')
                        key = ''
                        play_promt = '0'
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
                    play_promt = 'gameover'   

            if down_yard <= field_line_10:
                yard = 10
            if down_yard <= field_line_9 and down_yard >= field_line_10:
                yard = 9
            if down_yard <= field_line_8 and down_yard >= field_line_9:
                yard = 8
            if down_yard <= field_line_7 and down_yard >= field_line_8:
                yard = 7
            if down_yard <= field_line_6 and down_yard >= field_line_7:
                yard = 6
            if down_yard <= field_line_5 and down_yard >= field_line_6:
                yard = 5
            if down_yard <= field_line_4 and down_yard >= field_line_5:
                yard = 4
            if down_yard <= field_line_3 and down_yard >= field_line_4:
                yard = 3
            if down_yard <= field_line_2 and down_yard >= field_line_3:
                yard = 2
            if down_yard <= field_line_1 and down_yard >= field_line_2:
                yard = 1

            player_body.insert(0, list(player_position))
            player_body.pop() 
            #increaseing computers speed randomly
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


            for pos in compx_body:
                if compx_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()

                game_window.blit(impx, pygame.Rect(compx_position[0], compx_position[1], 10, 10))
            for pos in compx1_body:
                if compx1_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx1_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx1_position[0], compx1_position[1], 10, 10))
            for pos in compx2_body:
                if compx2_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx2_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx2_position[0], compx2_position[1], 10, 10))
            for pos in compx3_body:
                if compx3_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx3_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx3_position[0], compx3_position[1], 10, 10))
            for pos in compx4_body:
                if compx4_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx4_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx4_position[0], compx4_position[1], 10, 10))
        
        show_nextyardline(1, white, 'Arial', 80)
        show_speed(1, white, 'Arial', 30)
        show_downs(1, white, 'Arial', 30)
        show_score(1, white, 'Arial', 30)

    #opps ball tackle the reciver game play
    if play_promt == '3':

        if score[0] >= 30 or score[1] >= 30:
            start_screen = 0
            play_promt = 'gameover'

        if player_position[0] < 0:
            player_position[0] = 0

        if player_position[0] > 1300:
            player_position[0] = 1200

        if player_position[1] < 0:
            player_position[1] = 0

        if player_position[1] > 620:
            player_position[1] = 620

        if player_position[1] < 50:
            player_position[1] = 50

        if player_position[1] > 600:
            player_position[1] = 600

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
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))    
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))       

            for pos in player_body:
                impplayer = pygame.image.load("madden25_imgs/playercenter_flip.png").convert()
                game_window.blit(impplayer, pygame.Rect(player_position[0] + 300, player_position[1], 10, 10))
            for pos in gb_body:
                impball = pygame.image.load("madden25_imgs/ramgb0.png").convert()
                game_window.blit(impball, pygame.Rect(gb_position[0], gb_position[1], 10, 10))
            for pos in center_body:
                impball = pygame.image.load("madden25_imgs/ramcenter.png").convert()
                game_window.blit(impball, pygame.Rect(center_position[0], center_position[1], 10, 10))
            for pos in snapo1_body:
                impball = pygame.image.load("madden25_imgs/ramcenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo1_position[0], snapo1_position[1], 10, 10))
            for pos in snapo2_body:
                impball = pygame.image.load("madden25_imgs/ramcenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo2_position[0], snapo2_position[1], 10, 10))
            for pos in snapo3_body:
                impball = pygame.image.load("madden25_imgs/ramcenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo3_position[0], snapo3_position[1], 10, 10))
            for pos in snapo4_body:
                impball = pygame.image.load("madden25_imgs/ramcenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo4_position[0], snapo4_position[1], 10, 10))
            for pos in snapo5_body:
                impball = pygame.image.load("madden25_imgs/ramcenter.png").convert()
                game_window.blit(impball, pygame.Rect(snapo5_position[0], snapo5_position[1], 10, 10))
            for pos in snapx1_body:
                impball = pygame.image.load("madden25_imgs/raidercenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx1_position[0], snapx1_position[1], 10, 10))
            for pos in snapx2_body:
                impball = pygame.image.load("madden25_imgs/raidercenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx2_position[0], snapx2_position[1], 10, 10))
            for pos in snapx3_body:
                impball = pygame.image.load("madden25_imgs/raidercenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx3_position[0], snapx3_position[1], 10, 10))
            for pos in snapx4_body:
                impball = pygame.image.load("madden25_imgs/raidercenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx4_position[0], snapx4_position[1], 10, 10))
            for pos in snapx5_body:
                impball = pygame.image.load("madden25_imgs/raidercenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx5_position[0], snapx5_position[1], 10, 10))
            for pos in snapx5_body:
                impball = pygame.image.load("madden25_imgs/raidercenter_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx6_position[0], snapx6_position[1], 10, 10))

            for pos in timersnap_body:
                pygame.draw.rect(game_window, black,
                                pygame.Rect(timersnap_position[0], timersnap_position[1], 10, 10))       

            timersnap_position[0] += 40 
            if timersnap_position[0] > 1300:
                snap = 1
            if timersnap_position[0] < 1300:
                defend()
                defend1()
                timersack_position[0] = 0

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
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_blue_body:
                pygame.draw.rect(game_window, blue,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))  
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
                                pygame.Rect(pos[0] + 100, pos[1], 10, 10))
            for pos in field_lines_yellow_body:
                pygame.draw.rect(game_window, yellow,
                                pygame.Rect(pos[0] + 100, pos[1] + 550, 10, 10))  

            compx_dist = pygame.Vector2(player_position).distance_to(compx_position)
            if compx_dist < 10:
                if down <= 5:        
                    if direction == 'RIGHT':
                        player_position[0] -= 25                        
                    if direction == 'LEFT':
                        player_position[0] += 25                        
                    if direction == 'UP':
                        player_position[1] -= 25                        
                    if direction == 'DOWN':
                        player_position[1] += 25

            compx1_dist = pygame.Vector2(player_position).distance_to(compx1_position)
            if compx1_dist < 10:
                if down <= 5:   

                    if direction == 'RIGHT':
                        player_position[0] -= 35                        
                    if direction == 'LEFT':
                        player_position[0] += 35                        
                    if direction == 'UP':
                        player_position[1] -= 35                        
                    if direction == 'DOWN':
                        player_position[1] += 35

            compx2_dist = pygame.Vector2(player_position).distance_to(compx2_position)
            if compx2_dist < 10:
                if down <= 5:                      
                    if direction == 'RIGHT':
                        player_position[0] -= 15                        
                    if direction == 'LEFT':
                        player_position[0] += 15                        
                    if direction == 'UP':
                        player_position[1] -= 15                        
                    if direction == 'DOWN':
                        player_position[1] += 15
                else:
                    play_promt = 'gameover'      
            compx3_dist = pygame.Vector2(player_position).distance_to(compx3_position)
            if compx3_dist < 10:
                if down <= 5:                     
                    if direction == 'RIGHT':
                        player_position[0] -= 15                        
                    if direction == 'LEFT':
                        player_position[0] += 15                        
                    if direction == 'UP':
                        player_position[1] -= 15                        
                    if direction == 'DOWN':
                        player_position[1] += 15
                else:
                    play_promt = 'gameover'      
            compx4_dist = pygame.Vector2(player_position).distance_to(compx4_position)
            if compx4_dist < 10:
                if down <= 5:                    
                    if direction == 'RIGHT':
                        player_position[0] -= 25                        
                    if direction == 'LEFT':
                        player_position[0] += 25                        
                    if direction == 'UP':
                        player_position[1] -= 25                        
                    if direction == 'DOWN':
                        player_position[1] += 25
                else:
                    play_promt = 'gameover'  

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

            for pos in compx_body:
                if compx_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx_position[0], compx_position[1], 10, 10))
        
            for pos in compx1_body:
                if compx1_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx1_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx1_position[0], compx1_position[1], 10, 10))
        
            for pos in compx2_body:
                if compx2_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx2_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx2_position[0], compx2_position[1], 10, 10))
        
            for pos in compx3_body:
                if compx3_direction == 'RIGHT':
                    impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                elif compx3_direction == 'LEFT':
                    impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                game_window.blit(impx, pygame.Rect(compx3_position[0], compx3_position[1], 10, 10))
        
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
                if direction == 'LEFT':
                    impplayer = pygame.image.load("madden25_imgs/playersnap_flip.png").convert()
                if direction == 'RIGHT':
                    impplayer = pygame.image.load("madden25_imgs/playersnap.png").convert()
                game_window.blit(impplayer, pygame.Rect(player_position[0], player_position[1], 10, 10))

            for pos in gb_body:
                if play == 0:
                    impball = pygame.image.load("madden25_imgs/ramgb.png").convert()
                if play == 1:
                    impball = pygame.image.load("madden25_imgs/ram_catch.png").convert()
                game_window.blit(impball, pygame.Rect(gb_position[0], gb_position[1], 10, 10))
            for pos in center_body:
                impball = pygame.image.load("madden25_imgs/ramx.png").convert()
                game_window.blit(impball, pygame.Rect(center_position[0], center_position[1], 10, 10))
            for pos in snapo1_body:
                impball = pygame.image.load("madden25_imgs/ramx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo1_position[0], snapo1_position[1], 10, 10))
            for pos in snapo2_body:
                impball = pygame.image.load("madden25_imgs/ramx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo2_position[0], snapo2_position[1], 10, 10))
            for pos in snapo3_body:
                impball = pygame.image.load("madden25_imgs/ramx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo3_position[0], snapo3_position[1], 10, 10))
            for pos in snapo4_body:
                impball = pygame.image.load("madden25_imgs/ramx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo4_position[0], snapo4_position[1], 10, 10))
            for pos in snapo5_body:
                impball = pygame.image.load("madden25_imgs/ramx.png").convert()
                game_window.blit(impball, pygame.Rect(snapo5_position[0], snapo5_position[1], 10, 10))
            for pos in snapx1_body:
                impball = pygame.image.load("madden25_imgs/raiderx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx1_position[0], snapx1_position[1], 10, 10))
            for pos in snapx2_body:
                impball = pygame.image.load("madden25_imgs/raiderx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx2_position[0], snapx2_position[1], 10, 10))
            for pos in snapx3_body:
                impball = pygame.image.load("madden25_imgs/raiderx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx3_position[0], snapx3_position[1], 10, 10))
            for pos in snapx4_body:
                impball = pygame.image.load("madden25_imgs/raiderx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx4_position[0], snapx4_position[1], 10, 10))
            for pos in snapx5_body:
                impball = pygame.image.load("madden25_imgs/raiderx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx5_position[0], snapx5_position[1], 10, 10))
            for pos in snapx6_body:
                impball = pygame.image.load("madden25_imgs/raiderx_flip.png").convert()
                game_window.blit(impball, pygame.Rect(snapx6_position[0], snapx6_position[1], 10, 10))
                
            timersnap_position[0] = 0
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

            # if down_yard <= field_line_10:
            #     yard = 10
            # if down_yard < field_line_9 and down_yard >= field_line_10:
            #     yard = 9
            # if down_yard < field_line_8 and down_yard >= field_line_9:
            #     yard = 8
            # if down_yard < field_line_7 and down_yard >= field_line_8:
            #     yard = 7
            # if down_yard < field_line_6 and down_yard >= field_line_7:
            #     yard = 6
            # if down_yard < field_line_5 and down_yard >= field_line_6:
            #     yard = 5
            # if down_yard < field_line_4 and down_yard >= field_line_5:
            #     yard = 4
            # if down_yard < field_line_3 and down_yard >= field_line_4:
            #     yard = 3
            # if down_yard < field_line_2 and down_yard >= field_line_3:
            #     yard = 2
            # if down_yard < field_line_1 and down_yard >= field_line_2:
            #     yard = 1
            
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
                if ball_dist < 50 and ballcatch != 1:
                    if down <= 4: 
                            
                        if ball_position[0] >= 200:
                            sack()
                            play = 0    
                            snap = 0
                            player_position[0] = 50
                            player_position[1] = 205
                            gb_position[1] = 305
                            ball_position[0] = 50
                            ballcatch = 0
                            down += 1
                            play_promt = '3'
                            timeroppsgoal_position[0] = 0

                        if down >= 5:
                            play_promt = '0' 
                            start_screen = 1
                            player_position[0] = 50
                            player_position[1] = 205
                            gb_position[1] = 305
                            ball_position[0] = 0
                            down = 1

                if ballcatch != 1:
                    for pos in ball_body:
                        impball = pygame.image.load("madden25_imgs/ram0.png").convert()
                        game_window.blit(impball, pygame.Rect(ball_position[0], ball_position[1], 10, 10))

                ball_direction_start = random.choice(ball_direction)
                ball_position[0] += 15 
                
                if ballcatch != 1:
                    if ball_direction_start == 2:
                        ball_position[1] += 20 
                    elif ball_direction_start == 3:
                        ball_position[1] -= 20 
                    
                    if ball_position[0] > 1300:
                        play_promt = 'oppsgoal'
                        key = ''
                        oppsgoal_position[0] = 0
                        play = 0
                        snap = 0
                        ballcatch = 0
                        player_position[0] = 50
                        player_position[1] = 205
                        gb_position[1] = 305
                        ball_position[0] = 0

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
                        down = 1
                    
        if snap == 2:

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


            #speed of the computers
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

                #drawing the computers 
                for pos in compx_body:
                    if compx_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx_position[0], compx_position[1], 10, 10))
            
                for pos in compx1_body:
                    if compx1_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx1_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx1_position[0], compx1_position[1], 10, 10))
            
                for pos in compx2_body:
                    if compx2_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx2_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx2_position[0], compx2_position[1], 10, 10))
            
                for pos in compx3_body:
                    if compx3_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx3_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx3_position[0], compx3_position[1], 10, 10))
            
                for pos in compx4_body:
                    if compx4_direction == 'RIGHT':
                        impx = pygame.image.load("madden25_imgs/ramx.png").convert()
                    elif compx4_direction == 'LEFT':
                        impx = pygame.image.load("madden25_imgs/ramx_flip.png").convert()
                    game_window.blit(impx, pygame.Rect(compx4_position[0], compx4_position[1], 10, 10))

        
        show_nextyardline(1, white, 'Arial', 80)
        show_speed(1, white, 'Arial', 30)
        show_downs(1, white, 'Arial', 30)
        show_score(1, white, 'Arial', 30)

    #after opps score screen                          
    if play_promt == 'oppsgoal':
        yard = 1
        yardline = 10 

        oppsgoall = random.choice(rand0oppgoall)

        for pos in oppsgoal_body:
            if oppsgoal == 1:
                impog = pygame.image.load("madden25_imgs/oppsgoalwf.png").convert()
                game_window.blit(impog, pygame.Rect(oppsgoal_position[0], oppsgoal_position[1], 10, 10))
            elif oppsgoal == 2:
                impog = pygame.image.load("madden25_imgs/oppsgoalnof.png").convert()
                game_window.blit(impog, pygame.Rect(oppsgoal_position[0], oppsgoal_position[1], 10, 10))

        for pos in timeroppsgoal_body:
            pygame.draw.rect(game_window, white, pygame.Rect(timeroppsgoal_position[0], timeroppsgoal_position[1], 10, 10))   

        if timeroppsgoal_position[0] < 1300:
            timeroppsgoal_position[0] += 15

        if timeroppsgoal_position[0] >= 1000:
            snap = 0
            start_screen = 1   
            play_promt = '0'
            down = 1
            if oppsgoal == 1:
                score[1] += 7
            if oppsgoal == 2:
                score[1] += 6

    #point conversion screen
    if play_promt == 'pc':

        ball_position[0] = 50
        snap = 0 
        ballcatch = 0
        yardline = 10
        yard = 1

        if pc == 1:
            for pos in pc_body:
                imppc = pygame.image.load("madden25_imgs/1ptw.png").convert()
                game_window.blit(imppc, pygame.Rect(pc_position[0], pc_position[1], 10, 10))
        elif pc == 2:
            for pos in pc_body:
                imppc = pygame.image.load("madden25_imgs/1ptl.png").convert()
                game_window.blit(imppc, pygame.Rect(pc_position[0], pc_position[1], 10, 10))
        if pc == 3:
            for pos in pc_body:
                imppc = pygame.image.load("madden25_imgs/2ptw.png").convert()
                game_window.blit(imppc, pygame.Rect(pc_position[0], pc_position[1], 10, 10))
        elif pc == 4:
            for pos in pc_body:
                imppc = pygame.image.load("madden25_imgs/2ptl.png").convert()
                game_window.blit(imppc, pygame.Rect(pc_position[0], pc_position[1], 10, 10))

        for pos in timerpc_body:
            pygame.draw.rect(game_window, white, pygame.Rect(timerpc_position[0], timerpc_position[1], 10, 10))   

        if timerpc_position[0] < 1300:
            timerpc_position[0] += 15

        if timerpc_position[0] >= 1300:
            if score[0] >= 30 or score[1] >= 30:
                play_promt = 'gameover'
            else:
                play_promt = '3'
                timeroppsgoal_position[0] = 0
                snap = 0
                start_screen = 1  
                down = 1
                ball_position[0] = 0
                ball_position[1] = 0 
                if pc == 1:
                    score[0] += 1
                    print('pc1')
                if pc == 3:
                    score[0] += 2
                    print('pc2')
                pc = '0'
    
    #gamer over screen
    if play_promt == 'gameover':

        game_window.fill(black)

        if score[0] < 30 or score[1] < 30:
            play_promt = '0'
            start_screen = 1

        for pos in gameover_body:
            if score[0] >= 30:
                impgo = pygame.image.load("madden25_imgs/w.png").convert()
                game_window.blit(impgo, pygame.Rect(gameover_position[0], gameover_position[1], 10, 10))
            if score[1] >= 30:
                impgo = pygame.image.load("madden25_imgs/l.png").convert()
                game_window.blit(impgo, pygame.Rect(gameover_position[0], gameover_position[1], 10, 10))

        for pos in timergo_body:
            pygame.draw.rect(game_window, white, pygame.Rect(timergo_position[0], timergo_position[1], 10, 10))   

        if timergo_position[0] < 1300:
            timergo_position[0] += 15

        if timergo_position[0] >= 1300:
            quit()


    pygame.display.update()

    fps.tick(player_speed)

    
