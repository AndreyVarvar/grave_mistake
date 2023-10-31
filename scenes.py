import settings as stt
import pygame as pg
import os
from room import Room
from math import asin, pi

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
        camera = args[0]

        frame = self.frames[self.current_frame]
        scaled_frame = pg.transform.scale_by(frame, stt.D_H/frame.get_height())
        camera.frame.blit(scaled_frame, (0, 0))

    def get_frames(self, path):
        frames = [f for f in os.listdir(path)]
        frames.sort(key=lambda x: int(x[3:-4]))
        frames = [pg.image.load(f"{path}/{f}").convert_alpha() for f in frames]

        return frames


class GameplayState(Scene):
    def __init__(self, name, room_n):
        super().__init__(name, "gameplay")
        self.room = Room(room_n)

    def draw(self, *args):
        pass

    def update(self, *args):
        pass

    def handle_events(self, events):
        pass


class SurvivalState(GameplayState):
    def __init__(self, room_n):
        super().__init__("normal", room_n)
        self.heartbeat = pg.mixer.Sound("assets/SFX/heartbeat.ogg")

    def draw(self, *args):
        camera = args[0]

        camera.blit(self.room.map, (0, 0))

    def update(self, *args):
        dt = args[0]

    def sfx(self, snake, player):
        x = snake.pos.y - player.rect.y

        if x <= 400:
            sound_volume = (4/pi)*asin(1-(x/400))
            self.heartbeat.set_volume(sound_volume)

            if not stt.sfx_channel.get_busy():
                stt.sfx_channel.play(self.heartbeat)

            stt.debugger.update("playing", "heartbeat")
        else:
            stt.sfx_channel.stop()
            stt.debugger.update("not playing", "heartbeat")

