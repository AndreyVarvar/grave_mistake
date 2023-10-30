import settings as stt
import pygame as pg
from math import sin


class BlinkingText:
    def __init__(self, image, scale, pos, blink_speed):
        self.image = pg.transform.scale_by(image, scale).convert_alpha()
        self.pos = pos
        self.bl_speed = blink_speed/100

    def draw(self, surf):
        surf.blit(self.image, self.pos)

    def update(self, dt):
        self.image.set_alpha(int(100*abs(sin(stt.sin_clock*self.bl_speed))))

