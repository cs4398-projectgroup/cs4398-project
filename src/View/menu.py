import pygame


class Menu():

    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('BlackJackTrainerAlfa')
    clock = pygame.time.Clock()
    crashed = False

    def __init__(self):
        None

    def game_intro(self):
        intro = True


        #while intro:
            #for event in pygame.event.get():
                #if



if __name__ == '__main__':
    pygame.init()
    testmenu = Menu()
