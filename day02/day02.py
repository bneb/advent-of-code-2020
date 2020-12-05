'''Day 02 of Advent of Code 2020

The prompt is to count valid passwords from a list of rule, password pairs.
'''

from argparse import ArgumentParser
from collections import Counter
from pathlib import PurePath
import re

def main(data, part):
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

        arg1, arg2, character, password = parse_pair(pair_str)

        if part == 1:
            lower_limit = int(arg1)
            upper_limit = int(arg2)
        elif part == 2:
            # for part 2 the character should occur only once
            lower_limit = 1
            upper_limit = 1
            # we only care to examine two indices in the string
            index1 = convert_to_index(arg1)
            index2 = convert_to_index(arg2)
            password = password[index1] + password[index2]
        else:
            raise Exception("ohno: bad part 🤮")

        if validate(lower_limit, upper_limit, character, password):
            count += 1

    return count


def convert_to_index(index_str):
    # cast to int and decrement since the index string is 1-based
    return int(index_str)-1


def validate(lower_limit, upper_limit, character, password):
    counter = Counter(password)
    character_count = counter.get(character, 0) # default to 0

    return lower_limit <= character_count <= upper_limit


def parse_pair(pair):
    '''Given a pair of rule to password in the format:
    <arg1>-<arg2> <character>: <password>
    we aim to return a list of (arg1, arg2, character, password).

    Example:
      "1-3 a: abcde" --> ["1", "3", "a", "abcde"]
    '''
    # The split pattern is a greedy non-alphanumeric substring
    return re.split("[^A-Za-z0-9]+", pair)


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    parser.add_argument('-p', type=int, default=1, help='part 1 or 2')
    args = parser.parse_args()

    with open(args.f, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    part = args.p
    solution = main(data, part)
    print("Day 02 Part {} solution: {}".format(part, solution))
