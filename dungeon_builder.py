from stage_builder import StageBuilder
from tile import TILE_WALL, TILE_FLOOR
from random import randint
from rectangle import Rect


class DungeonBuilder(StageBuilder):

    def __init__(self):
        self.num_room_attempts = 20
        self.room_size_variance = 0
        self.extra_connector_chance = 0

    # this particular map layout
    def bind_stage(self, stage):
        if stage.width % 2 == 0 or stage.height % 2 == 0:
            raise ValueError("Input a stage with odd (%2 == 1) dimensions.")
        else:
            self.stage = stage

    def update_parameters(self, num_room_attempts=None, room_size_variance=None, extra_connector_chance=None):
        if num_room_attempts is not None:
            self.num_room_attempts = num_room_attempts
        if room_size_variance is not None:
            self.room_size_variance = room_size_variance
        if extra_connector_chance is not None:
            self.extra_connector_chance = extra_connector_chance

    def generate_map(self):

        # fill the stage with walls
        self.stage.layout.fill_area(self.stage.width, self.stage.height, TILE_WALL)

        self.generate_rectangles()

        raise NotImplementedError("Not done yet")

    def generate_rectangles(self):

        # this made need to belong to the whole DungeonBuilder class? not sure. generate_map may need it
        rooms = []
        room_counter = 0
        for i in range(self.num_room_attempts):
            # the * 2 + 1 ensures it is an odd sized room. The minimum size effectively being 3.
            size = randint(1, 3 + self.room_size_variance) * 2 + 1
            rectangularity = randint(0, 1 + size // 2) * 2
            width = size
            height = size
            if randint(0, 1):
                width += rectangularity
            else:
                height += rectangularity

            x = (randint(0, (self.stage.width - width - 1)) // 2) * 2 + 1
            y = (randint(0, (self.stage.height - height - 1)) // 2) * 2 + 1

            new_room = Rect(x, y, width, height)

            # check to see if new room will overlap with an existing room
            failed = False
            for other_room in rooms:
                if new_room.does_intersect(other_room):
                    failed = True
                    break

            if not failed:
                rooms.append(new_room)
                room_counter += 1
                self.stage.fill_area(x, y, width, height)

        raise NotImplementedError("WIP")
