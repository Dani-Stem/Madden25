import pygame
import sys
import math
import time


class FieldGoal:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        self.SCREEN_WIDTH = 1368
        self.SCREEN_HEIGHT = 712

        # Colors
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        # Set up the screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Meter properties
        self.METER_WIDTH = 400
        self.METER_HEIGHT = 20
        self.METER_X = (self.SCREEN_WIDTH - self.METER_WIDTH) // 2 + 10
        self.METER_Y = self.SCREEN_HEIGHT - self.METER_HEIGHT - 50
        self.BAR_SPEED = 5
        self.bar_x = self.METER_X
        self.bar_direction = 1

        # Target lines
        self.TARGETS = [
            (self.METER_X + 188, self.RED),
            (self.METER_X + 215, self.RED),
        ]

        # Game state
        self.running = True
        self.bar_stopped = False
        self.success = False
        self.animate_curve = False
        self.show_top_placeholder = True

        # Clock for controlling frame rate
        self.clock = pygame.time.Clock()

        # Load images for background and animation
        self.sky_images = [
            pygame.image.load(f"../madden25_imgs/{i}.png").convert_alpha()
            for i in range(1, 6)
        ]
        self.sky_images = [
            pygame.transform.scale(
                image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT * 2 // 3)
            )
            for image in self.sky_images
        ]
        self.ground_image = pygame.image.load(
            "../madden25_imgs/field1.png"
        ).convert_alpha()
        self.ground_image = pygame.transform.scale(
            self.ground_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT // 3)
        )
        self.fieldgoal_image = pygame.image.load(
            "../madden25_imgs/fieldgoal.png"
        ).convert_alpha()
        self.placeholder_top_image = pygame.image.load(
            "../madden25_imgs/fgBall.png"
        ).convert_alpha()

        self.original_image = pygame.image.load(
            "../madden25_imgs/fgBall.png"
        ).convert_alpha()

        self.kick_sound = pygame.mixer.Sound("../madden25_imgs/kick.wav")
        self.kick_sound.set_volume(0.2)

        self.fg_sound = pygame.mixer.Sound("../madden25_imgs/fg.wav")
        self.fg_sound.set_volume(0.1)

        self.fg_sound2 = pygame.mixer.Sound("../madden25_imgs/no_good.wav")
        self.fg_sound2.set_volume(0.1)

        # Rotation and curve motion variables
        self.angle = 0
        self.rotation_speed = 12
        self.c_curve_amplitude = 150
        self.c_curve_height = 400
        self.c_curve_speed = 3
        self.y_position = 0
        self.curve_center_x = self.SCREEN_WIDTH // 2
        self.curve_center_y = self.SCREEN_HEIGHT // 2

    def display_splash_screen(self, message, color, duration=1):
        """Displays a splash screen with a message for a specified duration."""
        self.screen.fill(self.BLACK)

        # Render the message
        font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(self.SCREEN_WIDTH / 2, 300))
        self.screen.blit(text_surface, text_rect)

        pygame.display.flip()
        time.sleep(2.5)

    def reset(self):
        self.bar_stopped = False
        self.bar_x = self.METER_X + 10
        self.success = False
        self.animate_curve = False
        self.show_top_placeholder = True
        self.y_position = 0

    def opp_ball(self, time, screen):
        screen.fill((0, 0, 0))

        my_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)

        downs_surface = my_font.render("OPPONENT'S BALL", True, "red")

        downs_rect = downs_surface.get_rect()
        downs_rect.midtop = (self.SCREEN_WIDTH / 2, 300)
        screen.blit(downs_surface, downs_rect)
        pygame.display.flip()
        time.sleep(2)

    def run(
        self,
        score,
        stop_opp,
        screen,
        touchdown,
        opp_transition,
        opponents_turn,
        down,
        render_end_menu,
        end_menu,
    ):
        opponents_turn = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.kick_sound.play()
                        if not self.bar_stopped:
                            self.bar_stopped = True
                            self.show_top_placeholder = False

                            # Check if the bar is within the target lines
                            bar_center = self.bar_x + self.METER_HEIGHT // 2
                            if self.TARGETS[0][0] <= bar_center <= self.TARGETS[1][0]:
                                self.success = True
                                self.animate_curve = True
                            else:
                                self.success = False

            if not self.bar_stopped:
                self.bar_x += self.BAR_SPEED * self.bar_direction
                if (
                    self.bar_x <= self.METER_X
                    or self.bar_x + self.METER_HEIGHT >= self.METER_X + self.METER_WIDTH
                ):
                    self.bar_direction *= -1

            for sky_image in self.sky_images:
                self.screen.blit(sky_image, (0, 0))
            self.screen.blit(
                self.ground_image, (0, self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 3)
            )
            self.screen.blit(
                self.fieldgoal_image, (self.SCREEN_WIDTH / 2.4, self.SCREEN_HEIGHT / 4)
            )

            if self.show_top_placeholder:
                self.screen.blit(
                    self.placeholder_top_image,
                    (
                        (self.SCREEN_WIDTH // 2) - 68,
                        540,
                    ),
                )

            pygame.draw.rect(
                self.screen,
                self.BLACK,
                (self.METER_X, self.METER_Y, self.METER_WIDTH, self.METER_HEIGHT),
                2,
            )

            pygame.draw.rect(
                self.screen,
                self.YELLOW,
                (self.bar_x, self.METER_Y, self.METER_HEIGHT, self.METER_HEIGHT),
            )

            for target_x, color in self.TARGETS:
                pygame.draw.line(
                    self.screen,
                    color,
                    (target_x, self.METER_Y),
                    (target_x, self.METER_Y + self.METER_HEIGHT),
                    2,
                )

            if self.bar_stopped and not self.animate_curve:
                self.animate_curve = True

            # Animation upon success
            if self.animate_curve:
                # Update rotation angle
                self.angle = (self.angle + self.rotation_speed) % 360

                # Update vertical "C" curve motion
                self.y_position += self.c_curve_speed
                if self.y_position > self.c_curve_height:
                    if self.success:
                        self.fg_sound.play()
                        self.display_splash_screen("IT'S GOOD!", self.GREEN, duration=1)
                        score[0] += 3
                    else:
                        self.fg_sound2.play()
                        self.display_splash_screen("NO GOOD", self.RED, duration=1)

                    self.reset()  # Reset after animation finishes

                    touchdown = False
                    opp_transition = True
                    opponents_turn = True
                    down = 1

                    if score[0] >= 30:
                        render_end_menu(True)
                        end_menu()
                    self.opp_ball(time, screen)

                    return (
                        score[0],
                        stop_opp,
                        touchdown,
                        opp_transition,
                        opponents_turn,
                        down,
                    )
                if self.success:

                    # Calculate the position based on the "C" curve
                    curve_progress = (
                        self.y_position / self.c_curve_height
                    )  # Progress along the curve (0 to 1)
                    y_offset = self.c_curve_height * (
                        curve_progress - 0.5
                    )  # Shift to center vertically
                    x_offset = -self.c_curve_amplitude * math.sin(
                        math.pi * curve_progress
                    )  # "C" curve motion

                    current_x = self.curve_center_x - x_offset
                    current_y = self.curve_center_y - y_offset

                    # Scale the image based on progress (largest at the start, smallest at the end)
                    scale_factor = 2.0 - (1.5 * curve_progress)  # Scale from 2.0 to 0.5
                    new_size = (
                        int(self.original_image.get_width() * scale_factor),
                        int(self.original_image.get_height() * scale_factor),
                    )
                    scaled_image = pygame.transform.scale(self.original_image, new_size)

                    # Rotate the scaled image
                    rotated_image = pygame.transform.rotate(scaled_image, self.angle)

                    # Center the rotated image at the current position
                    rotated_rect = rotated_image.get_rect(center=(current_x, current_y))
                else:
                    # Calculate the position based on diagonal motion
                    curve_progress = (
                        self.y_position / self.c_curve_height
                    )  # Progress along the motion (0 to 1)

                    # Diagonal motion: x and y decrease proportionally
                    x_offset = (
                        self.c_curve_amplitude * curve_progress
                    )  # Horizontal movement to the left
                    y_offset = (
                        self.c_curve_height * curve_progress
                    )  # Vertical upward movement

                    current_x = self.curve_center_x - x_offset
                    current_y = 600 - y_offset

                    # Scale the image based on progress (largest at the start, smallest at the end)
                    scale_factor = 2.0 - (1.5 * curve_progress)  # Scale from 2.0 to 0.5
                    new_size = (
                        int(self.original_image.get_width() * scale_factor),
                        int(self.original_image.get_height() * scale_factor),
                    )
                    scaled_image = pygame.transform.scale(self.original_image, new_size)

                    # Rotate the scaled image
                    rotated_image = pygame.transform.rotate(scaled_image, self.angle)

                    # Center the rotated image at the current position
                    rotated_rect = rotated_image.get_rect(center=(current_x, current_y))

                    # Draw the transformed image
                    self.screen.blit(rotated_image, rotated_rect)

                # Draw the transformed image
                self.screen.blit(rotated_image, rotated_rect)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = FieldGoal()
    game.run()
