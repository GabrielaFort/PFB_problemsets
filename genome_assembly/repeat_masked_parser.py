#!/usr/bin/env python3

import sys 
import re

### Usage: This script will take an input soft-masked fasta file
### It will return: 1) Number of contigs, 2) Nucleotide content (both masked and unmasked), 3) Proportion of genome comprised ot gaps (N's)

fasta_file = sys.argv[1]

contig_fasta = open(fasta_file, 'r')

if len(sys.argv) != 2:
	print("Please enter one and only one fasta file")
	sys.exit(1)
if not fasta_file.endswith(('.fa','.fasta','.fna')):
	print("Query file must end with .fa or .fasta or .fna and be in fasta format")

contigs = []
contig = ''
#Make list of contigs
for line in contig_fasta:
	line=line.rstrip()
	if line.startswith('>'):
		if contig:
			contigs.append(contig)
		contig=''
	else:
		contig+=line
contigs.append(contig)
#Report number of contigs
num_contigs = len(contigs)

#Make string of all contigs
contig_string = ''.join(contigs)

#Make dictionary of counts of all the unique nts in the contig string
unique_nts = set(contig_string)
unique_dict = {}
for nt in unique_nts:
	nt_count = contig_string.count(nt)
	unique_dict[nt] = nt_count

# Now make another dict that has proportions out of total for each nt
proportion_dict = {}
for nt in unique_dict:
	nt_proportion = unique_dict[nt]/(len(contig_string))
	proportion_dict[nt] = nt_proportion

print(f'_______________________________________________________\n')
print(f'The number of contigs in the input file is: {num_contigs}\n')

print(f'The number of each nucleotide is:')
for nt in unique_dict:
	print(f'{nt}: {unique_dict[nt]}')

print(f'\nThe proportion of each nucleotide is:')
for nt in proportion_dict:
	print(f'{nt}: {proportion_dict[nt]}')

print(f'________________________________________________________\n')	


contig_fasta.close()
