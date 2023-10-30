import pygame as pg
from debuger import Debugger

pg.init()

D_W, D_H = 1200, 800
DISPLAY = pg.display.set_mode((D_W, D_H))
pg.display.set_caption("grave mistake...")

FPS = 60

cell_size = D_H//6
wall_size = D_H//4

sin_clock = 0

debugger = Debugger()
