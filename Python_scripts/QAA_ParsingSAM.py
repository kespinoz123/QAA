#!/bin/env python3.10

import argparse
import re

def get_args():
	parser = argparse.ArgumentParser(description="A program to introduce yourself")
	parser.add_argument("-f", "--file", help="File name")
	parser.add_argument("-o", "--output", help="Ouput File")
	return parser.parse_args()
args=get_args()


number_mapped = 0
number_unmapped = 0
number_reads = 0
with open(args.file, 'r') as fh:
	for line in fh:
		# if not line.startswith("@"):
		if line[0] != '@':
			number_reads += 1
	
			#split first and then specify index 
			line = line.split('\t')
			flag = int(line[1])
					#----checking for secondary alignment, so we have to verify 256 -----
					#reasong being;
					#You may encounter each read in a file more than once. 
					#This will occur when you have multiple alignments for a single read. 
					#You should be careful not to count reads as aligned more than once.
			#not equal to 256
			
			if((flag & 256) != 256):
				#Primary alignment 
				#not equal to 4
				if((flag & 4) == 4):
					number_unmapped += 1
					
				else:
					number_mapped +=1
					
print("Number mapped: ", number_mapped)
print("Number unmapped: ",number_unmapped)
print("Number of reads: ",number_reads)






