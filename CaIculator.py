from tkinter import *
from tkinter import messagebox
from tkinter import ttk
s=0
k=''
root=Tk()
root.geometry('380x290')
root.title("Siva Creations")
style=ttk.Style()
class fu():
    def __init__(self,num):
        if num==".":
            global k
            k=" "
            equation.set(k)
        elif num != "=":
            k=k+num
            equation.set(k)
        elif num=="=":
            c = str(eval(k))
            equation.set(c)
            k=""
            k=str(c)
        elif num=='MSG':
           messagebox.showinfo(equation)


if __name__ == "__main__":
    l=[]
    w=[]

    root.configure(background="cyan")
    equation = StringVar()
    m = Entry(root, width=56, textvariable=equation)
    m.place(x=10, y=50)
    btn1=Button(root,text='1',command=lambda :fu('1'),background='cyan',foreground='black',width=9,bd=5)
    btn1.place(x=10,y=100)
    btn2 = Button(root, text='2', command=lambda : fu('2'),background='cyan',foreground='black',width=9,bd=5)
    btn2.place(x=98, y=100)
    btn3 = Button(root, text='3', command=lambda : fu('3'),background='cyan',foreground='black',width=9,bd=5)
    btn3.place(x=186, y=100)
    btnA =Button(root, text='+', command=lambda : fu("+"),background='cyan',foreground='black',width=9,bd=5)
    btnA.place(x=274, y=100)
    btn4=Button(root,text='4',command=lambda :fu('4'),background='cyan',foreground='black',width=9,bd=5)
    btn4.place(x=10,y=140)
    btn5 = Button(root, text='5', command=lambda : fu('5'),background='cyan',foreground='black',width=9,bd=5)
    btn5.place(x=98, y=140)
    btn6 =Button(root, text='6', command=lambda : fu('6'),background='cyan',foreground='black',width=9,bd=5)
    btn6.place(x=186, y=140)
    btnS = Button(root, text='-', command=lambda : fu("-"),background='cyan',foreground='black',width=9,bd=5)
    btnS.place(x=274, y=140)
    btn7=Button(root,text='7',command=lambda :fu('7'),background='cyan',foreground='black',width=9,bd=5)
    btn7.place(x=10,y=180)
    btn8 =Button(root, text='8', command=lambda : fu('8'),background='cyan',foreground='black',width=9,bd=5)
    btn8.place(x=98, y=180)
    btn9 =Button(root, text='9', command=lambda : fu('9'),background='cyan',foreground='black',width=9,bd=5)
    btn9.place(x=186, y=180)
    btnM =Button(root, text='*', command=lambda : fu("*"),background='cyan',foreground='black',width=9,bd=5)
    btnM.place(x=274, y=180)
    btnD=Button(root,text='/',command=lambda :fu('/'),background='cyan',foreground='black',width=9,bd=5)
    btnD.place(x=10,y=220)
    btnD=Button(root,text='CLEAR',command=lambda :fu('.'),background='red',foreground='black',width=9,bd=5)
    btnD.place(x=10,y=14)
    btn2 =Button(root, text='0', command=lambda : fu('0'),background='cyan',foreground='black',width=9,bd=5)
    btn2.place(x=98, y=220)
    btn3 =Button(root, text='%', command=lambda : fu('%'),background='cyan',foreground='black',width=9,bd=5)
    btn3.place(x=186, y=220)
    btnA =Button(root, text='=', command=lambda : fu("="),background='cyan',foreground='black',width=9,bd=5)
    btnA.place(x=274, y=220)


    root.mainloop()
