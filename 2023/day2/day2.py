import re
import math

#Part 1

threshold = {'red': 12, 'green': 13, 'blue': 14}
sum = 0

with open ('input.txt') as input:

    games = input.read().strip().split('\n')

    for id, game in enumerate(games, start=1):

        for num, color in re.findall('(\d+) (red|green|blue)', game):
            if int(num) > threshold[color]:
                break
        else:
            sum += id

print(sum)

#Part 2

sum = 0

with open ('input.txt') as input:
    games = input.read().strip().split('\n')
    
    for id, game in enumerate(games, start=1):
        max_vals = {'red': 0, 'green': 0, 'blue': 0}
        
        for num, color in re.findall('(\d+) (red|green|blue)', game):
            max_vals[color] = max(max_vals[color], int(num))
        
        else:
            sum += math.prod(max_vals.values())


print(sum)