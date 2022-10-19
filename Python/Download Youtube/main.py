import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

from PIL import Image , ImageTk
from pytube import YouTube

import datetime
import calendar

import requests

cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#6f9fbd"  # azul
cor3 = "#38576b"  # valor
cor4 = "#403d3d"   # letra
fundo = "#3b3b3b"

# definição Janela

Janela = Tk()
Janela.title()
Janela.geometry('500x300')
Janela.configure(bg=fundo)

ttk.Separator(Janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=250)

# divizão janela

frame_cima = Frame(Janela, width=500, height=110, bg=fundo, pady=5, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(Janela, width=500, height=300, bg=fundo, pady=12, padx=0)
frame_baixo.grid(row=2, column=0, sticky=NW)

# configuração frame cima

logo = Image.open('youtube.png')
logo = logo.resize((50,50), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

l_logo = Label(frame_cima, image=logo, compound=LEFT, bg=fundo, font=('arial 10 bold'), anchor='nw')
l_logo.place(x=5, y=5)

l_name = Label(frame_cima, text="Youtube Download", width=32, bg=fundo, fg=cor1, font=('arial 15 bold'), anchor='nw')
l_name.place(x=65, y=15)

# FUNÇÃO PESQUISAR

def pesquisar():
    global img

    url = e_url.get()
    yt = YouTube(url)

    titulo = yt.title
    view = yt.views
    duração = str(datetime.timedelta(seconds=yt.length))
    thumb = yt.thumbnail_url

    img = Image.open(requests.get(thumb, stream=True).raw)
    img = img.resize((230,150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    l_imagem['image'] = img

    l_titulo['text'] ="Titulo : " + titulo
    l_views['text'] ="Views : "  + str('{:,}' .format(view))
    l_time['text'] ="Duração : " + duração

# FUNÇÃO PARA A BARRA DE PROGRESSO
previousprogress = 0

def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    
    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(liveprogress)
        bar.place(x=250, y=120)
        bar['value'] = liveprogress
        Janela.update_idletasks()

# FUNÇÃO PARA FAZER O DOWNLOAD
def download():
    url=e_url.get()
    yt=YouTube(url)
    
    yt.register_on_progress_callback(on_progress)
    yt.streams.filter(file_extension='mp4')
    yt.streams.get_by_itag(22).download()
    # yt.streams.filter(file_extension='mp4').download()

l_url = Label(frame_cima, text="Entre o link", bg=fundo, fg=cor1, font=('arial 10 bold'), anchor='nw', )
l_url.place(x=10, y=80)

e_url = Entry(frame_cima, width=50, justify='left', relief=SOLID)
e_url.place(x=100, y=80)

b_pesquisar = Button(frame_cima, command=pesquisar, text="Pesquisar", width=10, bg=cor2, fg=cor1, font=('arial 7 bold'), relief=RAISED, overrelief=RIDGE, )
b_pesquisar.place(x=404, y=80)

# OPERAÇÕES

l_imagem = Label(frame_baixo, compound=LEFT, bg=fundo, font=('arial 10 bold'), anchor='nw')
l_imagem.place(x=10, y=10)

l_titulo = Label(frame_baixo, text="Titulo", height=2, wraplength=225, compound=LEFT, bg=fundo, fg=cor1, font=('arial 10 bold'), anchor='nw')
l_titulo.place(x=250, y=15)

l_views = Label(frame_baixo, text="00,000,00", bg=fundo, fg=cor1, font=('arial 15 bold'), anchor='nw')
l_views.place(x=250, y=60)

l_time = Label(frame_baixo, text="00:00:00", bg=fundo, fg=cor1, font=('arial 15 bold'), anchor='nw')
l_time.place(x=250, y=85)

down = Image.open('download2.png')
down = down.resize((20,20), Image.ANTIALIAS)
down = ImageTk.PhotoImage(down)

b_down = Button(frame_baixo, command=download, image=down, compound=LEFT, bg=fundo, font=('arial 10 bold'), overrelief=RIDGE)
b_down.place(x=444, y=85)

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='#00E676')
style.configure("TProgressbar", thickness=6)

bar = Progressbar(frame_baixo, length=190,style='black.Horizontal.TProgressbar')

Janela.mainloop()