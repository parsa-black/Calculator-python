from tkinter import *
import tkinter.messagebox

# ======================= tanzimat ========================

root = Tk()
root.geometry('400x400')
root.title('calculator')
root.resizable(width=False, height=False)
root.configure(bg='gray')
color='gray'
# ======================= maqadir =========================

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# ======================= function =========================

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error','Something went wrong')
    elif ms == 'division \'ZERO\' error':
        tkinter.messagebox.showerror('Error','Can not division')

def plus():
    try:
        values = float(num1.get()) + float(num2.get())
        res_value.set(values)
    except:
        errorMsg('error')

def minus():
    try:
        values = float(num1.get()) - float(num2.get())
        res_value.set(values)
    except:
        errorMsg('error')

def zarb():
    try:
        values = float(num1.get()) * float(num2.get())
        res_value.set(values)
    except:
        errorMsg('error')

def divide():
    if num2.get() == '0' :
        errorMsg('division \'ZERO\' error')
    else :
        try:
            values = float(num1.get()) / float(num2.get())
            res_value.set(values)
        except:
            errorMsg('error')

#======================= freame =========================

top_first = Frame(root, width=400, height=100, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=100, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=100, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=100, bg=color)
top_forth.pack(side=TOP)
#======================= buttons =========================
btn_plus= Button(top_third, text="+", width=10, command =lambda :plus())
btn_plus.pack(side=LEFT,padx=10,pady=10 )

btn_MIN= Button(top_third, text="-", width=10, command =lambda :minus())
btn_MIN.pack(side=LEFT,padx=10,pady=10)

btn_mul= Button(top_third, text="*", width=10, command =lambda :zarb())
btn_mul.pack(side=LEFT,padx=10,pady=10)

btn_divide= Button(top_third, text="/", width=10, command =lambda :divide())
btn_divide.pack(side=LEFT,padx=10,pady=10)
#======================= Enteries and leibels=========================
label_first_num= Label(top_first, text="input num 1 :",bg="red")
label_first_num.pack(side=LEFT,pady=5)

first_num=Entry(top_first,highlightbackground="red", textvariable = num1)
first_num.pack(side=LEFT,pady =5)

label_second_num= Label(top_first, text="input num 2 :",bg="red")
label_second_num.pack(side=LEFT,pady=5)

second_num=Entry(top_first,highlightbackground="red", textvariable = num2)
second_num.pack(side=LEFT,pady =5)

res = Label(top_forth, text="Result  :",bg="yellow")
res.pack(side=LEFT,pady=5)

res_num=Entry(top_forth,highlightbackground="yellow", textvariable = res_value)
res_num.pack(side=LEFT,pady =5)


root.mainloop()
