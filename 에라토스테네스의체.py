import math

n = 5
prime = [True]*(n+1)
for i in range(2,int(math.sqrt(n)+1)):
    if not prime[i]: continue
    for j in range(i+i,n+1,i):
        prime[j] = False
        