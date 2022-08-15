from cgitb import text
from email.quoprimime import body_length
from faulthandler import disable
from pickle import GLOBAL
from tkinter import *
from turtle import color, width
calcWindow=Tk()
calcWindow.title("Calculator")
calcWindow.geometry("160x308")
calcWindow.resizable(0,0)
#calcWindow.configure( color='black')
mathexpression=""
input_text=StringVar()


def buttonclick(var):
    exp=var
    set_mathexpression(exp)
    #print (exp)
    
def set_mathexpression(exp):
    global mathexpression
    mathexpression=mathexpression+str(exp)
    input_text.set(mathexpression)

def btn_clr():
    mathexpression=""
    input_text.set("")

def btn_eql():
    global mathexpression
  #  answer=eval(mathexpression)
  #  input_text.set(answer)
    mathexpression=""

def btn_on():
    text1.configure(state='normal')



input_frame = Frame(calcWindow, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
    

text1= Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=12, bg="#eee", bd=0, justify=RIGHT)    

text1.grid(row=0, column=0)
 
text1.pack(ipady=10)
text1.configure(state='disabled')

#text1.pack(expand = True, fill = "both")  
#textfeild.pack()



btn_frame = Frame(calcWindow, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
btn_frame.pack()

btn1=Button(btn_frame,text=1,height=2,width=4,background='gray',command=lambda:buttonclick(1))
btn2=Button(btn_frame,text=2,height=2,width=4,background='gray',command=lambda:buttonclick(2))
btn3=Button(btn_frame,text=3,height=2,width=4,background='gray',command=lambda:buttonclick(3))
btn4=Button(btn_frame,text=4,height=2,width=4,background='gray',command=lambda:buttonclick(4))
btn5=Button(btn_frame,text=5,height=2,width=4,background='gray',command=lambda:buttonclick(5))
btn6=Button(btn_frame,text=6,height=2,width=4,background='gray',command=lambda:buttonclick(6))
btn7=Button(btn_frame,text=7,height=2,width=4,background='gray',command=lambda:buttonclick(7))
btn8=Button(btn_frame,text=8,height=2,width=4,background='gray',command=lambda:buttonclick(8))
btn9=Button(btn_frame,text=9,height=2,width=4,background='gray',command=lambda:buttonclick(9))
btn0=Button(btn_frame,text=0,height=2,width=4,background='gray',command=lambda:buttonclick(0))
btn00=Button(btn_frame,text="00",height=2,width=4,background='gray',command=lambda:buttonclick(00))
btndot=Button(btn_frame,text=".",height=2,width=4,background='gray',command=lambda:buttonclick('.'))
btnon=Button(btn_frame,text="ON",height=2,width=4,background='gray',command=lambda:btn_on())
btnadd=Button(btn_frame,text="+",height=2,width=4,background='gray',command=lambda:buttonclick('+'))
btnmin=Button(btn_frame,text="-",height=2,width=4,background='gray',command=lambda:buttonclick('-'))
btnmult=Button(btn_frame,text="*",height=2,width=4,background='gray',command=lambda:buttonclick('*'))
btndiv=Button(btn_frame,text="/",height=2,width=4,background='gray',command=lambda:buttonclick('/'))
btnperc=Button(btn_frame,text="%",height=2,width=4,background='gray',command=lambda:buttonclick('%'))
btnsqr=Button(btn_frame,text="^",height=2,width=4,background='gray',command=lambda:buttonclick('^'))
btnroot=Button(btn_frame,text="~",height=2,width=4,background='gray',command=lambda:buttonclick('~'))
btneql=Button(btn_frame,text="=",height=2,width=4,background='white',command=btn_eql())
btnclr=Button(btn_frame,text="C",height=2,width=4,background='orange',command=btn_clr())
btnopen=Button(btn_frame,text="(",height=2,width=4,background='gray',command=lambda:buttonclick('('))
btncls=Button(btn_frame,text=")",height=2,width=4,background='gray',command=lambda:buttonclick(')'))


#text1.grid(row=0,column=0,rowspan=4,columnspan=2)

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnon.grid(row=4,column=3)

btn4.grid(row=5,column=0)
btn5.grid(row=5,column=1)
btn6.grid(row=5,column=2)
btnadd.grid(row=5,column=3)

btn7.grid(row=6,column=0)
btn8.grid(row=6,column=1)
btn9.grid(row=6,column=2)
btnmin.grid(row=6,column=3)

btn0.grid(row=7,column=0)
btn00.grid(row=7,column=1)
btndot.grid(row=7,column=2)
btnmult.grid(row=7,column=3)

btnsqr.grid(row=8,column=0)
btnroot.grid(row=8,column=1)
btnperc.grid(row=8,column=2)
btndiv.grid(row=8,column=3)


btnopen.grid(row=9,column=0)
btncls.grid(row=9,column=1)
btnclr.grid(row=9,column=2)
btneql.grid(row=9,column=3)







calcWindow.mainloop()
