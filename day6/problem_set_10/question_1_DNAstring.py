#!/usr/bin/env python3
import sys
import re

# This script will take an input DNA sequence string and 
# Divide the sequence into fragments of the appropriate length 
# Regardless of the presence of new line characters

try:
	DNA_string=sys.argv[1]
	length=sys.argv[2]
	
	if len(sys.argv) > 3:
		raise IndexError("More than two inputs - this script takes only one input...")

except IndexError:
	print("Please provide two inputs = one dna string and a length")
	sys.exit()


#Make function that takes any input string and formats it correctly:
def custom_DNA_string(user_DNA_string, line_length):
	user_DNA_string = user_DNA_string.replace('\n','')
	new_DNA_string = '' 
	my_regex = r'.{1,' + line_length + r'}'
	sixties=re.findall(my_regex, user_DNA_string)
	new_string='\n'.join(sixties)
	return new_string

print(custom_DNA_string(DNA_string,length))





