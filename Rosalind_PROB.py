import sys
import math

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(filename,"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

filestringlist = file.read().split('\n')
file.close()


DNAString = filestringlist[0]
probabilities = map(lambda x: float(x),filestringlist[1].split(' '))

outputlist = []

for prob in probabilities:
    charprob = {}           #Build dictionary of the probabilities for each character
    charprob['G'] = prob/2
    charprob['C'] = prob/2
    charprob['A'] = (1-prob)/2
    charprob['T'] = (1-prob)/2
    
    logprob = 0
    for char in DNAString:           #Find the (log of the) probability of that DNA string
        logprob += math.log(charprob[char],10)
    outputlist += [logprob]

for elem in outputlist:         #Print out the list in the desired format
    print "%.3f " % elem,
