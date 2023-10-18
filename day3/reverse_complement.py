#!/usr/bin/env python3

print("This script will take a DNA sequence and generate a reverse complement sequence, regardless of case (it will, however, print any original lowercase as uppercase bases)")
 
input_string = input("Please input a DNA sequence:\n")

reverse_string = input_string[::-1]

reverse_complement = reverse_string.upper().replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
print(f'The reverse complement is:\n{reverse_complement}')

