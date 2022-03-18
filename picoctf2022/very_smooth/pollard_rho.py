# Python code for Pollard p-1 
# factorization Method
   
# importing "math" for 
# calculating GCD
import math
   
# importing "sympy" for 
# checking prime
import sympy
   
      
# function to generate 
# prime factors
def pollard(n):
   
    # defining base
    a = 2
   
    # defining exponent
    i = 2
   
    # iterate till a prime factor is obtained
    while(True):
   
        # recomputing a as required
        a = (a**i) % n
   
        # finding gcd of a-1 and n
        # using math function
        d = math.gcd((a-1), n)
   
        # check if factor obtained
        if (d > 1):
   
            #return the factor
            return d
   
            break
   
        # else increase exponent by one 
        # for next round
        i += 1
  
# Driver code
n = int('c5261293c8f9c420bc5291ac0c14e103944b6621bb2595089f1641d85c4dae589f101e0962fe2b25fcf4186fb259cbd88154b75f327d990a76351a03ac0185af4e1a127b708348db59cd4625b40d4e161d17b8ead6944148e9582985bbc6a7eaf9916cb138706ce293232378ebd8f95c3f4db6c8a77a597974848d695d774efae5bd3b32c64c72bcf19d3b181c2046e194212696ec41f0671314f506c27a2ecfd48313e371b0ae731026d6951f6e39dc6592ebd1e60b845253f8cd6b0497f0139e8a16d9e5c446e4a33811f3e8a918c6cd917ca83408b323ce299d1ea9f7e7e1408e724679725688c92ca96b84b0c94ce717a54c470d035764bc0b92f404f1f5', 16)
   
# temporarily storing n
num = n
   
# list for storing prime factors
ans = []
   
# iterated till all prime factors
# are obtained
while(True):
   
    # function call
    d = pollard(num)
   
    # add obtained factor to list
    ans.append(d)
   
    # reduce n
    r = int(num/d)
   
    # check for prime using sympy
    if(sympy.isprime(r)):
   
        # both prime factors obtained
        ans.append(r)
   
        break
   
    # reduced n is not prime, so repeat
    else:
   
        num = r
  
# print the result
print("Prime factors of", n, "are", *ans)