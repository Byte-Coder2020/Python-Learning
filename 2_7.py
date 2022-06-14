"""
for number in range(100, 200+1):
    if str(number)[0] == str(number)[-1]:
        print(number)
"""
num=int(input())
if len(str(num)) != 4:
    print("error")
else:
    strs = str(num)
    if (strs[0] == strs[-1]) and (strs[1] == strs[-2]):
        print("{}是回文数".format(num))
    else:
        print("{}不是回文数".format(num))

