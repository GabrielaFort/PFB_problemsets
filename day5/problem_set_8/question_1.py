#!/usr/bin/env python3
import sys
import re

print('This script takes a fasta file as user input, calculates the NT composition from each sequence, and prints out a nice datastructure with all of the counts')

# Which exceptions do I want?
	#I need the user to input a file
	#I need the user to input only one file (i am using logic before my try statement to make sure)
	#I need that file to exist and be found by python
	#I need it to be in fasta format - i am going to handle this later on with logic


# I am also mixing in some logic here to say that if there's more than one file we only want one
if len(sys.argv) > 2:
	print(f'Please only enter a single file!')
	sys.exit()

# In my try statement I am going to take an argument and read in the file
try:
	multi_fasta=sys.argv[1]
	print(f'User provided multi-FASTA file: {multi_fasta}')
	
	FASTA_object = open(multi_fasta, 'r')

#This means that there was an issue indexing the argv list
except IndexError:
	print(f"Please provide a file name!")
	sys.exit()
#Also want an error if the file cannot be found when we try to read it - going to access the error object and print
#The message in this case
except IOError as ex:
	print(f"Can't find file: {multi_fasta} : {ex.strerror}")
	sys.exit()



# Now I know that the user has entered a single file and that it exists and can be read by python
# Moving on to the actual job

#Create empty dictionary
NT_counts={}

#Iterate through each line in FASTA file
for line in FASTA_object:
	line=line.rstrip()
	#If the line starts with >, all we want from it is the gene name - and we want it to add to the dict as a key
	if line.startswith('>'):
		#finding instances where the start of the line has a > followed by one or more word chars until a space
		gene_name = re.search(r"^>(\w+)",line)
		#For these instances, we are going to add to our dict with the gene names as keys and add empty dicts as values
		gene_name = gene_name.group(1)
		NT_counts[gene_name] = {'A':0,'T':0,'C':0,'G':0}
		dna_string=''
		
	else:
		#This applies to any lines that do not start with > - so any lines between the > lines
		for NT in NT_counts[gene_name]:
			NT_counts[gene_name][NT] += line.count(NT)

#We have our listed dictionary constructed - now print it out in a nice way
for name in NT_counts:
	for NT in NT_counts[name]:
		count = NT_counts[name][NT]
		print(f'{name}\t{NT}\t{count}')
	print('\n')


FASTA_object.close()
