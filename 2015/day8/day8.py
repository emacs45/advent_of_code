with open('input.txt', 'r') as file:
    input_data = file.read().splitlines()

result = 0
encoded_length = 0

for line in input_data:
    # Part 1: Calculate the difference between code length and in-memory length
    result += len(line) - len(eval(line))  # eval interpretiert den String korrekt

    # Part 2: Encode the string and calculate the difference
    encoded = ''
    for char in line:
        if char == '\\':
            encoded += '\\\\'
        elif char == '\"':
            encoded += '\\\"'
        else:
            encoded += char

    # Surround the encoded string with additional quotes
    encoded = '\"' + encoded + '\"'
    encoded_length += len(encoded)

print(f'Part 1: {result}')
print(f'Part 2: {encoded_length - sum(len(line) for line in input_data)}')
