def getCalib(content):
    
    digits = []

    for char in content:
        if char.isdigit():
            digits.append(char)

    if digits:
        return int(digits[0] + digits[-1])
    else: return 0
#Part 1
result = 0

with open ('input.txt', 'r') as f:
    for line in f: 
        result += getCalib(line)

print(result)

#Part 2
result = 0
digits = {'zero': 'zero0zero', 'one': 'one1one', 'two': 'two2two', 
          'three': 'three3three', 'four': 'four4four', 'five': 'five5five', 
          'six': 'six6six', 'seven': 'seven7seven', 'eight': 'eight8eight', 
          'nine': 'nine9nine'
        }

with open ('input.txt', 'r') as file:
    for line in file:
        for key, value in digits.items():
            line = line.replace(key, value)

        result += getCalib(line)

print(result)