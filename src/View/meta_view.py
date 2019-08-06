import pygame
from View.menu import Menu
from View.table import Table
from View import config
from Control.blackjack_controller import BlackjackController


class MetaView:
    def __init__(self):
        self.controller = BlackjackController()
        self.new_table = Table(self.controller)

    @staticmethod
    def quit_game():
        pygame.quit()
        quit()

    # passes two objects that tell menu buttons where to go
    def meta_loop(self):
        config.game_exit = Menu().game_menu()
        while not config.game_exit:
            config.new_game = False
            self.new_table.player_hand_loop()
            if config.new_game:
                self.controller = BlackjackController()
                self.new_table = Table(self.controller)
            elif config.game_exit:
                break
            else:
                self.new_table.end_of_hand()
                if config.new_game:
                    self.controller = BlackjackController()
                    self.new_table = Table(self.controller)
            self.controller.get_new_player_hand()
            self.controller.get_new_dealer_hand()


if __name__ == "__main__":
    MetaView().meta_loop()
