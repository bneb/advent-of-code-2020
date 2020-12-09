'''Day 09 of Advent of Code 2020

The prompt is blah blah blah honestly who cares.
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re

def main(file_path):
    '''Given the input filepath, parse the input and print the solutions.
    '''
    with open(file_path, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]

    solution = part1(data)
    print("Day 09 Part 1 solution: {}".format(solution))

    solution = part2(data)
    print("Day 09 Part 2 solution: {}".format(solution))


def part1(data):
    '''Find the first number that isn't a sum of any two of the
    preceding 25 numbers.
    '''
    for i in range(25, len(data)):
        available_nums = set(data[i-25:i])
        sum_target = data[i]
        sum_found = False

        for num in available_nums:
            difference = sum_target - num

            if difference in available_nums:
                sum_found = True

        if not sum_found:
            return sum_target

    raise Exception('why u do this??!?!?! 🤮')


def part2(data):
    '''Find a run in the data that sums to the number returned in part 1.

    Return the min + max from that run.
    '''
    target = part1(data)

    index_start = 0
    index_stop = 1
    data_sum = sum(data_between(data, index_stop, index_stop))

    while(data_sum != target):
        if data_sum < target:
            index_stop += 1
        elif data_sum > target:
            index_start += 1

        data_sublist = data_between(data, index_start, index_stop)
        data_sum = sum(data_sublist)

    return min(data_sublist) + max(data_sublist)


def data_between(data, index_start, index_stop):
    '''Return an array of values in data between i and j inclusive.
    '''
    return data[index_start:index_stop+1]


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
