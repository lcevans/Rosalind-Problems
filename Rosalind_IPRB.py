# Given k YY, m Yy, and n yy individuals, computes the probability that the offspring of two randomly chosen individuals possesses the dominant allele Y.

import sys

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

def choose(n,k): #Define n choose k by recursion. I didn't end up using this
    if k == 0 or k == n:
        return 1
    else:
        return choose(n-1,k-1) + choose(n-1,k)

def cartesianproduct(list1, list2):  #The cartesian product of lists. Cool but I didn't end up using this either
    productlist = [[(elem1,elem2) for elem1 in list1] for elem2 in list2]
    return productlist

individuals = [2]*k + [1]*m + [0]*n  #list of individuals. The integer refers to how many dominant alleles they have.

count = 0.0
extra = 0

for i in range(len(individuals)):
    for j in range(len(individuals)):
        if i != j:
            extra += 1
            if individuals[i] == 2 or individuals[j]==2:       #When either of the mating individuals has two dominant alleles, the offspring has a dominant allele with probability 1
                count +=1
            elif individuals[i] == 1 and individuals[j]==1:    #When both have only one, the probability is only .75
                count +=0.75
            elif individuals[i] == 1 and individuals[j]==0:    #and so on...
                count += 0.5
            elif individuals[i] == 0 and individuals[j]==1:
                count += 0.5

probability = count/extra
print probability
       
