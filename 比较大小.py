num=int(input(""))
max=0  #用来存放最大的那个数位数字
digit_Ten = num // 10 %10
digit_unit = num % 10
digit_hundred =num // 100
print(digit_unit, digit_Ten, digit_hundred)
list = [digit_hundred, digit_Ten, digit_unit]
print(sorted(list)[-1])