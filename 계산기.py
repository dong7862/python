from tkinter import * #그래픽 모듈 불러오기

def click(key):
    if key=='=':
        result=eval(e1.get())
        result=str(result)
        e1.insert(END, "="+result)
    elif key=='C':
        e1.delete(0, END)
    elif key=='<-':
        length=len(e1.get())
        e1.delete(length-1, END)
    else:
        e1.insert(END, key)
#버튼
button_list=[
    '7','8','9','/','C',
    '4','5','6','*','<-',
    '1','2','3','-','',
    '0','.','=','+','']
  
win=Tk()
win.title("아주 멋져서 눈이 부신 계산기")

e1=Entry(win, width=42, bg='pink')
e1.grid(row=0, column=0,columnspan=5)

row_index=1
col_index=0

for button_text in button_list:
    def pro(t=button_text):
        click(t)
    Button(win,text=button_text,width=7, command=pro).grid(row=row_index, column=col_index)
    col_index=col_index+1
    if col_index >4:
        row_index+=1
        col_index=0


