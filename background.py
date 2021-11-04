import pygame
from colors import Color
from constants import *

class Background():

    def __init__(self,screen):
        self.screen = screen
        self.area = self.screen.get_rect()
        self.roadRect = self.getRoadRect()

    def getRoadRect(self):
        return pygame.rect.Rect(LAWN_MARGIN_WIDTH, 0, TOTAL_ROAD_WIDTH, SCREEN_HEIGHT)

    def draw(self):
        pygame.draw.rect(self.screen, Color.LAWN_GREEN, self.area)
        pygame.draw.rect(self.screen, Color.ROAD_GREY2, self.roadRect)

        midtop = self.area.midtop
        midtop_x, midtop_y = self.area.midtop
        line_height = 30
        line_space = 20
        total_lines = SCREEN_HEIGHT // (line_height + line_space)

        start_y = 0
        end_y = line_height
        prev_end_y = end_y

        for i in range(total_lines):
            if i > 0:
                start_y = prev_end_y + line_space
                end_y = start_y + line_height
                prev_end_y = end_y

            pygame.draw.line(self.screen, Color.ROAD_YELLOW, (midtop_x, start_y), (midtop_x, end_y), 10)

