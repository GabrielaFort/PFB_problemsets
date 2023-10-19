#!/usr/bin/env python3

input_string = input('Please input a list:\n')

input_list=input_string.split(',')

print('Printing only even members of the input list:')
for number in input_list:
	if int(number) % 2 == 0:
		print(number)

sorted_list=sorted(input_list)
print(f'The sorted input list looks like this:\n{sorted_list}')


evens=0
odds=0

for number in sorted_list:
	print(number)
	if int(number) % 2 == 0:
		evens += int(number)
	else:
		odds += int(number)

print(f'Sum of even numbers: {evens}')
print(f'Sum of odd numbers: {odds}')
