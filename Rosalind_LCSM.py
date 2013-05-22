###Overlap Graph

import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(filename,"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

#################################################################
##Text file is in FASTA format. Separate the labels from the DNA strings.

import re

full_string = "".join(file.read().split('\n'))

pattern = r'(Rosalind_\d+)((?:A|C|G|T)+)'

labels_DNAStrings = re.findall(pattern,full_string)  #List of pairs (label,DNAString)

#######################################################

DNA_Strings = [DNA_String for (label,DNA_String) in labels_DNAStrings]

def is_it_substring(string,candidate):
    for i in range(len(string)-len(candidate)+1):
        if string[i:i+len(candidate)] == candidate:
            return True
    return False

def longest_common_substring(collection_of_strings):
    for length in range(len(collection_of_strings[0]),0,-1):
        for i in range(len(collection_of_strings[0])-length+1):   
            candidate = collection_of_strings[0][i:i+length]                   #Cycles through all O(n^2) substrings of the first DNA string from greatest to shortest length.
            if candidate == "GTA": print "Testing GTA"
            goodmatch = True
            for string in collection_of_strings[1:]:
                goodmatch = goodmatch and is_it_substring(string,candidate)
            if goodmatch == True:
                return candidate
    print "No match found!"
    return None

outputfile = open("Rosalind_LCSM_Output.txt","w")
outputfile.write(longest_common_substring(DNA_Strings))

