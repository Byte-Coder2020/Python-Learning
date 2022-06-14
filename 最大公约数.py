a = eval(input("请输入a的值"))
b = eval(input("请输入b的值"))
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print("a和b的最大公约数为", i)
        break
for j in range(max(a, b), a * b + 1):
    if j % a == 0 and j % b == 0:
        print("a和b的最大公倍数为", j)
        break
