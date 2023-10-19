#!/usr/bin/env python3

print('This script will take an input string of nucleotides, report all unique characters, count the number of each and store these counts in a dictionary')

input_string = input('Please enter a string of nucleotides:')
input_string = input_string.upper()
input_set = set(input_string)

#Make empty dictionary 
nt_counts={}
GC_count=0
#Set up for loop that will count each NT in the original list (regardless of case) - and then will write to a dictionary
for nt in input_set:
	#Counting each unique nt within original list
	if nt == 'G' or nt == 'C':
		GC_count+=input_string.count(nt)
	count = input_string.count(nt)
	#Add the count to our growing dictionary
	nt_counts[nt] = count

print(nt_counts)
print(f'The GC content of this sequence is: {GC_count/len(input_string)}')

