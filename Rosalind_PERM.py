# Takes a number n and returns the total number of permutations on a list of n elements and a list of all such permutations

import sys

n = int(sys.argv[1])   # n is the number

# First of all, the total number of permutations is n! which I will compute directly.

def fact(n):    #Simple factorial function
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

#Now lets write the list of permutations!

def print_list_to_file(list, filepointer):  
    '''Prints a list to filepointer by putting spaces between the elements and '\n' at the end'''
    filepointer.write(" ".join([str(elem) for elem in list]) + "\n")

numbers = range(1,n+1) #list of numbers 1,...,n
file = open("Rosalind_PERM_Output.txt", "w") 
permutation_count = 0

def list_of_permutations(list):
    '''Takes in a list and returns a list of lists consisting of all permutations of the passed list. WARNING, the original list cannot contain duplicate elements'''
    if list == []:
        return [[]]
    return_list = []
    for elem in list:
        return_list += [[elem] + recursed_list for recursed_list in list_of_permutations(filter(lambda x: x != elem,list))] #The filter is my hack for removing an element from the list
    return return_list

permutation_list = list_of_permutations(numbers)

file.write(str(fact(n))+"\n")

for perms in permutation_list:
    print_list_to_file(perms,file)

