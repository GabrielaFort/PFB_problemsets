#!/usr/bin/env python3
import sys

input_string = sys.argv[1]

print('This script will take a DNA sequence as input and will output the AT and GC content of that sequence, regardless of case')

AT_content = (input_string.upper().count('A') + input_string.upper().count('T')) / len(input_string)
GC_content = (input_string.upper().count('G') + input_string.upper().count('C')) / len(input_string)

print(f'''The AT_content of your input sequence is: {AT_content}
The GC_content of your input sequence is: {GC_content}''')
