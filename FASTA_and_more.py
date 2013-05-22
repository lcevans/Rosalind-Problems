
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
###Read in the codon table

full_string = open("codontable.txt","r").read()

pattern = r'((?:A|C|G|U)+)\s+(\w+)'

RNATriples_aminoacids = re.findall(pattern,full_string)

#################################################
