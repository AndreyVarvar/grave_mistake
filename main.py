import settings as stt
import pygame as pg
from scenes import AnimationScene, NormalState
from effect import BlinkingText
from player import Player


class Game:
    def __init__(self):
        # essentials
        self.display_size = stt.D_W, stt.D_H
        self.display = stt.DISPLAY

        self.clock = pg.time.Clock()

        self.running = True

        # player
        self.player = Player()

        # scenes
        self.animations = [AnimationScene("intro1", 4, "assets/animations/lol"),
                           AnimationScene("intro2", 2, "assets/animations/lol2")]

        self.main_gameplay_state = NormalState()

        # special effects
        self.hint_1 = BlinkingText(pg.image.load("images/hint1.png"), 2, (600, 40), 3)

        # other stuff
        self.state = 0  # play first animation
        self.change_state = False
        self.current_scene = self.animations[0]

    def run(self):
        while self.running:
            events = pg.event.get()
            dt = self.clock.tick(stt.FPS)/1000

            self.update(dt)
            self.draw(dt)

            self.handle_events(events)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if self.current_scene.name in ["intro1", "intro2"]:
                        self.change_state = True

        keys_pressed = pg.key.get_pressed()

        self.player.handle_events(events, keys_pressed)

    def update(self, dt):
        self.current_scene.update(dt)
        self.player.update()

        if self.current_scene.type == "animation":
            if self.current_scene.over:
                self.change_state = True


        if self.change_state:
            self.change_state = False

            if self.current_scene.name == "intro1":
                self.state = 1
                self.current_scene = self.animations[1]

            elif self.current_scene.name == "intro2":
                self.state = 2
                self.current_scene = self.main_gameplay_state

    def draw(self, dt):
        self.display.fill("black")

        self.current_scene.draw(self.display)

        if self.current_scene.name in ["intro1", "intro2"]:
            self.hint_1.update(dt)
            self.hint_1.draw(self.display)

        elif self.current_scene.name in ["normal"]:
            self.player.draw(self.display)

        pg.display.update()


MA_GAME_WILL_WIN = Game()
MA_GAME_WILL_WIN.run()
