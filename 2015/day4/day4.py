import hashlib


def find_advent_coin(secret_key):
    number = 1

    while True:
        combined = secret_key + str(number)
        hash_result = hashlib.md5(combined.encode()).hexdigest()
        if hash_result.startswith('000000'):
            return number
        number += 1


input_key = 'iwrupvqb'
result = find_advent_coin(input_key)
print(result)
