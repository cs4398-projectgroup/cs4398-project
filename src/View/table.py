# displays main game board
import pygame
import time
from View import config
from View.soundeffects import Sound
from Control.blackjackController import BlackjackController
from View.button import Button

class Table:

    def __init__(self):
        model = BlackjackController()
        self.dealers_hand = model.get_dealers_hand()
        self.players_hand = model.get_players_hand()

    #@staticmethod
    #def display_card(x, y):
     #   config.gameDisplay.blit(config.demo_images[1][0], (x, y))
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

        # Sound Effect of Dealing 4 cards
        sound = Sound()
        sound.get_sound_effect('Deal4')

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

            #buttons for hit,stand,new game, and quit game
            hit_button = Button("HIT ME", 800, 550, 75, 30, config.green, config.dark_green)
                                #self.display_card((config.disp_width / 2.9), 40))
            hit_button.game_button()
            stand_button = Button("STAND", 890, 550,75,30, config.green, config.dark_green)
            stand_button.game_button()
            new_game_button = Button("NEW GAME",980, 550, 100,30, config.green, config.dark_blue)
            new_game_button.game_button()
            quit_button = Button("QUIT GAME", 1090, 550, 100, 30, config.green, config.dark_blue)
            quit_button.game_button()

            # displays elf in loop and displays elf phrase
            # self.elf(x, y)
            # if left_key == 1:
            #     say = "Hi im an elf"
            #     self.user_display(self, say)

            # allows to specific paramameter to update or the entire window if blank
            # pygame.display.flip() always just updates the entire surface
            #pygame.display.update()
            self.show_dealers_hand()

            self.show_players_hand()
            pygame.display.flip()

            config.clock.tick(30)
            left_key = False

    def show_dealers_hand(self):
        k = 1
        for i in range(len(self.dealers_hand)):
            right = 500
            down = 0
            card = pygame.image.load(str(self.dealers_hand[i].get_filename()))
            config.gameDisplay.blit(card, (right + k, down))
            k += 100


    def show_players_hand(self):
        k = 1
        for i in range(len(self.players_hand)):
            right = 500
            down = 400
            card = pygame.image.load(str(self.players_hand[i].get_filename()))
            config.gameDisplay.blit(card, (right + k, down))
            k += 100
