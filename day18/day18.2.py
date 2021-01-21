'''Day 18 of Advent of Code 2020

We're taking mathy strings with valid characters in [ \d\+*()]
and then evaluating them based on different rules than normal
arithmetic.

For 18.2, + has higher precedence than *
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re

def main(file_path):
    with open(file_path, 'r') as f:
        # Restrict input to valid tokens
        data = [re.findall('\d+|[\+*()]', line) for line in f.readlines()]

    solution = part2(data)
    print("Day 18 Part 2 solution: {}".format(solution))


def part2(data):
    total = 0

    for row in data:
        _, parens_grouped = group_parens(0, row)
        processed_input = split_mul(parens_grouped)

        result = evaluate(processed_input)
        total += result

    return total


def evaluate(data):
    lhs = None  # left hand side
    op = None

    for i, el in enumerate(data):
        if isinstance(el, list):
            el = evaluate(el)

        if lhs is None:
            lhs = el
        elif op is None:
            op = el
        else:
            lhs = compute(lhs, op, el)
            op = None

        i += 1

    return lhs


def split_mul(groups):
    i = 0

    while i < len(groups):
        el = groups[i]

        if isinstance(el, list):
            groups[i] = split_mul(el)
        elif el == "*":
            groups = [groups[:i], groups[i], split_mul(groups[i+1:])]

        i+=1
    
    return groups


def group_parens(i, data):
    grouping = []

    while i < len(data):
        el = data[i]
        
        if isinstance(el, list):
            _, el = group_parens(0, el)

        if el == "(":
            i, subgroup = group_parens(i+1, data)
            grouping.append(subgroup)
        elif el == ")":
            return i, grouping
        else:
            grouping.append(el)

        i+=1

    return i, grouping


def compute(lhs, op, rhs):
    result = int(lhs) + int(rhs)
    if op == "*":
        result = int(lhs) * int(rhs)

    return result


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
