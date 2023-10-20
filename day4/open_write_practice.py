#!/usr/bin/env python3
import sys

print('This script will take a file, will uppercase each line, and will print the output to the screen...')
print('The script will then do this again and write the contents to a new file...')

input_file=sys.argv[1]

#if you put in no files as an input or more than one youll get this error and the script will terminate...
if len(sys.argv) != 2:
	print('please input one file')
	sys.exit()


with open(input_file,'r') as seq_read:
	for line in seq_read:
		#For every line in the input file...
		line=line.rstrip().upper()
		#Make it uppercase and strip white space...
		#And print to screen...
		print(line)

#Now I'm going to do the same thing but I'll write the output to a new file instead of printing on screen...
#This is more complicated because I need to set up a file to write to and read from
with open(input_file,'r') as seq_read, open('Python_06_uc.txt','w') as seq_write:
	for line in seq_read:
		line=line.rstrip().upper()
		seq_write.write(f'{line}\n')
