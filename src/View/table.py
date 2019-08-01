# displays main game board
import pygame
import time
from View import config
from View.soundeffects import Sound
from Control.blackjack_controller import BlackjackController
from View.button import Button
from View.menu import Menu

class Table:
    def __init__(self):
        self.model = BlackjackController()
        self.result_msg = ''

    @staticmethod
    def text_objects(text, font):
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    @staticmethod
    def user_display(self, text):
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        text_surf, text_rect = self.text_objects(text, large_text)
        text_rect.center = ((config.disp_width / 2), (config.disp_height / 2.5))
        config.gameDisplay.blit(text_surf, text_rect)
        pygame.display.update()
        # starts game loop over and resets
        time.sleep(1)

    def game_loop(self):
        x = config.disp_width * 0.4
        y = config.disp_height * 0.6
        config.crashed = False
        config.game_exit = False

        # Sound Effect of Dealing 4 cards
        sound = Sound()
        sound.get_sound_effect("Deal4")

        config.gameDisplay.fill(config.board_color)

        self.show_dealers_hand()
        # self.show_players_hand()

        while not config.game_exit:
            # event loop / NOT logic loop
            # creates a list of events per frame per second (mouse movement/clicks etc)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.game_exit = True
                    config.crashed = True
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # buttons for hit,stand,new game, and quit game
                    hit_button = Button("HIT ME", 100, 500, 100, 50, config.rose_white, config.dark_red, self.hit)
                    hit_button.intro_button()
                    stand_button = Button("STAND", 300, 500, 100, 50, config.rose_white, config.dark_red, self.stand)
                    stand_button.intro_button()
                    new_game_button = Button("NEW GAME", 800, 500, 150, 50, config.rose_white, config.dark_red,
                                             self.new_game)
                    new_game_button.intro_button()
                    quit_button = Button("QUIT GAME", 1000, 500, 150, 50, config.rose_white, config.dark_red, self.quit_game)
                    quit_button.intro_button()

            # buttons for hit,stand,new game, and quit game
            hit_button = Button("HIT ME", 100, 500, 100, 50, config.light_gold, config.gold)
            hit_button.intro_button()
            stand_button = Button("STAND", 300, 500, 100, 50, config.light_gold, config.gold)
            stand_button.intro_button()
            new_game_button = Button("NEW GAME", 800, 500, 150, 50, config.light_gold, config.gold)
            new_game_button.intro_button()
            quit_button = Button("QUIT GAME", 1000, 500, 150, 50, config.light_gold, config.gold)
            quit_button.intro_button()

            self.show_players_hand()
            pygame.display.update()
            config.clock.tick(30)
            left_key = False

        self.end_of_game()

    def end_of_game(self):
        self.show_dealers_hand()
        self.show_players_hand()
        self.show_results(self.result_msg)
        while not config.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.game_exit = True
                    config.crashed = True
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_game_button2 = Button("NEW GAME", 800, 500, 150, 50, config.light_gold, config.gold,
                                              self.new_game)
                    new_game_button2.intro_button()
                    quit_button2 = Button("QUIT GAME", 1000, 500, 150, 50, config.light_gold, config.gold,
                                          self.quit_game)
                    quit_button2.intro_button()
            #config.gameDisplay.fill(config.board_color)
            hit_button = Button("", 100, 500, 100, 50, config.board_color, config.board_color)
            hit_button.intro_button()
            stand_button = Button("", 300, 500, 100, 50, config.board_color, config.board_color)
            stand_button.intro_button()
            new_game_button2 = Button("NEW GAME", 800, 500, 150, 50, config.light_gold, config.gold)
            new_game_button2.intro_button()
            quit_button2 = Button("QUIT GAME", 1000, 500, 150, 50, config.light_gold, config.gold)
            quit_button2.intro_button()

            pygame.display.update()
            config.clock.tick(30)
        config.crashed = True

    def new_game(self):
        config.crashed = True
        config.game_exit = True
        new_start = Table().game_loop
        menu_start = Menu(new_start, self.quit_game)
        menu_start.game_menu()

    def show_dealers_hand(self):
        k = 1
        dealers_hand = self.model.get_dealers_hand()
        for i in range(len(dealers_hand)):
            right = 500
            down = 0
            card = pygame.image.load(str(dealers_hand[i].get_filename()))
            config.gameDisplay.blit(card, (right + k, down))
            k += 100

    def show_players_hand(self):
        k = 1
        players_hand = self.model.get_players_hand()
        for i in range(len(players_hand)):
            right = 500
            down = 400
            card = pygame.image.load(str(players_hand[i].get_filename()))
            config.gameDisplay.blit(card, (right + k, down))
            k += 100

    def hit(self):
        (card, score) = self.model.hit_player()
        if score >= 21:
           self.stand()

    def stand(self):
        self.result_msg = self.model.hit_dealer()
        self.show_dealers_hand()
        config.game_exit = True

    def show_results(self, result_msg):
        self.user_display(self, result_msg)

    def quit_game(self):
        pygame.quit()
        quit()
