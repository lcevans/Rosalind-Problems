import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()
#################################################################

string1 = file.readline()[:-1]
string2 = file.readline()[:-1]

mismatches = [((char1!=char2) and 1 or 0) for (char1,char2) in zip(string1,string2)] #using the and/or trick to create the ternary (char1!=char2)?1:0
                                                                                     #mismatches is a list of 0s and 1s, 0 for a match and 1 for a mismatch
print sum(mismatches)    #prints the total number of mismatches


