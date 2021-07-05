from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from tkinter import messagebox
#=================================================
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import parser
#===================================================
from math import *
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.ticker import *
#===========================================draw====================================================
def draw(x1,x2,s):
    try:
        w=0
        formula = s
        code = parser.expr(formula).compile()
        xs=linspace(x1,x2,int((x2-x1+1)*20))
        xn=[]
        yn=[]
        plt.gca().set_aspect("equal")
        for x in xs:
            if isnan(eval(code))==True or isinf(eval(code))==True:
                xn.clear()
                yn.clear()
            else:
                xn.append(x)
                yn.append(eval(code))
                plt.plot(xn,yn,color='green')
        plt.axvline(0, color='r',linewidth=3)
        plt.axhline(0, color='r',linewidth=3)
        plt.grid(b=True, which='major', color='k', linestyle='-')
        plt.grid(b=True, which='minor', color='r', linestyle=':', alpha=0.9)
        plt.minorticks_on()
        plt.show()
    except:
        messagebox.showwarning("Warning","please enter correct equation")      
#======================================================================================================
def In():
        f=open("usrm.txt","r")
        s=f.readlines()
        win = tk.Tk()
        win.geometry("1000x500")
        win.title("INSTRUCTION")
        tk.Label(win,
                        text = "ARYABHATTA",
                        font = ("Times New Roman", 35),
                        background = 'green',
                        foreground = "white").place(x= 600,y = 0)
        text_area = st.ScrolledText(win,
                                                                width = 90,
                                                                height = 35,
                                                                font = ("Times New Roman",
                                                                                15),bg='pale goldenrod')

        text_area.place(x=300,y=50)
        text_area.insert(tk.INSERT,
         s)
        text_area.configure(state ='disabled')
        win.mainloop()
#======================================================================================================
root = Tk()
root.wm_title("ARYABHATTA")
root.geometry("6000x6000")
global logo,logo_final
logo = PhotoImage(file="bg.png")
logo_final= Label(root,image=logo,bg='#FFFFFF',fg = "Blue").place(x=0,y=0)
root.resizable(width=True, height=True)
horizontal_screen = root.winfo_screenwidth() / 2 - root.winfo_reqwidth()
vertical_screen = root.winfo_screenheight() / 2 - root.winfo_reqheight()
root.geometry("+%d+%d" % (horizontal_screen, vertical_screen))
canvas = Canvas(root)
Button(root, fg = "black", font = ('arial', 20, 'bold'), width = 10,activebackground="green",bg = 'green',text="Draw Graph", command=lambda:g(e1,r1,r2,root)).place(x=800, y=500)
Button(root, fg = "black", font = ('arial', 20, 'bold'), width = 10,activebackground="green",bg = 'green',text="HELP ?", command=lambda:In()).place(x=200, y=500)
Label(root, fg = "black", font = ('arial', 20, 'bold'), width = 10,bg = 'magenta2',text = "f(x) = ") .place(x=100,y=300)
Label(root,fg= "black", font = ('arial', 20, 'bold'), width = 25,bg = 'magenta2',text = "Domain of function f(x) is from ") .place(x=50,y=400)
Label(root,fg= "black", font = ('arial', 20, 'bold'), width = 5,bg = 'magenta2',text = " to ") .place(x=690,y=400)
r1 = Entry(root,bd=8,font = ('arial', 20, 'bold'),width=10,bg='#bc946b',insertwidth = 5)
r1.place(x=500,y=395)
r2=Entry(root,bd=8,font = ('arial', 20, 'bold'),width=10,bg='#bc946b',insertwidth = 5)
r2.place(x=800,y=395)
e1 = Entry(root,bd=10,font = ('arial', 20, 'bold'),width=30,bg='#bc947b',insertwidth = 5)
e1.place(x = 300, y = 295)
def g(e1,r1,r2,root):
    try:
        g1=e1.get()
        g2=int(r1.get())
        g3=int(r2.get())
        draw(g2,g3,g1) 
    except:
        messagebox.showwarning("Warning","Warning message for user . please fill up correctly")
def Hello(root):
        t=tkinter.Text(root)
        bot.title("Instructions")
        x=open("usrm.txt", "r")
        l=x.read()
        t.insert(tkinter.INSERT,l)
        t.grid(columnspan=11)
        bot.mainloop       
root.mainloop()
