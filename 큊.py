import random
import time
print("당신의 수학능력을 평가해보죠.")
randombox=range(100)
qwer=('+', '-', 'x')
print("\n문제를 풀어주세요.\n")
print("※주의 사항※\n■숫자가 아닌 다른것을 입력하면 자동종료됩니다.■")

question_num=1
while(True):
    #문제 생성
    x=random.choice(randombox)
    y=random.choice(qwer)
    z=random.choice(randombox)
    print("\n\n%d번 문제 :%s %s %s ="%(question_num, x, y, z))
    a=int(input("입력 :"))
    #정답 판별
    if y=='+':
        za=x+z
    elif y=='-':
        za=x-z
    elif y=='x':
        za=x*z
    if a==(za):
        print("\n정답")
    else:
        print("\n오답")
        str(za)
        print("\n답 :",za)
    question_num=question_num+1
