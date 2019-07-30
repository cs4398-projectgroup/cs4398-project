import pygame
from View import config
from View.button import Button


class Menu:

    def __init__(self, game_loop, quit_game):
        self.game_loop = game_loop
        self.quit_game = quit_game

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    # displays ace cards
    @staticmethod
    def ace_show(x, y):
        config.gameDisplay.blit(config.demo_images[1][0], (x, y))
        config.gameDisplay.blit(config.demo_images[0][0], (x + 100, y))
        config.gameDisplay.blit(config.demo_images[3][0], (x + 200, y))
        config.gameDisplay.blit(config.demo_images[2][0], (x + 300, y))

    def game_menu(self):
        config.menu = True
        while config.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            config.gameDisplay.fill(config.board_color)
            large_text = pygame.font.Font('freesansbold.ttf', 100)
            text_surf, text_rect = self.text_objects("BlackJack", large_text)
            text_rect.center = ((config.disp_width / 2), (config.disp_height / 2.2))
            config.gameDisplay.blit(text_surf, text_rect)

            button1 = Button("PLAY", 550, 350, 100, 50, config.white, config.dark_red, self.game_loop)
            button1.intro_button()
            button2 = Button("QUIT", 550, 425, 100, 50, config.white, config.dark_red, self.quit_game)
            button2.intro_button()

            self.ace_show((config.disp_width / 2.9), 40)
            pygame.display.update()
            config.clock.tick(15)