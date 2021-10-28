#!/usr/bin/python3

### cm-to-ft-in: Converts CM to feet and inches.

from sys import argv

if len(argv) != 2:
    print('Usage: {} CM'.format(argv[0]))
    exit(1)

try:
    cm = float(argv[1])
except:
    print('0\'0"')
    exit(0)

feet = int(cm / 30.48)
inches = cm % 30.48 / 2.54

# Truncate the number, rather than round it up
x = str(inches).split('.')
inches = float(x[0]) + float (x[1][:1]) / 10

print('%d\'%1g"' % (feet, inches))
