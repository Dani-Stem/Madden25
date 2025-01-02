import pygame
from random import randint, uniform
WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712

class Opps(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2(-1, uniform(-0.5, 0.5))

        self.import_assets()

        self.frame_index = 0

        self.ogPos = pos

        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = randint(100, 400)

    def import_assets(self):
        path = "../madden25_imgs/opps/"

        self.animation = []
        if int(self.direction.x) == -1:
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                flip = pygame.transform.flip(surf, True, False)
                self.animation.append(flip)
        elif int(self.direction.x) == 1:
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                self.animation.append(surf)

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def update(self, dt, outOfBounds, playerPos, caught, snap):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        self.animate(dt)

        if self.rect.left < -60 or self.rect.left > WINDOW_WIDTH + 450:
            self.direction.x *= -1  
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT - 50:
            self.direction.y *= -1  

        self.import_assets()

        if outOfBounds or not snap:
            self.kill()

        if playerPos == 0:
            self.rect = self.image.get_rect(center=self.ogPos)
            self.pos = pygame.math.Vector2(self.rect.center)
            self.direction = pygame.math.Vector2(-1, uniform(-0.5, 0.5))
        elif caught:
            self.pos.x = self.ogPos[0] + 300
            self.pos.y = self.ogPos[1]
            self.direction = pygame.math.Vector2(-1, uniform(-0.5, 0.5))


class Opps2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2(1, uniform(-0.5, 0.5))

        self.import_assets()

        self.frame_index = 0

        self.ogPos = pos

        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = randint(100, 400)

        self.outOfBounds = False

    def import_assets(self):
        path = "../madden25_imgs/opps/"

        self.animation = []
        if int(self.direction.x) == -1:
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                flip = pygame.transform.flip(surf, True, False)
                self.animation.append(flip)
        elif int(self.direction.x) == 1:
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                self.animation.append(surf)

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def update(self, dt, outOfBounds, playerPos, caught, snap, opp_posx, next_screen):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))
        self.animate(dt)

        if self.rect.left < -20 or self.rect.left > WINDOW_WIDTH - 120:
            self.direction.x *= -1  
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT - 50:
            self.direction.y *= -1  

        self.import_assets()

        self.outOfBounds = outOfBounds

        if next_screen:
            if self.outOfBounds and not opp_posx:
                self.kill()
                self.outOfBounds = False
        else:
            if self.outOfBounds:
                self.kill()
                self.outOfBounds = False

        if opp_posx or self.outOfBounds:
            self.rect = self.image.get_rect(center=self.ogPos)
            self.pos = pygame.math.Vector2(self.rect.center)
            self.direction = pygame.math.Vector2(1, uniform(-0.5, 0.5))
            self.outOfBounds = False

        return self.outOfBounds


class Opps3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.direction = pygame.math.Vector2(1, uniform(-0.5, 0.5))

        self.import_assets()

        self.frame_index = 0

        self.ogPos = pos

        self.posx = 0

        self.first = 0

        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = randint(200, 300)

        self.outOfBounds = False

    def import_assets(self):
        path = "../madden25_imgs/opponent/"

        self.animation = []
        if int(self.direction.x) == -1:
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                flip = pygame.transform.flip(surf, True, False)
                self.animation.append(flip)
        elif int(self.direction.x) == 1:
            for frame in range(8):
                surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
                self.animation.append(surf)

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def reset_positon(self):
        self.rect = self.image.get_rect(center=self.ogPos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(1, uniform(-0.5, 0.5))

    def update(self, dt, outOfBounds, playerPos, caught, yardline, posx):
        self.posx = posx
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.animate(dt)

        self.import_assets()

        self.outOfBounds = outOfBounds

        if self.first == 0:
            self.reset_positon()
            self.first = 1

        if self.rect.left < -20:
            self.direction.x *= -1  
        if self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT - 50:
            self.direction.y *= -1  

        if self.outOfBounds:
            self.reset_positon()
            self.outOfBounds = False

        if round(self.pos.x) >= 1200:
            self.posx = 1
            self.reset_positon()

        return self.posx, self.outOfBounds
