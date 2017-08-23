import random
import time
print("당신의 수학능력을 평가해보죠.")
randombox=range(100)
qwer=('+', '-', 'x')
print("\n시작을 입력해주세요\n")

question_num=1
while(True):
    a=input("입력 :")
    if a=='시작':
        x=random.choice(randombox)
        z=random.choice(randombox)
        y=random.choice(qwer)
        print("\n\n%d번 문제 :%s %s %s"%(question_num, x, y, z))
        question_num=question_num+1
    else:
        print("\n시작을 입력 하라고\n")
