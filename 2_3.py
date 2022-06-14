def factorial(n):
    if n == 0 or n == 1:
        factor = 1
    else:
        factor = 1
        for i in range(2, n + 1):
            factor = factor * i
    return factor


sum = 0
num = int(input())
for i in range(1, num + 1):
    sum += factorial(i)
print(sum)
