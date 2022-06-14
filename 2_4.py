import random
sum_random = 0
for i in range(10):
    sum_random = sum_random + random.randint(0, 100)
average_random = sum_random / 10
print(average_random)
