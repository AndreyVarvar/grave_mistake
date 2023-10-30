import settings as stt
import pygame as pg
from obstacles import possible_obstacles, ObstacleList, ObstacleEntity


class Room:
    def __init__(self, room_n):
        self.type, self.hitboxes, self.boundaries, self.map = self.load_room(room_n)

    def load_room(self, n):
        with open(f"levels/room{n}.txt", "r") as file:
            content = file.readlines()

        # remove every \n in the content var
        content = ("".join(content)).split("\n")

        # type of the level
        type = content[0]

        # calculate boundaries
        boundaries = {"x": [0, 0],
                      "y": [0, 0]}



        # start loading the obstacles in the level
        level = content[1:]
        # split the commas in the 'level' var, we don't need em
        level = [el.split(",") for el in level]

        room_size = (len(level[0])*stt.cell_size + 2*stt.wall_size,
                     len(level)*stt.cell_size + 2*stt.wall_size)

        room_map = pg.Surface(room_size, pg.SRCALPHA)

        # draw da walls yezzz
        # im going insaaaaaaaaneeeeeeee
        self.draw_walls(room_map, room_size)

        # load obstacles
        obstacle_list = ObstacleList()

        for row_counter, row in enumerate(level):
            for column_counter, cell in enumerate(row):
                if cell != "0":
                    obstacle = possible_obstacles[int(cell)]
                    obstacle_size = (int(obstacle.type[0])*stt.cell_size, int(obstacle.type[1])*stt.cell_size)
                    obstacle_pos = (stt.wall_size + column_counter*stt.cell_size,
                                    stt.wall_size + row_counter*stt.cell_size)

                    obstacle_entity = ObstacleEntity(obstacle_size, obstacle_pos, obstacle)
                    obstacle_list.add(obstacle_entity)

        # blit obstacle images on the room_map map
        for obstacle in obstacle_list.obstacles:
            obstacle_image = pg.transform.scale(obstacle.image, obstacle.size)
            obst_pos = obstacle.rect.topleft

            room_map.blit(obstacle_image, obst_pos)

        _ = 0
        return type, _, _, room_map

    def draw_walls(self, room_map, room_size):
        room_map.fill((120, 120, 120))
        pg.draw.rect(room_map, (170, 170, 170),
                     (stt.wall_size, stt.wall_size, room_size[0]-2*stt.wall_size, room_size[1]-2*stt.wall_size))
