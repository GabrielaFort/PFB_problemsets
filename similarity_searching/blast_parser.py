#!/usr/bin/env python3
import os 
import sys

# This script takes an input path to a directory containing files with # blast outputs 
# It will parse the first hit in each file and report some stats

# The output files were generated using blastp -outfmt 7 OR ssearch -m8c fields

input_dir = sys.argv[1]

# Initiate empty dictionary to store data
file_dict = {}

# iterate through files - need absolute path as input
for file in os.listdir(input_dir):
  # Initate directoy as a key for each of the matrices
  file_dict[file] = {"id":"","alen":"","eval":""}
  with open(f'{input_dir}/{file}', 'r') as file_obj:
    for line in file_obj:
      line=line.rstrip()
      # If not a header line, split on tabs
      if not line.startswith('#'):
        tab_list = line.split('\t')
        file_dict[file]['id'] = tab_list[2]
        file_dict[file]['alen'] = tab_list[3]
        file_dict[file]['eval'] = tab_list[-2]
        break

# Print table of results
print(f"Matrix\t   ID\t   alen\t  eval")
for matrix in file_dict:
  print(f"{matrix[0:-4]}\t  {file_dict[matrix]['id']}\t  {file_dict[matrix]['alen']}\t  {file_dict[matrix]['eval']}")
  

