sum_odd = 0
sum_even = 0
for i in range(1, 101):
    if i % 2 == 1 :
        sum_odd += i
    else:
        sum_even += i
print("奇数的和：", sum_odd)
print("偶数的和：", sum_even)