
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

s = labels_DNAStrings[0][1]
t = labels_DNAStrings[1][1]

print s
print t

#Let's do it functional programming style!

def subsequence(s,t,count): #Returns the indicies of where t is a subsequence of s
    if t == '':
        return []
    elif t[0]==s[0]:
        return [count]+subsequence(s[1:],t[1:],count + 1)
    else:
        return subsequence(s[1:],t,count+1)

print " ".join(map(lambda x: str(x),subsequence(s,t,1)))  #A hack to print the list of integers nicely with spaces.
