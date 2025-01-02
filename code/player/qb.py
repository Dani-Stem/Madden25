import pygame
from items.football import Football
import time

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


class QB(pygame.sprite.Sprite):

    def __init__(self, pos, groups, next_screen, qbt, snap, outOfBounds):
        super().__init__(groups)
        self.status = "right"
        self.next_screen = next_screen
        self.qbt = qbt
        self.import_assets()
        self.frame_index = 0
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.fOutOfBounds = False
        self.rbt = False
        self.rbt_td = False

        self.snap = snap
        self.throw = False
        self.pressed = 0
        self.moves = False
        self.menu = False

        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 200
        self.max_speed = 500  # Maximum speed when holding spacebar
        self.min_speed = 200  # Minimum speed
        self.speed_decay = 100  # How much speed decreases per second

        # Oscillation for speed meter
        self.meter_speed = 300  # How fast the meter oscillates
        self.current_meter_value = self.min_speed
        self.meter_increasing = True
        self.space_pressed = False  # Track space bar state

        self.snap_sound = pygame.mixer.Sound("../madden25_imgs/snap.wav")
        self.snap_sound.set_volume(0.05)

        self.throw_sound = pygame.mixer.Sound("../madden25_imgs/throw.wav")
        self.throw_sound.set_volume(0.1)

    def import_assets(self):
        path = "../madden25_imgs/qb/"

        self.animation = []
        for frame in range(3):
            surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
            self.animation.append(surf)

    def outofbounds(self, screen, time, menu):
        self.menu = menu

        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        # Set the overlay color and transparency (RGBA format)
        overlay.fill((0, 0, 0, 128))  # Black with 50% transparency

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
        downs_surface = my_font.render("INCOMPLETE PASS", True, "red")
        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        screen.blit(overlay, (0, 0))
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        self.fOutOfBounds = True
        time.sleep(1)

    def move(self, dt, yardline, screen, time):
        if self.moves and self.qbt:
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            # Decrease speed gradually
            if self.speed > self.min_speed:
                self.speed -= self.speed_decay * dt

            self.pos += self.direction * self.speed * dt
            self.rect.center = round(self.pos.x), round(self.pos.y)

            # Clamp speed to max and min values
            self.speed = max(self.min_speed, min(self.speed, self.max_speed))

            # Boundary conditions
            if self.pos.x < 50:
                self.pos.x = 50
            if self.pos.x > 150:
                self.pos.x = 150

            if self.next_screen is False:
                if self.pos.x > 1180 + 90 and yardline[0] >= 90:
                    self.pos.x = 1180 + 90
            elif self.next_screen:
                if self.pos.x > 1180 and yardline[0] >= 90:
                    self.pos.x = 1180

            if self.pos.y < 100:
                self.pos.y = 100
            if self.pos.y > 575:
                self.pos.y = 575

            if self.pos.x > WINDOW_WIDTH:
                self.pos.x = 0
                yardline[0] += 10
                self.next_screen = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def throw_football(self, football_group, screen, time):
        if self.pressed == 2:
            self.throw_sound.play()
            Football((self.rect.topright), football_group, self, screen, time)

            self.pressed = 3

    def input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                pygame.K_SPACE = 32
                if event.key == pygame.K_SPACE:
                    self.space_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.space_pressed = False
                    if self.pressed < 3:
                        self.pressed += 1
                        self.moves = True
                        self.direction.x = -1
                        if not self.throw and self.pressed == 1:
                            self.snap_sound.play()
                            self.snap = True

                        if self.pressed == 1 and self.rbt:
                            self.pressed = 3
                            self.qbt = False

                        if self.pressed == 2:
                            self.throw = True

                            # self.qbt = False  # change

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
        if self.snap:
            self.frame_index = 1
        if self.pressed == 3:
            self.frame_index = 2
            self.throw = False

        self.image = self.animation[int(self.frame_index)]

    def draw_speed_meter(self, screen):
        """bar_width = 200
        bar_height = 20
        bar_x = 170
        bar_y = 20
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height))

        green_bar_width = int(
            (self.current_meter_value - self.min_speed)
            / (self.max_speed - self.min_speed)
            * bar_width
        )
        pygame.draw.rect(
            screen, (0, 255, 0), (bar_x, bar_y, green_bar_width, bar_height)
        )

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        speed_surface = my_font.render("POWER:", True, pygame.Color(255, 255, 255))
        speed_rect = speed_surface.get_rect()
        speed_rect.midtop = (100, 10)
        screen.blit(speed_surface, speed_rect)"""

        if self.snap:
            if int(time.time() * 2) % 2 == 0:
                my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
                speed_surface = my_font.render("SPACEBAR TO THROW", True, "yellow")
                speed_rect = speed_surface.get_rect()
                speed_rect.midtop = (215, 5)
                screen.blit(speed_surface, speed_rect)

        else:
            if int(time.time() * 2) % 2 == 0:
                my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
                speed_surface = my_font.render("SPACEBAR TO SNAP", True, "white")
                speed_rect = speed_surface.get_rect()
                speed_rect.midtop = (200, 5)
                screen.blit(speed_surface, speed_rect)

    def opp_ball(self, time, screen):
        screen.fill((0, 0, 0))

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

        downs_surface = my_font.render("OPPONENT'S BALL", True, "red")

        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (WINDOW_WIDTH / 2, 300)
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        time.sleep(2)

    def update(
        self,
        dt,
        events,
        yardline,
        football_group,
        outOfBounds,
        screen,
        time,
        rbt,
        main_menu,
        winner,
        rbt_td,
        stop_opp,
        score,
        render_end_menu,
        end_menu,
        render_menu,
        selected_index,
        opp_transition,
    ):
        # Oscillate speed meter if space is held
        if self.space_pressed and self.pressed == 1:
            if self.meter_increasing:
                self.current_meter_value += self.meter_speed * dt
                if self.current_meter_value >= self.max_speed:
                    self.current_meter_value = self.max_speed
                    self.meter_increasing = False
            else:
                self.current_meter_value -= self.meter_speed * dt
                if self.current_meter_value <= self.min_speed:
                    self.current_meter_value = self.min_speed
                    self.meter_increasing = True

        self.winner = None
        self.throw_football(football_group, screen, time)
        self.input(events)
        self.move(dt, yardline, screen, time)
        self.animate(dt)
        self.rbt = rbt
        self.rbt_td = rbt_td
        self.outOfBounds = outOfBounds

        if outOfBounds or self.fOutOfBounds:
            self.pos.x = 120
            self.pos.y = 350
            self.rect.center = round(self.pos.x), round(self.pos.y)
            self.next_screen = False
            self.qbt = True
            self.snap = False
            self.pressed = 0
            self.frame_index = 0
            self.moves = False
            outOfBounds = False
            self.fOutOfBounds = False
            if not self.rbt and self.rbt_td:
                score[0] += 7
                if score[0] >=30:
                    render_end_menu(winner)
                    end_menu()
                yardline[0] = 30
                self.rbt_td = False
                self.opp_ball(time, screen)
                stop_opp()
            if not self.winner:
                self.snap = False
                if not opp_transition:
                    render_menu(selected_index, self.menu)
                    main_menu()

        return self.next_screen, self.qbt, self.snap, outOfBounds, self.rbt, self.rbt_td
