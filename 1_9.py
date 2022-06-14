numbers = 5000
rate = 0.05
years = 0
while numbers < 10000:
    numbers = numbers*(1 + rate)
    years = years + 1
print(years)