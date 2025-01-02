import pygame
import random

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


class Defender(pygame.sprite.Sprite):

    def __init__(self, pos, groups, next_screen, outOfBounds):
        super().__init__(groups)
        self.status = "right"
        self.next_screen = next_screen
        self.import_assets()
        self.frame_index = 0
        self.ogPos = pos
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.outOfBounds = outOfBounds
        self.stop_opps = False

        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(-1, 0)
        self.speed = 200
        self.max_speed = 500  # Maximum speed when tapping spacebar
        self.min_speed = 200  # Minimum speed
        self.speed_decay = 100  # How much speed decreases per second

        self.caught = False
        self.tackled = False
        self.hes_down = False

        self.first = 0

        self.skip = False
        self.turnover = False

        self.down = 1

        self.yard = 10
        self.white = (255, 255, 255)
        self.color = "green"

        self.touchdown = False
        self.opps_turn = False

        self.opp_transition = False
        self.opp_down = 1

        self.run_sound = pygame.mixer.Sound("../madden25_imgs/run.wav")
        self.run_sound.set_volume(0.05)

        self.tackle_sound = pygame.mixer.Sound("../madden25_imgs/tackle.wav")
        self.tackle_sound.set_volume(0.1)

        self.down_sound = pygame.mixer.Sound("../madden25_imgs/down.wav")
        self.down_sound.set_volume(0.04)

        self.opp_td_sound = pygame.mixer.Sound("../madden25_imgs/opp_td.wav")
        self.opp_td_sound.set_volume(0.05)

    def get_status(self):
        if self.direction.x == 1:
            self.status = "right"

        if self.direction.x == -1:
            self.status = "left"

    def import_assets(self):
        path = "../madden25_imgs/team/"

        self.animation = []
        if self.status == "right":
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                self.animation.append(surf)
        elif self.status == "left":
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                flip = pygame.transform.flip(surf, True, False)
                self.animation.append(flip)

    def outofbounds(self, screen, time, yardline):
        screen.fill((0, 0, 0))

        # Determine the current state
        if self._is_blocked():
            state = "blocked"
            downs_surface = self._handle_blocked(yardline)
        elif self._is_out():
            state = "out"
            downs_surface = self._handle_out(yardline)
        elif self._is_touchdown(yardline):
            state = "touchdown"
            self.opp_td_sound.play()
            downs_surface = self._handle_touchdown()
        elif self._is_hes_down():
            state = "he's down"
            self.down_sound.play()
            downs_surface = self._handle_hes_down()
        else:
            state = "default"
            downs_surface = self._handle_default()

        # print(f"State determined: {state}")  
        self._render_message(screen, downs_surface)

        self.outOfBounds = True
        self.stop_opps = False
        self.direction.x = -1
        time.sleep(2 if self.touchdown else 1)

        self._handle_special_conditions(time, screen, yardline)

    def _is_blocked(self):
        return self.tackled and not self.touchdown and not self.hes_down and self.down > 0

    def _is_out(self):
        return not self.tackled and not self.touchdown and not self.hes_down and self.down > 0

    def _is_touchdown(self, yardline):
        return yardline[0] == 90 and self.touchdown

    def _is_hes_down(self):
        return not self.tackled and self.hes_down

    def _handle_blocked(self, yardline):
        self.color = "red"
        self.skip = True
        self._advance_down()
        if yardline[0] < 90:
            yardline[0] += 10
        self.tackled = False
        self.turnover = False
        return self._render_text("BLOCKED", "red")

    def _handle_out(self, yardline):
        self.color = "red"
        self._advance_down()
        if yardline[0] < 90:
            yardline[0] += 10
        self.turnover = False
        return self._render_text("OUT", "red")

    def _handle_touchdown(self):
        self.color = "red"
        self._reset_flags()
        return self._render_text("TOUCHDOWN", "red")

    def _handle_hes_down(self):
        self.color = "green"
        self.turnover = True
        self.skip = False
        return self._render_text("HE'S DOWN", "green")

    def _handle_default(self):
        self.color = "red"
        self.turnover = False
        self.hes_down = False
        self._advance_down()
        return self._render_text("BLOCKED", "red")

    def _advance_down(self):
        if self.down == 1:
            self.down += 3
        elif self.down == 2:
            self.down += 2
        elif self.down == 3:
            self.down += 1
        self.yard = 10

    def _reset_flags(self):
        self.tackled = False
        self.hes_down = False
        self.color = "red"
        self.skip = False
        self.turnover = False

    def _render_text(self, text, color):
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
        return my_font.render(text, True, color)

    def _render_message(self, screen, downs_surface):
        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()

    def _handle_special_conditions(self, time, screen, yardline):
        if self.down == 0 and self.turnover and not self.next_screen:
            self.down += 1
            self.turnover = False
            self.stop_opps = True
            self.opp_transition = False
            self.reset_position()
            yardline[0] = 30
            self.your_ball(time, screen)
            self.main_menu()
        elif self.down == 0 and not self.turnover:
            self.down += 1

    def reset_position(self):
        self.pos = pygame.math.Vector2(WINDOW_WIDTH - 200, 350)
        self.rect.center = round(self.pos.x), round(self.pos.y)
        self.speed = 0

    def move(
        self,
        dt,
        yardline,
        screen,
        time,
        position,
        caught,
        opps_group,
        opps_group2,
        opp_posx,
    ):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        if self.speed > self.min_speed:
            self.speed -= self.speed_decay * dt

        self.pos += self.direction * self.speed * dt
        self.rect.center = round(self.pos.x), round(self.pos.y)

        if self.speed >= self.max_speed:
            self.speed = self.max_speed
        if self.speed < self.min_speed:
            self.speed = self.min_speed

        if self.pos.x > 1340:
            self.pos.x = 1340

        if self.pos.y < 70:
            self.direction.y = 0

        if self.pos.y > 575:
            self.pos.y = 575

        if pygame.sprite.spritecollide(
            self, opps_group, False, pygame.sprite.collide_mask
        ):
            self.tackle_sound.play()
            self.tackled = True
            self.hes_down = False
            self.outofbounds(screen, time, yardline)
            self.downs(screen, time)
            self.reset_position()
            self.direction.y = 0

        if pygame.sprite.spritecollide(
            self, opps_group2, False, pygame.sprite.collide_mask
        ):
            self.hes_down = True
            self.outofbounds(screen, time, yardline)
            self.downs(screen, time)
            self.opps_turn = False
            self.reset_position()
            self.direction.y = 0

        if self.pos.x < 20:
            self.pos.x = 20

        if self.opp_posx and yardline[0] >= 90:
            self.touchdown = True
            self.outofbounds(screen, time, yardline)
            self.stop_opps = True
            self.opps_turn = False
            self.reset_position()

            self.next_screen = True
            self.direction.y = 0
            self.next_screen = False

        elif self.opp_posx:
            self.rect = self.image.get_rect(center=self.ogPos)
            self.pos = pygame.math.Vector2(self.rect.center)
            self.direction = pygame.math.Vector2(-1, 0)

            yardline[0] += 10
            self.next_screen = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.run_sound.play()
                    self.speed += 50

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.status = "right"
            self.direction.x = 1
        if keys[pygame.K_LEFT]:
            self.status = "left"
            self.direction.x = -1
        if keys[pygame.K_UP]:
            self.direction.y = -1
        if keys[pygame.K_DOWN]:
            self.direction.y = 1

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def draw_speed_meter(self, screen):
        bar_width = 200
        bar_height = 20
        bar_x = 170
        bar_y = 20
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height))

        green_bar_width = int(
            (self.speed - self.min_speed)
            / (self.max_speed - self.min_speed)
            * bar_width
        )

        pygame.draw.rect(
            screen, (0, 255, 0), (bar_x, bar_y, green_bar_width, bar_height)
        )
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        speed_surface = my_font.render("SPEED:", True, pygame.Color(255, 255, 255))
        speed_rect = speed_surface.get_rect()
        speed_rect.midtop = (100, 10)
        screen.blit(speed_surface, speed_rect)

    def your_ball(self, time, screen):
        screen.fill((0, 0, 0))

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

        downs_surface = my_font.render("YOUR BALL", True, "green")

        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        time.sleep(2)

    def opp_show_downs(self, down, screen, main_menu, time):
        self.down = down % 4
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        if self.down == 1:
            self.yard = 10
            down_surface = my_font.render(
                str(self.down) + "ST & " + str(self.yard), True, self.white
            )
        elif self.down == 2:
            down_surface = my_font.render(
                str(self.down) + "ND & " + str(self.yard), True, self.white
            )
        elif self.down == 3:
            down_surface = my_font.render(
                str(self.down) + "RD & " + str(self.yard), True, self.white
            )
        elif self.down == 0:
            down_surface = my_font.render("4TH & " + str(self.yard), True, self.white)

        down_rect = down_surface.get_rect()
        down_rect.midtop = (689, 5)
        screen.blit(down_surface, down_rect)

        return self.down

    def downs(self, screen, time):
        self.down = (self.down % 4) + 1

        screen.fill((0, 0, 0))

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
        if not self.next_screen:
            if self.down == 1:
                downs_surface = my_font.render(
                    str(self.down) + "ST & " + str(self.yard), True, self.color
                )

            if self.down == 2:
                self.yard -= random.choice([1, 2, 3])
                downs_surface = my_font.render(
                    str(self.down) + "ND & " + str(self.yard), True, self.color
                )
            elif self.down == 3:
                self.yard -= random.choice([1, 2, 3])
                downs_surface = my_font.render(
                    str(self.down) + "RD & " + str(self.yard), True, self.color
                )
            elif self.down == 4:
                self.yard -= random.choice([1, 2, 3])
                downs_surface = my_font.render(
                    str(self.down) + "TH & " + str(self.yard), True, self.color
                )
        elif self.next_screen:
            downs_surface = my_font.render("1ST & 10", True, "red")
            self.next_screen = False

        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        time.sleep(1)

    def update(
        self,
        dt,
        events,
        yardline,
        screen,
        time,
        position,
        caught,
        opps_group,
        opps_group2,
        score,
        stop_opps,
        outOfBounds,
        opp_posx,
        main_menu,
        opps_turn,
        down,
        render_end_menu,
        end_menu,
    ):
        if down:
            down = 1
        self.main_menu = main_menu
        self.opps_turn = opps_turn
        self.opp_posx = opp_posx
        self.outOfBounds = outOfBounds
        self.stop_opps = stop_opps
        self.input(events)

        self.animate(dt)
        self.get_status()
        self.import_assets()

        if self.first == 0:
            self.reset_position()
            self.first = 1

        if self.touchdown and not self.outOfBounds:
            score[1] += 7
            yardline[0] = 30
            if score[1] >= 30:
                render_end_menu(False)
                end_menu()
            self.touchdown = False
            self.your_ball(time, screen)
            opps_turn = False
            main_menu()

        self.move(
            dt,
            yardline,
            screen,
            time,
            position,
            caught,
            opps_group,
            opps_group2,
            opp_posx,
        )

        return (
            self.next_screen,
            self.outOfBounds,
            self.pos.x,
            self.caught,
            score,
            yardline,
            self.stop_opps,
            0,
            self.opps_turn,
            self.skip,
            down,
        )
