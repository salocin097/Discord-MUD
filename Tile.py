class Tile:
    def __init__(self, walkable, transparent):
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

    def set_wall(self):
        self.walkable = False
        self.transparent = False

    def set_floor(self):
        self.walkable = True
        self.transparent = True

    def set_water(self):
        self.walkable = False
        self.transparent = True

    def set_tall_grass(self):
        self.walkable = True
        self.transparent = False
