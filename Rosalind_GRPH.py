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

def overlap(string1,string2,k):
    '''Returns True if the last k characters of string1 match the first k characters of string2'''
    return (string1[-k:]==string2[:k])


adjacency_list = []

for (label,DNAString) in labels_DNAStrings:
    for (label2,DNAString2) in labels_DNAStrings:
        if label != label2 and overlap(DNAString,DNAString2,3):
            adjacency_list += [[label,label2]]

outputfile = open("Rosalind_GRPH_Output.txt","w")

for (label1,label2) in adjacency_list:
    outputfile.write(label1+" "+label2+'\n')
