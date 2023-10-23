#!/usr/bin/env python3
import sys
import re



# This script will take an input fasta file and 
# Divide the sequence into fragments of the appropriate length 
# Regardless of the presence of new line characters


try:
	fasta_file=sys.argv[1]
	length=sys.argv[2]
	
	if len(sys.argv) > 3:
		raise IndexError("More than two inputs - this script takes only one input...")

except IndexError:
	print("Please provide two inputs = one fasta file and a length")
	sys.exit()


#Make function that takes any input string and formats it correctly:
def custom_DNA_string(user_DNA_string, line_length):
	user_DNA_string = user_DNA_string.replace('\n','')
	new_DNA_string = '' 
	my_regex = r'.{1,' + line_length + r'}'
	sixties=re.findall(my_regex, user_DNA_string)
	new_string='\n'.join(sixties)
	return new_string

try:
	my_fasta=open(fasta_file, 'r')

#Also want an error if the file cannot be found when we try to read it - going to access the error object and print
#The message in this case
except IOError as ex:
	print(f"Can't find file: {fasta_file} : {ex.strerror}")
	sys.exit()

#initialize string
dna_string=''
gene_name=''
#Iterate through each line in FASTA file
for line in my_fasta:
	line=line.rstrip()
	#If the line starts with >, all we want from it is the gene name - and we want it to add to the dict as a key
	if line.startswith('>'):
		#finding instances where the start of the line has a > followed by one or more word chars until a space
		#For these instances, we are going to add to our dict with the gene names as keys and add empty dicts as values
		#gene_name = gene_name.group(1)
		if dna_string:
			print(f'>{gene_name}')
			print(custom_DNA_string(dna_string,length))
		dna_string=''
		gene_name = re.search(r"^>(\w+)",line)				
		gene_name = gene_name.group(1)	
	else:
		#This applies to any lines that do not start with > - so any lines between the > lines
		dna_string+=line
print(f'>{gene_name}')
print(custom_DNA_string(dna_string,length))

#	print(custom_DNA_string(dna_string, length))

my_fasta.close()

