import settings as stt
import pygame as pg


class Camera:
    def __init__(self):
        self.frame = pg.Surface((stt.D_H, stt.D_H), pg.SRCALPHA)

        self.rect = pg.FRect((stt.D_H//2, 0), (stt.D_H, stt.D_H))

    def draw(self, surf):
        surf.blit(self.frame, ((stt.D_W-self.frame.get_width())//2, 0))

    def clear(self):
        self.frame.fill("black")

    def follow(self, pos, bounds):
        self.rect.x += pos[0] - self.rect.x
        self.rect.y += pos[1] - self.rect.y

        # check if camera can actually follow player so that it does not reveal blank space
        cam_pos_boundaries_collision = {"up": False, "down": False, "left": False, "right": False}

        if bounds["x"][0] > self.rect.left:
            self.rect.left = bounds["x"][0]
            cam_pos_boundaries_collision["left"] = True

        if bounds["x"][1] < self.rect.right:
            self.rect.right = bounds["x"][1]
            cam_pos_boundaries_collision["right"] = True

        if bounds["y"][0] > self.rect.top:
            self.rect.top = bounds["y"][0]
            cam_pos_boundaries_collision["bottom"] = True

        if bounds["y"][1] < self.rect.bottom:
            self.rect.top = bounds["y"][0]
            cam_pos_boundaries_collision["top"] = True

        stt.debugger.update(str(cam_pos_boundaries_collision), "bounds cam")
        stt.debugger.update(str(bounds), "bounds")

        # print(self.rect.center, pos, self.rect.centerx-pos[0], self.rect.centery-pos[1])

    def blit(self, surf, dest):
        pos_in_frame = (dest[0] - self.rect.x + self.rect.width//2, dest[1] - self.rect.y)

        self.frame.blit(surf, pos_in_frame)
