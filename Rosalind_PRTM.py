import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(filename,"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()
######

import re


protein_string = "".join(file.read().split('\n'))

masstablefile = open("masstable.txt","r")

pattern = r'(\w+)\s+((?:\d|.)+)'
matches = re.findall(pattern,masstablefile.read())  #Use RegEx to read off masstable.txt into (letter,mass) pairs

dictionary = {}                      #Build a dictionary from these pairs
for (key,item) in matches:
    dictionary[key] = item

total_weight = sum([float(dictionary[key]) for key in protein_string])  #Convert the characters in protein_strings into weights according to the dictionary and then sum them
print total_weight
