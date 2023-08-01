#!/usr/bin/env python
import argparse

def get_args(): #set variables in argparse to get input from command line 
    parser = argparse.ArgumentParser(description="A program to assign variables for demultiplex, part 1")
    parser.add_argument("-l", "--length", help="sequence read length", required=True, type=int)
    parser.add_argument("-f", "--filename", help="name of input file", required=True, type=str)
    parser.add_argument("-o", "--output", help="output file name", required=True, type=str)
    return parser.parse_args()

args=get_args()
sequence_length=args.length
output_file=args.output
filename=args.filename

import bioinfo #import bioinfo module
import gzip #import gzip module to read unzipped files 
from matplotlib import pyplot as plt #import matplotlib to plot 

my_list=[] #create an empty list 
my_list=[0]*sequence_length #fill an empty list with the same number of zeros as the sequence line 
#num_lines=0 #initialize variable for the number of  lines 

i=0
with gzip.open(filename,"rt") as fh1: #open the file to read using gzip
    for line in fh1:
    #loop through the record
        line=line.strip("\n")
        if i%4==3: #get only the quality score line
            k=0
            #num_lines+=1
        
            for character in line:
                score=bioinfo.convert_phred(character)
                my_list[k]+=score
                k+=1
        i+=1
    
for k,value in enumerate(my_list):
    my_list[k]=my_list[k]/(i/4)

plt.bar(range(len(my_list)), my_list)
plt.title('Mean Q scores over Illumina Base Positions')
plt.xlabel('Base Positions')
plt.ylabel('Mean Q-score')
plt.savefig(f'{output_file}.png')