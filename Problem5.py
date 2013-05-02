# Takes a DNAstring and computes its reverse complement (i.e. reverses it and then interchanges "A"/"T" and "C"/"G")

import sys

n = int(sys.argv[1])   # n is the number of generations
m = int(sys.argv[2])   # m is the months alive

rabbits = [1]+[0]*(m-1) # A hack to initialize an array of length m where the first entry is 1 and the rest are 0. The kth entry is the number of rabbits of age k (we start with one 1 yr old)

for i in range(1,n):
    rabbits = [sum(rabbits[1:])] + rabbits[0:-1] #The number of new 1-yr old rabbits is the sum of all the older rabbits (sum(rabbits[1:])).
                                                 #The all rabbits but the oldest (rabbits[0:-1]) all advance in age by one

print rabbits  #let's see dem rabbits of all ages!
print "In the %d-th generation there are a total of %d rabbits!" % (n,sum(rabbits))
