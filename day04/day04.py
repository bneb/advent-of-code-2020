'''Day 04 of Advent of Code 2020

The prompt is to process groups (separated by two newlines) of key-value-pairs
to count the number of valid groups.

In part 1, a valid group has all keys present except cid.
'''

from argparse import ArgumentParser
from pathlib import PurePath
import re

PATTERN = '(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([^\s]+)[\s\n]?'


def main(data, part):
    '''Given some data, return the number of valid 'passports'.
    '''
    # return sum([1 for passport in data if validate(passport, part)])
    count = 0
    for passport in data:
        if validate(passport, part):
            count += 1

    return count


def validate(passport, part):
    fields = dict(re.findall(PATTERN, passport))

    # For part 1, a passport is invalid if anything other than cid is missing
    if len(fields) < 7 or (len(fields) == 7 and 'cid' in fields):
        return False

    if part == 2:
        return check_fields(fields)

    return True


def check_fields(fields):
    '''Given a dictionary of passport fields perform validation on field values.
    
    Rules:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
        hgt See validate_height function
    '''
    try:
        height, units = re.match('(\d+)(cm|in)', fields['hgt']).groups()
    except:
        return False
    
    return (
        validate_year(fields['byr'], 1920, 2002) and
        validate_year(fields['iyr'], 2010, 2020) and
        validate_year(fields['eyr'], 2020, 2030) and
        validate_height(height, units) and
        validate_regex('^#[0-9a-f]{6}$', fields['hcl']) and
        validate_regex('^(amb|blu|brn|gry|grn|hzl|oth)$', fields['ecl']) and
        validate_regex('^\d{9}$', fields['pid'])
    )


def validate_year(year, start, stop):
    return start <= int(year) <= stop


def validate_height(height, units):
    '''Validate the height according to two rules:

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    '''
    return (
       (units == 'cm' and 150 <= int(height) <= 193) or
       (units == 'in' and 59 <= int(height) <= 76)
    )


def validate_regex(pattern, field):
    return re.match(pattern, field) is not None


if __name__ == '__main__':
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-f', type=PurePath, help='the input file')
    parser.add_argument('-p', type=int, default=1, help='which part to solve')
    args = parser.parse_args()

    with open(args.f, 'r') as f:
        # Distinct passport records are separated by two newlines
        data = f.read().split("\n\n")

    part = args.p
    solution = main(data, part)

    print("Day 04 Part {} solution: {}".format(part, solution))
