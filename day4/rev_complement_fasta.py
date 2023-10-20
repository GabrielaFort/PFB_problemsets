#!/usr/bin/env python3
import sys

input_file = sys.argv[1]

# This script addresses python 6 problem set question #7
print('This script will take an input fasta file, find the reverse complement of each sequence, and return a new file')

#Making a reverse complement function to return the reverse complement of an input string 
def reverse_complement(seq_string):
	reverse_string = seq_string[::-1]
	reverse_complement = reverse_string.upper().replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
	return reverse_complement

#Now im going to make a dictionary with key value pairs with the gene id and sequence from the fasta formatted file

#first make empty dictionary 
fasta_dict={}
#open the input file, then open a file that im going to write my rev complement sequences to:
with open(input_file, 'r') as seq_read, open('reverse_transcribed.fasta', 'w') as seq_write:
	#for line in the original file:
	for entry in seq_read:
		#get rid of the stupid new lines that print adds when we read in a string
		entry = entry.rstrip()
		#string.split() is a string method that will split your string on whatever is in () and make a list
		#Here we are going to split on tab characters beacause there are tabs separating gene and seq in this file 
		gene_id,seq = entry.split('\t')	
		#now we built our dictionary, one line at a time...
		fasta_dict[gene_id] = seq
	
# Now I need to iterate through all my values of this dictionary, and run the function I made above
	for gene in fasta_dict:
		#Write the gene name (dict key) and the reverse complement of the sequence to a new file (sep by tab) 
		seq_write.write(f'>{gene}\t{reverse_complement(fasta_dict[gene])}\n')








