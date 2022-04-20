import tkinter
from tkinter import *

# Logo: 170x40
# Filmes em cartaz: 170x300
# Botões laterais: 175x105
# Ambos os banners: 725x100


class Principal:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('900x600')
        self.window.resizable(False, False)

        self.frame1 = Frame(self.window, width=175, height=600, borderwidth=2, relief="solid")  # Barra Lateral
        self.frame2 = Frame(self.window, width=725, height=50, borderwidth=0, relief="solid")   # Nome do cinema
        self.frame3 = Frame(self.window, width=725, height=100, borderwidth=1, relief="solid")  # Banner 1
        self.frame4 = Frame(self.window, width=725, height=350, borderwidth=2, relief="solid")  # Filmes em cartaz
        self.frame5 = Frame(self.window, width=725, height=100, borderwidth=1, relief="solid")  # Banner 2

        self.frame1.pack(side=LEFT)
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        self.frame1.grid_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame3.grid_propagate(False)   # O grid não se ajusta automaticamente e sim as medidas impostas acima
        self.frame4.grid_propagate(False)
        self.frame5.grid_propagate(False)

        # Adicionando os elementos aos frames

        # Frame 1
        self.imag2 = PhotoImage(file=r"Imagens/lego2.png")
        self.nome_cine = Label(self.frame1, text="teste3", image=self.imag2)
        self.nome_cine.grid(column=0, row=0)

        self.imag3 = PhotoImage(file=r"Imagens/175x105-00000000.png")

        self.btn_filmes = Button(self.frame1, image=self.imag3)
        self.btn_filmes.grid()

        self.btn_comidas = Button(self.frame1, image=self.imag3)
        self.btn_comidas.grid()

        self.btn_retirar = Button(self.frame1, image=self.imag3)
        self.btn_retirar.grid()

        self.btn_carrinho = Button(self.frame1, image=self.imag3)
        self.btn_carrinho.grid()

        self.btn_adm = Button(self.frame1, image=self.imag3)
        self.btn_adm.grid()

        # Frame 2
        self.logo = Label(self.frame2, text="Cinema Local", font=("Arial", 20), padx=282.5)
        self.logo.grid()

        # Frame 3
        self.imag = PhotoImage(file=r"Imagens/Bertoldo.png")
        self.nome_cine = Label(self.frame3, image=self.imag)
        self.nome_cine.grid()

        # Frame 4
        self.imag4 = PhotoImage(file=r"Imagens/film2.png")

        self.film1 = Button(self.frame4, pady=25, image=self.imag4)
        self.film1.grid(column=0, row=0, pady=18, padx=2)

        self.film2 = Button(self.frame4, pady=25, image=self.imag4)
        self.film2.grid(column=1, row=0, pady=18, padx=2)

        self.film3 = Button(self.frame4, pady=25, image=self.imag4)
        self.film3.grid(column=2, row=0, pady=18, padx=2)

        self.film4 = Button(self.frame4, pady=25, image=self.imag4)
        self.film4.grid(column=3, row=0, pady=18, padx=2)

        # Frame 5
        self.logo = Label(self.frame5, text="teste5")
        self.logo.grid()

    def run(self):
        self.window.mainloop()
