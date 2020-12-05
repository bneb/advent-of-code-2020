'''Create a new day directory and files for Advent of Code 2020.'''

from argparse import ArgumentParser
from pathlib import Path

if __name__ == '__main__':
    parser = ArgumentParser(description='Create daily challenge boilerplate.')
    parser.add_argument('-d', type=int, help='the day of the advent calendar')
    args = parser.parse_args()
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

def day(data):
    \'''The docstring goes here.
    \'''
    pass


if __name__ == '__main__':
    parser = ArgumentParser(description=day.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    parser.add_argument('-p', type=int, default=1, help='which part to solve')
    args = parser.parse_args()

    with open(args.f, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    solution = day(data)

    print("Day {day:0>2} solution: {{}}".format(solution))
'''.format(day=day)
        )

    # create input file
    input_path = path / 'day{:0>2}_input.txt'.format(day)
    input_path.touch()

