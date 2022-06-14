def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = eval(input())
for n in range(2, N+1):
    if isprime(n):
        print(n)
