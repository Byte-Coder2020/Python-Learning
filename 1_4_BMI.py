"""
height = eval(input("请输入你的身高（cm）："))
weight = eval(input("请输入你的体重（kg）："))
height = height / 100
bmi = weight / height**2
if bmi > 32:
    print("过于肥胖")
elif bmi >= 28:
    print("肥胖")
elif bmi >=24:
    print("过重")
elif bmi >= 18.5:
    print("正常")
else:
    print("过轻")
"""
if diameter >= 80:
    print("特等果")
elif diameter >= 70:
    print("一等果")
elif diameter >= 65:
    print("二等果")
else:
    print("等外果")