# importing libraries
import pygame
import time
import random
from pygame.sprite import Sprite
from pygame.rect import Rect
from player.player import Player
from player.rb import RB
from player.defender import Defender
from player.qb import QB
from npcs.opps import Opps3
from field.field import Field
from field.fg import FieldGoal
from items.coin import Coin
from npcs.lineman import Linemen
from menus.start import start_menu, render_call_menu, call_menu, coin_menu
from menus.main_menu import main_menu, render_menu
from loops.player_loop import player_loop
from loops.opp_loop import opp_loop, stop_opp, render_stop_opp
from menus.end_menu import render_end_menu, end_menu

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


class Game:
    def __init__(self):
        # Initializing pygame
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("MADDEN 2K25")
        self.clock = pygame.time.Clock()

        # Groups
        self.player_group = pygame.sprite.Group()
        self.rb_group = pygame.sprite.Group()
        self.qb_group = pygame.sprite.Group()
        self.football_group = pygame.sprite.Group()
        self.opps_group = pygame.sprite.Group()
        self.opps_group2 = pygame.sprite.Group()
        self.opps_group3 = pygame.sprite.Group()
        self.team_group = pygame.sprite.Group()
        self.defender_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()

        # Timer
        self.opps_timer = pygame.event.custom_type()
        pygame.time.set_timer(self.opps_timer, 100)

        # Game state variables
        self.next_screen = False
        self.outOfBounds = False
        self.outOfBounds2 = False
        self.qbt = True
        self.rbt = False
        self.snap = False
        self.rb_snap = False
        self.caught = False
        self.opps_created = False
        self.stop_opps = None
        self.player_position = (150, 450)
        self.player_touchdown = False
        self.opp_touchdown = False
        self.opp_transition = False
        self.skip = False
        self.next_screen2 = False
        self.new_score = None
        self.rbt_td = False
        self.menu = False
        self.first_render = True  # Add a flag during initialization
        self.first_render2 = True
        self.spacebar_enabled = True

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.HIGHLIGHT = "green"
        self.start = True

        # Fonts
        self.font = pygame.font.Font(
            "../madden25_imgs/16bfZX.ttf", 74
        )  # Default font, size 74

        # Opponent settings
        self.opponents_turn = False
        self.coin_win = True

        # Game data
        self.yardline = [30]
        self.yardline2 = self.yardline[0] + 10
        self.down = 1
        self.yard = 10
        self.score = [0, 0]
        self.white = pygame.Color(255, 255, 255)
        self.playerPos = 1
        self.first = 0
        self.opp_posx = 0
        self.qOutOfBounds = False
        self.opp_down = 1
        self.show_too_far_message = None
        self.opp_sound_paused = False
        self.end_item = "Quit"
        self.winner = True
        self.selected_index = 0
        self.down2 = 1
        self.first = 0
        self.music_playing = False

        # Channels
        pygame.mixer.set_num_channels(16)

        if not hasattr(self, "player_channel"):
            self.player_channel = pygame.mixer.Channel(0)  # Assign sound to channel 1

        
        if not hasattr(self, "opp_channel"):
            self.opp_channel = pygame.mixer.Channel(1)  # Assign sound to channel 0

        if not hasattr(self, "start_channel"):
            self.start_channel = pygame.mixer.Channel(2)

        # Instructions
        self.instructions = [
            "HOW TO PLAY:",
            "",
            "CHOOSE TO RUN/PASS THE BALL",
            "- USE THE ARROW KEYS TO MOVE UP, DOWN, LEFT, RIGHT",
            "- PRESS SPACE BAR TO INCREASE SPEED",
            "",
            "CHOOSE TO KICK A FIELD GOAL",
            "- PRESS SPACE BAR TO GET THE KICK POWER UP",
            "- KEEP KICK POWER AT TARGET RATE UNTIL TIMER IS UP",
            "",
            "FIRST TEAM TO SCORE GREATER THAN 30 WINS",
        ]

        self.coin_instructions = [
            "COIN FLIP INSTRUCTIONS:",
            "",
            "WHEN YOU'RE READY, PRESS SPACE BAR TO",
            "STOP THE COIN FROM FLIPPING",
        ]

        self.call_menu_items = ["YOUR BALL", "OPPS BALL"]

        # Sounds
        self.start_music = pygame.mixer.Sound("../madden25_imgs/start.mp3")
        self.start_music.set_volume(0.1)

        self.player_music = pygame.mixer.Sound("../madden25_imgs/player.mp3")
        self.player_music.set_volume(0.04)

        self.opp_music = pygame.mixer.Sound("../madden25_imgs/opp.mp3")
        self.opp_music.set_volume(0.1)

        self.highlight_sound = pygame.mixer.Sound("../madden25_imgs/highlight.wav")
        self.highlight_sound.set_volume(0.05)

        self.confirm_sound = pygame.mixer.Sound("../madden25_imgs/confirm.wav")
        self.confirm_sound.set_volume(0.05)

        self.coin_sound = pygame.mixer.Sound("../madden25_imgs/coin.wav")
        self.coin_sound.set_volume(0.05)

        self.win_music = pygame.mixer.Sound("../madden25_imgs/win.mp3")
        self.win_music.set_volume(0.1)

        self.lose_music = pygame.mixer.Sound("../madden25_imgs/lose.mp3")
        self.lose_music.set_volume(0.1)

        self.start_sound = pygame.mixer.Sound("../madden25_imgs/start.wav")
        self.start_sound.set_volume(0.05)


        # Assets
        self.background = pygame.image.load("../madden25_imgs/field1.png").convert()
        self.rb_start = pygame.image.load("../madden25_imgs/playersnap.png")

        # Initialize player and QB
        self.player = Player(
            (120, 300), self.player_group, self.next_screen, self.outOfBounds
        )
        self.rb = RB((120, 280), self.rb_group, self.next_screen, self.outOfBounds)
        self.qb = QB(
            (120, 350),
            self.qb_group,
            self.next_screen,
            self.qbt,
            self.snap,
            self.outOfBounds,
        )
        self.defender = Defender(
            (WINDOW_WIDTH - 200, 350),
            self.defender_group,
            self.next_screen,
            self.outOfBounds,
        )

        # Initialize linemen
        self.raiders = Linemen(
            image_path="../madden25_imgs/raiderx.png",
            screen=self.screen,
            x=160,
            y_start=175,
            y_end=WINDOW_HEIGHT - 235,
            spacing=WINDOW_HEIGHT // 10,  # Spacing between raiders
            vibration_speed=5,  # Raiders move slower
            vibration_range=10,  # Small range of vibration
        )

        self.rams = Linemen(
            image_path="../madden25_imgs/ramx_flip.png",
            screen=self.screen,
            x=240,
            y_start=175,
            y_end=WINDOW_HEIGHT - 235,
            spacing=WINDOW_HEIGHT // 10,  # Spacing between rams
            vibration_speed=2,  # Rams move faster
            vibration_range=10,  # Larger range of vibration
        )

        # Opponent and coin
        self.opponent = Opps3((150, 300), self.opps_group2)
        self.coin = Coin((1075, 315), self.coin_group)

        # Field goal
        self.fg = FieldGoal()

        # Display field
        self.display = Field()

    def show_downs(self, down, screen, yard):
        self.down = down % 4
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        if self.down == 1:
            self.yard = 10
            down_surface = my_font.render(
                str(self.down) + "ST & " + str(self.yard), True, "white"
            )
        elif self.down == 2:
            down_surface = my_font.render(
                str(self.down) + "ND & " + str(self.yard), True, "white"
            )
        elif self.down == 3:
            down_surface = my_font.render(
                str(self.down) + "RD & " + str(self.yard), True, "white"
            )
        elif self.down == 0:
            down_surface = my_font.render("4TH & " + str(self.yard), True, "white")

        down_rect = down_surface.get_rect()
        down_rect.midtop = (689, 5)
        screen.blit(down_surface, down_rect)

        return (self.down, self.yard)

    def downs(self, screen, time):
        self.down2 = (self.down2 % 4) + 1

        screen.fill((0, 0, 0))

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
        if not self.next_screen:
            if self.down2 == 1:
                self.yard = 10
                downs_surface = my_font.render(
                    str(self.down2) + "ST & " + str(self.yard), True, "red"
                )

            if self.down2 == 2:
                self.yard -= random.choice([1, 2, 3])
                downs_surface = my_font.render(
                    str(self.down2) + "ND & " + str(self.yard), True, "red"
                )
            elif self.down2 == 3:
                self.yard -= random.choice([1, 2, 3])
                downs_surface = my_font.render(
                    str(self.down2) + "RD & " + str(self.yard), True, "red"
                )
            elif self.down2 == 4:
                self.yard -= random.choice([1, 2, 3])
                downs_surface = my_font.render(
                    str(self.down2) + "TH & " + str(self.yard), True, "red"
                )
        elif self.next_screen:
            downs_surface = my_font.render("1ST & 10", True, "green")
            self.next_screen = False

        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        time.sleep(1)

    def show_score(self):
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        score_surface = my_font.render(
            f"SCORE: {self.score[0]} vs {self.score[1]}", True, self.white
        )
        score_rect = score_surface.get_rect()
        score_rect.midtop = (1150, 5)
        self.screen.blit(score_surface, score_rect)

    def show_yard(self):
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        speed_surface = my_font.render(
            "YARDLINE: " + str(self.yardline[0]), True, self.white
        )
        speed_rect = speed_surface.get_rect()
        speed_rect.midtop = (205, 5)
        self.screen.blit(speed_surface, speed_rect)

    def show_startscreen(self):

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 45)
        speed_surface = my_font.render("MADDEN25", True, "yellow")
        speed_rect = speed_surface.get_rect()
        speed_rect.midtop = (320, 480)
        self.screen.blit(speed_surface, speed_rect)

    def show_startscreensub(self):

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 30)
        speed_surface = my_font.render("A DN INDUSTRIES PRODUCT", True, "yellow")
        speed_rect = speed_surface.get_rect()
        speed_rect.midtop = (320, 515)
        self.screen.blit(speed_surface, speed_rect)

    def show_startscreensub1(self):
        # Use time to determine if the text should be visible
        if int(time.time() * 2) % 2 == 0:  # Blink every 0.5 seconds
            my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 55)
            speed_surface = my_font.render("PRESS S TO START THE GAME", True, "white")
            speed_rect = speed_surface.get_rect()
            speed_rect.midtop = (906, 515)
            self.screen.blit(speed_surface, speed_rect)

    def logo(self):
        implogo = pygame.image.load("../madden25_imgs/logo.png").convert_alpha()
        self.screen.blit(
            implogo,
            pygame.Rect(195, 200, 10, 10),
        )

    def howto(self, lines, color, start_pos, line_spacing=5):
        font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 30)
        x, y = start_pos
        for line in lines:
            text_surface = font.render(line, True, color)
            self.screen.blit(text_surface, (x, y))
            y += font.get_height() + line_spacing  

    def coin_howto(self, lines, color, start_pos, line_spacing=5):
        font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        x, y = start_pos
        for line in lines:
            text_surface = font.render(line, True, color)
            self.screen.blit(text_surface, (x, y))
            y += font.get_height() + line_spacing  

    def choice(self, result):
        self.screen.fill((0, 0, 0))

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

        if result:
            downs_surface = my_font.render("OPPONENT'S BALL", True, "red")
        else:
            downs_surface = my_font.render("OPPONENT DEFERS", True, "green")

        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        self.screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        time.sleep(2)

    def toss(self, result):
        self.screen.fill((0, 0, 0))

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

        if result:
            downs_surface = my_font.render("YOU WON THE TOSS!", True, "green")
        else:
            downs_surface = my_font.render("OPPONENT WON THE TOSS", True, "red")

        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        self.screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        time.sleep(2)

    def show_teamquarter(self, result, choice):

        font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 70)
        speed_surface = font.render("YOUR TEAM CHOOSES " + choice, True, "yellow")
        speed_rect = speed_surface.get_rect()
        speed_rect.center = (470, 475)
        self.screen.blit(speed_surface, speed_rect)

    def play_player_music(self):
        if not self.player_channel.get_busy(): 
            self.player_channel.stop()  
            self.player_channel.play(self.player_music, loops=-1)  

    def start_menu(self):
        start_menu(self)

    def render_call_menu(self, selected_index2):
        render_call_menu(self, selected_index2)

    def call_menu(self):
        call_menu(self)

    def coin_menu(self):
        coin_menu(self)

    def render_menu(self, selected_index, menu):
        render_menu(self, selected_index, menu)

    def main_menu(self):
        main_menu(self)

    def player_loop(self):
        player_loop(self)

    def render_stop_opp(self):
        render_stop_opp(self)

    def stop_opp(self):
        stop_opp(self)

    def opp_loop(self):
        opp_loop(self)

    def render_end_menu(self, winner):
        render_end_menu(self, winner)

    def end_menu(self):
        end_menu(self)

    def run(self):
        self.start_menu()
        """self.coin_menu()
        self.call_menu()
        self.main_menu()
        self.player_loop()
        self.stop_opp()
        self.opp_loop()"""


if __name__ == "__main__":
    game = Game()
    game.run()
