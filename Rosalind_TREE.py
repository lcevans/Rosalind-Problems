
import sys

filename = sys.argv[1]   #Take data file as second argument

try:
    file = open(filename,"r")   #Store the file pointer as file
except IOError:
    print "File not found!"
    quit()

#################################################################

numbers = file.read().split('\n')[:-1] #Need to get rid of the extra '' that comes when you split
n = int(numbers[0]) # Number of verticies
e = len(numbers)-1 #Number of edges already in the graph

#max number of edges in a tree is n-1 so we have n-1-e edges remaining to insert!

print n-1-e

