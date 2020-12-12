'''Day 12 of Advent of Code 2020

The prompt is ...
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re
import numpy as np
import time

RIGHT_ROTATION_MATRIX = np.matrix([[0, -1],[1, 0]])
LEFT_ROTATION_MATRIX = np.matrix([[0, 1],[-1, 0]])

def main(file_path):
    '''You know the drill. Parse inputs from file. Produce solutions.
    '''
    with open(file_path, 'r') as f:
        data = [re.match('([NSEWRLF])(\d+)', line).groups() for line in f.readlines()]

    t = time.process_time()
    solution = part1(data)
    print("Day 12 Part 1 solution: {}".format(solution))
    print("Run time: {}".format(time.process_time() - t))

    t = time.process_time()
    solution = part2(data)
    print("Day 12 Part 2 solution: {}".format(solution))
    print("Run time: {}".format(time.process_time() - t))


def part1(data):
    '''We're moving in a grid based on instructions (i) and values (v)
    '''
    x = 0
    y = 0
    direction = (1, 0)

    for i, v in data:
        v = int(v)
        
        direction = turn(direction, i, v)
        delta = move(direction, i, v)
        dx, dy = delta
        
        x += dx
        y += dy

    if x < 0: x = -x
    if y < 0: y = -y

    return x+y


def turn(direction, instruction, value):
    '''See left and right rotation matrices
    Multiply by the matching rotation matrix once per 90 degrees.
    '''
    if instruction not in ['R', 'L']:
        return direction

    mat = np.matrix([direction, [0,0]])

    if instruction == 'R':
        rotate_mat = RIGHT_ROTATION_MATRIX
    elif instruction == 'L':
        rotate_mat = LEFT_ROTATION_MATRIX
    else:
        raise Exception('🤮', direction, instruction, value)

    turns90 = value//90

    for _ in range(turns90):
        mat = np.matmul(mat, rotate_mat)

    return tuple(mat.A[0])


def move(direction, i, v):
    '''NSEW moves us v steps in matching cardinal direction.
    F moves us in the direction of direction by v.
    L and R don't move us.
    '''
    if i in ['R', 'L']:
        dx, dy = 0, 0
    if i == 'F':
        dx, dy = direction
        dx *= v
        dy *= v
    elif i == 'N':
        dx, dy = 0, v
    elif i == 'S':
        dx, dy = 0, -v
    elif i == 'E':
        dx, dy = v, 0
    elif i == 'W':
        dx, dy = -v, 0

    return dx, dy


def part2(data):
    '''We're moving in a grid based on instructions (i) and values (v)

    The difference this time is that we move towards a waypoint (direction).
    We only actually move the ship when 'F' is the instruction.
    We take direction sized steps v-times.
    '''
    x = 0
    y = 0
    direction = (10, 1)

    for i, v in data:
        v = int(v)

        if i == 'F':
            dx, dy = direction
            for _ in range(v):
                x += dx
                y += dy
        else:
            direction = turn(direction, i, v)
            wpdx, wpdy = move(direction, i, v)
            wpx, wpy = direction
            direction = (wpx+wpdx, wpy+wpdy)

    if x < 0: x = -x
    if y < 0: y = -y

    return x + y


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
