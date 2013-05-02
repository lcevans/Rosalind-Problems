# Takes a DNAstring and computes its reverse complement (i.e. reverses it and then interchanges "A"/"T" and "C"/"G")

import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

dictionary = {"A":"T", "T":"A", "C":"G", "G":"C"} #Dictionary to store the mapping we want to apply

DNAstring = file.read()  #The string from the data file
DNAstring = DNAstring.strip("\n") #Remove the terminal end-line lest it give issues when applying the dictionary!

reversed_string = DNAstring[::-1] #A hack to reverse the string. [begin:end:step]... here begin and end are the ends of the string and the step is -1

reverse_complement = ''.join([dictionary[char] for char in reversed_string]) #replaces each char by dictionary[char]  (so changes "A" -> "T" etc)

print reverse_complement
