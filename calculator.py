from tkinter import *

global st
global ftnum 
ftnum=0
st=""
root = Tk()
root.title("Simple Calculator")

e=Entry(root, width=60, borderwidth=5,fg="green",bg="blue")
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def buttonclick(number):
    current=e.get()
    if current=="":
        current="0"    
    e.delete(0,END)
    S1=int(current)*10+number
    e.insert(0, S1)

def Symbol(str):
    global st
    global ftnum
    current=e.get()
    if current=="":
       current="0"

    ftnum=current
    st=str
    e.delete(0,END)

def Equal():
    global ftnum
    global st
    current=e.get()
    if current=="":
        current=0
    sdnum=current
    e.delete(0,END)
    
    if (st=="+"):
      sum=int(ftnum)+int(sdnum)
      e.insert(0, sum)

    elif(st=="-"):
      sum=int(ftnum)-int(sdnum)
      e.insert(0, sum)

    elif(st=="*"):
      sum=int(ftnum)*int(sdnum)
      e.insert(0, sum)

    elif(st=="/"):
      sum=float(ftnum)/float(sdnum)
      e.insert(0, sum)



      
def Clear():
   e.delete(0,END)
   global ftnum
   ftnum=0

   




button_1=Button(root,text="1", padx=40, pady=20,command=lambda: buttonclick(1))
button_2=Button(root,text="2", padx=40, pady=20,command=lambda: buttonclick(2))
button_3=Button(root,text="3", padx=40, pady=20,command=lambda: buttonclick(3))
button_4=Button(root,text="4", padx=40, pady=20,command=lambda: buttonclick(4))
button_5=Button(root,text="5", padx=40, pady=20,command=lambda: buttonclick(5))
button_6=Button(root,text="6", padx=40, pady=20,command=lambda: buttonclick(6))
button_7=Button(root,text="7", padx=40, pady=20,command=lambda: buttonclick(7))
button_8=Button(root,text="8", padx=40, pady=20,command=lambda: buttonclick(8))
button_9=Button(root,text="9", padx=40, pady=20,command=lambda: buttonclick(9))
button_0=Button(root,text="0", padx=40, pady=20,command=lambda: buttonclick(0))
button_add=Button(root,text="+", padx=39, pady=20,command=lambda: Symbol("+"))
button_sub=Button(root,text="-", padx=40, pady=20,command=lambda: Symbol("-"))
button_mul=Button(root,text="*", padx=40, pady=20,command=lambda: Symbol("*"))
button_div=Button(root,text="/", padx=40, pady=20,command=lambda: Symbol("/"))
button_equ=Button(root,text="=", padx=140, pady=20,command=Equal)
button_cle=Button(root,text="Clear", padx=133, pady=20,command=Clear)


button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=1,column=3)
button_5.grid(row=2,column=0)
button_6.grid(row=2,column=1)

button_7.grid(row=2,column=2)
button_8.grid(row=2,column=3)
button_9.grid(row=3,column=0)

button_0.grid(row=3,column=1)
button_add.grid(row=3,column=2)
button_sub.grid(row=3,column=3)

button_mul.grid(row=5,column=0)
button_cle.grid(row=5,column=1,columnspan=3)

button_div.grid(row=6,column=0)
button_equ.grid(row=6,column=1,columnspan=3)

root.mainloop()

