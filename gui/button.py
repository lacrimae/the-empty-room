import pygame


class Button:
    BG_COLOR = (134, 112, 112)
    FONT_COLOR = (255, 234, 210)
    BORDER_COLOR = (255, 234, 210)

    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 90
    PADDING = 1
    BORDER_WIDTH = 2

    def __init__(self, text, pos):
        self.text = text
        self.x, self.y = pos
        self.font = pygame.font.SysFont('Arial', 48)
        self.surface = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.surface.fill(self.BG_COLOR)
        self.label = self.font.render(text, True, self.FONT_COLOR)
        self.label_x = (self.surface.get_width() - self.label.get_width()) // 2
        self.label_y = (self.surface.get_height() - self.label.get_height()) // 2
        self.surface.blit(self.label, (self.label_x, self.label_y))

    def render(self, screen):
        self.surface.fill(self.BG_COLOR)
        self.surface.blit(self.label, (self.label_x, self.label_y))
        pygame.draw.rect(self.surface, self.BORDER_COLOR, (0, 0, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                         self.BORDER_WIDTH)
        screen.blit(self.surface, (self.x, self.y))

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.surface.get_width() and \
            self.y <= pos[1] <= self.y + self.surface.get_height()
