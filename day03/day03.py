'''Day 03 of Advent of Code 2020

The prompt is to count the number of '#' characters encountered in a grid when
moving from the top left down and to the right. Moving to the right will wrap
around to the left side of the grid if the width is exceeded.

Example:

  grid         traversal

  .#.#.#       X_____
  #.#.#.  -->  ____X_
  .#.#.#       __X___
  #.#.#.       X_____

  Then moving with slope {down: 1, right:4} gives the grid characters in order:
  ['.', '#', '.', '#'] from (Y,X) coordinates (0, 0), (1, 4), (2, 2), (3, 0)
'''

from argparse import ArgumentParser
from pathlib import PurePath

def day(grid, rise, run):
    '''Traverse a grid of snow '.' and trees '#' and return the number of
    encountered trees traversing from the top left with a given slope.
    '''
    count = 0
    column = 0
    width = len(grid[0])

    for row in range(0, len(grid), rise):
        if grid[row][column] == '#':
            count += 1

        column += run
        column %= width

    return count


if __name__ == '__main__':
    parser = ArgumentParser(description=day.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    parser.add_argument('-s', type=str, default="1/3", help='slope as rise/run')
    parser.add_argument('-p', type=int, default=1, help='part 1 or 2')
    args = parser.parse_args()

    part = args.p

    rise, run = args.s.split('/')

    with open(args.f, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    solution = day(data, int(rise), int(run))

    if part == 1:
        pass
    elif part == 2:
        for rise, run in [(1, 1), (1, 5), (1, 7), (2, 1)]:
            solution *= day(data, rise, run)
    else:
        raise Exception("ohno, bad part 🤮")

    print("Day 03 Part {} solution: {}".format(part, solution))
