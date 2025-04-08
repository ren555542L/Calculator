#1
import tkinter as tk
calc = ""
def atc(symbol):
    global calc
    calc += str(symbol)
    tr.delete(1.0,"end")#1.0 --- start
    tr.insert(1.0,calc)
def evalc():
    global calc
    try:
        calc = str(eval(calc))
        tr.delete(1.0,"end")
        tr.insert(1.0,calc)
    except:
        clear()
        tr.insert(1.0,"ERROR")
def clear():
    global calc
    calc =""
    tr.delete(1.0,"end")
a = tk.Tk(className = "Calculator")
a.geometry("300x275")
tr = tk.Text(a,height = 2, width = 16, font = ("Arial", 24))
tr.grid(columnspan = 5)
btn_1 = tk.Button(a, text = "1", command = lambda:atc(1), width = 5, font= ("Arial", 14))
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(a, text = "2", command = lambda:atc(2), width = 5, font= ("Arial", 14))
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(a, text = "3", command = lambda:atc(3), width = 5, font= ("Arial", 14))
btn_3.grid(row = 2, column = 3)
btn_1 = tk.Button(a, text = "+", command = lambda:atc("+"), width = 5, font= ("Arial", 14))
btn_1.grid(row = 2, column = 4)
btn_4 = tk.Button(a, text = "4", command = lambda:atc(4), width = 5, font= ("Arial", 14))
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(a, text = "5", command = lambda:atc(5), width = 5, font= ("Arial", 14))
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(a, text = "6", command = lambda:atc(6), width = 5, font= ("Arial", 14))
btn_6.grid(row = 3, column = 3)
btn_1 = tk.Button(a, text = "-", command = lambda:atc("-"), width = 5, font= ("Arial", 14))
btn_1.grid(row = 3, column = 4)
btn_7 = tk.Button(a, text = "7", command = lambda:atc(7), width = 5, font= ("Arial", 14))
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(a, text = "8", command = lambda:atc(8), width = 5, font= ("Arial", 14))
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(a, text = "9", command = lambda:atc(9), width = 5, font= ("Arial", 14))
btn_9.grid(row = 4, column = 3)
btn_1 = tk.Button(a, text = "*", command = lambda:atc("*"), width = 5, font= ("Arial", 14))
btn_1.grid(row = 4, column = 4)
btn_1 = tk.Button(a, text = "0", command = lambda:atc(0), width = 5, font= ("Arial", 14))
btn_1.grid(row = 5, column = 1)
btn_1 = tk.Button(a, text = "C", command = lambda:clear(), width = 5, font= ("Arial", 14))
btn_1.grid(row = 5, column = 2)
btn_1 = tk.Button(a, text = "/", command = lambda:atc("/"), width = 5, font= ("Arial", 14))
btn_1.grid(row = 5, column = 4)
btn_1 = tk.Button(a, text = "=", command = lambda:evalc(), width = 5, font= ("Arial", 14))
btn_1.grid(row = 5, column = 3)


a.mainloop()
