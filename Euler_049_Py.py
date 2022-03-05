#Ariel Tynan
#Euler Problem 049, Prime permutations, solved in Python
#Started 5 March 2022

#Prime number sieve up to 10000
def prime_Sieve(n): #Function modified from Geeksforgeeks
     
    primes = [] # initial empty list of primes
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes

primes = prime_Sieve(10000) #all 4 digit primes

#Using digits 1,2,3,4,5,6,7,8,9 (assuming no 0 even though it is possible, but unlikely)
#Generate permutations, 9 choose 4
import itertools
from itertools import permutations
from itertools import combinations
allComb = combinations([1,2,3,4,5,6,7,8,9],4)


temp1 = temp2 = 0 #temp variables for averaging permutations
success = False
trials = 0 #9 choose 4 combinations limits to 126 trials

for i in list(allComb):
    permTemp = permutations(i,4)
    perm = [] #temporary permutation list, used for iterating
    for q in list(permTemp): # for each of the 24 permutations, push back into usable list
        perm.append(q)
    for j in range(len(perm)): #24 permutations in each set (4!)
        for k in range(j+1,len(perm)):
            #print(i, perm[j])
            if perm[j][3] % 2 == 1 and perm[k][3] % 2 == 1: #Both must be odd
                temp1 = perm[j][0]*1000 + perm[j][1]*100 + perm[j][2]*10 + perm[j][3] #first num
                temp2 = perm[k][0]*1000 + perm[k][1]*100 + perm[k][2]*10 + perm[k][3] #second num
                ave = (temp1 + temp2)/2
                if temp1 in primes and temp2 in primes and ave in primes:
                    for x in perm:
                        temp3 = x[0]*1000 + x[1]*100 + x[2]*10 + x[3]
                        if temp3 == ave:
                                print("SUCCESS")
                                print(temp1,ave,temp2)
                                #success = True
                    


 
    #Take all 2-pair combinations of permutable numbers, average them, and see if the result is equal to a third permutation
    #Generate sets of permutations