'''Day 05 of Advent of Code 2020

The prompt is that you're given a list a boarding passes to process.
Boarding passes are formatted as follows:
    BFFFBBFRRR: row 70, column 7, seat ID 567

    Where the B and F determine which half of the current rows to search in.
    L and R determine which half (left or right) of the columns to search in.

    Replace B and R with 1, and F and L with 0 and it looks like two 0b numbers.
    The above becomes 1000110111
                      \     /\ /
                       \row/ col
'''

from argparse import ArgumentParser
from pathlib import PurePath

def main(filepath):
    with open(filepath, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    solution = part1(data)
    print("Day 05 Part 1 solution: {}".format(solution))

    solution = part2(data)
    print("Day 05 Part 2 solution: {}".format(solution))



def part1(data):
    '''Given a list of boarding passes, produce the highest seat ID.

    Seat ID is given by row_number * 8 + column.
    '''
    return max(get_seat_numbers(data))
    

def part2(data):
    '''All seats not at the very beginning or end are full.

    Using process of elimination, find your seat.
    '''
    seat_set = set(get_seat_numbers(data))
    min_seat = min(seat_set)
    max_seat = max(seat_set)

    for i in range(min_seat+1, max_seat):
        if i not in seat_set:
            return i

    raise Exception("ohno, I can't find my seat 🤮")


def get_seat_numbers(data):
    return map(get_seat_id, data)


def get_seat_id(seat):
    row, col = bin_cast(seat)
    return 8*row+col


def bin_cast(boarding_pass):
    row = int(boarding_pass[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(boarding_pass[7:].replace('R', '1').replace('L', '0'), 2)

    return row, col


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    parser.add_argument('-p', type=int, default=1, help='which part to solve')
    args = parser.parse_args()

    part = args.p
    filepath = args.f

    main(filepath)
