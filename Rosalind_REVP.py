
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

DNAString = labels_DNAStrings [0][1]

def reverse_complement(DNAString):
    complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
    reverse = DNAString[::-1]
    reverse_complement = ''.join([complement[char] for char in reverse])
    return reverse_complement

outputfile = open("Rosalind_REVP_Output.txt","w")

for i in range(len(DNAString)):                                            # i is the index
    for j in range(4,13):                                                  # j is the palindrome length
        if i+j <= len(DNAString):                                           #Make sure we don't go beyond the array bound!
            if DNAString[i:i+j] == reverse_complement(DNAString[i:i+j]):
                outputfile.write(str(i+1)+" "+str(j)+"\n")                  #print the index and reverse-palindrome length


