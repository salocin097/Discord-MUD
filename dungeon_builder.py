from stage_builder import StageBuilder
from tile import TILE_WALL, TILE_FLOOR


class DungeonBuilder(StageBuilder):

    def __init__(self):
        self.num_room_attempts = 0
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



        raise NotImplementedError("Not done yet")
