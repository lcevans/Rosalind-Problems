# Takes a DNAstring consisting of the letters AGCT and creates the corresponding RNA string by replacing each copy of T with U

import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

DNAstring = file.read()  #The string from the data file

RNAstring = ''.join([((char == "T") and "U" or char) for char in DNAstring])  # Using the python ternary trick:  A and B or C    is like  A?B:C

print RNAstring
