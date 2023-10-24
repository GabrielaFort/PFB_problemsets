#!/usr/bin/env python3

import sys
import re

# This script will take an input contig.fa file with contigs, and will return:
	# The number of contigs
	# The shortest contig
	# The longest contig
	# The total contig length
	# The L50 size
	# The N50 size

fasta_file = sys.argv[1]

contig_fasta = open(fasta_file, 'r')

if len(sys.argv) != 2:
	print('Please enter one and only one fasta file')
	sys.exit(1)

if not fasta_file.endswith(('.fa','.fasta')):
	print('Query file must end with .fa or .fasta and be in fasta format')
	sys.exit(3)

contigs = []
contig = ''

for line in contig_fasta:
	line=line.rstrip()
	if line.startswith('>'):
		if contig:
			contigs.append(contig)
		contig = ''				
	else:
		contig+=line
#This is so we get the last entry!
contigs.append(contig)

# Count total number of contigs
num_contigs = len(contigs)

# Report shortest and longest contigs
contig_length_list = []
for entry in contigs:
	contig_length_list.append(int(len(entry)))

shortest=min(contig_length_list)
longest=max(contig_length_list)

# Report total contig length
count = 0
for entry in contig_length_list:
	count += int(entry)
total_length = count

# N50 Size
# Sort list of contig lengths from largest to smallest
sorted_list = sorted(contig_length_list, reverse=True)
N50count = 0
for entry2 in sorted_list:
	if N50count < (total_length/2):
		N50count += entry2
	else:
		N50 = sorted_list[([entry2]+1)]
		break

# L50 Size
# Number of contigs that are as long or longer than N50 value
L50count = 0
for entry3 in sorted_list:
	if entry3 >= N50:
		L50count += 1
L50 = L50count

print(f'Number of contigs:\t{num_contigs}\nShortest contig:\t{shortest}\nLongest contig:\t{longest}\nTotal Contig Length:\t{total_length}\nN50:\t{N50}\nL50:\t{L50}')


contig_fasta.close()
