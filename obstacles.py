import settings as stt
import random as rng
import pygame as pg
import game_math as gm


class Obstacle:
    def __init__(self, sprite, type):
        self.image = sprite
        self.type = type

        self.form = int(self.type[0]), int(self.type[2])


class ObstacleEntity(Obstacle):
    def __init__(self, size, pos, obstacle):
        super().__init__(obstacle.image, obstacle.type)

        self.rect = pg.FRect(pos, size)

    def check_collision(self, rect):
        return self.rect.colliderect(rect)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


class ObstacleList:
    def __init__(self):
        self.obstacles: list[ObstacleEntity]
        self.obstacles = []

    def add(self, obstacle: ObstacleEntity):
        self.obstacles.append(obstacle)

    def kill(self, obstacle: ObstacleEntity):
        self.obstacles.remove(obstacle)

    def check_collision(self, rect):
        for obstacle in self.obstacles:
            if obstacle.check_collision(rect) is True:  # collision detected
                return True

        return False  # No obstacles in the list collided with the given rect

    def update(self, player_pos, snake_pos):
        pass


possible_obstacles = [
    Obstacle(pg.image.load("images/obstacles/banana_peel.png").convert_alpha(), "1x1"),
    Obstacle(pg.image.load("images/obstacles/chair.png").convert_alpha(), "1x1"),
    Obstacle(pg.image.load("images/obstacles/clock.png").convert_alpha(), "1x2"),
    Obstacle(pg.image.load("images/obstacles/conus.png").convert_alpha(), "1x1"),
    Obstacle(pg.image.load("images/obstacles/couch.png").convert_alpha(), "2x1"),
    Obstacle(pg.image.load("images/obstacles/GREEN_CUBE.png").convert_alpha(), "1x1"),
    Obstacle(pg.image.load("images/obstacles/lamp.png").convert_alpha(), "1x2"),
    Obstacle(pg.image.load("images/obstacles/puddle.png").convert_alpha(), "1x1"),
    Obstacle(pg.image.load("images/obstacles/pumpkin.png").convert_alpha(), "1x1"),
    Obstacle(pg.image.load("images/obstacles/wall.png").convert_alpha(), "1x1")
]
