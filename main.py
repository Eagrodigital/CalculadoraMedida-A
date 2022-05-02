from tarfile import PAX_FIELDS
from tkinter import *
from tkinter import ttk

#importando Pillow

from PIL import ImageTk, Image


#cores

cor1 = '#0D0D0D'  # black / preto
cor2 = '#9127B0' # purple / roxo
cor3 = '#A3EA29' # green / verde
cor4 = '#192617'

janela = Tk()
janela.title('Calculadora de Unidade de Medidas')
janela.geometry('650x260')
janela.configure(bg=cor1)

#----------------------------------------- frames para janela -----------------------------------------

frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady=0, padx=3, relief='flat')
frame_cima.place(x=2, y=2)

frame_esquerda = Frame(janela, width=450, height=220, bg=cor2, pady=0, padx=3, relief='flat')
frame_esquerda.place(x=2, y=54)

frame_direita = Frame(janela, width=198, height=260, bg=cor2, pady=0, padx=3, relief='flat')
frame_direita.place(x=454, y=2)


#----------------------------------------- estilo para janela -----------------------------------------

estilo = ttk.Style(janela)
estilo.theme_use("clam")

#----------------------------------------- Configurando Frame Cima -------------------------------------

l_app_nome = Label(frame_cima, text='Calculadora de Unidades de Medidas', height=1, padx=0, relief='flat', anchor='center', font=('Ivyy 15 bold'), bg=cor2, fg=cor3)
l_app_nome.place(x=50, y=10)

#----------------------------------------- Configurando Frame Esquerda -------------------------------------


img_0 = Image.open('Calculadoramedidas_python/Images/massa.png')
img_0 = img_0.resize((50,50), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)
b_0 = Button(frame_esquerda, text='Massa', image=img_0, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_0.grid(row=0, column=0, sticky=NSEW,pady=5, padx=5)

img_1 = Image.open('Calculadoramedidas_python/Images/area.png')
img_1 = img_1.resize((50,50), Image.ANTIALIAS)
img_1 = ImageTk.PhotoImage(img_1)
b_1 = Button(frame_esquerda, text='Área', image=img_1, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_1.grid(row=0, column=1, sticky=NSEW,pady=5, padx=5)

img_2 = Image.open('Calculadoramedidas_python/Images/comprimento.png')
img_2 = img_2.resize((45,45), Image.ANTIALIAS)
img_2 = ImageTk.PhotoImage(img_2)
b_2 = Button(frame_esquerda, text='Comprimento', image=img_2, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_2.grid(row=0, column=2, sticky=NSEW,pady=5, padx=5)

img_3 = Image.open('Calculadoramedidas_python/Images/energia.png')
img_3 = img_3.resize((50,50), Image.ANTIALIAS)
img_3 = ImageTk.PhotoImage(img_3)
b_3 = Button(frame_esquerda, text='Energia', image=img_3, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_3.grid(row=1, column=0, sticky=NSEW,pady=5, padx=5)

img_4 = Image.open('Calculadoramedidas_python/Images/pressão.png')
img_4 = img_4.resize((50,50), Image.ANTIALIAS)
img_4 = ImageTk.PhotoImage(img_4)
b_4 = Button(frame_esquerda, text='Pressão', image=img_4, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_4.grid(row=1, column=1, sticky=NSEW,pady=5, padx=5)

img_5 = Image.open('Calculadoramedidas_python/Images/tempo.png')
img_5 = img_5.resize((50,50), Image.ANTIALIAS)
img_5 = ImageTk.PhotoImage(img_5)
b_5 = Button(frame_esquerda, text='Tempo', image=img_5, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_5.grid(row=1, column=2, sticky=NSEW,pady=5, padx=5)

img_6 = Image.open('Calculadoramedidas_python/Images/termômetro.png')
img_6 = img_6.resize((45,45), Image.ANTIALIAS)
img_6 = ImageTk.PhotoImage(img_6)
b_6 = Button(frame_esquerda, text='Termômetro', image=img_6, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_6.grid(row=2, column=0, sticky=NSEW,pady=5, padx=5)

img_7 = Image.open('Calculadoramedidas_python/Images/velocidade.png')
img_7 = img_7.resize((45,45), Image.ANTIALIAS)
img_7 = ImageTk.PhotoImage(img_7)
b_7 = Button(frame_esquerda, text='Velocidade', image=img_7, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_7.grid(row=2, column=1, sticky=NSEW,pady=5, padx=5)

img_8 = Image.open('Calculadoramedidas_python/Images/volume.png')
img_8 = img_8.resize((50,50), Image.ANTIALIAS)
img_8 = ImageTk.PhotoImage(img_8)
b_8 = Button(frame_esquerda, text='Quantidade', image=img_8, compound=LEFT, width=130, height=50, relief='flat', overrelief='solid', anchor='nw', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
b_8.grid(row=2, column=2, sticky=NSEW,pady=5, padx=5)


#----------------------------------------- Configurando Frame Direita -------------------------------------


l_unidade_nome = Label(frame_direita, text='Unidade', width=16, height=2, padx=0, relief='groove', anchor='center', font=('Ivyy 15 bold'), bg=cor2, fg=cor3)
l_unidade_nome.place(x=0, y=0)

l_de = Label(frame_direita, text='De', height=1, padx=3, relief='groove', anchor='center', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
l_de.place(x=10, y=70)
c_de = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold') )
c_de.place(x=38, y=70)


l_para = Label(frame_direita, text='Para', height=1, padx=3, relief='groove', anchor='center', font=('Ivyy 10 bold'), bg=cor2, fg=cor3)
l_para.place(x=100, y=70)
c_para = ttk.Combobox(frame_direita, width=5, justify=('center'), font=('Ivy 8 bold') )
c_para.place(x=140, y=70)



janela.mainloop() 