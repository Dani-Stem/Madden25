import pygame, sys
import random
from pygame.sprite import Sprite
from pygame.rect import Rect

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


def start_menu(self):
    if not self.start_channel.get_busy():
        self.start_channel.play(self.start_music, loops=-1)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.start_sound.play()
                    self.coin_menu()

        self.screen.fill(self.BLACK)
        self.logo()
        self.howto(self.instructions, self.WHITE, (675, 150), line_spacing=5)
        self.show_startscreen()
        self.show_startscreensub()
        self.show_startscreensub1()
        pygame.display.flip()


def render_call_menu(self, selected_index2):
    self.screen.fill(self.BLACK)
    call_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 150)
    select_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

    score_surface = call_font.render("YOUR CALL", True, "yellow")
    score_rect = score_surface.get_rect()
    score_rect.midtop = (WINDOW_WIDTH // 2, WINDOW_HEIGHT / 10)
    self.screen.blit(score_surface, score_rect)
    for index, item in enumerate(self.call_menu_items):
        if index == selected_index2:
            text_color = self.HIGHLIGHT
            if self.call_menu_items[selected_index2] == "OPPS BALL":
                text_color = "red"
        else:
            text_color = self.WHITE

        menu_text = select_font.render(item, True, text_color)

        text_rect = menu_text.get_rect(
            center=(
                WINDOW_WIDTH / 1.48
                + (index - len(self.call_menu_items) // 2)
                * 480,  
                WINDOW_HEIGHT // 2,  
            )
        )
        self.screen.blit(menu_text, text_rect)


def call_menu(self):
        selected_index2 = 0
        running = True

        # Disable spacebar for a few seconds when the menu is rendered
        self.spacebar_enabled = False
        pygame.time.set_timer(pygame.USEREVENT, 100)  

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.USEREVENT:
                    self.spacebar_enabled = True
                    pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop the timer

                if event.type == pygame.KEYDOWN:
                    if not self.spacebar_enabled and event.key == pygame.K_SPACE:
                        continue  # Ignore spacebar presses if disabled

                    self.highlight_sound.play()
                    if event.key == pygame.K_LEFT:  
                        self.highlight_sound.play()
                        selected_index2 = (selected_index2 - 1) % len(self.call_menu_items)
                    elif event.key == pygame.K_RIGHT:  
                        self.highlight_sound.play()
                        selected_index2 = (selected_index2 + 1) % len(self.call_menu_items)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.confirm_sound.play()

                        if self.call_menu_items[selected_index2] == "YOUR BALL":
                            self.confirm_sound.play()
                            self.opponents_turn = False
                            self.main_menu()
                        elif self.call_menu_items[selected_index2] == "OPPS BALL":
                            self.opponents_turn = True
                            self.stop_opp()

            self.render_call_menu(selected_index2)
            pygame.display.flip()


def coin_menu(self):
    global opponents_turn
    pause_time = 1.0  
    paused = False
    start_pause_time = None
    choices = "HEADS"
    # choices = random.choice(["HEADS", "TAILS"])

    while True:
        dt = self.clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.coin_sound.play()
                    if not paused:
                        self.coin.pause_on_frame(0 if self.coin.frame_index < 1 else 2)
                        paused = True
                        start_pause_time = pygame.time.get_ticks()

        if paused:
            elapsed_time = (pygame.time.get_ticks() - start_pause_time) / 1000
            if elapsed_time >= pause_time:
                if self.coin.result == choices:
                    self.toss(1)
                    self.call_menu()
                else:
                    self.toss(0)
                    result = random.choice([0, 1])
                    self.choice(result)
                    opponents_turn = True
                    if result:
                        self.stop_opp()
                    else:
                        opponents_turn = False
                        self.main_menu()
                return  

            self.screen.fill(self.BLACK)
            self.coin_howto(
                self.coin_instructions, self.WHITE, (120, 200), line_spacing=5
            )
            self.show_teamquarter(self.coin.result, choices)
            self.coin_group.draw(self.screen)
            pygame.display.flip()
            continue

        self.screen.fill(self.BLACK)
        self.coin_howto(self.coin_instructions, self.WHITE, (120, 200), line_spacing=5)
        self.show_teamquarter(self.coin.result, choices)
        self.coin_group.update(dt)
        self.coin_group.draw(self.screen)
        pygame.display.flip()
