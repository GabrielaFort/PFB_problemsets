#!/usr/bin/env python3

import sys 

print('This script will take an input string and do a bunch of things with it as per question 2 of problem set 4')

taxa=sys.argv[1]

print(f'Print Input String:\n{taxa}')
print(f'\nPrint First Index of Input String:\n{taxa[1]}')

print('\nNow, split the string up by comma into a list with different words as each list element:')
species = taxa.split(', ')
print(species)

print(f'\nPrinting first index of this new list:\n{species[1]}')

print(f'\nThe type of the new list:\n{type(species)}')

