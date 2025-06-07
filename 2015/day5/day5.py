#!/usr/bin/env python3

import re


def find_nice_string(input_data):

    count = 0
    lines = input_data.split('\n')

    for line in lines:

        if re.search(r'ab|cd|pq|xy', line):
            pass

        elif not re.search(r'(.)\1', line):
            pass

        elif len(re.findall(r'[aeiou]', line)) < 3:
            pass

        else:
            count += 1

    return count


def find_nicer_string(input_data):

    count = 0
    lines = input_data.split('\n')

    for line in lines:

        if not re.search(r'(..).*\1', line):
            pass

        elif not re.search(r'(.).\1', line):
            pass

        else:
            count += 1

    return count


with open('input.txt') as file:
    input_data = file.read().strip()


part1 = find_nice_string(input_data)
part2 = find_nicer_string(input_data)
print(part1, part2)
