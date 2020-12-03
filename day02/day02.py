'''Day 02 of Advent of Code 2020

The prompt is to count valid passwords from a list of rule, password pairs.
'''

from argparse import ArgumentParser
from collections import Counter
from pathlib import PurePath
import re

def day(data, part):
    '''Given a list of (rule, password) pairs, return the count of passwords
    that satisfy their respective rules.

    Example for part 1:
      Rule interpretation is that the frequency of the character in the password
      is within the number rage (1-3), inclusive.

      1. 1-3 a: abcde
      2. 1-3 b: cdefg
      3. 2-9 c: ccccccccc

      Should produce 2, since pairs 1 and 3 are valid.

    Example for part 2:
      Rule interpretation is that the character should occur once at either
      index at either end of the '-'.

      1. 1-3 a: abcde
      2. 1-3 b: cdefg
      3. 2-9 c: ccccccccc

      Should produce 1, since pair 1 is valid.
    ''' 
    count = 0

    for pair_str in data:
        if part == 1:
            lower_limit, upper_limit, character, password = parse_pair(pair_str)

            if part1_validation(lower_limit, upper_limit, character, password):
                count += 1
        elif part == 2:
            lower_limit, upper_limit, character, password = parse_pair(pair_str)

            if part2_validation(lower_limit, upper_limit, character, password):
                count += 1
        else:
            raise Exception("ohno: bad part 🤮")

    return count


def part1_validation(lower_limit_str, upper_limit_str, character, password):
    counter = Counter(password)

    # default the count of the rule character to 0
    character_count = counter.get(character, 0)

    # convert limit strs to ints
    return int(lower_limit_str) <= character_count <= int(upper_limit_str)


def convert_to_index(index_str):
    # cast to int and decrement since the index string is 1-based
    return int(index_str)-1


def part2_validation(lower_index_str, upper_index_str, character, password):
    # create a counter of characters at either index
    lower_index = convert_to_index(lower_index_str)
    upper_index = convert_to_index(upper_index_str)
    counter = Counter(password[lower_index] + password[upper_index])

    # default the count of the rule character to 0
    character_count = counter.get(character, 0)

    # the character should only appear once at either index
    return character_count == 1


def parse_pair(pair):
    '''Given a pair of rule to password in the format:
    <arg1>-<arg2> <character>: <password>
    we aim to return a list of (arg1, arg2, character, password).

    Example:
      "1-3 a: abcde" --> ["1", "3", "a", "abcde"]
    '''
    # The split pattern is any non-alphanumeric substring
    return re.split("[^A-Za-z0-9]+", pair)


if __name__ == '__main__':
    parser = ArgumentParser(description=day.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    parser.add_argument('-p', type=int, default=1, help='part 1 or 2')
    args = parser.parse_args()

    part = args.p
    file_path = args.f

    with open(file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    solution = day(data, part)

    print("Day 02 Part {} solution: {}".format(part, solution))
