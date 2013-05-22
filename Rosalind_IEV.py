import sys

filename = sys.argv[1]
try:
    file = open(filename,"r")
except IOError:
    print "IOError!"
    quit()

pop = file.read().split(" ")
pop = map(int,pop)                

print 2*(pop[0]+pop[1]+pop[2]+.75*pop[3]+.5*pop[4]+0*pop[5])
