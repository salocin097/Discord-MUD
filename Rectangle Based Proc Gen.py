import random

# The first class, Tile will be used in basically all of the Proc Gen. It will contain information about the Tile
# The two current properties are pretty straightforward and will be used for pathfinding, fog of war, and rendering

# The way this works is we call the make_blank_map() method with a width and height and it will return a 2D array
# of Tiles, initialized as False for both walkable and transparent, implying they are walls

# Next we call populate_map(dungeon_map, map_height, map_width, max_rooms, room_min_size, room_max_size). First
# parameter will be the 2D array we created above. Next two are again the map_height and map_width. When I'm less
# lazy I can remove those and just do some type of .length() to find those parameters, but I've been jumping
# between C#, C++, Java and Python so I don't remember functions. Next we have the maximum number of rooms.

# Note: it's very likely that it will not populate with close to the # of max_rooms input, although that depends
# on the map size and room size parameters. max_rooms only denotes the number of rooms the populate_map() function
# will attempt to make. The function will create a random Rect, new_room, based on the size parameters and map
# parameters. It will then check against the other already existing rooms to see if it would intersect. If it does,
# it discards the new_room. If it will not overlap it will create the room, changing the Tiles in the 2D array to be
# both walkable and transparent, a floor tile. It then will create a tunnel from the last room to the current room.
# Lastly, it adds the Rect to the rooms[] array to ensure there will be no overlapping rooms.

# The function does not track the location of hallways, so the larger the maze, the more likely it is to have redundant
# tunnels or double wide tunnels.

# Issues: Currently don't have a way to display the maze!! Not sure what library we want to use to draw it?
# but just use the Tile.walkable/transparent to decide what is a wall, etc. Currently whatever is walkable is also
# transparent but that can be changed later.
# An example being lake tiles that are not walkable but transparent or something. Vice versa for a foggy level.



class Tile:
    def __init__(self, walkable, transparent):
        self.walkable = walkable

        # by default, if a tile is walkable it is also transparent
        if transparent is None:
            transparent = walkable
        self.transparent = transparent

        # Transparent refers to whether or not it blocks LoS (Line of Sight)

        # NOTE these are not booleans because in the future we may have flying/swimming mobs
        # and use variables such as swimmable etc


class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)

    def does_intersect(self, other):
        # returns true if the rectangle intersects with the other rectangle
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)


def create_room(dungeon_map, room):
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            dungeon_map[x][y].walkable = True
            dungeon_map[x][y].transparent = True


def create_h_tunnel(dungeon_map, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        dungeon_map[x][y].walkable = True
        dungeon_map[x][y].transparent = True


def create_v_tunnel(dungeon_map, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        dungeon_map[x][y].walkable = True
        dungeon_map[x][y].transparent = True


def make_blank_map(map_height, map_width):
    dungeon_map = [[Tile(False)
                    for y in range(map_height)]
                   for x in range(map_width)]
    return dungeon_map


def populate_map(dungeon_map, map_height, map_width, max_rooms, room_min_size, room_max_size):
    rooms = []
    num_rooms = 0

    for r in range(max_rooms):
        w = random.randint(room_min_size, room_max_size)
        h = random.randint(room_min_size, room_max_size)
        x = random.randint(0, map_width - w - 1)
        y = random.randint(0, map_height - h - 1)

        new_room = Rect(x, y, w, h)

        # check to see if new room will overlap with an existing room
        failed = False
        for other_room in rooms:
            if new_room.does_intersect(other_room):
                failed = True
                break

        if not failed:

            create_room(dungeon_map, new_room)

            (new_x, new_y) = new_room.center()

            if num_rooms == 0:
                # this will eventually have initial room stuff
                pass
            else:
                (prev_x, prev_y) = rooms[num_rooms - 1].center()

                if random.randint(0, 1) == 1:
                    # first move horizontally, then vertically
                    create_h_tunnel(prev_x, new_x, prev_y)
                    create_v_tunnel(prev_y, new_y, new_x)
                else:
                    # first move vertically, then horizontally
                    create_v_tunnel(prev_y, new_y, prev_x)
                    create_h_tunnel(prev_x, new_x, new_y)

            rooms.append(new_room)
            num_rooms += 1
