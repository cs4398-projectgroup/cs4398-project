import pygame
from View import config


class Button:

    def __init__(self, msg, x, y, w, h, ac, ic, action=None):
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ac = ac
        self.ic = ic
        self.action = action

    def text_objects(self, text, font):
        text_surface = font.render(text, True, config.black)
        return text_surface, text_surface.get_rect()

    # button functionality with message, coordinates, width/height, active/inactive color
    def intro_button(self, msg, x, y, w, h, ac, ic, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
            if click[0] == 1 and action:
                #POSSIBLE TEST CASE HERE
                action()
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        text_surf, text_rect = text_objects(msg, config.small_text)
        #                     center of x     center of y
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(text_surf, text_rect)