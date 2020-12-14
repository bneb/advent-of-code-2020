'''Day 14 of Advent of Code 2020

The prompt is to examine values in memory after a bitmask is applied
'''

from argparse import ArgumentParser
from itertools import product
from pathlib import PurePath
import time
import re

def main(file_path):
    '''Read data, calculate solutions, and print results.
    '''
    with open(file_path, 'r') as f:
        data = [re.match('(mem\[\d+\]|mask) = (.*)\n', line).groups() for line in f.readlines()]

    t0 = time.process_time()
    solution = part1(data)
    t1 = time.process_time()
    print("Day 14 Part 1 solution: {}".format(solution))
    print("Run time: {:.4f} milliseconds".format((t1-t0)*1000))

    t0 = time.process_time()
    solution = part2(data)
    t1 = time.process_time()
    print("Day 14 Part 2 solution: {}".format(solution))
    print("Run time: {:.4f} milliseconds".format((t1-t0)*1000))


def part1(data):
    '''Return the sum of all non-zero values in memory after the bitmask is applied.
    The strategy is to make two masks to handle wildcards appropriately
    Mask1 is the  OR_MASK: 0 for 0 and X, 1 for 1
    Mask2 is the AND_MASK: 1 for 1 and X, 0 for 0
    '''
    mem = {}
    or_mask = None
    and_mask = None

    for (k, v) in data:
        if k == 'mask':
            or_mask, and_mask = get_masks(v)
        else:
            int_v = int(v)
            int_v |= or_mask
            int_v &= and_mask
            
            k += (' = %d' % int_v)
            exec(k)

    return sum([int(v) for v in mem.values() if int(v) != 0])


def get_masks(v):
    or_mask  = int(''.join(['1' if x == '1' else '0' for x in v]), 2)
    and_mask = int(''.join(['0' if x == '0' else '1' for x in v]), 2)

    return or_mask, and_mask


def part2(data):
    mem = {}
    cur_mask = None    

    for (k, v) in data:
        if k == 'mask':
            cur_mask = v
        else:
            addr = int(re.match('mem\[(\d+)\]', k).groups()[0])
            addr_template, num_x = mask_addr(cur_mask, addr)
            all_addrs = get_all_addrs(addr_template, num_x)

            for a in all_addrs:
                mem[a] = int(v)

    return sum([v for v in mem.values() if v != 0])


def get_all_addrs(addr, num_x):
    addrs = []
    for replacements in product('10', repeat=num_x):
        addrs.append(int(addr.format(*replacements), 2))

    return addrs


def mask_addr(mask, addr):
    addr_bin_str = '{:036b}'.format(addr)
    num_x = 0
    addr_template = ''

    for (m, a) in zip(mask, addr_bin_str):
        if m == 'X':
            num_x += 1
            addr_template += '{}'
        elif m == '1':
            addr_template += '1'
        else:
            addr_template += a

    return addr_template, num_x


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
