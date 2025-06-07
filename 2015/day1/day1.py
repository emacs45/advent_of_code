sum = 0
position = 0

with open ('input.txt') as input:
    input = input.read().strip().split('\n')

    for lines in input:
        for pos, line in enumerate(lines, start=1):
            sum += line.count('(') + (-line.count(')'))
            if sum < 0:
                position = pos
                break

print(sum, position)
