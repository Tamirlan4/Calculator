import tkinter as tk

def add_digit(digit):
    value = calc.get()
    if len(value) >= 2:
        value = value
        if value[-1] =='0'       and value[-2] in '+-*/':
            value = value[:-1]
    elif value[0]=='0':
        value = value[1:]

    calc.delete(0,tk.END)
    calc.insert(0,value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value + operation)

def calculation():
    value = calc.get()
    calc.delete(0,tk.END)
    if value[-1] in '+-*/':
        value = value[:-1]
    calc.insert(0,eval(value))
    
def clear():
    value = calc.get()
    value = value[:-1] 
    calc.delete(0,tk.END)
    if len(value) == 0:
        value = '0'
    calc.insert(0,value) 

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial',22), command=lambda : add_digit(digit))
    
def make_operation_button(operation):
        return tk.Button(text=operation, bd=5, font=('Arial',22), fg='red' , command=lambda : add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',22), fg='red' , command=lambda : calculation())

def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',22), fg='red' , command=lambda : clear())

win = tk.Tk()   
win.iconbitmap('./assets/ico/icon.ico')
win.geometry("240x300+100+200")
win['bg'] = "#FF9900"
win.title('Калькулятор')
win.resizable(width=False, height=False)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial',15),width=15,background='#F5F5F5',)
calc.insert(0,'0')
calc.grid(row = 0, column = 0, columnspan=4, stick='we',padx=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=2, pady=2)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=2, pady=2)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=2, pady=2)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=2, pady=2)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=2, pady=2)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=2, pady=2)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=2, pady=2)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=2, pady=2)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=2, pady=2)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=2, pady=2)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=2, pady=2)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=2, pady=2)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=2, pady=2)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=2, pady=2)
make_clear_button('C').grid(row=4,column=1, stick='wens', padx=2, pady=2)
make_calc_button('=').grid(row=4, column=2, stick='wens', padx=2, pady=2)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)
win.grid_rowconfigure(5,minsize=60)

win.mainloop()
