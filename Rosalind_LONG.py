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

import random

DNAStrings = [DNAString for (label,DNAString) in labels_DNAStrings] #Ignore the labels and just get the collection of DNAStrings

min_overlap = min(map(len,DNAStrings))/2           #This is KEY. We set the minimum allowed overlap at the outset. If we allow too small of an overlap we get meaningless overlaps. If we 
                                                   #set the overlap length to be half of the smaller of string1 and string2, then that is too stringent later on when dealing with big strings.

def merge(string1,string2,minolap = 1):
    '''Takes two strings and tries to overlay them into a single string by finding a portion where they overlap. 'minolap' is the minimum overlap allowed
    to prevent trivial overlaps'''
    if len(string1) > len(string2):
        longer = string1
        shorter = string2
    else:
        longer = string2
        shorter = string1
    for i in range(0,len(longer)-len(shorter)):    #Check to see if the shorter is entirely contained in the longer
        if longer[i:i+len(shorter)] == shorter:    
            return longer
    for olap in range(len(shorter)-1,minolap,-1):        #Check to see if the shorter overlaps at the ends of the longer. Seeks maximum overlap.
        if longer[-olap:]== shorter[:olap]:        #Does the shorter overlap by olap at the end?
            return longer[:-olap]+shorter
        if longer[:olap] == shorter[-olap:]:       #Does the shorter overlap by olap at the beginning?
            return shorter + longer[olap:]
#    print "No Overlap!"
    return None

while len(DNAStrings) > 1:
#    print "Length: %d" % len(DNAStrings)
    i = random.randint(0,len(DNAStrings)-1)
    j = random.randint(0,len(DNAStrings)-1)
    if i != j:
        merged_string = merge(DNAStrings[i],DNAStrings[j],min_overlap)
        if merged_string:                          #If was able to merge, then remove the two strings and replace by the merged string
            DNAStrings[i] = merged_string
            DNAStrings.pop(j)

outputfile = open("Rosalind_LONG_Output.txt","w")
outputfile.write(DNAStrings[0])
