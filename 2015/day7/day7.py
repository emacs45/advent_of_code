import re

# Funktion, die die Anweisungen verarbeitet
def evaluate_instructions(instructions):
    # Speichert die Signale der Kabel
    signals = {}
    
    # Hilfsfunktion, um den Wert eines Kabels oder einer Zahl zu erhalten
    def get_value(x):
        if x.isdigit():  # Falls x eine Zahl ist, direkt zurückgeben
            return int(x)
        elif x in signals:  # Falls x ein bereits berechnetes Signal ist, zurückgeben
            return signals[x]
        else:
            return None  # Falls x noch nicht bekannt ist
    
    # Schleife solange Anweisungen vorhanden sind
    while instructions:
        remaining = []  # Liste für nicht bearbeitete Anweisungen
        
        # Jede Anweisung verarbeiten
        for instruction in instructions:
            # Zerlegt die Anweisung in die Teile links und rechts von " -> "
            left, target = instruction.split(" -> ")
            parts = left.split()
            
            if len(parts) == 1:  # Anweisung wie "123 -> x" oder "dy -> er"
                value = get_value(parts[0])
                if value is not None:
                    signals[target] = value
            
            elif len(parts) == 2:  # Anweisung wie "NOT dy -> er"
                op, arg = parts
                value = get_value(arg)
                if value is not None:
                    signals[target] = ~value & 0xFFFF  # 16-bit Komplement
            
            elif len(parts) == 3:  # Anweisung wie "dy RSHIFT 2 -> er" oder "dy AND iu -> er"
                a, op, b = parts
                val_a = get_value(a)
                val_b = get_value(b)
                
                if val_a is not None and val_b is not None:
                    if op == "AND":
                        signals[target] = val_a & val_b
                    elif op == "OR":
                        signals[target] = val_a | val_b
                    elif op == "LSHIFT":
                        signals[target] = val_a << val_b
                    elif op == "RSHIFT":
                        signals[target] = val_a >> val_b
            
            # Falls die Anweisung nicht ausgeführt werden konnte, bleibt sie bestehen
            if target not in signals:
                remaining.append(instruction)
        
        # Wenn keine Anweisungen mehr übrig sind, ist die Berechnung abgeschlossen
        if not remaining:
            break
        
        # Aktualisiere die Liste der verbleibenden Anweisungen
        instructions = remaining
    
    return signals

# Beispielinput (ersetze dies durch deinen tatsächlichen Input)
with open('./input.txt') as file:
    input_data = file.read().strip()

# Input bereinigen und in eine Liste von Anweisungen umwandeln
instructions = input_data.strip().splitlines()

# Anweisungen auswerten
result = evaluate_instructions(instructions)

# Signal des Kabels 'a' anzeigen (falls vorhanden)
print("Signal an Kabel 'a':", result.get('a', 'Kabel nicht vorhanden'))
