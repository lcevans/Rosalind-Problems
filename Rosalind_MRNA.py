
import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(filename,"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

#######################################################
###Read in the codon table
import re

full_string = open("codontable.txt","r").read()

pattern = r'((?:A|C|G|U)+)\s+(\w+)'

RNATriples_aminoacids = re.findall(pattern,full_string)

#################################################
import collections           #imported to use defaultdict


protein_string = file.read().strip()

frequency_table = collections.defaultdict(int)    #This sets the default value of each key to 0 (A bit confuse here... I guess int defaults to 0?)

for RNATriple,aminoacid in RNATriples_aminoacids:
    frequency_table[aminoacid] += 1


combinations = 1
for aminoacid in protein_string:
    combinations *= frequency_table[aminoacid]        #How many ways are there to create that amino acid?
    combinations %= (10**6)
combinations *= frequency_table['Stop']               #Also need to keep track of the number of stop codons
combinations %= (10**6)

print combinations
