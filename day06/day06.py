'''Day 06 of Advent of Code 2020

Data contains answers from groups separated by '\n\n', with individuals' answers
separated by '\n' within a group.
'''

from argparse import ArgumentParser
from pathlib import PurePath

def main(file_path):
    '''From an input file, parse data and calculate solutions for part 1 and 2.
    '''
    with open(file_path, 'r') as f:
        data = f.read().split('\n\n')

    solution = count_total_answers(data, set.union)
    print("Day 06 Part 1 solution: {}".format(solution))

    solution = count_total_answers(data, set.intersection)
    print("Day 06 Part 2 solution: {}".format(solution))


def count_total_answers(data, op):
    '''A group's (g) answers are those reduced across people (p) by op.

    Return the sum of the count of each group's answers.
    '''
    total_answer_count = 0

    for g in data:
        answers = op(*[set(p) for p in g.split('\n') if p != ''])
        total_answer_count += len(answers)

    return total_answer_count


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
