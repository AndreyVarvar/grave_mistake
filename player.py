import settings as stt
import pygame as pg


class Player:
    def __init__(self):
        self.column = 0

        self.normal, self.night_vision = self.process_spritesheets()
        self.state = "normal"
        self.current_spritesheet = self.normal

        self.current_image = self.current_spritesheet[0]

    def update(self):
        pass

    def draw(self, surf):
        image = pg.transform.scale_by(self.current_image, 6)
        image_rect = image.get_rect()
        image_rect.center = (stt.D_W//2, stt.D_H//2)

        surf.blit(image, image_rect)

    def handle_events(self, events, keys_pressed):
        self.current_image = self.get_image(keys_pressed)

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
        night_vision = [night_vision_spritesheet.subsurface((i*16, 0, 16, 16)).convert_alpha() for i in range(4)]

        programier_spritesheet = pg.image.load("images/programier.png")
        programier = [programier_spritesheet.subsurface((i * 16, 0, 16, 16)).convert_alpha() for i in range(4)]

        return programier, night_vision
