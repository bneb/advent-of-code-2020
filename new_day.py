'''Create a new day directory and files for Advent of Code 2020.

Usage:
    $ python3 new_day.py [-d=<puzzle day>]
'''

from argparse import ArgumentParser
from glob import glob
from pathlib import Path
import os

if __name__ == '__main__':
    # The next few lines glob directories to find the first day not to exist
    directory = os.path.dirname(os.path.realpath(__file__))
    path_pattern = os.path.join(directory, 'day*')

    day = 1
    for i, f in enumerate(sorted(glob(path_pattern))):
        if int(f[-2:]) == i+1:
            day += 1
        else:
            break

    # Default to the latest day that has yet to be done
    parser = ArgumentParser(description='Create daily challenge boilerplate.')
    parser.add_argument('-d', type=int, default=day, help='the puzzle day')
    args = parser.parse_args()

    # Overwrite if a day argument has been passed from the command line
    day = args.d
    path = Path('./day{:0>2}'.format(day))
    path.mkdir()

    # write stub of python file
    python_path = path / 'day{:0>2}.py'.format(day)
    with python_path.open('w') as f:
        f.write('''\'''Day {day:0>2} of Advent of Code 2020

The prompt is ...
\'''

from argparse import ArgumentParser
from pathlib import PurePath

def main(file_path):
    \'''The docstring goes here.
    \'''
    with open(file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    solution = part1()
    print("Day {day:0>2} Part 1 solution: {{}}".format(solution))

    solution = part2()
    print("Day {day:0>2} Part 2 solution: {{}}".format(solution))


def part1(data):
    return None


def part2(data):
    return None


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
'''.format(day=day)
        )

    # create input and test input files
    input_path = path / 'input.txt'.format(day)
    input_path.touch()
    test_input_path = path / 'test_input.txt'.format(day)
    test_input_path.touch()

