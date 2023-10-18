#!/usr/bin/env python3


 
input_string = input("Please input a DNA sequence:\n")


substring=input_string[99:200]
G_count=substring.upper().count('G')


print(f'The substring from nucleotide #100 to nucleotide #200 is:\n{substring}')
print(f'The number of Gs (regardless of case) in this substring is:\n{G_count}')

