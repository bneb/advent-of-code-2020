'''Day 01 of Advent of Code 2020

The prompt is that a sub list of integers from the input should sum to a target
value, in this case 2020, and that we want to return the product of the numbers
in that sublist.
'''

from argparse import ArgumentParser
from functools import reduce
from itertools import combinations
from pathlib import PurePath

def main(data, n, target_number):
    '''With a list of numbers, how many numbers to use (n), and a target sum:
    return the product of a combination of n numbers that sum to the target.
    '''
    for combo in combinations(data, n):
        if sum(combo) == target_number:
            return reduce(lambda x, y: x*y, combo)


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    parser.add_argument('-n', type=int, default=2, help='use this many numbers')
    parser.add_argument('-t', type=int, default=2020, help='the target number')
    args = parser.parse_args()
    
    with open(args.f, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]

    solution = main(data, args.n, args.t)
    print("Day 01 solution: {}".format(solution))
