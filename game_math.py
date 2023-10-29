import settings as stt
import pygame as pg


def calculate_pos(column, player_pos):
    return pg.Vector2(column*stt.column_width + stt.D_H//4, player_pos.y - 600)
