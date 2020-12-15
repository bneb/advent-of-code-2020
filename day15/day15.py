'''Day 15 of Advent of Code 2020

The prompt is to predict number at turn i in the elves' memory game.
'''

from argparse import ArgumentParser
from pathlib import PurePath
from time import process_time
from re import findall

def main(file_path):
    '''Parse input data from file. Produce and print solutions.
    '''
    with open(file_path, 'r') as f:
        data = findall('\d+', f.read())

    t0 = process_time()
    solution = memory_game(data, 2020)
    t1 = process_time()
    print("Day 15 Part 1 solution: {}".format(solution))
    print("Run time: {:.3f} seconds".format(t1-t0))

    t0 = process_time()
    solution = memory_game(data, 30000000)
    t1 = process_time()
    print("Day 15 Part 2 solution: {}".format(solution))
    print("Run time: {:.3f} seconds".format(t1-t0))


def memory_game(data, stop_turn):
    '''Start with given numbers, then at each turn if the last number is new
    the next number is 0, else the nex number is the difference between the
    current turn number and turn number on which the number was last said.
    '''
    turn = len(data)+1
    latest_number_turns = {int(n): int(i)+1 for i, n in enumerate(data)}
    current_number = 0

    while turn < stop_turn:
        next_number = turn - latest_number_turns.get(current_number, turn)

        latest_number_turns[current_number] = turn
        current_number = next_number
        turn += 1

    return current_number


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
