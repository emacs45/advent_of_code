def part1(l, w, h):

    sum = 0

    side1 = l * w
    side2 = w * h
    side3 = h * l
    smallest_side = min(side1, side2, side3)

    sum += 2 * side1 + 2 * side2 + 2 * side3 + smallest_side

    return sum

def part2(l, w, h):

    vol = l * w * h
    scopes = [2 *(l + w), 2 * (w + h), 2 * (h + l)]

    return min(scopes) + vol

sum = 0
total_ribbon = 0

with open ('input.txt') as input:
    input = input.read().strip().split('\n')

    for line in input:
        dimensions = list(map(int, line.split('x', maxsplit=2)))
        l, w, h = dimensions
        sum += part1(l, w, h)
        total_ribbon += part2(l, w, h)


    print(sum, total_ribbon)