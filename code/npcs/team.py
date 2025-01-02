import pygame
from random import randint, uniform
WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712



class Team(pygame.sprite.Sprite):
    def __init__(self, pos, groups):

        super().__init__(groups)
        self.import_assets()

        self.frame_index = 0

        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.midleft)
        self.direction = pygame.math.Vector2(1, uniform(-0.5, 0.5))
        self.speed = randint(100, 200)

    def import_assets(self):
        path = "../madden25_imgs/team/"

        self.animation = []
        for frame in range(8):
            surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
            self.animation.append(surf)

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def update(self, dt, outOfBounds, caught, snap):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.animate(dt)

        if self.rect.left < -50 or self.rect.left > WINDOW_WIDTH + 20:
            self.kill()
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT - 50:
            self.direction.y *= -1  

        if outOfBounds or caught or not snap:
            self.kill()
