#!/usr/bin/env python3
import sys
import re 

# This script will find and print all FASTA header lines in a FASTA file to STDOUT
# It will then extract the sequence name and discription if there is a match and will print that info 

input_fasta = sys.argv[1]

fasta_string=''
with open(input_fasta,'r') as fasta:
	for line in fasta:
		line=line.rstrip()
		for gene_name in re.findall(r'>\S+',line):
			gene=gene_name
			for gene_discription in re.findall(r'[ ][^\n]*',line):
				discription=gene_discription
				print(f'id:{gene}\tdesc:{discription}')

#fasta_string+=line

#gene_names=re.findall(r'>\S+',fasta_string)
#description=re.findall(r'[ ][^\n]*',fasta_string)
#print(gene_names)
#print(description)
#print("My header lines are:")
#for header in header_lines:
#	print(f'{header}')
  
