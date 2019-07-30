import pygame
from View.menu import Menu
from View.table import Table


def quit_game():
    pygame.quit()
    quit()


# passes two objects that tell menu buttons where to go
game_start = Table().game_loop
menu_start = Menu(game_start, quit_game)
menu_start.game_menu()

pygame.quit()
quit()
