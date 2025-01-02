import pygame, sys
from pygame.sprite import Sprite
from pygame.rect import Rect

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712


def render_end_menu(self, winner):

    self.screen.fill(self.BLACK)

    end_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 150)
    select_font = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 100)
    select_font2 = pygame.font.Font("../madden25_imgs/16bfZX.ttf", 75)

    if not winner:
        self.win_music.stop()
        self.lose_music.play()
        result_text = "YOU LOSE"
        result_color = "red"
    else:
        self.lose_music.stop()
        self.win_music.play()
        result_text = "YOU WIN"
        result_color = "green"

    result_surface = end_font.render(result_text, True, result_color)
    result_rect = result_surface.get_rect(
        midtop=(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 10)
    )

    if winner:
        quit_surface2 = select_font2.render("Sweet Victory!", True, "yellow")
        quit_rect2 = quit_surface2.get_rect(center=(WINDOW_WIDTH // 2, 225))
        self.screen.blit(quit_surface2, quit_rect2)

    self.screen.blit(result_surface, result_rect)

    quit_surface = select_font.render(self.end_item, True, result_color)
    quit_rect = quit_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 2))
    self.screen.blit(quit_surface, quit_rect)


def end_menu(self):
    self.player_music.stop()
    self.opp_music.stop()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
