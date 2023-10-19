#!/usr/bin/env python3

print('This script will take a number n as input and use list comprehension (not a for loop) to make a list with every number between 1 and n')

input_number = int(input('Please input a number:'))

number_list = [number for number in range(input_number+1)]

#This will include zero , so going to remove that from our output list....
number_list.pop(0)

print(number_list)
