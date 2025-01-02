import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


class RB(pygame.sprite.Sprite):

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

        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 200
        self.max_speed = 500  # Maximum speed when tapping spacebar
        self.min_speed = 200  # Minimum speed
        self.speed_decay = 100  # How much speed decreases per second

        self.newPos = None
        self.caught = False
        self.tackled = False

        self.down = 1
        self.yard = 10

        self.touchdown = False

        self.rbt = False

        self.run_sound = pygame.mixer.Sound("../madden25_imgs/run.wav")
        self.run_sound.set_volume(0.05)

        self.tackle_sound = pygame.mixer.Sound("../madden25_imgs/tackle.wav")
        self.tackle_sound.set_volume(0.1)

        self.td_sound = pygame.mixer.Sound("../madden25_imgs/td.wav")
        self.td_sound.set_volume(0.05)

        self.out_sound = pygame.mixer.Sound("../madden25_imgs/out.wav")
        self.out_sound.set_volume(0.2)

    def get_status(self):
        if self.direction.x == 1:
            self.status = "right"

        if self.direction.x == -1:
            self.status = "left"

    def import_assets(self):
        path = "../madden25_imgs/player/"
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
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

        if self.touchdown:
            self.td_sound.play()
            message = "TOUCHDOWN"
            color = "green"
            self.opp_down = 1
            self.rbt = False
        elif self.tackled:
            message = "TACKLED"
            color = "red"
            self.tackled = False
        else:
            self.out_sound.play()
            message = "OUT"
            color = "red"

        downs_surface = my_font.render(message, True, color)
        downs_rect = downs_surface.get_rect(center=(WINDOW_WIDTH / 2, 335))
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        
        if self.touchdown:
            time.sleep(2)
        else:
            time.sleep(1)

        self.outOfBounds = True

    def reset_position(self):
        self.rect = self.image.get_rect(center=self.ogPos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 0

    def move(self, dt, yardline, screen, time, position, caught, opps_group):
        """Update player movement and handle interactions."""
        # Normalize direction
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Gradually decrease speed
        if self.speed > self.min_speed:
            self.speed -= self.speed_decay * dt

        # Update position
        self.pos += self.direction * self.speed * dt
        self.rect.center = round(self.pos.x), round(self.pos.y)

        # Handle caught scenario
        if caught:
            self.rect = self.image.get_rect(center=position)
            self.pos = pygame.math.Vector2(self.rect.center)
            self.direction = pygame.math.Vector2(1, 0)
            self.speed = 50

        # Clamp speed
        self.speed = max(self.min_speed, min(self.speed, self.max_speed))

        # Check boundaries and collisions
        if self.pos.x < 20:
            self.pos.x = 20
        if self.pos.y < 70 or self.pos.y > 575:
            self.outofbounds(screen, time, yardline)
            self.downs(screen, time)
            self.reset_position()
            self.direction.y = 0
            self.next_screen = False

        # Touchdown logic
        if self.pos.x > 1180 and yardline[0] >= 90:
            self.touchdown = True
            self.outofbounds(screen, time, yardline)
            self.reset_position()
            self.direction.y = 0
            self.next_screen = False

        # Handle opponent collision
        if pygame.sprite.spritecollide(
            self, opps_group, True, pygame.sprite.collide_mask
        ):
            self.tackle_sound.play()
            self.tackled = True
            self.outofbounds(screen, time, yardline)
            self.downs(screen, time)
            self.reset_position()
            self.direction.y = 0
            self.next_screen = False

        # Cross screen logic
        if self.pos.x > WINDOW_WIDTH:
            self.pos.x = 0
            yardline[0] += 10
            self.next_screen = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.touchdown:
                    pygame.K_SPACE = False
                else:
                    pygame.K_SPACE = 32
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
        # Speed meter background (static bar)
        bar_width = 200
        bar_height = 20
        bar_x = 170
        bar_y = 20
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height))

        # Calculate the width of the green bar based on the player's speed
        green_bar_width = int(
            (self.speed - self.min_speed)
            / (self.max_speed - self.min_speed)
            * bar_width
        )

        # Draw the dynamic green bar
        pygame.draw.rect(
            screen, (0, 255, 0), (bar_x, bar_y, green_bar_width, bar_height)
        )
        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 50)
        speed_surface = my_font.render("SPEED:", True, pygame.Color(255, 255, 255))
        speed_rect = speed_surface.get_rect()
        speed_rect.midtop = (100, 10)
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
        screen,
        time,
        position,
        caught,
        outOfBounds,
        opps_group,
        score,
        qbt,
        stop_opp,
        opp_transition,
        opp_down,
        rbt,
        rbt_td,
        downs,
        render_end_menu,
        end_menu,
    ):
        self.downs = downs
        self.rbt = rbt
        self.opp_down = opp_down
        self.opp_transition = opp_transition
        self.qbt = qbt
        self.outOfBounds = outOfBounds
        self.input(events)
        self.move(dt, yardline, screen, time, position, caught, opps_group)
        self.animate(dt)
        self.get_status()
        self.import_assets()

        if rbt_td:
            self.touchdown = False

        return (
            self.next_screen,
            self.outOfBounds,
            self.pos.x,
            self.caught,
            score,
            yardline,
            self.opp_transition,
            self.opp_down,
            self.touchdown,
            self.rbt,
        )
