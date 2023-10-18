#!/usr/bin/env python3
import sys

input_string = sys.argv[1]

print("This script will take as input any string of nucleotides and count the number of each base, irregardless of case")

Number_of_As = input_string.count('A') + input_string.count('a') 
Number_of_Cs = input_string.count('C') + input_string.count('c')
Number_of_Gs = input_string.count('G') + input_string.count('g')
Number_of_Ts = input_string.count('T') + input_string.count('t')

print(f"Your sequence contains {Number_of_As} As, {Number_of_Cs} Cs, {Number_of_Gs} Gs, and {Number_of_Ts} Ts!") 




