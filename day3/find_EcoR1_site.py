#!/usr/bin/env python3

print('This script will take an input DNA sequence, and output the starting and ending positions of an EcoR1 site\nif no site is found it will give an error')

input_string = input("Please input a DNA sequence:\n")

#This will report the starting position of an EcoR1 site
#If not found it will be -1
eco_site = input_string.upper().find('GAATTC')

start_position = eco_site + 1 
end_position = eco_site + 6

if eco_site != -1:
	print(f'EcoR1 startPos:{start_position} endPos:{end_position}')
else:
	print('There was no EcoR1 site found within this sequence')



