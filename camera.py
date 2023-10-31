import settings as stt
import pygame as pg


class Camera:
    def __init__(self):
        self.frame = pg.Surface((stt.D_H, stt.D_H), pg.SRCALPHA)

        self.rect = pg.FRect((0, 0), (stt.D_H, stt.D_H))

    def draw(self, surf):
        surf.blit(self.frame, ((stt.D_W-self.frame.get_width())//2, 0))

    def clear(self):
        self.frame.fill("black")

    def follow(self, pos, bounds: pg.Rect):
        self.rect.x += pos[0] - self.rect.centerx
        self.rect.y += pos[1] - self.rect.centery

        if self.rect.top < bounds.top:
            self.rect.top = bounds.top
        elif self.rect.bottom > bounds.bottom:
            self.rect.bottom = bounds.bottom

        if self.rect.left < bounds.left:
            self.rect.left = bounds.left
        elif self.rect.right > bounds.right:
            self.rect.right = bounds.right

        stt.debugger.update(str(bounds), "bounds")

        # print(self.rect.center, pos, self.rect.centerx-pos[0], self.rect.centery-pos[1])

    def blit(self, surf, dest):
        pos_in_frame = (dest[0] - self.rect.centerx + self.rect.width//2, dest[1] - self.rect.centery + self.rect.height//2)

        self.frame.blit(surf, pos_in_frame)
