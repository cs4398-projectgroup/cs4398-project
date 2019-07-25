import pygame


class Button():

    # button functionality with message, coordinates, width/height, active/inactive color
    def into_button(msg, x, y, w, h, ac, ic, action=None):
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
        text_surf, text_rect = text_objects(msg, small_text)
        #                     center of x     center of y
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(text_surf, text_rect)