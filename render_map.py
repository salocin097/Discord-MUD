

# This method assumes it accepts a filled rectangular 2D array
def render_dungeon(dungeon):
    for y in range(len(dungeon[0])):
        for x in range(len(dungeon)):
            wall = (not dungeon[x][y].walkable and not dungeon[x][y].transparent)
            floor = dungeon[x][y].walkable and dungeon[x][y].transparent
            if wall:
                print('#')
            elif floor:
                print('.')
    print('\n')
