import pygame
from pygame import WINDOWRESIZED
import pieces
from view import View
from controller import Controller

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("DHAMET_essai_3")

# screen resolution
res = (800, 700)

# opens up a window
screen = pygame.display.set_mode(res)

bo = pygame.image.load("imgs/screen.png")
# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 75)
buttonFont = pygame.font.SysFont('Arial', 40)

# rendering a text written in
# this font
Welcome = smallfont.render('Soyez le bienvenue', True, color)
Jouer = buttonFont.render('JOUER', True, color)


def play():
    V = View()
    C = Controller()
    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == WINDOWRESIZED:
                V.size = (V.board.get_width(), V.board.get_height())
            if event.type == pygame.MOUSEBUTTONDOWN:
                C.action()
        if pieces.whiteCount == 40 or pieces.blackCount == 40:
            print("Le match est terminé")
            break

        V.redrawGame()


while True:
    screen.blit(bo, (0, 0))
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            quit()
        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated
            if 233 <= mouse[0] <= 467 and height / 2 <= mouse[1] <= height / 2 + 60:
                play()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if 233 <= mouse[0] <= 566 and height / 2 <= mouse[1] <= height / 2 + 60:
        pygame.draw.rect(screen, color_light, [233, height / 2, 333, 60])

    else:
        pygame.draw.rect(screen, color_dark, [233, height / 2, 333, 60])
    # superimposing the text onto our button
    screen.blit(Jouer, (340, height / 2 + 7))
    # updates the frames of the game
    pygame.display.update()