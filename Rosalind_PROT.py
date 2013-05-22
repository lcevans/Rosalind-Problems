# Takes a DNA string and replaces triples by letters according to the 'codon dictionary' stopping when you reach a stop-triple

import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

#################################################################
###First build the codon dictionary from the codontable.txt file using regular expressions

import re

codonpointer = open("codontable.txt","r")
codon = codonpointer.read()
pattern = r'([A-Z]{3})\s(\w+)'
string_list = re.findall(pattern, codon)

codon_dictionary = {}

for (key,item) in string_list:
    codon_dictionary[key] = item
##########################################
##Breaking a long string of DNA into triples is a breeze with regular expressions! 

DNA_string = file.read()
pattern = r'[A-Z]{3}'
DNAtriples_list = re.findall(pattern,DNA_string)

outputstring = ''
for triple in DNAtriples_list:
    if codon_dictionary[triple] == "Stop":
        break
    else:
        outputstring += codon_dictionary[triple]

print outputstring
