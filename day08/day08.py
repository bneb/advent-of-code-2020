'''Day 08 of Advent of Code 2020

You have a list of instructions as operator, value pairs of the form:
    "(acc|jmp|nop) [+-]\d+"
  where
    - acc updates an accumulator
    - jmp jumps by the value to another instruction
    - nop noops to the next instruction

Process the imput according to some goal and return the accumulator
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re
from functools import reduce
from itertools import combinations

def main(file_path):
    '''Parse input, compute solutions, and print them.
    '''
    with open(file_path, 'r') as f:
        data = [re.match('(\w{3}) ([+-]\d+)', line.strip()).groups() for line in f.readlines()]
    
    _, solution = part1(data)
    print("Day 08 Part 1 solution: {}".format(solution))

    _, solution = part2(data)
    print("Day 08 Part 2 solution: {}".format(solution))


def part1(data):
    '''Return the accumulator once you revisit an instruction.
    '''
    acc = 0
    i = 0
    visited = set()

    while 0 <= i < len(data):
        op, val = data[i]

        if i in visited:
            return (i, acc)

        visited.add(i)

        if op == 'acc':
            acc += int(val)
            i += 1
        if op == 'jmp':
            i += int(val)
        if op == 'nop':
            i += 1

    return (i, acc)


def part2(data):
    '''Try to avoid an infinite loop by swapping jmp for nop or visa versa once.
    '''
    for i, d in enumerate(data):
        op, val = d

        # perform swap of instruction
        if op == 'nop':
            new_data = data[:i] + [('jmp', val)] + data[i+1:]
        elif op == 'jmp':
            new_data = data[:i] + [('nop', val)] + data[i+1:]
        else:
            # exit if no swap occurs since we must swap once
            continue

        # evaluate in the same fashion as part1 
        i, acc = part1(new_data)

        # if we've exceeded the number of instructions, we made it!
        if i >= len(data):
            return i, acc

    raise Exception("ohfuck 🤮")

        
    

if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
