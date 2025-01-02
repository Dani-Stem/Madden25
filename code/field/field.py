import pygame
WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712



class Field:
    def __init__(self):
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.font = "../madden25_imgs/16bfZX.ttf"

    def draw(self, screen, next_screen, yardline):
        # Draw the field lines (scaling them to fit the window width)
        line_spacing = self.width // 12  # 12 lines spaced evenly across the width
        if next_screen == True:
            for i in range(150, self.width - 80, line_spacing):
                pygame.draw.line(screen, (255, 255, 255), (i, 60), (i, 110), 10)
                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (i, self.height - 100),
                    (i, self.height - 50),
                    10,
                )
        else:
            for i in range(150, self.width - 80, line_spacing):
                pygame.draw.line(
                    screen, (255, 255, 255), (i + 90, 60), (i + 90, 110), 10
                )
                pygame.draw.line(
                    screen,
                    (255, 255, 255),
                    (i + 90, self.height - 100),
                    (i + 90, self.height - 50),
                    10,
                )
        # current yardline
        yardline_font = pygame.font.Font(self.font, 100)
        yardline_surface = yardline_font.render(str(yardline[0]), True, "white")
        yardline_rect = yardline_surface.get_rect()
        yardline_rect.midtop = (140, 300)
        #

        # next yardline
        nextyardline_font = pygame.font.Font(self.font, 100)

        nextyardline_surface = nextyardline_font.render(
            str(yardline[0] + 10), True, "white"
        )

        nextyardline_rect = nextyardline_surface.get_rect()
        if next_screen == False:
            nextyardline_rect.midtop = (1180 + 90, 300)
        else:
            nextyardline_rect.midtop = (1180, 300)
        #

        yardline_left = yardline_rect
        yardline_right = nextyardline_rect

        screen.blit(yardline_surface, yardline_left)

        # blit
        if yardline[0] < 90:

            screen.blit(nextyardline_surface, yardline_right)

        else:
            # Characters and their vertical positions
            characters = [("G", 160), ("O", 260), ("A", 360), ("L", 460)]

            # Loop through each character and its position
            for char, y_pos in characters:
                font_obj = pygame.font.Font(self.font, 100)
                surface = font_obj.render(char, True, "white")
                rect = surface.get_rect()

                if next_screen == True:
                    rect.midtop = (1180, y_pos)
                else:
                    rect.midtop = (1180 + 90, y_pos)
                screen.blit(surface, rect)
