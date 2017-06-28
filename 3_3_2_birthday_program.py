birth={}
while(True):
    print('당신의 생일정보를 알려드립니다!')
    print('q를 입력하면 프로그램이 종료됩니다')
    name=input('당신의 이름은? :')
    if name in birth.keys():
        print('\n',birth[name],'\n')
    elif name==('q'): #종료
        import time
        print('어? 종료가 안되')
        time.sleep(1)
        print('아..앙대 앙댄다고!')
        time.sleep(1)
        break
    else:
        print('당신의 정보가 없습니다.')
        print('\n당신의 생일을 입력해주세요(예:9-15 :')
        b=input()
        birth[name]=b
            
