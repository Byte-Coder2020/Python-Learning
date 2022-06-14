import math
value_pi = 0
i = 1
sum =0
while abs(math.pow(-1, i-1) / (2*i - 1)) >= 1e-4:
    value_pi = value_pi + math.pow(-1, i-1) / (2*i - 1)
    i = i + 1
    sum += 1
print("sum = ",sum)
print(value_pi*4)
