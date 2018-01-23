import rectangle_based_proc_gen
import render_map


MAP_HEIGHT = 25
MAP_WIDTH = 80


test_map = rectangle_based_proc_gen.make_blank_map(MAP_HEIGHT, MAP_WIDTH)
rectangle_based_proc_gen.populate_map(test_map, MAP_HEIGHT, MAP_WIDTH, 25, 4, 8)

render_map.render_dungeon(test_map)
