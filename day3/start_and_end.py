#!/usr/bin/env python3

import sys

print('This script will take two inputs, and print numbers occuring between and including the two numbers')

num_1=int(sys.argv[1])
num_2=int(sys.argv[2])

count = num_1

if num_1 > num_2:
	print('Please make sure your first number is smaller than your second!')
	exit()

print('Starting by printing all numbers')
while count <= num_2:
	print(count)
	count += 1


new_count = num_1

print('Now will only print odd numbers!')
while new_count <= num_2:
	if new_count % 2 == 1:
		print(new_count)
	new_count += 1
