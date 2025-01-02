# importing libraries
import pygame, sys
import time
import random
from pygame.sprite import Sprite
from pygame.rect import Rect

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712

from npcs.opps import Opps2


def render_stop_opp(self):
    """Render the end menu with results and a single quit option."""
    background = pygame.image.load("../madden25_imgs/field1.png").convert()
    self.screen.blit(background, (0, 0))

    # Create a semi-transparent overlay
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)

    # Set the overlay color and transparency (RGBA format)
    overlay.fill((0, 0, 0, 128))  # Black with 50% transparency

    end_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 120)
    select_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

    select_font2 = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 40)

    result_text = "STOP THE RECIEVER!"
    result_color = "yellow"

    result_surface = end_font.render(result_text, True, result_color)
    result_rect = result_surface.get_rect(midtop=(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 5))
    self.screen.blit(overlay, (0, 0))
    self.screen.blit(result_surface, result_rect)

    quit_surface = select_font.render("Start", True, result_color)
    quit_rect = quit_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 2))
    quit_surface2 = select_font2.render("(Press Spacebar)", True, result_color)
    quit_rect2 = quit_surface2.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 1.7))
    self.screen.blit(quit_surface, quit_rect)
    self.screen.blit(quit_surface2, quit_rect2)


def stop_opp(self):
    pygame.K_SPACE = False
    self.start_channel.pause()
    self.player_channel.pause()

    # Play the sound if it is not already playing
    if self.first_render2:
        channel = pygame.mixer.find_channel()  # Find the first available channel
        if channel:
            self.opp_channel.play(
                self.opp_music, loops=-1
            )  # Ensure it plays on first render
        self.first_render2 = False  # Reset the flag
    else:
        if not self.opp_channel.get_busy():
            self.opp_channel.play(self.player_music, loops=-1)
        else:
            self.opp_channel.unpause()

    """Loop for the end menu."""
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle pressing Enter or Space to quit
            if event.type == pygame.KEYDOWN:
                pygame.K_SPACE = 32
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self.stop_opps = True
                    self.outOfBounds2 = True
                    self.opps_created = False
                    self.opp_loop()

        self.render_stop_opp()
        self.display.draw(self.screen, True, self.yardline)
        self.defender.opp_show_downs(self.opp_down, self.screen, self.main_menu, time)
        self.show_score()
        self.show_yard()

        pygame.display.update()

        pygame.display.flip()


def opp_loop(self):
    running = True
    while running:
        events = pygame.event.get()

        dt = self.clock.tick() / 1000

        self.screen.blit(self.background, (0, 0))
        self.display.draw(self.screen, True, self.yardline)
        self.defender.opp_show_downs(self.opp_down, self.screen, self.main_menu, time)
        self.show_score()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.opps_timer:
                opps_y_pos = random.randint(100, 400)
                opps_x_pos = 200

                if (
                    not self.outOfBounds2
                    and not self.opps_created
                    and not self.next_screen
                ) or self.opp_transition:
                    for _ in range(5):
                        opps_y_pos = random.randint(100, 400)
                        opps_x_pos = 200
                        Opps2((opps_x_pos, opps_y_pos), self.opps_group3)

                    self.opps_created = True
                    self.opp_transition = False
                self.opponent

        self.defender.draw_speed_meter(self.screen)
        if not self.next_screen:
            opp_posx = []  

            out_of_bounds_flags = []  

            for opp in self.opps_group2:  
                pos_x, out_of_bounds = opp.update(
                    dt,
                    self.outOfBounds2,
                    self.playerPos,
                    self.caught,
                    self.yardline,
                    self.opp_posx,
                )
                opp_posx.append(pos_x)  
                out_of_bounds_flags.append(
                    out_of_bounds
                )

            self.opp_posx = opp_posx[0]

            local_outOfBounds = False

            for opp in self.opps_group3:
                local_outOfBounds = (
                    opp.update(
                        dt,
                        self.outOfBounds2,
                        self.playerPos,
                        self.caught,
                        self.stop_opps,
                        self.opp_posx,
                        self.next_screen,
                    )
                    or local_outOfBounds
                )

            self.outOfBounds2 = any(out_of_bounds_flags)  

            self.opps_group3.draw(self.screen)
            self.opps_group2.draw(self.screen)

        else:
            opp_posx = []  
            out_of_bounds_flags = []  

            for opp in self.opps_group2:  
                pos_x, out_of_bounds = opp.update(
                    dt,
                    self.outOfBounds2,
                    self.playerPos,
                    self.caught,
                    self.yardline,
                    self.opp_posx,
                )
                opp_posx.append(pos_x)  
                out_of_bounds_flags.append(
                    out_of_bounds
                )  

            self.opp_posx = opp_posx[0]

            local_outOfBounds = False

            for opp in self.opps_group3:
                local_outOfBounds = (
                    opp.update(
                        dt,
                        self.outOfBounds2,
                        self.playerPos,
                        self.caught,
                        self.stop_opps,
                        self.opp_posx,
                        self.next_screen,
                    )
                    or local_outOfBounds
                )

            self.opps_group3.draw(self.screen)
            self.opps_group2.draw(self.screen)

            self.outOfBounds2 = any(out_of_bounds_flags)  
            self.next_screen2 = self.next_screen

        self.defender_group.draw(self.screen)

        (
            self.next_screen,
            self.outOfBounds2,
            self.playerPos,
            self.caught,
            self.score,
            self.yardline,
            self.stop_opps,
            self.opp_posx,
            self.opponents_turn,
            self.skip,
            self.down,
        ) = self.defender.update(
            dt,
            events,
            self.yardline,
            self.screen,
            time,
            self.player_position,
            self.caught,
            self.opps_group3,
            self.opps_group2,
            self.score,
            self.stop_opps,
            self.outOfBounds2,
            self.opp_posx,
            self.main_menu,
            self.opponents_turn,
            self.down,
            self.render_end_menu,
            self.end_menu,
        )

        if self.outOfBounds2:
            down = self.opp_down % 4
            if self.skip or (self.next_screen2 and not self.skip):
                if down == 1:
                    self.opp_down += 3
                elif down == 2:
                    self.opp_down += 2
                elif down == 3:
                    self.opp_down += 1
                self.next_screen2 = False
            self.opp_down += 1

        if not self.stop_opps:
            self.opps_created = False
            self.stop_opp()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.opponents_turn = True
            self.main_menu()
        pygame.display.update()
