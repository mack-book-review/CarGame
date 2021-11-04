from car import Car
from vehicle import Vehicle
from constants import *
import random
import pygame

class EnemyCar(Car):

    def __init__(self):
        randColorIndex = random.randint(1,4)
        randColor = Car.CarColor(randColorIndex)

        randTypeIndex = random.randint(1, 4)
        randType = Car.CarType(randTypeIndex)

        super().__init__(randColor,randType,Car.CarSize.SMALL,Vehicle.Orientation.DOWN)
        self.old_pos = (self.rect.x, self.rect.y)
        self.new_pos = self.old_pos

        self.setInitialPosition()
        self.setRandomTargetPosition()

        self.width = self.rect.width
        self.height = self.rect.height

        self.prev_ticks = 0
        self.current_ticks = 0
        self.elapsed_ticks = 0

        self.isMoving = True
        self.moveTimer = 0
        self.moveInterval = random.randint(2000,4000)



    def lerp(self, old_pos, new_pos, percent):
        print("Calling lerp function...")
        if old_pos and new_pos:
            dist_y = (new_pos[1] - old_pos[1]) * percent
            self.setPosition(old_pos[0], old_pos[1] + dist_y)


    def update(self):
        print(self.rect)
        print(self.new_pos)

        if self.rect.top >= SCREEN_HEIGHT:
            self.resetPosition()

            self.setRandomTargetPosition()

        self.current_ticks = pygame.time.get_ticks()
        self.elapsed_ticks = self.current_ticks - self.prev_ticks


        self.moveTimer += self.elapsed_ticks
        percent = self.moveTimer / self.moveInterval
        self.lerp(self.old_pos, self.new_pos, percent)

        if self.moveTimer >= self.moveInterval:
            self.moveTimer = 0



        self.prev_ticks = self.current_ticks

    def setRandomTargetPosition(self):
        self.new_pos = (self.rect.x,SCREEN_HEIGHT+50)

    def setInitialPosition(self):
        self.resetPosition()

    def resetPosition(self):
        randX = random.randrange(self.rect.width//2 + LAWN_MARGIN_WIDTH, SCREEN_WIDTH - LAWN_MARGIN_WIDTH - self.rect.width//2)
        randY = random.randrange(-100,-50)
        self.setPosition(randX, randY)
        self.old_pos = (self.rect.x, self.rect.y)
        self.new_pos = self.old_pos