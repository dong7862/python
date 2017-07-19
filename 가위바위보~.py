print("가위바위보 게임!")
while(True):
    a=input("입력해주세요 :")
    randombox=('가위','바위','보')
    cu=("\n이제 그만하고 싶으신건가요?\n\n그렇다면 '종료'를 입력해주세요.\n","\n가위,바위,보 중 한가지를 입력해주세요.\n")
    import random
    import time
    #가위를 냈을떄
    if a=='가위':
        x=random.choice(randombox)
        print("결과 계산중...")
        time.sleep(1)
        print("\n내가 낸 것 :%s\n\n컴퓨터가 낸 것 :%%s" % (a) % (x))
        if x=='가위':
            print("\n=-=-=-=-=-=-=-무승부!-=-=-=-=-=-=-=\n")
        elif x=='바위':
            print("\n=-=-=-=-=-=-=-패배!-=-=-=-=-=-=-=\n")
        elif x=='보':
            print("\n=-=-=-=-=-=-=-승리!-=-=-=-=-=-=-=\n")
    #바위를 냈을떄
    elif a=='바위':
        x=random.choice(randombox)
        print("결과 계산중...")
        time.sleep(1)
        print("\n내가 낸 것 :%s\n\n컴퓨터가 낸 것 :%%s" % (a) % (x))
        if x=='가위':
            print("\n=-=-=-=-=-=-=-승리!-=-=-=-=-=-=-=\n")
        elif x=='바위':
            print("\n=-=-=-=-=-=-=-무승부!-=-=-=-=-=-=-=\n")
        elif x=='보':
            print("\n=-=-=-=-=-=-=-패배!-=-=-=-=-=-=-=\n")
    #보를 냈을떄
    elif a=='보':
        x=random.choice(randombox)
        print("결과 계산중...")
        time.sleep(1)
        print("\n내가 낸 것 :%s\n\n컴퓨터가 낸 것 :%%s" % (a) % (x))
        if x=='가위':
            print("\n=-=-=-=-=-=-=-패배!-=-=-=-=-=-=-=\n")
        elif x=='바위':
            print("\n=-=-=-=-=-=-=-승리!-=-=-=-=-=-=-=\n")
        elif x=='보':
            print("\n=-=-=-=-=-=-=-무승부!-=-=-=-=-=-=-=\n")
    elif a=='종료':
        break
    else:
        x=random.choice(cu)
        print(x)
        
