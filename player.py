import settings as stt
import pygame as pg


class Player:
    def __init__(self):
        self.column = 0

        self.normal, self.night_vision = self.process_spritesheets()
        self.state = "normal"
        self.current_spritesheet = self.normal

        self.current_image = self.current_spritesheet[0]

        self.rect = pg.FRect((stt.D_H//2, stt.D_H//2),
                             self.current_image.get_size())

        self.movement = {"up": False, "down": False, "left": False, "right": False}

        self.speed = 50

    def update(self, dt):
        if self.movement["up"]:
            self.rect.y -= self.speed*dt
            print("up")

        if self.movement["down"]:
            self.rect.y += self.speed*dt

        if self.movement["left"]:
            self.rect.x -= self.speed*dt

        if self.movement["right"]:
            self.rect.x += self.speed*dt

        stt.debugger.update(str(self.movement), "movement")


    def draw(self, camera):
        image_rect = self.current_image.get_rect(center=self.rect.center)

        camera.blit(self.current_image, image_rect)

    def handle_events(self, events, keys_pressed):
        self.current_image = self.get_image(keys_pressed)

        self.movement["up"] = keys_pressed[pg.K_UP] or keys_pressed[pg.K_w]
        self.movement["down"] = keys_pressed[pg.K_DOWN] or keys_pressed[pg.K_s]
        self.movement["left"] = keys_pressed[pg.K_LEFT] or keys_pressed[pg.K_a]
        self.movement["right"] = keys_pressed[pg.K_RIGHT] or keys_pressed[pg.K_d]

    def get_image(self, keys_pressed):
        image = None

        if keys_pressed[pg.K_a] or keys_pressed[pg.K_LEFT]:
            image = self.current_spritesheet[3]

        elif keys_pressed[pg.K_d] or keys_pressed[pg.K_RIGHT]:
            image = self.current_spritesheet[1]

        if keys_pressed[pg.K_w] or keys_pressed[pg.K_UP]:
            image = self.current_spritesheet[0]

        elif keys_pressed[pg.K_s] or keys_pressed[pg.K_DOWN]:
            image = self.current_spritesheet[2]

        return image or self.current_image


    def process_spritesheets(self):
        night_vision_spritesheet = pg.image.load("images/night_vision.png")
        night_vision = [pg.transform.scale_by(night_vision_spritesheet.subsurface((i*16, 0, 16, 16)), 6).convert_alpha() for i in range(4)]

        programier_spritesheet = pg.image.load("images/programier.png")
        programier = [pg.transform.scale_by(programier_spritesheet.subsurface((i * 16, 0, 16, 16)), 6).convert_alpha() for i in range(4)]

        return programier, night_vision
