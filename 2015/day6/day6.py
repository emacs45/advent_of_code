#!/usr/bin/python3

import re

def draw_grid(default=1000):
    # Initialisiere das Gitter mit 0 (aus für Part 1, Helligkeit 0 für Part 2)
    return [[0] * default for _ in range(default)]

def read_instructions(input):
    # Liest die Anweisungen und extrahiert die benötigten Informationen
    lines = input.split('\n')
    instructions = []

    for line in lines:
        if re.search(r'turn on|turn off|toggle', line):
            nums = re.findall(r'\d+', line)
            nums = list(map(int, nums))
            instructions.append((line, nums))
    return instructions

def execute_instructions(grid, instructions, mode='part1'):
    # Führt die Anweisungen auf dem Gitter aus
    for instruction, coordinate in instructions:
        start_x, start_y = coordinate[0], coordinate[1]
        end_x, end_y = coordinate[2], coordinate[3]

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if mode == 'part1':
                    # Part 1: Ein/Aus-Schaltung
                    if 'turn on' in instruction:
                        grid[x][y] = 1
                    elif 'turn off' in instruction:
                        grid[x][y] = 0
                    elif 'toggle' in instruction:
                        grid[x][y] = 1 - grid[x][y]  # Umschalten von 0 auf 1 und umgekehrt

                elif mode == 'part2':
                    # Part 2: Helligkeitssteuerung
                    if 'turn on' in instruction:
                        grid[x][y] += 1
                    elif 'turn off' in instruction:
                        grid[x][y] = max(0, grid[x][y] - 1)  # Nicht unter 0
                    elif 'toggle' in instruction:
                        grid[x][y] += 2

def count_lights(grid):
    # Zählt die Anzahl der eingeschalteten Lichter (für Part 1)
    return sum(sum(row) for row in grid)

def calculate_total_brightness(grid):
    # Berechnet die Gesamthelligkeit (für Part 2)
    return sum(sum(row) for row in grid)

# Lese die Eingabedatei ein
with open('input.txt') as file:
    input_data = file.read().strip()

# Initialisiere das Gitter
grid = draw_grid()

# Lese und parse die Anweisungen
instructions = read_instructions(input_data)

# Wähle den Modus: 'part1' für Ein/Aus-Schaltung, 'part2' für Helligkeitsteuerung
mode = 'part2'

# Führe die Anweisungen aus
execute_instructions(grid, instructions, mode=mode)

# Berechne das Ergebnis basierend auf dem Modus
if mode == 'part1':
    result = count_lights(grid)  # Anzahl der eingeschalteten Lichter
else:
    result = calculate_total_brightness(grid)  # Gesamthelligkeit

print(result)