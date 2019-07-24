import pygame
import time
import config

# pygame constructors
# displays game window, flag pygame.SCALED scales reselution based on display
# requires pygame 1.9.6
pygame.init()
gameDisplay = pygame.display.set_mode((config.disp_width, config.disp_height))
pygame.display.set_caption('BlackJackTrainerAlfa')
clock = pygame.time.Clock()
# images
elfPic = pygame.image.load('Lore-race-Dunmer.png')
aceClub = pygame.image.load('ace_club.png')
aceDiamond = pygame.image.load('ace_diamond.png')
aceHeart = pygame.image.load('ace_hearts.png')
aceSpade = pygame.image.load('ace_spade.png')
# displays an elf


def elf(x, y):
    gameDisplay.blit(elfPic, (x, y))


# displays ace cards
def ace_show(x, y):
    gameDisplay.blit(aceClub, (x, y))
    gameDisplay.blit(aceDiamond, (x+100, y))
    gameDisplay.blit(aceHeart, (x+200, y))
    gameDisplay.blit(aceSpade, (x+300, y))


def text_objects(text, font):
    text_surface = font.render(text, True, config.black)
    return text_surface, text_surface.get_rect()


def user_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((config.disp_width/2), (config.disp_height/5))
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()
    # starts game loop over and resets
    time.sleep(2)
    game_loop()


def elf_phrase(phrase):
    user_display(phrase)


# button functionality with message, coordinates, width/height, active/inactive color
def button(msg, x, y, w, h, ac, ic, action=None):
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


def game_menu():
    config.menu = True
    while config.menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        gameDisplay.fill(config.board_color)
        large_text = pygame.font.Font('freesansbold.ttf', 100)
        text_surf, text_rect = text_objects("BlackJack", large_text)
        text_rect.center = ((config.disp_width / 2), (config.disp_height / 2.2))
        gameDisplay.blit(text_surf, text_rect)

        # button functionality
        button("PLAY", 550, 350, 100, 50, config.white, config.dark_red, game_loop)
        button("QUIT", 550, 425, 100, 50, config.white, config.dark_red, quit_game)

        ace_show((config.disp_width / 2.9), 40)
        pygame.display.update()
        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


def game_loop():
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
        gameDisplay.fill(config.board_color)

        # displays elf in loop and displays elf phrase
        elf(x, y)
        if left_key == 1:
            say = "Hi im an elf"
            elf_phrase(say)

        # allows to specific paramameter to update or the entire window if blank
        # pygame.display.flip() always just updates the entire surface
        pygame.display.update()
        clock.tick(30)


game_menu()
game_loop()
pygame.quit()
quit()
