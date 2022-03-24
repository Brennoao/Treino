from cgitb import text
from msilib.schema import Font
from re import A
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
from turtle import width

White = "#ffffff"  # WWHITE
Light_gray = "#A5A5A5" # LIGHT GRAY
Dark_gray = "#414141" # DARK GRAY
Black = "#000000" # BLACK
Orange = "#FF9500" # ORANGE




# FRAMES

Janela =Tk()
Janela.title("Calculadora")
Janela.geometry("235x310")
Janela.config(bg=Black)

frame_tela = Frame(Janela, width=235, height=50, bg=White)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(Janela, width=235, height=268, bg=Black)
frame_corpo.grid(row=1, column=0)

# VARIAVEL TODOS OS VALORES

todos_valores = ''

# FUNÇÃO

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
    
    # VALOR PARA TELA
    
    valor_texto.set(todos_valores)

# FUNÇÃO OPERAÇÕES

def calcular():
    global todos_valores

    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

# FUNÇÃO LIMPA TELA

def limpar_tela():
    global todos_valores

    todos_valores = ""
    valor_texto.set("")

# LABEL 

valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('arial 18'), bg=White, fg=Black)
app_label.place(x=0, y=0)

# BOTÕES

b_1 = Button(frame_corpo, command = limpar_tela, text="AC", width=5, height=2, bg=Light_gray, fg=Black, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, command = lambda: entrar_valores('+/-'), text="+/-", width=5, height=2, bg=Light_gray, fg=Black, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=0)

b_3 = Button(frame_corpo, command = lambda: entrar_valores('%'), text="%", width=5, height=2, bg=Light_gray, fg=Black, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=0)

b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text="÷", width=5, height=2, bg=Orange, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

# BOTÕES NÚMEROS 1ª Linha

b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text="7", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text="8", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text="9", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text="x", width=5, height=2, bg=Orange, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

# BOTÕES NÚMEROS 2ª Linha

b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text="4", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text="5", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text="6", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text="-", width=5, height=2, bg=Orange, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

# BOTÕES NÚMEROS 3ª Linha

b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text="1", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text="2", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text="3", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text="+", width=5, height=2, bg=Orange, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

# BOTÕES NÚMEROS 4ª Linha

b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text="0", width=11, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo, command = lambda: entrar_valores(','), text=",", width=5, height=2, bg=Dark_gray, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=Orange, fg=White, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

Janela.mainloop()