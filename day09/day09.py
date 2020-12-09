'''Day 09 of Advent of Code 2020

The prompt is ...
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re

def main(file_path):
    '''The docstring goes here.
    '''
    with open(file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    solution = part1(data)
    print("Day 09 Part 1 solution: {}".format(solution))

    solution = part2(data)
    print("Day 09 Part 2 solution: {}".format(solution))


def part1(data):
    for i in range(25, len(data)):
        pre = set([int(d) for d in data[i-25:i]])
        found = False
        target = int(data[i])

        for num in pre:
            search_num = target-num

            if search_num in pre:
                found = True

        if not found:
            return target


def part2(data):
    target = part1(data)

    for i in range(len(data)):
        for j in range(i+2, len(data)):

            r = [int(x) for x in data[i:j]]
            if sum(r) == target:
                return min(r) + max(r)
            if sum(r) > target:
                continue


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
