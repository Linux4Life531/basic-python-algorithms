primes = [2]
j = 3

def test(n):
    prime = True
    for i in primes:
        if n/i==round(n/i):
            prime = False
    if prime:
        primes.append(n)
        return True
    else:
        return False

while True:
    if test(j):
        print(j)
    j += 1