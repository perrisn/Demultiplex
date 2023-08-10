#!/usr/bin/env python

import argparse
import gzip

def get_args(): #set variables in argparse to get input from command line 
    parser = argparse.ArgumentParser(description="A program to assign variables for demultiplex, part 1")
    parser.add_argument("-i", "--index", help="indext text file path", required=True)
    parser.add_argument("-f1", "--file1", help="read1 file path", required=True)
    parser.add_argument("-f2", "--file2", help="index1 file path", required=True)
    parser.add_argument("-f3", "--file3", help="index2 file path", required=True)
    parser.add_argument("-f4", "--file4", help="read2 text file path", required=True)
    return parser.parse_args()

args=get_args()
R1=args.file1
R2=args.file2
R3=args.file3
R4=args.file4

#THESE ARE THE ACTUAL FILES,UNCOMMENT AND RUN FOR FINAL SUBMISSION
# R1="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz"
# R2="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz"
# R3="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz"
# R4="/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz"

#THESE ARE THE TEST FILES
# R1="/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_test_read1.fq"
# R2="/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_test_index1.fq"
# R3="/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_test_index2.fq"
# R4="/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_test_read2.fq"

R1_record_list=["","","",""] #initializing an empty list with 4 empty strings to hold each record file  
R2_record_list=["","","",""] 
R3_record_list=["","","",""]
R4_record_list=["","","",""]

def reverse_complement_func(seq):
    complement_base={'A':'T','T':'A','G':'C','C':'G','N':'N'} #creating a dictionary with complement bases
    reverse_sequence=seq[::-1] #reverse the input sequence
    rev_comp_seq="" #create empty string for the 
    for base in reverse_sequence: #for each base in the reverse sequence 
        rev_comp_seq+=complement_base[base] #add the reverse complement to the empty string
    #print(rev_comp_seq)
    return rev_comp_seq #return the reverse complement string

with open(args.index,"r") as fh_indexes:
    index_set=set() #creating an empty set 
    num_line=0 #counting the lines in a file 
    for line in fh_indexes: #looping through each line in the file 
        num_line+=1 #incrementing the line counter 
        if num_line > 1: #getting everything but the header line 
            split_line=line.strip().split("\t") #splitting on the tab 
            index_set.add(split_line[4]) #grabbing only the sequence and adding it to a list of known indexes 

file_handle_dictionary={}

for index in index_set: #looping through the indexes in index list
    fhR1=open(index + '_R1.fq','w') #making a new file handle to write to 
    fhR2=open(index + '_R2.fq','w') #making a new file handle to write to 
    file_handle_dictionary[index]=[fhR1,fhR2] #creating a dictionary to store the file handles

unkR1=open('unknown_R1.fq','w') 
unkR2=open('unknown_R2.fq','w')
hopR1=open('hopped_R1.fq','w')
hopR2=open('hopped_R2.fq','w')

mismatch_counter={}
matched_counter={}
unknown_counter=0

with gzip.open(R1,"rt") as fh1, gzip.open(R2,"rt") as fh2, gzip.open(R3,"rt") as fh3, gzip.open(R4,"rt") as fh4: #opening each file 

    while True:
        R1_record_list[0]=fh1.readline().strip("\n") #reading each line and adding it to the list at correct positions 
        if R1_record_list[0]=="":
            break
        R1_record_list[1]=fh1.readline().strip("\n")
        R1_record_list[2]=fh1.readline().strip("\n")
        R1_record_list[3]=fh1.readline().strip("\n")

        R2_record_list[0]=fh2.readline().strip("\n")
        R2_record_list[1]=fh2.readline().strip("\n")
        R2_record_list[2]=fh2.readline().strip("\n")
        R2_record_list[3]=fh2.readline().strip("\n")

        R3_record_list[0]=fh3.readline().strip("\n")
        R3_record_list[1]=fh3.readline().strip("\n")
        R3_record_list[2]=fh3.readline().strip("\n")
        R3_record_list[3]=fh3.readline().strip("\n")

        R4_record_list[0]=fh4.readline().strip("\n")
        R4_record_list[1]=fh4.readline().strip("\n")
        R4_record_list[2]=fh4.readline().strip("\n")
        R4_record_list[3]=fh4.readline().strip("\n")
        
        headerR1=R1_record_list[0] #creating a variable to append the indexes to the header for read1
        headerR4=R4_record_list[0] #creating a variable to append the indexes to the header for read2
        index1=R2_record_list[1] #creating a variable for the first index
        rev_comp_index2=reverse_complement_func(R3_record_list[1]) #getting the reverse complement for index 2
        headerR1+=(f" {index1}-{rev_comp_index2}") #appending the indexes to the header
        headerR4+=(f" {index1}-{rev_comp_index2}") #appending the indexes to the header

        if "N" in index1 or "N" in rev_comp_index2: #IF YOU WANT TO ADD QUALITY SCORE CUTOFF DO IT HERE
            unkR1.write(headerR1+"\n"+R1_record_list[1]+"\n"+R1_record_list[2]+"\n"+R1_record_list[3]+"\n")
            unkR2.write(headerR4+"\n"+R4_record_list[1]+"\n"+R4_record_list[2]+"\n"+R4_record_list[3]+"\n")
            unknown_counter+=1
        
        elif index1 not in index_set or rev_comp_index2 not in index_set: #looking to see if it is known indexes
            unkR1.write(headerR1+"\n"+R1_record_list[1]+"\n"+R1_record_list[2]+"\n"+R1_record_list[3]+"\n")
            unkR2.write(headerR4+"\n"+R4_record_list[1]+"\n"+R4_record_list[2]+"\n"+R4_record_list[3]+"\n")
            unknown_counter+=1
        
        elif index1 != rev_comp_index2: #checking if it is unmatched
            hopR1.write(headerR1+"\n"+R1_record_list[1]+"\n"+R1_record_list[2]+"\n"+R1_record_list[3]+"\n")
            hopR2.write(headerR4+"\n"+R4_record_list[1]+"\n"+R4_record_list[2]+"\n"+R4_record_list[3]+"\n")
            if (index1,rev_comp_index2) in mismatch_counter: #if in dictionary adds to it 
                mismatch_counter[(index1,rev_comp_index2)]+=1
            else:
                mismatch_counter[(index1,rev_comp_index2)]=1 #if not in dictionary creates instance
    
        elif index1 == rev_comp_index2: #if equal, looks up the index in the dictionary and writes it to file 
            file_handle_dictionary[index1][0].write(headerR1+"\n"+R1_record_list[1]+"\n"+R1_record_list[2]+"\n"+R1_record_list[3]+"\n") 
            file_handle_dictionary[index1][1].write(headerR4+"\n"+R4_record_list[1]+"\n"+R4_record_list[2]+"\n"+R4_record_list[3]+"\n")
            if index1 in matched_counter:
                matched_counter[index1]+=1
            else:
                matched_counter[index1]=1
        else:
            raise Exception('Impossible')
        

        R1_list=["","","",""] #clearing the lists for each record 
        R2_list=["","","",""]
        R3_list=["","","",""]
        R4_list=["","","",""]

total_number=sum(mismatch_counter.values())+sum(matched_counter.values())+unknown_counter

with open('hopped_data.tsv','w') as fh1, open('matched_data.tsv','w') as fh2, open('overall_data.tsv','w') as fh3:
    print(f'index-pair\thopped count\tpercent of hopped pair overall',file=fh1)
    for index_pair in mismatch_counter: #writing the index pair to a file that will count each instance
        percent_pairhopped_overall=mismatch_counter[index_pair]/total_number*100
        print(f'{index_pair}\t{mismatch_counter[index_pair]}\t{percent_pairhopped_overall}%',file=fh1)

    print(f'index\tmatched count\tpercent index in sample\tpercent index overall',file=fh2)        
    for index in matched_counter: #writing how many indexes were matched
        percent_indexes_matched=matched_counter[index]/sum(matched_counter.values())*100 #calculating the number of unique indexes in matched 
        percent_indexes_matched_total=matched_counter[index]/total_number*100 #calculating the number of unique matched indexes in total
        print(f'{index}\t{matched_counter[index]}\t{percent_indexes_matched}%\t{percent_indexes_matched_total}%',file=fh2)
            
    print(f'type of data\tcount\tpercent of total',file=fh3)
    percent_hopped=sum(mismatch_counter.values())/total_number*100
    percent_matched=sum(matched_counter.values())/total_number*100
    percent_unknown=unknown_counter/total_number*100
    print(f'hopped\t{sum(mismatch_counter.values())}\t{percent_hopped}%', file=fh3)
    print(f'matched\t{sum(matched_counter.values())}\t{percent_matched}%', file=fh3)
    print(f'unknown\t{unknown_counter}\t{percent_unknown}%', file=fh3)

unkR1.close()
unkR2.close()
hopR1.close()
hopR2.close()

for index in file_handle_dictionary: #looping through the indexes in dctionary to close the files
    file_handle_dictionary[index][0].close() 
    file_handle_dictionary[index][1].close()
