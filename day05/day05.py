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
    '''Given an input filepath, load input and produce solutions.
    '''
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
    '''Given a list of boarding passes, find the only missing value.

    One seat between the first and last seat id is not present. Return it.
    '''
    seat_set = set(get_seat_numbers(data))
    min_seat = min(seat_set)
    max_seat = max(seat_set)

    for i in range(min_seat+1, max_seat):
        if i not in seat_set:
            return i

    raise Exception("ohno, I can't find my seat 🤮")


def get_seat_numbers(data):
    '''For each seat string, compute the seat id and return the list
    '''
    return map(get_seat_id, data)


def get_seat_id(seat):
    '''Seat ID is the 8*row + col
    '''
    row, col = bin_cast(seat)
    return 8*row+col


def bin_cast(boarding_pass):
    '''Given a boarding pass string, return the row and col as ints

    Convert the strs to binary ints: first 7 are the row, last 3 are the column.
    '''
    row = int(boarding_pass[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(boarding_pass[7:].replace('R', '1').replace('L', '0'), 2)

    return row, col


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
