from tile import Tile, TILE_WALL, TILE_FLOOR # not sure how necessary this import is? or which parts
# from abc import ABC, abstractmethod, abstractproperty


# This is taken from a dart implementation of a procedurally generated dungeon. It is
# in the game "hauberk" https://github.com/munificent/hauberk/blob/db360d9efa714efb6d937c31953ef849c7394a39/COPYRIGHT
# It uses the MIT License. I am unsure how similar my code is to it to force us to also
# use the MIT License - but our intention was to make this open source regardless...I think
# I still need to look into legal shenanigans

# This is an abstract class that can be implemented to build maps with different generators
# This class will not permanently "own" the stage. The bind_stage method allows the class to
# modify the stage without having to pass the stage as a parameter over and over (I think
# this is the purpose???). The generate_map() will be the main method that creates the dungeon
# I do not think I am supposed to have the __init__ method? But I am unsure how to
# create properties for this class without the method. I will look into the ABC module and
# it's usage. The fill_area() method is just a nice method to make rectangles of a single
# tile_type. Or straight lines.


class StageBuilder:

    def __init__(self):
        self.stage = None
        self.width = None
        self.height = None

    # this allows the stageBuilder to modify the stage
    def bind_stage(self, stage):
        self.stage = stage
        # storing the width and height for later use
        self.width = len(stage)
        if self.width != 0 or None:
            self.height = len(stage[0])

    def generate_map(self):
        raise NotImplementedError('This method has not been overridden yet.')

    # to fill full map simply do fill_area(stage.width, stage.height, TILE_WALL)
    def fill_area(self, x, y, tile_type):
        for x in range(x):
            for y in range(y):
                self.stage[x][y].set_tile_type(tile_type)