'''Day 18 of Advent of Code 2020

The prompt is ...
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re

def main(file_path):
    '''The docstring goes here.
    '''
    with open(file_path, 'r') as f:
        data = [re.findall('\d+|[\+*]|[()]', line) for line in f.readlines()]

    # print(data)

    solution = part1(data)
    print("Day 18 Part 1 solution: {}".format(solution))


def part1(data):
    total = 0
    for d in data:
        _, result = evaluate(0, d)
        total += result

    return total


def evaluate(i, data):
    '''Takes list of strings and an index and returns the correct evaluation
    Example:
      data = ['9', '+', '12', '*', '(', '1', '+', '1', ')']
      result = 42
    '''
    lhs = None
    op = None

    while i < len(data):
        el = data[i]
        
        if el == ")":
            return i, lhs

        if el == "(":
            i, el = evaluate(i+1, data)

        if lhs is None:
            lhs = el
        elif op is None:
            op = el
        else:
            lhs = compute(lhs, op, el)
            op = None

        i += 1

    return i, lhs


def compute(lhs, op, rhs):
    if op == "+":
        return int(lhs) + int(rhs)
    elif op == "*":
        return int(lhs) * int(rhs)


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
