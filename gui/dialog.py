import time

import pygame


class Dialog:
    WIDTH = 800
    HEIGHT = 200

    BG_COLOR = (74, 63, 63)
    FONT_COLOR = (255, 234, 210)

    def __init__(self, screen, text):
        self.screen = screen
        self.text = text
        self.x = (self.screen.get_width() - self.WIDTH) // 2
        self.y = self.screen.get_height() - self.HEIGHT - 20
        self.font = pygame.font.SysFont('font.otf', 24)
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.surface.fill(self.BG_COLOR)
        self.font_color = self.FONT_COLOR
        self.padding = 10
        self.line_spacing = 5
        self.delay = 0.1

    def render(self, screen):
        self.surface.fill(self.BG_COLOR)
        x, y = self.padding, self.padding
        for line in self.text.split('\n'):
            words = line.split()
            space_width, _ = self.font.size(' ')
            symbols = [char for word in words for char in list(word + " ")]

            for letter in symbols:
                letter_surface = self.font.render(letter, True, self.font_color)
                letter_rect = letter_surface.get_rect()
                letter_rect.topleft = (x, y)
                self.surface.blit(letter_surface, letter_rect)
                x += letter_rect.width + space_width

                # Renders each letter separately to obtain delay typing effect
                screen.blit(self.surface, (self.x, self.y))
                pygame.display.flip()  # update the screen
                time.sleep(self.delay)  # wait for a short time

                # If the letter is a newline character, move to the next line
                if letter == "\n":
                    x, y = self.padding, y + letter_rect.height + self.line_spacing
                # If the letter reaches the right edge of the surface, move to the next line
                elif x + letter_rect.width > self.surface.get_width() - self.padding:
                    x, y = self.padding, y + letter_rect.height + self.line_spacing

        screen.blit(self.surface, (self.x, self.y))
