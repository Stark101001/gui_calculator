from tkinter import *

window = Tk()
window.title("CALCULATOR")
window.geometry("390x495+700+140")
window.config(bg="grey")
window.resizable(0, 0)
window.iconbitmap("E:\\c.ico")

# ----------------Functions-------------
def Enter_number(x):
    if entry_box.get() == '0':
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


def Enter_operator(x):
    # if entry_box.get() !='0':
    length = len(entry_box.get())
    entry_box.insert(length, btn_operator[x]['text'])


def Clear():
    entry_box.delete(0, 'end')
    entry_box.insert(0, '0')


result = 0
history = []


def Func_equal():
    all_text = entry_box.get()
    Result = eval(all_text)
    entry_box.delete(0, 'end')
    entry_box.insert(0, Result)
    history.append(all_text)
    history.reverse()
    status.configure(text='History:' + ' | '.join(history[:10]))


def Func_del():
    length = len(entry_box.get())
    entry_box.delete(length - 1, 'end')
    if length == 1:
        entry_box.insert(0, '0')


# ---------------Entry box-------------
entry_box = Entry(font='verdana 14 bold', bd=8, width=22, justify=RIGHT, bg="lightblue")
entry_box.insert(0, "0")
entry_box.place(x=30, y=10)

# ---------------BUTTONS------------------
btn_number = []
for i in range(0, 10):
    btn_number.append(Button(width=8, text=str(i), bd=6, command=lambda x=i: Enter_number(x)))

btn_text = 9
for i in range(0, 3):
    for j in range(0, 3):
        btn_number[btn_text].place(x=30 + j * 90, y=70 + i * 70)
        btn_text -= 1

btn_zero = Button(width=8, text=0, bd=6, command=lambda x=0: Enter_number(x))
btn_zero.place(x=120, y=280)

clr_photo = PhotoImage(file="clear.png")

btn_clr = Button(image=clr_photo, width=87, height=32, font=("monotype", 9, 'bold'), bd=6, command=Clear)
btn_clr.place(x=210, y=330)

btn_point = Button(width=8, text='.', font=("monotype", 9, 'bold'), bd=6, command=lambda x='.': Enter_number(x))
btn_point.place(x=210, y=280)

btn_equal = Button(width=8, text='=', font=("monotype", 9, 'bold'), bd=6, command=Func_equal)
btn_equal.place(x=30, y=280)

photo = PhotoImage(file="delete.png")

btn_del = Button(image=photo, width=150, height=38, text='Del', font=("monotype", 9, 'bold'), bd=4, command=Func_del)
btn_del.place(x=30, y=330)

# ---------------Operators_Buttons-----------------

btn_operator = []

for i in range(0, 4):
    btn_operator.append(Button(width=8, font='times 10 bold', bd=5, command=lambda x=i: Enter_operator(x)))

btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for i in range(4):
    btn_operator[i].place(x=300, y=70 + i * 70)

# ------------------HISTORY TAG---------------------

status = Label(window, text='History:', bg="lightblue", relief=SUNKEN, width=38, height=3, anchor=W,
               font='verdana 11 bold')
status.place(x=1, y=400)

name = Label(window, text="Created by: Pawan Kumar", font='SFArborcrest,BOLD', bg="grey")
name.place(x=200, y=465)

window.mainloop()
