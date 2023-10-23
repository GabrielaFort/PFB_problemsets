#!/usr/bin/env python3
import re

def gc_content(dna_seq):
	dna_seq=dna_seq.upper()
	Gs = dna_seq.count('G')
	Cs = dna_seq.count('C')
	GC_content = (int(Gs) + int(Cs))/len(dna_seq)
	return GC_content

def get_reverse_complement(dna_seq):
	reverse_string = dna_seq[::-1]
	reverse_complement = reverse_string.upper().replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
	return reverse_complement
