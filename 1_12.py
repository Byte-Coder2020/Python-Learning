def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for n in range(100, 201):
    if isprime(n):
        print(n)
