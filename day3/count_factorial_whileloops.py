#!/usr/bin/env python3

print('This script will take any number n and will print out numbers from 1-n and calculate the factorial of n')
input_number=int(input('Please input a number:'))

count=1
factorial=1

while count <= input_number:
	print('count:', count)
	factorial=factorial*count
	count+=1

print(f'The facorial of {input_number} is: {factorial}')
