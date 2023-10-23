#!/usr/bin/env python3
import sys
import re

# This is a script to practice exception handling 

# Throw and handle the exception:
	#If no input is provided
	#If the file cannot be opened
	#If the file does not end in .fasta or .fa or .nt
	#If a non ATGCN character is found in the sequence
		# I cant figure out how to do the last thing and have decided its probs not that important, oh well

# I could also mix in some logic here e.g. to say that if there's more than one file we only want one
#if len(sys.argv) > 2:
#	print(f'Please only enter a single file!')
#	sys.exit()

# In my try statement I am going to take an argument and read in the file
try:
	multi_fasta=sys.argv[1]
	print(f'User provided multi-FASTA file: {multi_fasta}')
	
	#opening file to see if file opens without errors
	FASTA_object = open(multi_fasta, 'r')
	
	#Here we raise an IndexError (don't think it matters what the error is as long as its one that exists)
	#We will also get an IndexError by default if there is no argument provided!
	if len(sys.argv) > 2:
		raise IndexError("Have only one name!") 

	#Here we raise a value error if the file name doesn't have the endings we want!
	if not multi_fasta.endswith('.fa') or multi_fasta.endswith('.nt') or multi_fasta.endswith('.fasta'):
		raise ValueError("Not a fasta file") 


#This means that there was an issue indexing the argv list OR that the length of sys.argv > 2:
except IndexError:
	print(f"Please provide one and only one file name!")
	sys.exit()

#Also want an error if the file cannot be found when we try to read it - going to access the error object and print
#The message in this case
except IOError as ex:
	#This time we also print the more specific error message
	print(f"Can't find file: {multi_fasta} : {ex.strerror}")
	sys.exit()

#Now we have that value error that i raised above - this is sorta custom and refers to the ending of the filename
except ValueError:
	print("File needs to be in FASTA format and end with .fasta or .fa or .nt")
	sys.exit()
FASTA_object.close()



# Now we are going to move on with our task (from question 1 of the previous problem set)
# But we are going to add another try statement that will send a message if our sequences
# contain something other than an ATGCN


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



















