from tkinter import *
from tkinter import ttk, messagebox
import model as m
import logger as log
import view

logger = []
spisok = []
otvet = ""
root = Tk()
#Основные параметры рамки
root['bg'] = 'black'
root.title('Калькулятор')
root.geometry("260x300")
#Фиксация изменения размера рамки
root.resizable(width=False, height=False)
#Верняя часть приложения со строкой ввода
frame1 = Frame (root,bg="gold3")
frame1.place(relwidth=1, relheight=0.4)

label_header_line = ttk.Label(font=10, text="Введенная строка:", background="gold3")
label_header_line.pack(anchor=NW, padx=0, pady=[20, 0])

label_enter = ttk.Label(font=50)
label_enter.pack(anchor=NW, padx=0, pady=0)

label_header_result = ttk.Label(font=10, text="Результат:", background="gold3")
label_header_result.pack(anchor=NW, padx=0, pady=0)

label_result = ttk.Label(font=50)
label_result.pack(anchor=NW, padx=0, pady=0)

#Строка введения значений
#field_enter = Entry(frame1, bg="white", font=100)
#field_enter.pack(pady=5,)

#def get_field_enter():
    #return field_enter.get()

def set_label_enter(text):
    label_enter["text"] = text

def set_label_result(text):
    label_result["text"] = text

def click_btn1():
    spisok.append("1")
    set_label_enter(spisok)

def click_btn2():
    spisok.append("2")
    set_label_enter(spisok)

def click_btn3():
    spisok.append("3")
    set_label_enter(spisok)

def click_btn4():
    spisok.append("4")
    set_label_enter(spisok)

def click_btn5():
    spisok.append("5")
    set_label_enter(spisok)

def click_btn6():
    spisok.append("6")
    set_label_enter(spisok)

def click_btn7():
    spisok.append("7")
    set_label_enter(spisok)

def click_btn8():
    spisok.append("8")
    set_label_enter(spisok)

def click_btn9():
    spisok.append("9")
    set_label_enter(spisok)

def click_zero():
    spisok.append("0")
    set_label_enter(spisok)

def click_clear():
    spisok = ""
    otvet = ""
    set_label_enter(spisok)
    set_label_result(otvet)
    view.spisok = []
    view.otvet = []


def click_mult():
    spisok.append("*")
    set_label_enter(spisok)

def click_div():
    spisok.append("/")
    set_label_enter(spisok)

def click_sum():
    spisok.append("+")
    set_label_enter(spisok)

def click_min():
    spisok.append("-")
    set_label_enter(spisok)

def click_equa():
    set_label_enter(spisok)
    m.calculation(spisok)
    set_label_result(otvet)
    log.logger_calc(spisok, otvet)

def click_logger():
    log.get_logger()
    logg = ''.join(logger)
    messagebox.showinfo(title="logger", message=logg)

#Нижняя часть приложения с кнопками
frame = Frame(root, bg="green")
frame.place(relwidth=1, relheight=0.6, y=120)
#Установка для каждой кнопки одинаковый "вес"
for c in range(5): frame.columnconfigure(index=c, weight=1)
for c in range(5): frame.rowconfigure(index=c, weight=1)
#Первый ряд кнопок
#Установка каждой кнопки идет по номеру строки и номеру колонки
btn1 = ttk.Button(frame,text="1",command=click_btn1)
btn1.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)

btn2 = ttk.Button(frame,text="2",command=click_btn2)
btn2.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)

btn3 = ttk.Button(frame,text="3",command=click_btn3)
btn3.grid(row=0, column=2, ipadx=5, ipady=5, padx=5, pady=5)

btn_mult = ttk.Button(frame,text="*", command=click_mult)
btn_mult.grid(row=0, column=3, ipadx=5, ipady=5, padx=5, pady=5)

#Второй ряд кнопок
btn4 = ttk.Button(frame,text="4", command=click_btn4)
btn4.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5)

btn5 = ttk.Button(frame,text="5", command=click_btn5)
btn5.grid(row=1, column=1, ipadx=5, ipady=5, padx=5, pady=5)

btn6 = ttk.Button(frame,text="6", command=click_btn6)
btn6.grid(row=1, column=2, ipadx=5, ipady=5, padx=5, pady=5)

btn_div = ttk.Button(frame,text="/", command=click_div)
btn_div.grid(row=1, column=3, ipadx=5, ipady=5, padx=5, pady=5)

#Третий ряд кнопок
btn7 = ttk.Button(frame,text="7", command=click_btn7)
btn7.grid(row=2, column=0, ipadx=5, ipady=5, padx=5, pady=5)

btn8 = ttk.Button(frame,text="8", command=click_btn8)
btn8.grid(row=2, column=1, ipadx=5, ipady=5, padx=5, pady=5)

btn9 = ttk.Button(frame,text="9", command=click_btn9)
btn9.grid(row=2, column=2, ipadx=5, ipady=5, padx=5, pady=5)

btn_sum = ttk.Button(frame,text="+", command=click_sum)
btn_sum.grid(row=2, column=3, ipadx=5, ipady=5, padx=5, pady=5)

#Четвертый ряд кнопок
btn_dot = ttk.Button(frame,text="C", command=click_clear)
btn_dot.grid(row=3, column=0, ipadx=5, ipady=5, padx=5, pady=5)

btn_zero = ttk.Button(frame,text="0", command=click_zero)
btn_zero.grid(row=3, column=1, ipadx=5, ipady=5, padx=5, pady=5)

btn_equ = ttk.Button(frame,text="=", command=click_equa)
btn_equ.grid(row=3, column=2, ipadx=5, ipady=5, padx=5, pady=5)

btn_min = ttk.Button(frame,text="-", command=click_min)
btn_min.grid(row=3, column=3, ipadx=5, ipady=5, padx=5, pady=5)

#Пятый ряд кнопок
btn_log = ttk.Button(frame,text="logger", command=click_logger)
btn_log.grid(row=4, column=0, ipadx=5, ipady=5, padx=5, pady=5)
#Зацикливание приложения
root.mainloop()