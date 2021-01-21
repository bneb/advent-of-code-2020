'''Day 17 of Advent of Code 2020

The prompt is ...
'''

from argparse import ArgumentParser
from pathlib import PurePath

def main(file_path):
    '''The docstring goes here.
    '''
    grid = set()

    with open(file_path, 'r') as f:
        for i, row in enumerate(f.readlines()):
            for j, col in enumerate(row):
                if col == '#':
                    grid.add((j, i, 0))

    solution = part1(grid)
    print("Day 17 Part 1 solution: {}".format(solution))

    grid4d = set()
    for g in grid:
        x, y, z = g
        grid4d.add((x, y, z, 0))

    solution = part2(grid4d)
    print("Day 17 Part 2 solution: {}".format(solution))


def get_neighborhood(c, grid):
    x, y, z = c
    # print('for', x, y, z)

    acc = 0

    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            for k in [z-1, z, z+1]:
                # print('testing', i, j, k)
                if x == i and y == j and z == k:
                    continue


                if (i, j, k) in grid:
                    # print('found', i, j, k)
                    acc += 1

    return acc


def get_search_bounds(grid):
    '''Returns min x - 1, max x + 1, min y - 1, max y + 1, min z - 1, max z + 1
    '''
    minx = 1
    maxx = -1
    miny = 1
    maxy = -1
    minz = 1
    maxz = -1

    for x, y, z in grid:
        minx = min(x, minx)
        maxx = max(x, maxx)
        miny = min(y, miny)
        maxy = max(y, maxy)
        minz = min(z, minz)
        maxz = max(z, maxz)

    return minx-1, maxx+1, miny-1, maxy+1, minz-1, maxz+1


def tic(grid):
    minx, maxx, miny, maxy, minz, maxz = get_search_bounds(grid)
    new_grid = set()

    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            for z in range(minz, maxz+1):
                n = get_neighborhood((x, y, z), grid)
                if (x, y, z) in grid and n in [2, 3]:
                    new_grid.add((x, y, z))
                elif (x, y, z) not in grid and n == 3:
                    new_grid.add((x, y, z))

    return new_grid


def part1(grid):
    for i in range(6):
        grid = tic(grid)

    return len(grid)


def print_grid(grid):
    print('#'*42)
    minx, maxx, miny, maxy, minz, maxz = get_search_bounds(grid)
    for z in range(minz+1, maxz):
        print('z', z)
        for y in range(miny, maxy+1):
            s = ''
            for x in range(minx, maxx+1):
                s += '#' if (x, y, z) in grid else '.'
            print(s)


def part2(grid):
    for i in range(6):
        grid = tic4(grid)

    return len(grid)


def get_search_bounds4(grid):
    '''Returns min x - 1, max x + 1, min y - 1, max y + 1, min z - 1, max z + 1
    '''
    minx = 1
    maxx = -1
    miny = 1
    maxy = -1
    minz = 1
    maxz = -1
    minw = 1
    maxw = -1

    for x, y, z, w in grid:
        minx = min(x, minx)
        maxx = max(x, maxx)
        miny = min(y, miny)
        maxy = max(y, maxy)
        minz = min(z, minz)
        maxz = max(z, maxz)
        minw = min(w, minw)
        maxw = max(w, maxw)

    return minx-1, maxx+1, miny-1, maxy+1, minz-1, maxz+1, minw-1, maxw+1


def get_neighborhood4(c, grid):
    x, y, z, w = c
    # print('for', x, y, z)

    acc = 0

    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            for k in [z-1, z, z+1]:
                for l in [w-1, w, w+1]:
                    # print('testing', i, j, k)
                    if x == i and y == j and z == k and l == w:
                        continue


                    if (i, j, k, l) in grid:
                        # print('found', i, j, k)
                        acc += 1

    return acc


def tic4(grid):
    minx, maxx, miny, maxy, minz, maxz, minw, maxw = get_search_bounds4(grid)
    new_grid = set()

    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            for z in range(minz, maxz+1):
                for w in range(minw, maxw+1):
                    n = get_neighborhood4((x, y, z, w), grid)
                    if (x, y, z, w) in grid and n in [2, 3]:
                        new_grid.add((x, y, z, w))
                    elif (x, y, z, w) not in grid and n == 3:
                        new_grid.add((x, y, z, w))

    return new_grid


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
