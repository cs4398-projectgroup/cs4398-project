# displays main game board
import pygame
import time
from View import config


class Table:

    # displays elf
    @staticmethod
    def elf(x, y):
        config.gameDisplay.blit(config.demo_images[2][0], (x, y))

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    @staticmethod
    def user_display(self, text):
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf, text_rect = self.text_objects(text, large_text)
        text_rect.center = ((config.disp_width / 2), (config.disp_height / 5))
        config.gameDisplay.blit(text_surf, text_rect)
        pygame.display.update()
        # starts game loop over and resets
        time.sleep(1)

    def game_loop(self):
        x = (config.disp_width * 0.4)
        y = (config.disp_height * 0.6)
        left_key = False

        while not config.game_exit:
            # event loop / NOT logic loop
            # creates a list of events per frame per second (mouse movement/clicks etc)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.game_exit = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left_key = True

            # Background Color
            config.gameDisplay.fill(config.board_color)

            # displays elf in loop and displays elf phrase
            self.elf(x, y)
            if left_key == 1:
                say = "Hi im an elf"
                self.user_display(self, say)

            # allows to specific paramameter to update or the entire window if blank
            # pygame.display.flip() always just updates the entire surface
            pygame.display.update()
            config.clock.tick(30)
            left_key = False