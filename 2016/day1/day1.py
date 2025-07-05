def calculate_distances(instruction_line: str):
    instructions = instruction_line.strip().split(', ')


    x,y = 0,0
    facing = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1,0)]

    visited = set()
    visited.add((x,y))

    first_repeated_distance = None

    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])

        if turn == 'R':
            facing = (facing + 1) % 4
        elif turn == 'L':
            facing = (facing - 1) % 4

        dx, dy = directions[facing]

        for _ in range(steps):
            x += dx
            y += dy
            pos = (x, y)

            if first_repeated_distance is None:
                if pos in visited:
                    first_repeated_distance = abs(x) + abs(y)
                else:
                    visited.add(pos)
            
    final_distance = abs(x) + abs(y)
    return final_distance, first_repeated_distance
                

with open ('./day1/input.txt', 'r') as file:
    line = file.readline()

    dist1, dist2 = calculate_distances(line)

    print(f"Teil 1: Entfernung zur Endposition = {dist1} Blöcke")
    print(f"Teil 2: Entfernung zur ersten doppelt besuchten Position = {dist2} Blöcke")

