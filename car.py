import pygame
import enum
import os
from colors import Color
from vehicle import Vehicle

class Car(Vehicle):

    class CarSize(enum.Enum):
        SMALL = "small"
        REGULAR = ""

        def __str__(self):
            return self.value

    class CarType(enum.Enum):
        TYPE1 = 1
        TYPE2 = 2
        TYPE3 = 3
        TYPE4 = 4

        def __str__(self):
            return str(self.value)

    class CarColor(enum.Enum):
        black = 1
        blue = 2
        green = 3
        yellow = 4

        def __str__(self):
            return self.name

    def __init__(self,color = CarColor.blue,car_type = CarType.TYPE1,car_picture_size = CarSize.SMALL,orientation = Vehicle.Orientation.UP):
        self.color = color
        self.type = car_type
        self.picSize = car_picture_size

        super().__init__(orientation)


    def getImagePath(self):
        path = "car_"
        path += str(self.color) + "_"
        if self.picSize == Car.CarSize.SMALL:
            path += str(self.picSize) + "_"
        path += str(self.type)
        path += ".png"
        path = os.path.join("assets/cars",path)
        return path