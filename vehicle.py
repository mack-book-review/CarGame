import pygame
from colors import Color
import enum

class Vehicle(pygame.sprite.Sprite):

    class Orientation(enum.Enum):
        UP = 1
        DOWN = 2

    def __init__(self,orientation = Orientation.UP):

        super().__init__()
        self.image = pygame.image.load(self.getImagePath()).convert()
        self.image.set_colorkey(Color.BLACK)
        self.rect = self.image.get_rect()
        self.orientation = orientation

        if self.orientation == Vehicle.Orientation.DOWN:
            self.image = pygame.transform.flip(self.image,False,True)


    def setSize(self, *args):
        if len(args) == 1:
            self.rect.size = args[0]

        if len(args) == 2:
            self.rect.size = args[0], args[1]

    def setPosition(self, *args):
        if len(args) == 1:
            if self.orientation == Vehicle.Orientation.UP:
                self.rect.midbottom = args[0]
            elif self.orientation == Vehicle.Orientation.DOWN:
                self.rect.midtop = args[0]

        if len(args) == 2:
            if self.orientation == Vehicle.Orientation.UP:
                self.rect.midtop = args[0], args[1]
            elif self.orientation == Vehicle.Orientation.DOWN:
                self.rect.midtop = args[0], args[1]


    def getImagePath(self):
        return ""
