from tkinter import *

mmd = Tk()
mmd.title("Calculator")
mmd.geometry("300x300")

l0 = Label(mmd, text="First Number:")
l0.pack()

entry = Entry(mmd)
entry.pack()

l1 = Label(mmd, text="Second Number:")
l1.pack()

entry1 = Entry(mmd)
entry1.pack()

def calculate(op):
    try:
        a = float(entry.get())
        b = float(entry1.get())

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                label_result.config(text="Error: Division by zero")
                return
            result = a / b

        label_result.config(text=f"Result: {result}")

    except:
        label_result.config(text="Invalid input")

label_result = Label(mmd, text="Result:")
label_result.pack(pady=5)

frame = Frame(mmd)
frame.pack()

Button(frame, text="+", width=5, command=lambda: calculate('+')).grid(row=0, column=0)
Button(frame, text="-", width=5, command=lambda: calculate('-')).grid(row=0, column=1)
Button(frame, text="*", width=5, command=lambda: calculate('*')).grid(row=0, column=2)
Button(frame, text="/", width=5, command=lambda: calculate('/')).grid(row=0, column=3)

mmd.mainloop()
