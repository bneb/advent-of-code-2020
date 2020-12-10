'''Day 10 of Advent of Code 2020

The prompt is ...
'''

from argparse import ArgumentParser
from pathlib import PurePath
from collections import Counter
import time

def main(file_path):
    '''The docstring goes here.
    '''
    with open(file_path, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
        data = [0] + sorted(data) + [max(data)+3]

    solution = part1(data)
    print("Day 10 Part 1 solution: {}".format(solution))

    t = time.process_time()
    solution = part2(data)
    print('elapsed time', time.process_time(), 'for input size', len(data)-2)
    print("Day 10 Part 2 solution: {}".format(solution))


def part1(data):
    counter = Counter([data[i]-data[i-1] for i in range(1, len(data))])

    return counter[1] * counter[3]


def part2(data):
    paths = {}
    stop = max(data)

    for el in data:
        paths[el] = [x for x in data if el < x <= el + 3]

    
    return part2_recurse(0, paths, stop)


def part2_recurse(cur, paths, stop):

    # print('checking', cur, 'in', paths)
    if cur == stop:
        return 1
    
    return sum([part2_recurse(x, paths, stop) for x in paths[cur]])


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
