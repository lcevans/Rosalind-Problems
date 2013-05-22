import sys
from scipy.stats import binom

k = int(sys.argv[1])
N = int(sys.argv[2])

#Let X be the number of AaBb offspring. Then X~Binomial(2^k,.25) since each is that independantly with probability 1/4 (they have to get the opposite pair of alleles from the AaBb parent).
#We therefore need to compute Pr(X>=N)

print 1-binom.cdf(N-1,2**k,.25)
