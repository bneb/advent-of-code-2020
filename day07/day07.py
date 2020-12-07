'''Day 07 of Advent of Code 2020

The prompt is that there are rules for how bags must be packed.
The gist is that a bag must congain n some bags, m other bags, ...
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re

def main(file_path):
    '''Read data from the file_path, parse it and produce solutions.
    '''
    with open(file_path, 'r') as f:
        data = [line.strip() for line in f.readlines()]

    solution = part1(data)
    print("Day 07 Part 1 solution: {}".format(solution))

    solution = part2(data)
    print("Day 07 Part 2 solution: {}".format(solution))


def part1(data):
    '''How many bags could contain at any depth a shiny gold bag?
    '''
    bag_rules = {}
    for rule_str in data:
        # parse out '(<descriptive> <color>)' for each bag type in the rule
        bags = re.findall('(\w+ \w+) bag', rule_str)
        for bag in bags[1:]:
            bag_rules[bag] = bag_rules.get(bag, set())
            bag_rules[bag].add(bags[0])

    # Queue up bags for which we still need to process rules
    valid_bags = set()
    start = bag_rules.get('shiny gold', None)

    # Add the queued bag to the valid ones, set the queue to be the next depth.
    while start:
        valid_bags = valid_bags.union(start)

        next_start = set()
        for s in start:
            next_start = next_start.union(bag_rules.get(s, set()))

        start = next_start

    return len(valid_bags)


def part2(data):
    bag_rules = {}
    for rule_str in data:
        bags = re.findall('([\d ])?\s?(\w+ \w+) bag', rule_str)
        _, bag = bags[0]
        bag_rules[bag] = {b:int(n.replace(' ', '0')) for n, b in bags[1:]}

    return recursive_part2('shiny gold', bag_rules, 1) - 1


def recursive_part2(bag, rules, num):
    '''Recursive helper function that traverses between the bag and those it contains

    Returns this number of bags and the product of this number and any nested bags.
    '''
    if bag in rules:
        num += num * sum([recursive_part2(b, rules, int(v)) for b, v in rules[bag].items()])

    return num


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
