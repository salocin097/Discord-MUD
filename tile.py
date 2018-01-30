TILE_WALL = 0
TILE_FLOOR = 1
TILE_WATER = 2
TILE_TALL_GRASS = 3

class Tile:
    def __init__(self, walkable, transparent=None):
        self.walkable = walkable

        # by default, if a tile is walkable it is also transparent
        if transparent is None:
            transparent = walkable
        self.transparent = transparent

        # Transparent refers to whether or not it blocks LoS (Line of Sight)

    # These may become enums in the future where we have set_water() make self.walkable = SWIMMABLE or
    # something similar. For now my maze gens will just use this class and the first two methods.
    # In general, walls will be printed as '#' and floors as '.'. Obviously this won't matter later
    # but it's a placeholder. The Tile itself does not contain information about how it's drawn. The
    # Tile will only contain information about how to interact with it.

    def set_tile_type(self, tile_type):
        if tile_type == TILE_WALL:
            self.walkable = False
            self.transparent = False
        elif tile_type == TILE_FLOOR:
            self.walkable = True
            self.transparent = True
        elif tile_type == TILE_WATER:
            self.walkable = False
            self.transparent = True
        elif tile_type == TILE_TALL_GRASS:
            self.walkable = True
            self.transparent = False
        else:
            raise TypeError('Either the input is not yet implemented or the wrong type.')
