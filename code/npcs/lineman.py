import pygame
import sys
WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


BLACK = (0, 0, 0)
FPS = 60

class Linemen:
    def __init__(self, image_path, screen, x, y_start, y_end, spacing, width=90, height=90, vibration_speed=1, vibration_range=5):
        """
        Initialize the Linemen class with independent vibration functionality for each lineman.

        :param image_path: Path to the lineman image.
        :param screen: The Pygame screen to render on.
        :param x: Initial X-coordinate for the linemen.
        :param y_start: Starting Y-coordinate for the linemen.
        :param y_end: Ending Y-coordinate for the linemen.
        :param spacing: Vertical spacing between the linemen.
        :param width: Width of the linemen image.
        :param height: Height of the linemen image.
        :param vibration_speed: Speed of vibration for the linemen.
        :param vibration_range: Range of vibration for the linemen.
        """
        self.screen = screen
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (70, 70))

        self.linemen = []
        for y in range(y_start, y_end, spacing):
            lineman = {
                "x": x,
                "y": y,
                "initial_x": x,
                "vibration_direction": 1,  
                "vibration_range": vibration_range,  
                "vibration_speed": vibration_speed  
            }
            self.linemen.append(lineman)

    def update_positions(self):
        """
        Update the X-coordinates for independent vibration effect.
        """
        for lineman in self.linemen:
            lineman["x"] += lineman["vibration_speed"] * lineman["vibration_direction"]
            if abs(lineman["x"] - lineman["initial_x"]) > lineman["vibration_range"]:
                lineman["vibration_direction"] *= -1

    def render(self):
        """
        Render the linemen on the screen.
        """
        for lineman in self.linemen:
            lineman_rect = pygame.Rect(lineman["x"], lineman["y"], self.width, self.height)
            self.screen.blit(self.image, lineman_rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Independent Vibrating Linemen")
    clock = pygame.time.Clock()

    raiders = Linemen(
        image_path="../madden25_imgs/raiderx.png",
        screen=screen,
        x=150,
        y_start=250,
        y_end=WINDOW_HEIGHT - 150,
        spacing=WINDOW_HEIGHT // 2,
        vibration_speed=5,  
        vibration_range=10  
    )

    rams = Linemen(
        image_path="../madden25_imgs/ramx_flip.png",
        screen=screen,
        x=240,
        y_start=250,
        y_end=WINDOW_HEIGHT - 150,
        spacing=WINDOW_HEIGHT // 2,
        vibration_speed=2,  
        vibration_range=10  
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        raiders.update_positions()
        rams.update_positions()

        screen.fill(BLACK)

        raiders.render()
        rams.render()

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()