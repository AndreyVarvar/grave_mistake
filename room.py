import settings as stt
import pygame as pg
from obstacles import possible_obstacles, ObstacleList, ObstacleEntity


class Room:
    def __init__(self, room_n):
        self.type, self.hitboxes, self.boundaries, self.map, self.wall_rects = self.load_room(room_n)

        self.player_spawn_pos = (self.boundaries.centerx, self.boundaries.bottom - stt.wall_size - stt.cell_size)

    def load_room(self, n):
        with open(f"levels/room{n}.txt", "r") as file:
            content = file.readlines()

        # remove every \n in the content var
        content = ("".join(content)).split("\n")

        # type of the level
        type = content[0]

        # contents of the level
        level = content[1:]

        # room size duh
        room_size = (len(level[0]) * stt.cell_size + 2 * stt.wall_size,
                     len(level) * stt.cell_size + 2 * stt.wall_size)

        # calculate boundaries
        boundaries = pg.Rect((0, 0), room_size)

        # split the commas in the 'level' var, we don't need em
        level = [el.split(",") for el in level]

        room_map = pg.Surface(room_size, pg.SRCALPHA)

        # draw da walls yezzz
        # im going insaaaaaaaaneeeeeeee
        room_map.fill((120, 120, 120))

        wall_rects = [pg.Rect(0, 0, (room_size[0]-stt.cell_size)//2, stt.wall_size),
                      pg.Rect(0, 0, stt.wall_size, room_size[1]),
                      pg.Rect(0, room_size[1]-stt.wall_size, (room_size[0] - stt.cell_size)//2, stt.wall_size),
                      pg.Rect((room_size[0] + stt.cell_size)//2, room_size[1] - stt.wall_size, (room_size[0] - stt.cell_size)//2, stt.wall_size),
                      pg.Rect(room_size[0]-stt.wall_size, 0, stt.wall_size, room_size[1]),
                      pg.Rect((room_size[0]+stt.cell_size)//2, 0, (room_size[0]-stt.cell_size)//2, stt.wall_size)]

        for wall_rect in wall_rects:
            pg.draw.rect(room_map, (170, 170, 170), wall_rect)

        # load obstacles
        obstacle_list = ObstacleList()
        hitboxes = []

        for row_counter, row in enumerate(level):
            for column_counter, cell in enumerate(row):
                if cell != "0":
                    obstacle = possible_obstacles[int(cell)]
                    obstacle_size = (int(obstacle.type[0])*stt.cell_size, int(obstacle.type[2])*stt.cell_size)
                    obstacle_pos = (stt.wall_size + column_counter*stt.cell_size,
                                    stt.wall_size + row_counter*stt.cell_size)

                    obstacle_entity = ObstacleEntity(obstacle_size, obstacle_pos, obstacle)
                    obstacle_list.add(obstacle_entity)

                    hitbox = pg.transform.scale(obstacle.image, obstacle_size).get_rect()
                    hitbox.topleft = obstacle_pos

                    hitboxes.append(hitbox)

        # blit obstacle images on the room_map map
        for obstacle in obstacle_list.obstacles:
            obstacle_image = pg.transform.scale(obstacle.image, obstacle.rect.size)
            obst_pos = obstacle.rect.topleft

            room_map.blit(obstacle_image, obst_pos)

        return type, hitboxes, boundaries, room_map, wall_rects
