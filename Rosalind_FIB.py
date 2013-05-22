import sys

n = int(sys.argv[1])   # n is the number of generations
k = int(sys.argv[2])   # k is the litter size

rabbits = [1,0] # start with 1 young and 0 old rabbits

for i in range(1,n):
    print i
    totalrabbits = rabbits[0]+rabbits[1] # The total rabbits (young and old) at the nth step
    rabbits[0] = k* rabbits[1]  #Number of young rabbits in the next generation is k times the number of old rabbits
    rabbits[1] = totalrabbits   #Number of old rabbits in the next generation is the total number of rabbits in the previous generation

print "In the %d-th generation there are %d young and %d old rabbits for a total of %d rabbits!" % (n,rabbits[0],rabbits[1],rabbits[0]+rabbits[1])
