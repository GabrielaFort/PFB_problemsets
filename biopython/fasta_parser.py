#!/usr/bin/env python3
import sys
import re 
from Bio import SeqIO

# This script will take an input file in fasta format and will generate:
	#### 1) Total # of sequences
   #### 2) Total # of nucleotides
   #### 3) Average length of sequences
   #### 4) Shortest sequence length
   #### 5) Longest sequence length
   #### 6) Average GC content 
   #### 7) Highest GC content 
   #### 8) Lowest GC content


input_fasta=sys.argv[1]

if len(sys.argv) != 2:
	print('This script takes one and only one input file!')
	sys.exit(1)

if not input_fasta.endswith(('.fa','.fasta')):
	print('Query file must end with .fa or .fasta and be in fasta format')
	sys.exit(2)

seq_list = []
NT_count = 0
GC_dict = {}

# Read in fasta file with biopython
for seq_record in SeqIO.parse(input_fasta, "fasta"):
	# Now we can access gene IDs in seq_record.id and sequences in str(seq_record.seq)
	seq_list.append(str(seq_record.seq))
	NT_count += len(str(seq_record.seq))
	
print(f'sequence count: {len(seq_list)}')
print(f'total number of nucleotides: {NT_count}')
print(f'average length: {NT_count/len(seq_list):.2f}')
print(f'shortest length: {len(min(seq_list, key=len))}')
print(f'longest length: {len(max(seq_list, key=len))}')
	
# Now iterate through this list of sequences to get a bunch of attributes of the input file!
# Initiating a dict to get GC content for every entry 
GC_list = []
total_GC = 0

for seq in seq_list:
	seq.upper()
	gandc_count = seq.count('G') + seq.count('C')
	GC_content = gandc_count/len(seq)
	GC_list.append(GC_content)
	total_GC += GC_content
	
average_GC = total_GC/len(seq_list)
	
print(f'average GC content: {average_GC:.2f}')
print(f'highest GC content: {max(GC_list):.2f}')
print(f'lowest GC content: {min(GC_list):.2f}')



