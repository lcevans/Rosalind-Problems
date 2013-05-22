
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
###Read in the codon table, build codon dictionary

full_string = open("codontable.txt","r").read()

pattern = r'((?:A|C|G|U)+)\s+(\w+)'

RNATriples_aminoacids = re.findall(pattern,full_string)

codondict = {}
for RNATriple,aminoacid in RNATriples_aminoacids:
    codondict[RNATriple] = aminoacid

#################################################

fullDNAString = labels_DNAStrings[0][1]

for label,string in labels_DNAStrings[1:]:
    fullDNAString = "".join(fullDNAString.split(string))

RNAString = 'U'.join(fullDNAString.split('T'))

protein = ""
for i in range(0,len(RNAString),3):
    if codondict[RNAString[i:i+3]] == "Stop":
        break
    else:
        protein += codondict[RNAString[i:i+3]]

print protein

