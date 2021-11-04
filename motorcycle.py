import pygame
import enum
import os
from colors import Color
from vehicle import Vehicle


class Motorcycle(Vehicle):


    class Color(enum.Enum):
        BLACK = "black"
        BLUE = "blue"
        GREEN = "green"
        YELLOW = "yellow"
        RED = "red"

        def __str__(self):
            return self.value

    def __init__(self, color = Color.RED,orientation = Vehicle.Orientation.UP):
        self.color = color

        super().__init__(orientation)

    def getImagePath(self):
        path = "motorcycle_"
        path += str(self.color)
        path = os.path.join("assets/Motorcycles", path)
        path += ".png"
        return path