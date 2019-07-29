import pygame
#  File Configurations including Globals




# game control/testing
crashed = False
game_exit = False
menu = False

# colors
board_color = (255, 60, 90)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (200, 0, 0)
green = (0, 255, 0)
dark_green = (0, 200, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 200)

# display dimensions
disp_width = 1200
disp_height = 600

#
gameDisplay = pygame.display.set_mode((config.disp_width, config.disp_height))
pygame.display.set_caption('BlackJackTrainerAlfa')
clock = pygame.time.Clock()
# res
elfPic = pygame.image.load('Lore-race-Dunmer.png')
aceClub = pygame.image.load('ace_club.png')
aceDiamond = pygame.image.load('ace_diamond.png')
aceHeart = pygame.image.load('ace_hearts.png')
aceSpade = pygame.image.load('ace_spade.png')

# pygame constructors

small_text = pygame.font.Font("freesansbold.ttf", 20)
