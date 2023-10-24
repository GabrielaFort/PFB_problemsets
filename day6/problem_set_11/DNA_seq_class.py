#!/usr/bin/env python3

# I am making a new class containing a sequence, its name, and its organism of origin

class DNASequence(object):
	
	# Defining class attributes
	def __init__(self, sequence, name, organism):
		self.sequence = sequence
		self.name = name
		self.organism = organism

	# Defining methods for this class
	def sequence_length(self):
		length = len(self.sequence)
		return length


	def NT_comp(self):
		uppercase_seq = self.sequence.upper()
		NT_dict = {}
		for NT in uppercase_seq:
			if NT not in NT_dict:
				NT_dict[NT] = 1
			else:
				new_count = NT_dict[NT] + 1
				NT_dict[NT] = new_count
		#This is fine but I kind of want the composition in percent of each NT.
		#Going to replace the keys of this dict with the percent 
		seq_length = len(self.sequence)
		comp_dict = {}
		for base in NT_dict:
			comp_dict[base] = (NT_dict[base]/seq_length)	
		# Return a dict with composition of each NT in the original sequence
		return comp_dict

	def GC_content(self):
		uppercase_seq = self.sequence.upper()
		GC_number = uppercase_seq.count('G') + uppercase_seq.count('C')
		proportion_GC = GC_number/(len(self.sequence))
		return proportion_GC	

	def FASTA_format(self):
		fasta_string = f'>{self.name} {self.organism}\n{self.sequence}'
		return fasta_string 


### Now I'm going to write code that demonstrates the initiation and usage of this class
# Could also take user input to specify class inputs - or could use this within other scripts

# Creating a new DNASequence object with user input
DNASeq_object = DNASequence('AATcGTTGG','HNF4A','Mus musculus')

# Print sequence attributes
print(f'__________________________________________________\n')
#Print sequence
print(f'The sequence of my gene is: {DNASeq_object.sequence}')
# Print name
print(f'The name of my gene is: {DNASeq_object.name}')
# Print organism
print(f'The species of my gene is: {DNASeq_object.organism}')

# Use list sequence_length method to report length of sequence
print(f'\n\nThe length of my sequence is: {DNASeq_object.sequence_length()}\n\n')

# Use NT_comp method to report composition of each NT in seq
print(f'The NT composition of my sequence is:')
composition = DNASeq_object.NT_comp()
for base in composition:
	print(f'{base}:  {composition[base]}')

# Use GC_content method to report GC composition in seq
print(f'\n\nThe GC content of my sequence is: {DNASeq_object.GC_content()}')

# Use FASTA format method to report the object in fasta format
print(f'\n\nMy object in fasta format looks like this:\n{DNASeq_object.FASTA_format()}')

