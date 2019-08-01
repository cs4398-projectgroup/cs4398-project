import pygame
import platform
import os
#  File Configurations including Globals

# game control/testing
crashed = False
game_exit = False
menu = False

# colors
# board_color = (255, 60, 90)
board_color = (23, 79, 7)
black = (0, 0, 0)
white = (255, 255, 255)
rose_white = (235, 131, 131)
red = (255, 0, 0)
dark_red = (194, 35, 35)
green = (0, 255, 0)
dark_green = (0, 200, 0)
blue = (0, 0, 255)
dark_blue = (0, 0, 200)
light_gray = (159, 180, 194)
gold = (201, 173, 24)
light_gold = (237, 214, 97)

# display dimensions
disp_width = 1200
disp_height = 600

# pygame constructors
pygame.init()
small_text = pygame.font.Font("freesansbold.ttf", 20)
gameDisplay = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption('BlackJackTrainerAlfa')
clock = pygame.time.Clock()

# loads images in test folder
# 2d list with two variables, pygame image and image name

if platform.system() == 'Windows':
    path = os.getcwd() + r"\images\test_folder"
else:
    path = os.getcwd() + "/images/test_folder"

print(path)
demo_images = []
for image in os.listdir(path):
    demo_images.append([pygame.image.load(path + '/' + image).convert_alpha(), image])

