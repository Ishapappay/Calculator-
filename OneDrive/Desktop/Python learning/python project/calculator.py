from cgitb import text
from email.quoprimime import body_length
from tkinter import *
from turtle import color, width
calcWindow=Tk()
calcWindow.title("Simple Calculator")
calcWindow.geometry("300x300")
#calcWindow.configure( color='black')
text1=Entry(calcWindow)
#textfeild.pack()
mathexpression=""

btn1=Button(calcWindow,text=1,height=2,width=4,background='gray')
btn2=Button(calcWindow,text=2,height=2,width=4,background='gray')
btn3=Button(calcWindow,text=3,height=2,width=4,background='gray')
btn4=Button(calcWindow,text=4,height=2,width=4,background='gray')
btn5=Button(calcWindow,text=5,height=2,width=4,background='gray')
btn6=Button(calcWindow,text=6,height=2,width=4,background='gray')
btn7=Button(calcWindow,text=7,height=2,width=4,background='gray')
btn8=Button(calcWindow,text=8,height=2,width=4,background='gray')
btn9=Button(calcWindow,text=9,height=2,width=4,background='gray')
btn0=Button(calcWindow,text=0,height=2,width=4,background='gray')
btn00=Button(calcWindow,text="00",height=2,width=4,background='gray')
btndot=Button(calcWindow,text=".",height=2,width=4,background='gray')
btnon=Button(calcWindow,text="ON",height=2,width=4,background='gray')
btnadd=Button(calcWindow,text="+",height=2,width=4,background='gray')
btnmin=Button(calcWindow,text="-",height=2,width=4,background='gray')
btnmult=Button(calcWindow,text="*",height=2,width=4,background='gray')
btndiv=Button(calcWindow,text="/",height=2,width=4,background='gray')
btnperc=Button(calcWindow,text="%",height=2,width=4,background='gray')
btnsqr=Button(calcWindow,text="^",height=2,width=4,background='gray')
btnroot=Button(calcWindow,text="~",height=2,width=4,background='gray')
btneql=Button(calcWindow,text="=",height=2,width=4,background='white')
btnclr=Button(calcWindow,text="C",height=2,width=4,background='orange')
btnopen=Button(calcWindow,text="(",height=2,width=4,background='gray')
btncls=Button(calcWindow,text=")",height=2,width=4,background='gray')


text1.grid(row=0,column=0,rowspan=4,columnspan=2)

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
