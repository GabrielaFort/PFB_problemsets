#!/usr/bin/env python3
import sys

number = float(sys.argv[1])

print(f'This script will test the input number {number} for a variety of conditions')

 
if number > 0:
	print(f'{number} is positive')
	if number < 50:
		print(f'{number} is smaller than 50!')
		if number % 2 == 0:
			print(f"{number} is even and smaller than 50!")
	elif number > 50:
		print(f'{number} is larger than 50!')
		if number % 3 == 0:
			print(f'{number} is larger than 50 and divisible by 3!')
	else:
		print(f'{number} must be 50') 
elif number < 0:
	print(f'{number} is negative')

else:
	print(f'{number} must be zero!')

