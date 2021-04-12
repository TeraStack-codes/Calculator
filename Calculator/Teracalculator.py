#Hope You like it :)

#Imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Main

root = tk.Tk()
root.geometry('250x400+300+300')
root.iconbitmap(r'Calculator\Images\python_image.ico')
root.resizable(0,0)
root.title('CalCuLaToR')

#Variables

data = StringVar()
val = ""
operator = ""
ASDF = 0

#Functions for number buttons

def btn_1_clicked():
    global val
    val = val + '1'
    data.set(val)

def btn_2_clicked():
    global val 
    val = val + '2'
    data.set(val)

def btn_3_clicked():
    global val
    val = val + '3'
    data.set(val)

def btn_4_clicked():
    global val
    val = val + '4'
    data.set(val)

def btn_5_clicked():
    global val 
    val = val + '5'
    data.set(val)

def btn_6_clicked():
    global val
    val = val + '6'
    data.set(val)

def btn_7_clicked():
    global val
    val = val + '7'
    data.set(val)

def btn_8_clicked():
    global val 
    val = val + '8'
    data.set(val)

def btn_9_clicked():
    global val
    val = val + '9'
    data.set(val)

def btn_0_clicked():
    global val
    val = val + '0'
    data.set(val)

#Function for C and =

def btn_C_clicked():
    global val,ASDF,operator 
    val = ''
    ASDF = 0
    operator = ''
    data.set(val)

def result():
    global A, val , operator
    val2 = val 
    if operator == '+':
        x = int((val2.split('+')[1]))
        Cat = ASDF + x
        data.set(Cat)
        val = str(Cat)
    elif operator == '-':
        x = int((val2.split('-')[1]))
        Cat = ASDF - x
        data.set(Cat)
        val = str(Cat)
    elif operator == '*':
        x = int((val2.split('*')[1]))
        Cat = ASDF * x
        data.set(Cat)
        val = str(Cat)
    elif operator == '/':
        x = int((val2.split('/')[1]))
        if x == 0:
            messagebox.showerror('NOT POSSIBLE !!!', 'Dividing by 0 is not supported.')
            A = ""
            val = ""
            data.set(val)
        else :
            Cat = ASDF / x
            data.set(Cat)
            val = str(Cat)
    

#Function for Operators

def btn_plus_clicked():
    global val,ASDF,operator
    ASDF = int(float(val))
    operator = '+'
    val = val + "+" 
    data.set(val)

def btn_minus_clicked():
    global val,ASDF,operator
    ASDF = int(float(val))
    operator = '-'
    val = val + "-" 
    data.set(val)

def btn_star_clicked():
    global val,ASDF,operator
    ASDF = int(float(val))
    operator = '*'
    val = val + "*" 
    data.set(val)

def btn_divide_clicked():
    global val,ASDF,operator
    ASDF = int(float(val))
    operator = '/'
    val = val + "/" 
    data.set(val)


#Label

qwerty=Label(root,
    text = "Hello",
    anchor = SE,
    textvariable = data,
    background = '#ffffff',
    fg = '#000000',
    font = ('Verenda',22) )

qwerty.pack(expand = True, fill = 'both')

#Rows

btnrow1 = Frame(root,bg = '#000000')
btnrow1.pack(expand = True, fill = "both", )

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both", )

btnrow3 = Frame(root,bg='#000000')
btnrow3.pack(expand = True, fill = "both", )

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both", )

#Buttons

btn1 = Button(
    btnrow1,
    text = '1',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_1_clicked
)

btn1.pack(side = LEFT, expand = True,fill='both')

btn2 = Button(
    btnrow1,
    text = '2',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_2_clicked
)

btn2.pack(side = LEFT, expand = True,fill='both')

btn3 = Button(
    btnrow1,
    text = '3',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_3_clicked
)

btn3.pack(side = LEFT, expand = True,fill='both')

btn4 = Button(
    btnrow1,
    text = '+',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_plus_clicked
)

btn4.pack(side = LEFT, expand = True,fill='both')



btn5 = Button(
    btnrow2,
    text = '4',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_4_clicked
)

btn5.pack(side = LEFT, expand = True,fill='both')

btn6 = Button(
    btnrow2,
    text = '5',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_5_clicked
)

btn6.pack(side = LEFT, expand = True,fill='both')

btn7 = Button(
    btnrow2,
    text = '6',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_6_clicked
)

btn7.pack(side = LEFT, expand = True,fill='both')

btn8 = Button(
    btnrow2,
    text = '-',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_minus_clicked
)

btn8.pack(side = LEFT, expand = True,fill='both')




btn9 = Button(
    btnrow3,
    text = '7',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_7_clicked
)

btn9.pack(side = LEFT, expand = True,fill='both')

btn10 = Button(
    btnrow3,
    text = '8',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_8_clicked
)

btn10.pack(side = LEFT, expand = True,fill='both')

btn11 = Button(
    btnrow3,
    text = '9',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_9_clicked
)

btn11.pack(side = LEFT, expand = True,fill='both')

btn12 = Button(
    btnrow3,
    text = '*',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_star_clicked
)

btn12.pack(side = LEFT, expand = True,fill='both')




btn13 = Button(
    btnrow4,
    text = 'C',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_C_clicked
)

btn13.pack(side = LEFT, expand = True,fill='both')

btn14 = Button(
    btnrow4,
    text = '0',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_0_clicked
)

btn14.pack(side = LEFT, expand = True,fill='both')

btn15 = Button(
    btnrow4,
    text = '/',
    font = ('Verdana', 22),
    relief = GROOVE,
    border = 1,
    command = btn_divide_clicked
)

btn15.pack(side = LEFT, expand = True,fill='both')

btn16 = Button(
    btnrow4,
    text = '=',
    font = ('Verdana', 22),
    bg = "Orange",
    relief = GROOVE,
    border = 1,
    command = result

)

btn16.pack(side = LEFT, expand = True,fill='both')

root.mainloop()