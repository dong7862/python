while(True):
    print("예)000000-0000000(6글자-7글자)")
    a=input("당신의 주민번호를 입력해주세요 :")
    #종료
    if a=='q':
        break
    zxc=int(a[7:8])
    #글자수가 안맞아
    if len(a)!=14:
        print("\n정확히 13자리를 입력해주세요(예를 보세요)\n")
        continue
    #오류!
    if a[6:7]!="-":
        print('\n"-"를 입력해주세요\n')
        continue
    #성별 구분
    if zxc%2==1:
        print("\n남자\n")
    else:
        print("\n여자\n")
