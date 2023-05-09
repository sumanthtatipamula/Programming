# from math import gcd
# from bisect import bisect_right
# n = int(input())
# elements = list(map(int , input().split()))
# dp = [1] * len(elements)
# for i in range(0, n):
#     for j in range(i - 1, -1, -1):
#         if(gcd(elements[i], elements[j]) != 1):
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

from collections import defaultdict

def getPrimeFactors(num):
    primeFactors = []
    i = 2
    while(i * i <= num):
        if(num % i == 0):
            primeFactors.append(i)
            while(num % i == 0):
                num //= i
        i += 1
    if(num >= 2):
        primeFactors.append(num)
    return primeFactors


n = int(input())
elements = list(map(int , input().split()))
result = 0
prime_map = [0] * (10 ** 5)
for i in range(0, len(elements)):
   prime_factors = getPrimeFactors(elements[i])
   max_length = 1
   for factor in prime_factors:
       max_length = max(max_length, prime_map[factor] + 1)
   for factor in prime_factors:
       prime_map[factor] = max_length
   result = max(result, max_length)
print(result)
