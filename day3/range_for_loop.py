#!/usr/bin/env python3

print('This script will take an input number n and print out every number between 1 and n')

input_number = int(input('Please input a number:'))

for number in range(input_number+1):
	if number > 0:
		print(number)

