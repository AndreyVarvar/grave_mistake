import settings as stt
import pygame as pg
from math import sin


class Snake:
    def __init__(self, room):
        self.image = pg.transform.scale_by(pg.image.load("images/snake.png").convert_alpha(), 6)
        size = self.image.get_size()

        self.pos = pg.Vector2(room.boundaries.centerx - size[0]//2, room.boundaries.bottom + 200)

        self.speed = 60

    def update(self, dt):
        self.pos.y -= self.speed*dt

    def draw(self, surf):
        surf.blit(self.image, (self.pos.x+40*sin(stt.sin_clock/20), self.pos.y))
