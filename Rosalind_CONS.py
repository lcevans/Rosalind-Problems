import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

#################################################################
import re
import numpy

inputstring = "".join(file.read().split('\n'))

pattern = r'((?:A|G|C|T)+)'                   #Search for DNA sequences in the text file
DNAstrings = re.findall(pattern, inputstring)     #Store them as a list of strings

#print DNAstrings

DNAMatrix = numpy.matrix(map(list,DNAstrings))    #Matrix of all the DNA strings with the DNA strings as rows
(m,n) = DNAMatrix.shape                           #Dimensions of the array

Aprofile = numpy.sum(numpy.vectorize(lambda x: x == 'A' and 1 or 0)(DNAMatrix), axis = 0) #Apply indicator for 'A' to DNAmatrix and then sum the columns to get the total number of A at each index
Cprofile = numpy.sum(numpy.vectorize(lambda x: x == 'C' and 1 or 0)(DNAMatrix), axis = 0) #Ditto
Gprofile = numpy.sum(numpy.vectorize(lambda x: x == 'G' and 1 or 0)(DNAMatrix), axis = 0) #Ditto
Tprofile = numpy.sum(numpy.vectorize(lambda x: x == 'T' and 1 or 0)(DNAMatrix), axis = 0) #Ditto

ProfileMatrix = numpy.concatenate((Aprofile,Cprofile,Gprofile,Tprofile))  #Combine the row vectors into the profile matrix


index = [0]*n     
for j in range(n):  #Figure out the row index for each column which contains the largest element
    maxindex = 0
    for i in range(4):
        if ProfileMatrix[i,j]>ProfileMatrix[maxindex,j]:
            maxindex = i
    index[j] = maxindex

dictionary = {0:'A', 1:'C', 2:'G', 3:'T'}
consensus = "".join([dictionary[key] for key in index])  #Use the dictionary to turn the row index into the appropriate letter. Store as the consensus string.


####Now we format the output as desired

outputfile = open("Rosalind_CONS_Output.txt","w")
outputfile.write(consensus+"\n")  #Write the consensus DNA string

i = 0
for row in ProfileMatrix:                                                #Iterate over the rows in the Profile Matrix.
    writestring = " ".join([str(elem) for elem in numpy.nditer(row)])    #Format the row into the appropriate text string.
    outputfile.write(dictionary[i]+": "+writestring+'\n')                #Write the text string to the file.
    i += 1                                                               #i keeps track of which row we are in. dictionary[i] then tells us which DNA letter we are working with.














