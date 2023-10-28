#!/usr/bin/env python

import os, sys

from sequence_to_kmer_list import *
from fastq_file_to_sequence import *


## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }


def count_kmers(kmer_list):
	kmer_count_dict = {}
	for kmer in kmer_list:
		#If the kmer isnt in the dict, add it and start count at 1 
		if not kmer in kmer_count_dict:
			kmer_count_dict[kmer] = 1
		else:
			#could also do kmer_count_dict[kmer] += 1
			previous_count = kmer_count_dict[kmer]
			new_count = previous_count + 1
			kmer_count_dict[kmer] = new_count 		

	return kmer_count_dict


def main():
	progname = sys.argv[0]
	usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(progname)

	if len(sys.argv) < 4:
		sys.stderr.write(usage)
		sys.exit(1)

    # capture command-line arguments
	fastq_filename = sys.argv[1]
	kmer_length = int(sys.argv[2])
	num_top_kmers_show = int(sys.argv[3])

	seq_list = seq_list_from_fastq_file(fastq_filename)

	all_kmers = []
	# This should return a long list of every kmer in any read!	
	for seq in seq_list:
		kmer_list = sequence_to_kmer_list(seq, kmer_length)
		for kmer in kmer_list:
			all_kmers.append(kmer)
	
	kmer_count_dict = count_kmers(all_kmers)  # see step 2 above. You implement this. :-)
	
	sorted_kmer_list = sorted(kmer_count_dict.items(), key=lambda x:x[1], reverse=True)
	sorted_kmer_dict = dict(sorted_kmer_list)
	
	unique_sorted_kmers = list(sorted_kmer_dict.keys())

	top_kmers_show = unique_sorted_kmers[0:num_top_kmers_show]

	for kmer in top_kmers_show:
		print("{}: {}".format(kmer, sorted_kmer_dict[kmer]))

	sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
	main()

