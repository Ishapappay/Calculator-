from cgitb import text
from email.quoprimime import body_length
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
#text1=Label(calcWindow, text = "Label",  
 #   font = ("Cambria Math", 20),  
  #  background = "white",  
   # textvariable=mathexpression)
def buttonclick(var):
    exp=var
    set_mathexpression(exp)
    #print (exp)
    
def set_mathexpression(exp):
    global mathexpression
    mathexpression=mathexpression+str(exp)
    #text1.bind(mathexpression)
    input_text.set(mathexpression)




input_frame = Frame(calcWindow, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
    

text1= Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=12, bg="#eee", bd=0, justify=RIGHT)    

text1.grid(row=0, column=0)
 
text1.pack(ipady=10)

#text1.pack(expand = True, fill = "both")  
#textfeild.pack()



btn_frame = Frame(calcWindow, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
btn_frame.pack()

btn1=Button(btn_frame,text=1,height=2,width=4,background='gray',command=buttonclick(1))
btn2=Button(btn_frame,text=2,height=2,width=4,background='gray',command=buttonclick(2))
btn3=Button(btn_frame,text=3,height=2,width=4,background='gray',command=buttonclick(3))
btn4=Button(btn_frame,text=4,height=2,width=4,background='gray',command=buttonclick(4))
btn5=Button(btn_frame,text=5,height=2,width=4,background='gray',command=buttonclick(5))
btn6=Button(btn_frame,text=6,height=2,width=4,background='gray',command=buttonclick(6))
btn7=Button(btn_frame,text=7,height=2,width=4,background='gray',command=buttonclick(7))
btn8=Button(btn_frame,text=8,height=2,width=4,background='gray',command=buttonclick(8))
btn9=Button(btn_frame,text=9,height=2,width=4,background='gray',command=buttonclick(9))
btn0=Button(btn_frame,text=0,height=2,width=4,background='gray',command=buttonclick(0))
btn00=Button(btn_frame,text="00",height=2,width=4,background='gray',command=buttonclick(00))
btndot=Button(btn_frame,text=".",height=2,width=4,background='gray',command=buttonclick('.'))
btnon=Button(btn_frame,text="ON",height=2,width=4,background='gray',command=buttonclick(1))
btnadd=Button(btn_frame,text="+",height=2,width=4,background='gray',command=buttonclick('+'))
btnmin=Button(btn_frame,text="-",height=2,width=4,background='gray',command=buttonclick('-'))
btnmult=Button(btn_frame,text="*",height=2,width=4,background='gray',command=buttonclick('*'))
btndiv=Button(btn_frame,text="/",height=2,width=4,background='gray',command=buttonclick('/'))
btnperc=Button(btn_frame,text="%",height=2,width=4,background='gray',command=buttonclick('%'))
btnsqr=Button(btn_frame,text="^",height=2,width=4,background='gray',command=buttonclick('^'))
btnroot=Button(btn_frame,text="~",height=2,width=4,background='gray',command=buttonclick('~'))
btneql=Button(btn_frame,text="=",height=2,width=4,background='white',command=buttonclick('='))
btnclr=Button(btn_frame,text="C",height=2,width=4,background='orange',command=buttonclick('c'))
btnopen=Button(btn_frame,text="(",height=2,width=4,background='gray',command=buttonclick('('))
btncls=Button(btn_frame,text=")",height=2,width=4,background='gray',command=buttonclick(')'))


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
