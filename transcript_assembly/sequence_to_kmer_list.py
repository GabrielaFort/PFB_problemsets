#!/usr/bin/env python3

import sys
import subprocess
import os

## method: sequence_to_kmer_list(sequence, kmer_length)
##
##  Extracts all kmers of a specified length from a sequence
##
##  ie.  sequence: GATCGATCGATCGA
##   and given kmer_length = 4
##   would yield
##                 GATC
##                  ATCG
##                   TCGA
##                    .... and so forth
##                       
##  input parameters:
##
##  seuqence : nucleotide sequence (type: string)
##
##  returns kmer_list : list of kmer sequences.
##                    ie.  ["GATC", "ATCG", ...]


def sequence_to_kmer_list(sequence, kmer_length):
	kmers_list = []
	kmer_length = int(kmer_length)
	for NT in sequence:
		#This will only be executed at beginning of the string
		if len(kmers_list) == 0:
			kmers_list.append(sequence[0:kmer_length])
			start_count = 1
		else:
			while len(sequence[start_count:(start_count+kmer_length)]) == kmer_length:
				kmers_list.append(sequence[start_count:(start_count+kmer_length)])
				start_count += 1
	return kmers_list



def main():

	progname = sys.argv[0]
    
	usage = "\n\n\tusage: {} sequence kmer_length\n\n\n".format(progname)
    
	if len(sys.argv) < 3:
		sys.stderr.write(usage)
		sys.exit(1)

    # capture command-line arguments
	sequence = sys.argv[1]
	kmer_length = int(sys.argv[2])

	kmers  = sequence_to_kmer_list(sequence, kmer_length)

	print(kmers)

	sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
	main()

			

