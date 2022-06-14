string = input()
sum_upper = 0
sum_lower = 0
sum_dig = 0
for s in string:
    if s.isupper(): sum_upper += 1
    if s.islower(): sum_lower += 1
    if s.isdigit(): sum_dig += 1
sum_letters = sum_lower + sum_upper
print(sum_letters, sum_dig, end="")

