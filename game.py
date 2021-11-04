import pygame,sys,random
from colors import Color
from constants import *
from background import Background
from car import Car
from motorcycle import Motorcycle
from vehicle import Vehicle
from player import Player
from enemycar import EnemyCar

class Game():


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.area = self.screen.get_rect()
        self.background = Background(self.screen)

        self.clock = pygame.time.Clock()
        self.gameWon = False
        self.gameLost = False

        self.player = Player()
        self.player.setPosition(self.area.midbottom)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.createEnemyCars(3)


    def createEnemyCars(self,number_cars,added_cars = []):

        possible_pos = []
        i = LAWN_MARGIN_WIDTH
        while i < LAWN_MARGIN_WIDTH + TOTAL_ROAD_WIDTH:
            possible_pos.append(i)
            i += LANE_WIDTH

        upper_bound = len(possible_pos)
        for _ in range(number_cars):
            e = EnemyCar()
            randIndex = random.randint(0,upper_bound)
            self.enemy_sprites = pygame.sprite.Group()
            self.enemy_sprites.add(e)
            self.all_sprites.add(e)

            e.setPosition(possible_pos[randIndex],e.rect.top)
            possible_pos.pop(randIndex)
            upper_bound = len(possible_pos)






    def handleInput(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.moveRight()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def run(self):
        while not self.gameLost and not self.gameWon:
            self.handleInput(pygame.event.get())

            self.background.draw()

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)


            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
