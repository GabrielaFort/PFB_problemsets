#!/usr/bin/env python3
import sys
import re

input_file = sys.argv[1]

#First what I am doing is reading in this file and reporting every line and position in which nobody is found

#read in the file into a string per line
count = 1
with open(input_file, 'r') as file:
	for line in file:
		line=line.rstrip()
		for nobody in re.finditer(r'Nobody',line):
			start = nobody.start() + 1
			print(f'Line: {count}, Start of Nobody: {start}')	
			count += 1



#Next I am going to address question 2, which wants me to substitute every occurance of nobody with another name
with open(input_file, 'r') as file_read, open('Kayla.txt', 'w') as file_write:
	for line in file_read:
		line=line.rstrip()
		new_line = re.sub(r'Nobody', 'Kayla',line)
		file_write.write(f'{new_line}\n')
		



