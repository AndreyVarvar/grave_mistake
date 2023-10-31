import settings as stt
import pygame as pg
from math import sin


class Player:
    def __init__(self, pos):
        self.column = 0

        self.normal, self.night_vision = self.process_spritesheets()
        self.state = "normal"
        self.current_spritesheet = self.normal

        self.current_image = self.current_spritesheet[0]

        self.rect = pg.FRect(pos, self.current_image.get_size())

        self.movement = {"up": False, "down": False, "left": False, "right": False}
        self.moveingg = False  # moving or not lol

        self.speed = 100

    def update(self, dt, hitboxes):
        self.moveingg = any(self.movement.values())
        dy = 0
        dx = 0

        if self.movement["up"]:
            dy = -self.speed*dt

        if self.movement["down"]:
            dy = self.speed*dt

        if self.movement["left"]:
            dx = -self.speed*dt

        if self.movement["right"]:
            dx = self.speed*dt

        self.resolve_collision(hitboxes, dx, dy)

        stt.debugger.update(str(self.movement), "movement")


    def draw(self, camera):
        image_rect = self.current_image.get_rect(center=self.rect.center)

        if self.moveingg:
            image_rect.y -= 5*sin(abs(stt.sin_clock/3))

        camera.blit(self.current_image, image_rect)

    def handle_events(self, events, keys_pressed):
        self.current_image = self.get_image(keys_pressed)

        self.movement["up"] = keys_pressed[pg.K_UP] or keys_pressed[pg.K_w]
        self.movement["down"] = keys_pressed[pg.K_DOWN] or keys_pressed[pg.K_s]
        self.movement["left"] = keys_pressed[pg.K_LEFT] or keys_pressed[pg.K_a]
        self.movement["right"] = keys_pressed[pg.K_RIGHT] or keys_pressed[pg.K_d]

    def get_image(self, keys_pressed):
        image = None

        if keys_pressed[pg.K_w] or keys_pressed[pg.K_UP]:
            image = self.current_spritesheet[0]

        elif keys_pressed[pg.K_s] or keys_pressed[pg.K_DOWN]:
            image = self.current_spritesheet[2]

        if keys_pressed[pg.K_a] or keys_pressed[pg.K_LEFT]:
            image = self.current_spritesheet[3]

        elif keys_pressed[pg.K_d] or keys_pressed[pg.K_RIGHT]:
            image = self.current_spritesheet[1]

        return image or self.current_image


    def process_spritesheets(self):
        night_vision_spritesheet = pg.image.load("images/night_vision.png")
        night_vision = [pg.transform.scale_by(night_vision_spritesheet.subsurface((i*16, 0, 16, 16)), 6).convert_alpha() for i in range(4)]

        programier_spritesheet = pg.image.load("images/programier.png")
        programier = [pg.transform.scale_by(programier_spritesheet.subsurface((i * 16, 0, 16, 16)), 6).convert_alpha() for i in range(4)]

        return programier, night_vision

    def resolve_collision(self, hitboxes, dx, dy):
        if dx != 0:
            self.rect.x += dx
            collided, rect = self.check_collision(hitboxes)

            if collided:
                if dx > 0:
                    self.rect.right = rect.left
                else:
                    self.rect.left = rect.right

        if dy != 0:
            self.rect.y += dy
            collided, rect = self.check_collision(hitboxes)

            if collided:
                if dy > 0:
                    self.rect.bottom = rect.top
                else:
                    self.rect.top = rect.bottom

    def check_collision(self, hitboxes):
        for hitbox in hitboxes:
            if hitbox.colliderect(self.rect):
                return True, hitbox

        return False, None
