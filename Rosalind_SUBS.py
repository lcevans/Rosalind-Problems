# Given two strings s and t, find the indicies at which t appears as a substring of s

import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

#################################################################

output = open("Rosalind_Subs_Output.txt","w")

s = file.readline()[:-1]
t = file.readline()[:-1]

for i in range(len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        output.write(str(i+1)+" ")
