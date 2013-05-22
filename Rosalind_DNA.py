import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(sys.argv[1],"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

string = file.read()  #The string from the data file

print "Number of A's is %d" % (len(''.join([char for char in string if char not in "GCT"]))-1) #A hack to strip all non-A from the string and then take its length
print "Number of C's is %d" % (len(''.join([char for char in string if char not in "GTA"]))-1) #ditto
print "Number of G's is %d" % (len(''.join([char for char in string if char not in "CTA"]))-1) #ditto
print "Number of T's is %d" % (len(''.join([char for char in string if char not in "GCA"]))-1) #ditto


