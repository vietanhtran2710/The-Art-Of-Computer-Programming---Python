import sys

prime = [2]
n = 3
while (len(prime) < 5000):
    prime.append(n)
    n += 2
    k = 1
    while (n % prime[k] == 0):
        n += 2
        k = 1
        while (n / prime[k] > prime[k]):
            k += 1

print(prime)
