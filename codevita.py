
n = 505
primes = [True] * (n + 1)

for p in range(2, int(n**0.5) + 1):
    if primes[p]:
        for i in range(p*p, n+1, p):
            primes[i] = False

primes[0] = primes[1] = False


d, p = map(int, input().split())
n = d // p

count = sum(all(primes[i + j * n] for j in range(p)) for i in range(2, n))

print(count)
