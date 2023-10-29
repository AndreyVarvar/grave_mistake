import settings as stt
import random as rng
import pygame as pg
import game_math as gm


class Obstacle:
    def __init__(self, sprite, type):
        self.image = sprite
        self.type = type


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
        self.obstacles = []

        self.possible_obstacles = [
            Obstacle(pg.image.load("images/obstacles/wall.png").convert_alpha(), "1x1"),
            Obstacle(pg.image.load("images/obstacles/lamp.png").convert_alpha(), "1x2"),
            Obstacle(pg.image.load("images/obstacles/pumpkin.png.png").convert_alpha(), "1x1"),
            Obstacle(pg.image.load("images/obstacles/chair.png").convert_alpha(), "1x1"),
            Obstacle(pg.image.load("images/obstacles/couch.png").convert_alpha(), "2x1"),
            Obstacle(pg.image.load("images/obstacles/banana_peel.png").convert_alpha(), "1x1"),
            Obstacle(pg.image.load("images/obstacles/puddle.png").convert_alpha(), "1x1"),
            Obstacle(pg.image.load("images/obstacles/conus.png").convert_alpha(), "1x1"),
            Obstacle(pg.image.load("images/obstacles/clock.png").convert_alpha(), "1x1"),
            Obstacle(pg.image.load("images/obstacles/GREEN_CUBE.png").convert_alpha(), "1x1")]

    def add(self, obstacle):
        self.obstacles.append(obstacle)

    def kill(self, obstacle):
        self.obstacles.remove(obstacle)

    def check_collision(self, rect):
        for obstacle in self.obstacles:
            if obstacle.check_collision(rect) is True:  # collision detected
                return True

        return False  # No obstacles in the list collided with the given rect

    def update(self, player_pos, snake_pos):
        while self.obstacles[0].rect.top <= snake_pos.y:
            self.kill(self.obstacles[-1])
            self.add_random_obstacle(player_pos)


    def add_random_obstacle(self, player_pos):
        new_obstacle = rng.choice(self.possible_obstacles)

        if new_obstacle.type == "2x1":
            column = rng.randint(0, 1)
        else:
            column = rng.randint(0, 2)

        new_obstacle_entity = ObstacleEntity((stt.column_width * int(new_obstacle.type[0]),
                                              stt.column_width * int(new_obstacle.type[2])),
                                             gm.calculate_pos(column, player_pos),
                                             new_obstacle)

        self.obstacles.append(new_obstacle_entity)
