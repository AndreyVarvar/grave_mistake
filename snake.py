import settings as stt
import pygame as pg
from math import sin


class Snake:
    def __init__(self, player_pos):
        self.image = pg.transform.scale_by(pg.image.load("images/snake.png").convert_alpha(), 6)

        self.pos = pg.Vector2((stt.D_H-self.image.get_width())//2, player_pos[1]+200)

        self.speed = 30

    def update(self, dt):
        self.pos.y -= self.speed*dt

    def draw(self, surf):
        surf.blit(self.image, (self.pos.x+40*sin(stt.sin_clock/20), self.pos.y))
