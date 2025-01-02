import pygame, sys
import time
import random
from npcs.opps import Opps
from npcs.team import Team

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


def player_loop(self):
    while True:

        if self.caught and self.qbt:
            # Create a semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))  # Black with 50% transparency

            my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
            downs_surface = my_font.render("NICE CATCH", True, "green")
            downs_rect = downs_surface.get_rect()
            downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
            self.screen.blit(overlay, (0, 0))
            self.screen.blit(downs_surface, downs_rect)
            pygame.display.flip()
            time.sleep(1)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == self.opps_timer:
                opps_y_pos = WINDOW_HEIGHT // 2
                opps_x_pos = WINDOW_WIDTH - 200

                team_y_pos = random.randint(100, 400)
                team_x_pos = 350

                if self.snap and not self.opps_created:
                    for _ in range(5):
                        opps_y_pos = WINDOW_HEIGHT // 2
                        opps_x_pos = WINDOW_WIDTH - 200
                        Opps((opps_x_pos, opps_y_pos), self.opps_group)
                    if not self.rbt:
                        for _ in range(4):
                            team_y_pos = random.randint(100, 400)
                            team_x_pos = 350
                            Team((team_x_pos, team_y_pos), self.team_group)

                    self.opps_created = True

                if not self.snap:
                    self.opps_created = False

        dt = self.clock.tick() / 1000

        self.screen.blit(self.background, (0, 0))
        self.display.draw(self.screen, self.next_screen, self.yardline)

        self.down, self.yard = self.show_downs(self.down, self.screen, self.yard)

        self.show_score()

        if not self.next_screen:
            if self.snap:
                # Update positions for independent vibration
                self.raiders.update_positions()
                self.rams.update_positions()

                # Render updated positions
                self.raiders.render()
                self.rams.render()

            else:
                line_spacing = WINDOW_HEIGHT // 10
                for i in range(250, WINDOW_HEIGHT - 150, line_spacing):
                    line = pygame.image.load("../madden25_imgs/raidercenter.png")
                    line = pygame.transform.scale(line, (85, 85))
                    linemen = self.screen.blit(line, pygame.Rect(180, i - 100, 10, 10))

                for i in range(250, WINDOW_HEIGHT - 150, line_spacing):
                    line = pygame.image.load("../madden25_imgs/ramcenter_flip.png")
                    line = pygame.transform.scale(line, (85, 85))
                    linemen = self.screen.blit(line, pygame.Rect(240, i - 100, 10, 10))

        if self.qbt:

            self.qb_group.draw(self.screen)

            self.opps_group.draw(self.screen)
            if self.rbt:
                self.rb_start
                self.screen.blit(self.rb_start, (90, 250))

            (
                self.next_screen,
                self.qbt,
                self.snap,
                self.qOutOfBounds,
                self.rbt,
                self.rbt_td,
            ) = self.qb.update(
                dt,
                events,
                self.yardline,
                self.football_group,
                self.outOfBounds,
                self.screen,
                time,
                self.rbt,
                self.main_menu,
                self.winner,
                self.rbt_td,
                self.stop_opp,
                self.score,
                self.render_end_menu,
                self.end_menu,
                self.render_menu,
                self.selected_index,
                self.opp_transition,
            )
            if not self.rbt:
                self.qb.draw_speed_meter(self.screen)
                self.football_group.draw(self.screen)
                self.team_group.draw(self.screen)

                collision_positions = []
                for football in self.football_group:
                    position = football.update(dt, self.team_group, self.opps_group)
                    if position:
                        collision_positions.append(position)
                if collision_positions:
                    self.player_position = collision_positions[0]
                    self.caught = True
                self.team_group.update(dt, self.outOfBounds, self.caught, self.snap)
            else:
                self.qb.draw_speed_meter(self.screen)
                self.football_group.draw(self.screen)
                self.team_group.draw(self.screen)

                collision_positions = []
                for football in self.football_group:
                    position = football.update(dt, self.team_group, self.opps_group)
                    if position:
                        collision_positions.append(position)
                if collision_positions:
                    self.player_position = collision_positions[0]
                    self.caught = True
                self.team_group.update(dt, self.outOfBounds, self.caught, self.snap)

            self.opps_group.update(
                dt, self.outOfBounds, self.playerPos, self.caught, self.snap
            )
        elif self.rbt:
            self.rb.draw_speed_meter(self.screen)
            if not self.next_screen:
                (
                    self.next_screen,
                    self.qbt,
                    self.rb_snap,
                    self.qOutOfBounds,
                    self.rbt,
                    self.rbt_td,
                ) = self.qb.update(
                    dt,
                    events,
                    self.yardline,
                    self.football_group,
                    self.outOfBounds,
                    self.screen,
                    time,
                    self.rbt,
                    self.main_menu,
                    self.winner,
                    self.rbt_td,
                    self.stop_opp,
                    self.score,
                    self.render_end_menu,
                    self.end_menu,
                    self.render_menu,
                    self.selected_index,
                    self.opp_transition,
                )

                self.opps_group.update(
                    dt, self.outOfBounds, self.playerPos, self.caught, self.rb_snap
                )
                self.qb_group.draw(self.screen)
                self.opps_group.draw(self.screen)

            else:
                self.opps_group.update(
                    dt, self.outOfBounds, self.playerPos, self.caught, self.rb_snap
                )
                self.opps_group.draw(self.screen)

            self.rb_group.draw(self.screen)

            (
                self.next_screen,
                self.outOfBounds,
                self.playerPos,
                self.caught,
                self.score,
                self.yardline,
                self.opp_transition,
                self.opp_down,
                self.rbt_td,
                self.rbt,
            ) = self.rb.update(
                dt,
                events,
                self.yardline,
                self.screen,
                time,
                self.player_position,
                self.caught,
                self.qOutOfBounds,
                self.opps_group,
                self.score,
                self.qbt,
                self.stop_opp,
                self.opp_transition,
                self.opp_down,
                self.rbt,
                self.rbt_td,
                self.downs,
                self.render_end_menu,
                self.end_menu,
            )
        else:
            self.player.draw_speed_meter(self.screen)
            if not self.next_screen:
                (
                    self.next_screen,
                    self.qbt,
                    self.snap,
                    self.qOutOfBounds,
                    self.rbt,
                    self.rbt_td,
                ) = self.qb.update(
                    dt,
                    events,
                    self.yardline,
                    self.football_group,
                    self.outOfBounds,
                    self.screen,
                    time,
                    self.rbt,
                    self.main_menu,
                    self.winner,
                    self.rbt_td,
                    self.stop_opp,
                    self.score,
                    self.render_end_menu,
                    self.end_menu,
                    self.render_menu,
                    self.selected_index,
                    self.opp_transition,
                )
                self.football_group.draw(self.screen)

                position = self.football_group.update(
                    dt, self.team_group, self.opps_group
                )

                self.team_group.update(dt, self.outOfBounds, self.caught, self.snap)
                self.opps_group.update(
                    dt, self.outOfBounds, self.playerPos, self.caught, self.snap
                )
                self.qb_group.draw(self.screen)
                self.team_group.draw(self.screen)
                self.opps_group.draw(self.screen)

            else:
                self.opps_group.update(
                    dt, self.outOfBounds, self.playerPos, self.caught, self.snap
                )
                self.opps_group.draw(self.screen)

            self.player_group.draw(self.screen)

            (
                self.next_screen,
                self.outOfBounds,
                self.playerPos,
                self.caught,
                self.score,
                self.yardline,
                self.opp_transition,
                self.opp_down,
                self.winner,
                self.rbt_td,
            ) = self.player.update(
                dt,
                events,
                self.yardline,
                self.screen,
                time,
                self.player_position,
                self.caught,
                self.qOutOfBounds,
                self.opps_group,
                self.score,
                self.stop_opp,
                self.opp_transition,
                self.opp_down,
                self.main_menu,
                self.render_end_menu,
                self.end_menu,
                self.winner,
                self.rbt_td,
                self.down,
                self.downs,
            )

        if self.outOfBounds:
            self.snap = False
            self.down += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.main_menu()

        pygame.display.update()