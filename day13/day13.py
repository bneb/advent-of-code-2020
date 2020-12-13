'''Day 13 of Advent of Code 2020

The prompt is about a transportation time table with input like
t
b1,x,b2...

- t is the time you arrive at the terminal
- bn is bus n
- for part 2, the index of the bus in that list is the offset
'''

from argparse import ArgumentParser
from pathlib import PurePath
import time

def main(file_path):
    '''Parse data, compute solutions, and print them (with run time)
    '''
    with open(file_path, 'r') as f:
        t = int(f.readline())
        buses = {int(b):i for i, b in enumerate(f.readline().split(',')) if b != 'x'}

    t0 = time.process_time()
    solution = part1(t, buses.keys())
    t1 = time.process_time()
    print("Day 13 Part 1 solution: {}".format(solution))
    print("Run time: {:.4f} ms".format((t1-t0)*1000))

    t0 = time.process_time()
    solution = part2(buses)
    t1 = time.process_time()
    print("Day 13 Part 2 solution: {}".format(solution))
    print("Run time: {:.4f} ms".format((t1-t0)*1000))


def part1(t, buses):
    '''Return the soonest time after t that a bus departs times its number
    '''
    bus = None
    soonest = None

    for b in buses:
        soonest_for_bus = b - (t % b)
        if soonest is None or soonest_for_bus < soonest:
            soonest = soonest_for_bus
            bus = b
    
    return bus * soonest


def part2(buses):
    '''Return the time that begins a run where
    each bus departs at an offset of its index
    '''
    buses = list(buses.items())

    # modulus is the step size, index is where to step from
    modulus, cur_time = buses[0]

    # we started with bus at bus_index 0, so now it's 1
    bus_index = 1

    while bus_index < len(buses):
        bus_modulus, bus_offset = buses[bus_index]

        if (cur_time + bus_offset) % bus_modulus == 0:
            # the time works, so accumulate the modulus
            modulus *= bus_modulus
            # move on to next bus
            bus_index += 1 
        else:
            # take a step
            cur_time += modulus 

    # the index satisfies all buses
    return cur_time
    

if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    args = parser.parse_args()

    main(args.f)
