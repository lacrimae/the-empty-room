import os

import pygame as pygame

import constants
from act1 import bedroom
from gui.button import Button

# Initialize Pygame
pygame.init()

# Set up the window and load the background image
size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Empty Room")
# Get the path to the image file
image_path = os.path.join("images", "background.png")
# Load the image
background_image = pygame.image.load(image_path)

# Set up graphics
font = pygame.font.SysFont('Arial', 48)

# Set up buttons
button_x = (constants.SCREEN_WIDTH - Button.BUTTON_WIDTH) // 2
button_y = constants.SCREEN_HEIGHT - Button.BUTTON_HEIGHT - constants.SCREEN_HEIGHT // 2
play_button = Button('Play', (button_x, button_y - Button.BUTTON_HEIGHT))
quit_button = Button('Quit', (button_x, button_y + constants.PADDING))


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_button.is_clicked(event.pos):
                bedroom.play(screen)
            elif quit_button.is_clicked(event.pos):
                pygame.quit()


# Main loop
while True:
    handle_events()
    # Clear the screen
    screen.blit(background_image, (0, 0))
    # Draw graphics
    play_button.render(screen)
    quit_button.render(screen)
    # Update the display
    pygame.display.flip()
