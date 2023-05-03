import pygame

from gui.dialog import Dialog


def play(screen):
    bg = pygame.image.load('act1/images/bedroom.png')

    dialog = Dialog(screen,
                    'Hello, welcome to the game. This is a point and click game about trauma. Click on the objects to '
                    'interact with them.')

    while True:
        screen.blit(bg, (0, 0))
        dialog.render(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dialog.next()
