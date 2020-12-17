'''Day 16 of Advent of Code 2020

The prompt is to examine tickets in an incomprehensible language.
'''

from argparse import ArgumentParser
from pathlib import PurePath
from time import process_time
import re

def main(file_path):
    '''Read input from file, produce solutions, and print them.
    '''
    with open(file_path, 'r') as f:
        rules, yours, nearby = parse_input(f.readlines())


    t0 = process_time()
    solution = part1(rules, nearby)
    t1 = process_time()
    print("Day 16 Part 1 solution: {}".format(solution))
    print('Run time: {:0.2f} milliseconds'.format((t1-t0)*1000))

    t0 = process_time()
    solution = part2(rules, yours, nearby)
    t1 = process_time()
    print("Day 16 Part 2 solution: {}".format(solution))
    print('Run time: {:0.2f} milliseconds'.format((t1-t0)*1000))


def parse_input(lines):
    rules = {}
    yours = None
    nearby = []

    section = 0
    for line in lines:
        if line == '\n':
            section += 1

        elif section == 0:
            tokens = re.findall('^[\w ]+|\d+', line)
            rule_name = tokens[0]
            num_ranges = []
            for i in range(1, len(tokens)-1, 2):
                num_ranges.append(list(range(int(tokens[i]), int(tokens[i+1])+1)))

            rules[rule_name] = set().union(*num_ranges)

        elif section == 1:
            yours = [int(n) for n in re.findall('\d+', line)]

        elif section == 2:
            numbers = [int(n) for n in re.findall('\d+', line)]
            if numbers:
                nearby.append(numbers)

    return rules, yours, nearby


def part1(rules, nearby):
    all_rule_numbers = get_all_rule_numbers(rules)

    rate = 0
    for n in nearby:
        rate += sum(list(set(n) - all_rule_numbers))

    return rate


def part2(rules, yours, nearby):
    all_rule_numbers = get_all_rule_numbers(rules)

    valid_nearby = [s for s in nearby if is_ticket_valid(all_rule_numbers, s)]
    valid = valid_nearby + [yours]

    field_sets = get_field_sets(valid)
    num_fields = len(field_sets)

    rule_indices = {r: get_possible_indices(v, field_sets) for r, v in rules.items()}

    while any([len(v) > 1 for v in rule_indices.values()]):
        process_of_elimination(rule_indices)

    acc = 1
    for r, v in rule_indices.items():
        if re.match('^departure', r):
            i = v.pop()
            acc *= yours[i]

    return acc


def get_field_sets(nearby):
    field_sets = [set() for _ in range(len(nearby[0]))]

    for n in nearby:
        for i, v in enumerate(n):
            field_sets[i].add(v)

    return field_sets
            

def get_all_rule_numbers(rules):
    return set().union(*list(rules.values()))


def is_ticket_valid(rule_numbers, ticket):
    return set(ticket).issubset(rule_numbers)


def get_possible_indices(rule_values, field_sets):
    possible_indices = set()

    for i, fs in enumerate(field_sets):
        if fs.issubset(rule_values):
            possible_indices.add(i)

    return possible_indices


def process_of_elimination(set_map):
    to_eliminate = set()
    to_review = []

    for k, s in set_map.items():
        if len(s) == 1:
            to_eliminate = to_eliminate.union(s)
        else:
            to_review.append(s)

    for s in to_review:
        s -= to_eliminate


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
