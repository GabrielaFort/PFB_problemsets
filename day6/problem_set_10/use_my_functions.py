#!/usr/bin/env python3

import sys
from my_functions import gc_content, get_reverse_complement

# This script will use functions found in the my_functions.py script
# It will take an input dna sequence and utilize both of these functions to return the GC content and the rev complement

dna_seq = sys.argv[1]

gc_content=gc_content(dna_seq)
reverse_comp = get_reverse_complement(dna_seq)

print(f'The input sequence is: {dna_seq}')

print(f'The GC content of this sequence is:\n{gc_content}')
print(f'The reverse complement of this sequence is:\n{reverse_comp}')
