#!/usr/bin/env python

# Author: <Perris Navarro> <perrisn@uoregon.edu>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
Module has been updated over Bi621'''

#__version__ = "0.4"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNAbases = set("ATGCNatcgn")
RNAbases = set("AUGCNaucgn")
DNA="ATGC"
RNA="AUGC"

def convert_phred(letter: str) -> int:
    """Converts a single character into a phred score""" 
    return ord(letter)-33

def validate_base_seq(seq,RNAflag=False):
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    return set(seq)<=(RNAbases if RNAflag else DNAbases)


def gc_content(DNA):
    '''Will calculate the total DNA content and then calculate the GC content, and returns as a decimal'''
    validate_base_seq(DNA)
    DNA=DNA.upper() #Make sure sequence is all uppercase
    content_GC=DNA.count ("G") + DNA.count ("C") #Count number of Cs and Gs
    return (content_GC/len(DNA)) 
    

def qual_score(phred_score: str) -> float:
    """Takes a string of phred_score as a parameter and calculates the average quality score of the whole phred string"""
    total:int=0
    for letter in (phred_score):
        total+=convert_phred(letter)
    
    return total/len(phred_score)

def calc_median(sub_list):
    '''Calculates the median of a list'''
    sublist_length=len(sub_list)
        
    if sublist_length%2==0:
        median1_index=(sublist_length+1)//2
        median2_index=(sublist_length-1)//2
        median=(sub_list[median1_index]+sub_list[median2_index])/2
        
    else:
        median_index=(sublist_length//2)
        median=sub_list[median_index]
    
    return median

def online_fasta(input_file): 
    '''Takes a fasta file and converts the sequence line to one line, if on multiple lines'''
    with open (input_file,"r") as fh1, open("one_line_fasta_output.fa","w") as fh2:
        line=fh1.readline()
        fh2.write(line) #writes the first header line to the file 
        seq=""
        for fasta in fh1:
            if fasta.startswith(">"):
                fh2.write(seq+"\n")
                fh2.write(fasta)
                seq =""
            else:
                seq+=fasta.strip("\n")
        fh2.write(seq+"\n")


if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

    assert qual_score("EEE") == 36
    assert qual_score("#I") == 21
    assert qual_score("EJ") == 38.5
    #assert qual_score(phred_score) == 37.62105263157895, "wrong average phred score"
    print("Your qual_score function is working! Nice job")

    assert validate_base_seq(DNA), "String contains invalid characters - are you sure you used DNA sequence?"

    assert calc_median([1,2,3]) == 2, "calc_median function does not work for odd length list"
    assert calc_median([1,2]) == 1.5, "calc_median function does not work for even length list"
    print("Median works for even and odd length lists")