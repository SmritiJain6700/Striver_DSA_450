#Sieve of Eratosthene - algorithm to find all prime numbers <= n
# logic
# Why only till √n?
# Suppose you want to mark all multiples of a number p as non-prime.
# Any composite number(having more than 2 factors i.e is not prime and greater than 1) c ≤ n can be written as c = a × b.
# At least one of a or b must be ≤ √n.
# So, if there is a factor larger than √n, the other factor must be smaller than √n.

# Time - complexity - O(n*log(log(n))). For each prime number, we mark its multiples, which takes around n/p steps. The total time is proportional to n*(1/2 + 1/3 + 1/5 + ....).
# This sum over primes grows slowly and is approximately O(n*log(log(n)))
# Space - Compleixty - O(n) -- O(n)(boolean array to track primes)

def sieveOfEratosthene(n):
    prime = [True]*(n+1) # True if a number is Prime and False if a number is not Prime. Initially assuming all the numbers to be prime
    # 0 and 1 are not prime
    prime[0] = False 
    prime[1] = False

    i = 2
    while (i * i <= n):
        if(prime[i] == True):
            # marks all multiples of i as false
            for j in range(i*i, n+1, i):
                prime[j] = False
        i += 1
    
    ans = []
    for i in range(0, len(prime)):
        if(prime[i] == True):
            ans.append(i)

    return ans

n = int(input("Enter a number:"))
print(f"All prime numbers upto {n} are :", sieveOfEratosthene(n))

