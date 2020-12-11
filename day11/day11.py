'''Day 11 of Advent of Code 2020

The prompt is ...
'''

from argparse import ArgumentParser
from pathlib import PurePath
import time

def main(file_path):
    '''The docstring goes here.
    '''
    grid = {}
    with open(file_path, 'r') as f:
        for y, row in enumerate(f.readlines()):
            for x, col in enumerate(row):
                if col == '.':
                    continue

                grid[(x, y)] = col.strip()

    t = time.process_time()
    solution = part1(grid)
    print("Day 11 Part 1 solution: {}".format(solution))
    print('run time: {}'.format(time.process_time()-t))

    t = time.process_time()
    solution = part2(grid)
    print("Day 11 Part 2 solution: {}".format(solution))
    print('run time: {}'.format(time.process_time()-t))


def get_neighbors(coords, grid):
    x, y = coords

    neighbors = 0
    for xi in range(x-1, x+2):
        for yi in range(y-1, y+2):
            if xi == x and yi == y:
                continue

            if grid.get((xi, yi), False) == '#':
                neighbors += 1

    return neighbors


def part1(grid):
    last_grid = None
            
    while grid != last_grid:
        last_grid = grid
        grid = tic(grid, 4, get_neighbors)

    return sum([1 for v in grid.values() if v == '#'])


def tic(grid, n, get_neighbors_fun):
    new_grid = {}
    
    for (x, y), v in grid.items():
        neighbors = get_neighbors_fun((x, y), grid)
        if neighbors == 0 and v == 'L':
            new_grid[(x, y)] = '#'
        elif neighbors >= n and v == '#':
            new_grid[(x, y)] = 'L'
        else:
            new_grid[(x, y)] = grid[(x, y)]

    return new_grid


def get_visible_neighbors(coords, grid):
    x, y = coords

    neighbors = 0
    for search_dir in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        xi, yi = search_dir
        xs = x+xi
        ys = y+yi

        while -1 < xs < 100 and -1 < ys < 100 and (xs, ys) not in grid:
            xs += xi
            ys += yi

        if grid.get((xs, ys), '.') == '#':
            neighbors += 1

    return neighbors


def part2(grid):
    last_grid = None
            
    while grid != last_grid:
        last_grid = grid
        grid = tic(grid, 5, get_visible_neighbors)

    return sum([1 for v in grid.values() if v == '#'])


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
