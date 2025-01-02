import pygame, sys
import time
from pygame.sprite import Sprite
from pygame.rect import Rect

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


def render_menu(self, selected_index, menu):
    self.menu = menu
    if self.menu:
        self.snap = False
        self.menu = False
    self.screen.fill(self.BLACK)
    self.opponents_turn
    if self.opponents_turn or self.snap:
        menu_items = ["Resume", "Quit"]
    else:
        menu_items = ["Run", "Pass", "Field Goal", "Quit"]

    turn_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
    if self.opponents_turn:
        score_surface = turn_font.render("OPPONENT'S BALL", True, "yellow")
    else:
        score_surface = turn_font.render("YOUR BALL", True, "yellow")
    score_rect = score_surface.get_rect()
    score_rect.midtop = (WINDOW_WIDTH // 2, WINDOW_HEIGHT / 10)
    self.screen.blit(score_surface, score_rect)

    for index, item in enumerate(menu_items):
        text_color = self.HIGHLIGHT if index == selected_index else self.WHITE

        if self.yardline[0] < 60:
            self.show_too_far_message = True
            if (
                index == selected_index
                and item == "Field Goal"
                and self.show_too_far_message
            ):
                display_text = "Too Far"
                text_color = "red"
            else:
                display_text = item
        else:
            self.show_too_far_message = False
            display_text = item

        if index == selected_index and item == "Quit":
            display_text = "Quit"
            text_color = "red"

        menu_text = self.font.render(display_text, True, text_color)
        text_rect = menu_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 3 + index * 100)
        )
        self.screen.blit(menu_text, text_rect)


def main_menu(self):
    self.opp_channel.pause()
    self.start_channel.stop()

    if self.first_render:
        channel = pygame.mixer.find_channel()  
        if channel:
            self.player_channel.play(
                self.player_music, loops=-1
            )  
        self.first_render = False  
    else:
        if not self.player_channel.get_busy():
            self.player_channel.play(self.player_music, loops=-1)
        else:
            self.player_channel.unpause()

    last_index = -1
    if self.opponents_turn:
        self.player_channel.pause()
        self.opp_channel.unpause()
        self.selected_index = 0
        menu_items = ["Resume", "Quit"]

    elif self.snap:
        self.player_channel.unpause()
        self.opp_channel.pause()
        self.selected_index = 0
        menu_items = ["Resume", "Quit"]
    else:
        menu_items = ["Run", "Pass", "Field Goal", "Quit"]

    while True:
        self.clock.tick(60) / 1000  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.highlight_sound.play()
                    self.selected_index = (self.selected_index - 1) % len(
                        menu_items
                    )  
                elif event.key == pygame.K_DOWN:
                    self.highlight_sound.play()
                    self.selected_index = (self.selected_index + 1) % len(
                        menu_items
                    )  
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.confirm_sound.play()
                    if menu_items[self.selected_index] == "Pass":
                        pygame.K_SPACE = False
                        self.rbt = False
                        self.outOfBounds = False
                        self.player_loop()
                    elif menu_items[self.selected_index] == "Run":
                        pygame.K_SPACE = False
                        self.rbt = True
                        self.outOfBounds = False
                        self.player_loop()
                    elif (
                        menu_items[self.selected_index] == "Field Goal"
                        and not self.snap
                    ):
                        self.outOfBounds = False
                        if not self.show_too_far_message:
                            (
                                self.score[0],
                                stop,
                                self.player_touchdown,
                                self.opp_transition,
                                self.opponents_turn,
                                self.opp_down,
                            ) = self.fg.run(
                                self.score,
                                self.stop_opp,
                                self.screen,
                                self.player_touchdown,
                                self.opp_transition,
                                self.opponents_turn,
                                self.opp_down,
                                self.render_end_menu,
                                self.end_menu,
                            )
                            if stop:
                                self.yardline[0] = 30
                                self.stop_opp()
                        else:
                            self.main_menu()
                    elif menu_items[self.selected_index] == "Resume":
                        if self.opponents_turn:
                            self.opponents_turn = False
                            self.opp_loop()
                        else:
                            self.player_loop()
                    elif menu_items[self.selected_index] == "Quit":
                        pygame.quit()
                        sys.exit()

        if self.selected_index != last_index:
            last_index = self.selected_index

        self.render_menu(self.selected_index, self.menu)

        if self.opponents_turn:
            self.defender.opp_show_downs(
                self.opp_down, self.screen, self.main_menu, time
            )
        else:
            self.down, self.yard = self.show_downs(self.down, self.screen, self.yard)

        self.show_score()
        self.show_yard()

        pygame.display.flip()
