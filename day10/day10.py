'''Day 10 of Advent of Code 2020

The prompt is ...
'''

from argparse import ArgumentParser
from pathlib import PurePath
from collections import Counter

def main(file_path):
    '''The docstring goes here.
    '''
    with open(file_path, 'r') as f:
        data = [int(line.strip()) for line in f.readlines()]
        data = [0] + sorted(data) + [max(data)+3]

    solution = part1(data)
    print("Day 10 Part 1 solution: {}".format(solution))

    solution = part2(data)
    print("Day 10 Part 2 solution: {}".format(solution))


def part1(data):
    # count by diff between adjacent sorted values
    counter = Counter([data[i]-data[i-1] for i in range(1, len(data))])

    # return the produce of the number of 1 diffs and 3 diffs
    return counter[1] * counter[3]


def part2(data):
    '''It's amazing that I've never had to solve a problem this way before.
    Very cool. Shouts to Ajit for suggesting this 😎.

    Intuition is that the only way to get to the end is to get to any node
    with a value within three of the ultimate node. The same is true for each
    of those nodes, and so on.

    Build a table with the number of ways to get to each node (1 way to start!)
    Then apply the logic above.
    '''
    # one way to start at 0
    path_counts = {0: 1}

    # set counts for each node
    for i, node in enumerate(data[1:]):
        print(path_counts)

        # accumulate the path_counts of nodes within 3 of the current
        num_paths = 0

        # lookback at most 3, unless i-3 is out of bounds
        lookback_index = max(i-3, 0)

        for other_node in data[lookback_index:]:
            if other_node >= node - 3:
                num_paths += path_counts.get(other_node, 0)

        path_counts[node] = num_paths

    # return the path_count of the max element
    return path_counts[max(data)]




if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
