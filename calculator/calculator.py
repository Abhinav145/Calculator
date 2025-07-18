from tkinter import *
first_num=second_num=operator=None
def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

def get_clear():
    result_label.config(text='')

def get_operator(oper):
    global first_num,operator

    first_num=int(result_label['text'])
    operator=oper
    result_label.config(text='')

def do_operation():
    global first_num,second_num,operator
    second_num=int(result_label['text'])

    if operator=='+':
        result_label.config(text=first_num+second_num)

    elif operator=='-':
        result_label.config(text=first_num-second_num)
    
    elif operator=='*':
        result_label.config(text=first_num*second_num)
    else:
        if second_num==0:
            result_label.config(text='Error')
        elif operator=='/':
            result_label.config(text=first_num/second_num)
       
root=Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,sticky="w",pady=(50,25))
result_label.config(font=('verdana',30,'bold'))


btn7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(7)) 
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height='2',command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

add=Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('+'))
add.grid(row=1,column=4)
add.config(font=('vendana',15))

btn4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

sub=Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('-'))
sub.grid(row=2,column=4)
sub.config(font=('vendana',15))

btn1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

mul=Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('*'))
mul.grid(row=3,column=4)
mul.config(font=('vendana',14))

btn0=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=0)
btn0.config(font=('verdana',14))

btnc=Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command=get_clear)
btnc.grid(row=4,column=1)
btnc.config(font=('verdana',14))

equal=Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=do_operation)
equal.grid(row=4,column=2)
equal.config(font=('verdana',14))

div=Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda:get_operator('/'))
div.grid(row=4,column=4)
div.config(font=('vendana',15))











root.mainloop()
