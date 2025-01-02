import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


clock = pygame.time.Clock()


class Football(pygame.sprite.Sprite):

    def __init__(self, pos, groups, qb, screen, time):
        super().__init__(groups)
        self.image = pygame.image.load("../madden25_imgs/football.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        # self.mask = pygame.mask.from_surface(self.image)
        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 400
        self.qb = qb
        self.screen = screen
        self.time = time
        self.menu = False

        self.catch_sound = pygame.mixer.Sound("../madden25_imgs/catch.wav")
        self.catch_sound.set_volume(0.05)

        self.incomplete_sound = pygame.mixer.Sound("../madden25_imgs/incomplete.wav")
        self.incomplete_sound.set_volume(0.2)

    def catch(self, team_group):
        # Detect collisions and get the colliding sprite(s)
        colliding_sprites = pygame.sprite.spritecollide(
            self, team_group, True, pygame.sprite.collide_mask
        )
        if colliding_sprites:
            # Get the position of the first collision
            for sprite in colliding_sprites:
                collision_position = (
                    sprite.rect.center
                )  # Or use another rect property like `topleft`

            # Handle collision: kill the football and update qb.qbt
            self.catch_sound.play()
            self.kill()
            self.qb.qbt = False
            return collision_position

    def int(self, opps_group):
        # Detect collisions and get the colliding sprite(s)
        if pygame.sprite.spritecollide(
            self, opps_group, True, pygame.sprite.collide_mask
        ):
            self.incomplete_sound.play()

            self.kill()
            self.qb.qbt = False
            self.menu = True
            self.qb.outofbounds(self.screen, self.time, self.menu)

    def update(self, dt, team_group, opps_group):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        self.int(opps_group)

        if self.rect.left > WINDOW_WIDTH:
            self.incomplete_sound.play()
            self.menu = True
            self.qb.outofbounds(self.screen, self.time, self.menu)
            self.kill()

        if self.rect.bottom < 0:
            self.kill()

        collision_position = self.catch(team_group)
        if collision_position != None:
            return collision_position
