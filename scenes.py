import settings as stt
import pygame as pg
import os
from obstacles import ObstacleList


class Scene:
    def __init__(self, name, type):
        """
        :param name:  name of the scene object
        :param type:  what type od scene it is. There are 3: GUI scene, animation scene, and gameplay scene
        """
        self.name = name
        self.type = type


class AnimationScene(Scene):
    def __init__(self, name, framerate, animation_folder_path):
        super().__init__(name, "animation")

        self.framerate = framerate  # how many frames per second there are
        self.current_frame = 0
        self.time_since_last_frame = 0

        self.frames = self.get_frames(animation_folder_path)

        self.over = False

    def update(self, *args):
        dt = args[0]

        self.time_since_last_frame += dt

        if self.time_since_last_frame >= 1/self.framerate and not self.over:
            self.time_since_last_frame = 0
            self.current_frame += 1

            if self.current_frame >= len(self.frames):
                self.over = True
                self.current_frame -= 1

    def draw(self, *args):
        surf = args[0]

        frame = self.frames[self.current_frame]
        scaled_frame = pg.transform.scale_by(frame, stt.D_H/frame.get_height())
        surf.blit(scaled_frame,
                  ((stt.D_W-scaled_frame.get_width())//2, 0))

    def get_frames(self, path):
        frames = [f for f in os.listdir(path)]
        frames.sort(key=lambda x: int(x[3:-4]))
        frames = [pg.image.load(f"{path}/{f}").convert_alpha() for f in frames]

        return frames


class GameplayState(Scene):
    def __init__(self, name):
        super().__init__(name, "gameplay")

    def draw(self, *args):
        pass

    def update(self, *args):
        pass

    def handle_events(self, events):
        pass


class NormalState(GameplayState):
    def __init__(self):
        super().__init__("normal")

        self.objects = ObstacleList()

    def draw(self, *args):
        surf = args[0]

        walls = [pg.Rect(0, 0, stt.D_H//4, stt.D_H),
                 pg.Rect(3*stt.D_H//4, 0, stt.D_H//4, stt.D_H)]

        track = pg.Rect((stt.D_H//4, 0, stt.D_H//2, stt.D_H))

        frame = pg.Surface((stt.D_H, stt.D_H))


        pg.draw.rect(frame, (120, 120, 120), track)

        pg.draw.rect(frame, (170, 170, 170), walls[0])
        pg.draw.rect(frame, (170, 170, 170), walls[1])

        # draw row outlines on the track
        for i in range(2):
            pg.draw.rect(frame, (100, 100, 100), (track.x+track.width//3 * (i+1), 0, 4, stt.D_H))

        surf.blit(frame, ((stt.D_W - stt.D_H)//2, 0))

    def update(self, *args):
        dt = args[0]
