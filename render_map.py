

# This method assumes it accepts a filled rectangular 2D array
def render_dungeon(dungeon):
    for y in range(dungeon[0].len()):
        for x in range(dungeon.len()):
            wall = (not dungeon[x][y].walkable and not dungeon[x][y].transparent)
            floor = dungeon[x][y].walkable and dungeon[x][y].transparent
            if wall:
                print('#')
            elif floor:
                print('.')
        print('\n')
