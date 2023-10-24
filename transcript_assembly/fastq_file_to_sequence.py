#!/usr/bin/env python3

import os, sys
import subprocess

## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]
    
def seq_list_from_fastq_file(fastq_filename):
	seq_list = []

	#Would be nice to use awk to parse the fastq file and return the sequence lines...
	extract_seq = f"awk 'NR%4==2' {fastq_filename} > reads_only.fq" 	
	extract_seq_run = subprocess.run(extract_seq, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	if extract_seq_run.returncode !=0:
		print("File parsing failed")
		exit(1)
	
	fastq_file = open('reads_only.fq', 'r')
	for line in fastq_file:
		line=line.rstrip()
		seq_list.append(line)
	fastq_file.close()

	return seq_list




def main():
	progname = sys.argv[0]
    
	usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
	if len(sys.argv) < 3:
		sys.stderr.write(usage)
		sys.exit(1)

    # capture command-line arguments
	fastq_filename = sys.argv[1]
	num_seqs_show = int(sys.argv[2])

	seq_list = seq_list_from_fastq_file(fastq_filename)

	print(seq_list[0:num_seqs_show])

	sys.exit(0)  # always good practice to indicate worked ok!


# This means that this function main() will run if you are executing this script
# So when I execute this script - I can test out my function within - otherwise I'll just import the function within # Other scripts
if __name__ == '__main__':
    main()
