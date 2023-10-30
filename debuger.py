import pygame as pg
# NOOO I MADE A TYPO IN THE FILE NAME BRUUUUUH
# what kind of typo madness is this :sob:


class Debugger:
    def __init__(self):
        self.font = pg.font.SysFont(None, 40)
        self.text = dict()

    def add(self, description):
        self.text.update({description: 0})

    def update(self, text, description):
        self.text[description] = text

    def draw(self, surf):
        for i, description in enumerate(self.text):
            rendered_text = self.font.render(f"{description}: {self.text[description]}", True, (20, 120, 12))

            surf.blit(rendered_text, (10, 10+i*50))
