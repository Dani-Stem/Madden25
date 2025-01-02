import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.import_assets()

        self.frame_index = 0
        self.pos = pygame.math.Vector2(pos)
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=self.pos)

        self.pause_frame = None  # Add this to track which frame to pause on
        self.result = None  # Store the result (Heads or Tails)

    def import_assets(self):
        path = "../madden25_imgs/coin/"
        self.animation = []
        for frame in range(3):  # Assuming 3 frames for the animation
            surf = pygame.image.load(f"{path}{frame}.png").convert_alpha()
            self.animation.append(surf)

    def animate(self, dt):
        # If we are pausing, skip the frame update
        if self.pause_frame is not None:
            return

        self.frame_index += 10 * dt  # Update frame index based on time
        if self.frame_index >= len(self.animation):
            self.frame_index = 0

        self.image = self.animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.pos)

    def pause_on_frame(self, frame):
        frame = 0
        # frame = random.choice([0, 2])
        """Pause animation on a specific frame."""
        if 0 <= frame < len(self.animation):
            self.pause_frame = frame
            self.image = self.animation[frame]
            self.rect = self.image.get_rect(center=self.pos)

            # Determine result based on frame
            if frame == 0:
                self.result = "HEADS"
            elif frame == 2:
                self.result = "TAILS"

    def unpause(self):
        """Unpause the animation."""
        self.pause_frame = None
        self.result = None  # Reset result when unpaused

    def update(self, dt):
        self.animate(dt)
