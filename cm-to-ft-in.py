#!/usr/bin/python3

### cm-to-ft-in: Converts CM to feet and inches.

from sys import argv

def cm_to_feet_inches(cm):
    feet = int(cm // 30.48)
    inches = (cm % 30.48) / 2.54
    inches = int(inches)  # Truncate inches
    
    return feet, inches

if len(argv) != 2:
    print(f'Usage: {argv[0]} CM')
    exit(1)

try:
    cm = float(argv[1])
except ValueError:
    print("0'0\"")
    exit(0)

feet, inches = cm_to_feet_inches(cm)

if inches:
    print(f"{feet}'{inches}\"")
else:
    print(f"{feet}'")
