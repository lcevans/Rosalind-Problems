
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

DNAString = labels_DNAStrings [0][1]
RNAString = "U".join(DNAString.split("T"))


complement = {"A":"U", "U":"A", "C":"G", "G":"C"}
reversedRNA = RNAString[::-1]
reverse_complement = ''.join([complement[char] for char in reversedRNA])

codondict = {}
for RNATriple,aminoacid in RNATriples_aminoacids:   #Build a codon dictionary!
    codondict[RNATriple] = aminoacid

def possible_proteins(RNAString):
    proteinlist = []
    for i in range(len(RNAString)):
        if RNAString[i:i+3] == "AUG":
            protein = ""
            stopped = 0                            #flag to make sure that we stop at a stop codon and not just because the string ended
            for j in range(i,len(RNAString),3):     #Go three at a time and feed into the codon dictionary to get the appropriate amino acid
                if codondict[RNAString[j:j+3]] == 'Stop':
                    stopped = 1
                    break
                else:
                    protein += codondict[RNAString[j:j+3]]
            if stopped == 1: proteinlist += [protein]
    return proteinlist

raw_candidate_proteins =  possible_proteins(RNAString) + possible_proteins(reverse_complement)  #Careful! There may be duplicates!
candidate_proteins = list(set(raw_candidate_proteins))  #Turn it to a set to remove duplicates. Then back into a list.

outputfile = open("Rosalind_ORF_Output.txt","w")
for protein in candidate_proteins:
    outputfile.write(protein + '\n')

