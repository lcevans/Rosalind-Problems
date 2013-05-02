# Takes a collection of DNA strings in FASTA format and returns that with the highest GC-content

import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()
#################################################################

labels = []
DNA_strings = []
GC_contents = []

strings = file.read().split('>')[1:]  #Break up the data file by '>'. Also eliminate the initial space. Returns a list consisting of labels interlaced with DNA strings.
                                      #Now we need only deal with each of these individually. Each element of strings looks like "LABEL\nACTGTACGTAG\nACTAGATACAGT\n"
for elem in strings:
    pieces = elem.split('\n')[:-1]   #Break up each element by \n and remove the trailing '' 
    labels.append(pieces[0])         #The first entry of the list is the label and so goes in the label array
    DNA_strings.append("".join(pieces[1:]))  #the other entries are strings so they are combined into one large string and stored in the DNA_strings array

for strand in DNA_strings:            #In each strand, count the number of G,C and divide by the total length of the strand to get the GC-percentage
    GC_count = 0.0
    for char in strand:
        if char == 'G' or char == 'C':
            GC_count += 1
    GC_percentage = GC_count/len(strand)
    GC_contents.append(GC_percentage)  #Add this to the list of GC-contents

max_index = 0
max_value = 0
for i in range(len(GC_contents)):
    if GC_contents[i] > max_value:
        max_value = GC_contents[i]
        max_index = i


print labels[max_index]
print 100*GC_contents[max_index]  #Gives the GC-content as a %




