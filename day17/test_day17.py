from day17 import *

grid = { # 27 around (0, 0, 0)
    (1, -1, -1),
    (1, -1, 0),
    (1, -1, 1),
    (0, -1, -1),
    (0, -1, 0),
    (0, -1, 1),
    (-1, -1, -1),
    (-1, -1, 0),
    (-1, -1, 1),
    (1, 0, -1),
    (1, 0, 0),
    (1, 0, 1),
    (0, 0, -1),
    # (0, 0, 0), The center of the grid
    (0, 0, 1),
    (-1, 0, -1),
    (-1, 0, 0),
    (-1, 0, 1),
    (1, 1, -1),
    (1, 1, 0),
    (1, 1, 1),
    (0, 1, -1),
    (0, 1, 0),
    (0, 1, 1),
    (-1, 1, -1),
    (-1, 1, 0),
    (-1, 1, 1)
}

print(get_neighborhood((0, 0, 0), grid), 'should be', 26)
