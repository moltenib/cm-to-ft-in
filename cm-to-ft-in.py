#!/usr/bin/python3

### cm-to-ft-in: Converts CM to feet and inches.

from sys import argv

def usage(err_code):
    print('Usage: {} CM'.format(argv[0]))
    exit(err_code)

if len(argv) != 2:
    usage(1)

try:
    a = int(argv[1])
except:
    usage(2)

feet = a / 30.48
inches = a % 30.48 / 2.54

x = str(inches).split('.')
inches = float(x[0]) + float (x[1][:1]) / 10

print('%d\'%1g"' % (feet, inches))
