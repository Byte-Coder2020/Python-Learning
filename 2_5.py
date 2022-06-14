sum_total = 0
i = 1
m = eval(input())
while abs(pow(-1, i-1)*(2*i - 1)) <= m:
    sum_total += pow(-1, i-1)*(2*i - 1)
    i = i+1
print(sum_total)