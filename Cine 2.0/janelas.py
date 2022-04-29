import tkinter
from tkinter import *
import itens

# Logo: 170x40
# Filmes em cartaz: 170x300
# Botões laterais: 175x105
# Ambos os banners: 725x100


class Principal:
    def __init__(self, carrinho):

        self.window = Tk()
        self.window.geometry('900x600')
        self.window.resizable(False, False)
        #self.window.overrideredirect(True)  # Desativa os botoes padroes da janela
        self.centraliza_janela()

        self.carrinho = carrinho

        print(self.carrinho.filme)

        self.frame1 = Frame(self.window, width=175, height=600, borderwidth=0, relief="solid")  # Barra Lateral
        self.frame2 = Frame(self.window, width=725, height=50, borderwidth=1, relief="solid")   # Nome do cinema
        self.frame3 = Frame(self.window, width=725, height=100, borderwidth=1, relief="solid")  # Banner 1
        self.frame4 = Frame(self.window, width=725, height=350, borderwidth=1, relief="solid")  # Filmes em cartaz
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
        #self.frame6.grid_propagate(False)

        #self.logo22 = Button(self.frame6, text="X", command=lambda: self.window.destroy())
        #self.logo22.grid(padx=835, ipadx=25)

        # Adicionando os elementos aos frames

        # Frame 1
        self.imag2 = PhotoImage(file=r"Imagens/lego2.png")
        self.nome_cine = Label(self.frame1, text="teste3", image=self.imag2)
        self.nome_cine.grid(column=0, row=0)

        self.imag3 = PhotoImage(file=r"Imagens/175x105-00000000.png")

        self.imag7 = PhotoImage(file=r"Imagens/btn_filmes.png")
        self.btn_filmes = Button(self.frame1, image=self.imag7, command=lambda: self.abrir_janela())
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

    def janela_filme(self):
        j_filme = tkinter.Toplevel()
        j_filme.geometry("900x600")
        j_filme.geometry(f"+{int((j_filme.winfo_screenwidth() / 2) - (900 / 2))}+"
                         f"{int((j_filme.winfo_screenheight() / 2) - (600 / 2))}")
        j_filme.resizable(False, False)

        frame1 = Frame(j_filme)
        frame1.pack()

        self.imag2 = PhotoImage(file=r"Imagens/film2.png")
        nome_cine = Label(frame1, text="teste3", image=self.imag2)
        nome_cine.pack()

        j_filme.grab_set()

    def abrir_janela(self):
        self.window.destroy()
        janela_filme = Filme(self.carrinho)
        janela_filme.run()

    def centraliza_janela(self):
        self.window.geometry(f"+{int((self.window.winfo_screenwidth() / 2) - (900 / 2))}+"
                             f"{int((self.window.winfo_screenheight() / 2) - (600 / 2))}")

    def run(self):
        self.window.mainloop()


class Filme:
    def __init__(self, carrinho):
        self.window = Tk()
        self.window.geometry('900x600')
        self.window.resizable(False, False)
        #self.window.overrideredirect(True)
        self.centraliza_janela()

        self.horario = ""
        self.poltrona = 0
        self.tipo_ingresso = ""
        self.valor = 0

        self.carrinho = carrinho
        self.descricao = itens.Filme()

        self.frame1 = Frame(self.window, borderwidth=0, relief="solid")  # Barra Lateral
        self.frame2 = Frame(self.window, borderwidth=0, relief="solid")  # Nome do cinema

        self.frame1.grid(column=0, row=0, sticky="N,S,E,W")
        self.frame2.grid(column=0, row=1, sticky="N,S,E,W", padx=1)

        # Imagem do filme 222 x 285

        self.btn1 = Button(self.frame1, text="Voltar", bg="green", command=lambda: self.voltar(), width=130)
        self.btn1.grid(column=0, row=0)

        self.imag1 = PhotoImage(file=r"Imagens/Filmes/filme 1.png")
        self.imag2 = PhotoImage(file=r"Imagens/Filmes/filme 2.png")
        self.imag3 = PhotoImage(file=r"Imagens/Filmes/filme 3.png")
        self.imag4 = PhotoImage(file=r"Imagens/Filmes/filme 4.png")

        self.imag5 = PhotoImage(file=r"Imagens/Filmes/filme 5.png")
        self.imag6 = PhotoImage(file=r"Imagens/Filmes/filme 6.png")
        self.imag7 = PhotoImage(file=r"Imagens/Filmes/filme 7.png")
        self.imag8 = PhotoImage(file=r"Imagens/Filmes/filme 8.png")

        self.imag9 = PhotoImage(file=r"Imagens/Filmes/pol.png")

        self.label1 = Button(self.frame2, image=self.imag1, borderwidth=0,
                             command=lambda: (self.descricao.filme1(), self.janela_horarios()))
        self.label1.grid(column=0, row=0)

        self.label2 = Button(self.frame2, image=self.imag2, borderwidth=0,
                             command=lambda: (self.descricao.filme2(), self.janela_horarios()))
        self.label2.grid(column=1, row=0)

        self.label3 = Button(self.frame2, image=self.imag3, borderwidth=0,
                             command=lambda: (self.descricao.filme3(), self.janela_horarios()))
        self.label3.grid(column=2, row=0)

        self.label4 = Button(self.frame2, image=self.imag4, borderwidth=0,
                             command=lambda: (self.descricao.filme4(), self.janela_horarios()))
        self.label4.grid(column=3, row=0)

        self.label5 = Button(self.frame2, image=self.imag5, borderwidth=0,
                             command=lambda: (self.descricao.filme5(), self.janela_horarios()))
        self.label5.grid(column=0, row=1)

        self.label6 = Button(self.frame2, image=self.imag6, borderwidth=0,
                             command=lambda: (self.descricao.filme6(), self.janela_horarios()))
        self.label6.grid(column=1, row=1)

        self.label7 = Button(self.frame2, image=self.imag7, borderwidth=0,
                             command=lambda: (self.descricao.filme7(), self.janela_horarios()))
        self.label7.grid(column=2, row=1)

        self.label8 = Button(self.frame2, image=self.imag8, borderwidth=0,
                             command=lambda: (self.descricao.filme8(), self.janela_horarios()))
        self.label8.grid(column=3, row=1)

    def janela_ingresso(self):
        newWindow = tkinter.Toplevel()

        newWindow.resizable(False, False)
        newWindow.geometry(f"600x450+"
                           f"{int((newWindow.winfo_screenwidth() / 2) - (600 / 2))}+"
                           f"{int((newWindow.winfo_screenheight() / 2) - (450 / 2))}")

        frame1 = Frame(newWindow)
        frame2 = Frame(newWindow)
        frame3 = Frame(newWindow)

        frame1.grid(column=0, row=0)
        frame2.grid(column=0, row=1, sticky="")
        frame3.grid(column=0, row=2, pady=20)

        # Frame 1
        bt1 = Button(frame1, text="Voltar", bg="green", width=87,
                     command=lambda: (newWindow.destroy(), self.janela_poltrona()))
        bt1.grid()

        # Frame 2
        label1 = Label(frame2, text="Escolha seu Ingresso", font=("Arial", 20))
        label1.grid()

        # Frame 3
        btn2 = Button(frame3, text="INTEIRO: R$ 39,99", font=("Arial", 25),
                      command=lambda: (self.janela_pagamento(), newWindow.destroy()))
        btn2.grid(column=0, row=0)

        btn3 = Button(frame3, text="MEIA ENTRADA: R$ 19,99", font=("Arial", 25),
                      command=lambda: (self.janela_pagamento(), newWindow.destroy()))
        btn3.grid(column=0, row=1)

        newWindow.grab_set()

    def janela_poltrona(self):
        newWindow = tkinter.Toplevel()

        newWindow.resizable(False, False)
        newWindow.geometry(f"600x450+"
                           f"{int((newWindow.winfo_screenwidth() / 2) - (600 / 2))}+"
                           f"{int((newWindow.winfo_screenheight() / 2) - (450 / 2))}")

        frame1 = Frame(newWindow)
        frame2 = Frame(newWindow)
        frame3 = Frame(newWindow)
        frame4 = Frame(newWindow)

        frame1.grid(column=0, row=0)
        frame2.grid(column=0, row=1)
        frame3.grid(column=0, row=2)
        frame4.grid(column=0, row=3, pady=10)

        #Frame 1
        bt1 = Button(frame1, text="Voltar", bg="green", width=87,
                     command=lambda: (newWindow.destroy(), self.janela_horarios()))
        bt1.grid()

        #Frame 2
        label = Label(frame2, text="Escolha a Poltrona ", font=("Arial", 20))
        label.grid()

        #Frame 3
        for i in range(0, 5):
            for j in range(0, 5):
                btn = Button(frame3, image=self.imag9, compound=BOTTOM, text=((i*5) + j+1),
                             command=lambda x=((i*5)+j+1): (self.escolhe_poltrona(x), self.janela_ingresso(),
                                                            newWindow.destroy()))
                btn.grid(column=j, row=i)

        #Frame 4
        label2 = Label(frame4, text="TELA", font=("Arial", 20), fg="White", background="Black")
        label2.grid(ipadx=110)

        newWindow.grab_set()

    def janela_horarios(self):
        newWindow = tkinter.Toplevel()

        newWindow.resizable(False, False)
        newWindow.geometry(f"600x450+"
                           f"{int((newWindow.winfo_screenwidth() / 2) - (600 / 2))}+"
                           f"{int((newWindow.winfo_screenheight() / 2) - (450 / 2))}")

        frame1 = Frame(newWindow)
        frame2 = Frame(newWindow)
        frame3 = Frame(newWindow)

        frame1.grid(column=0, row=0)
        frame2.grid(column=0, row=1, sticky="W")
        frame3.grid(column=0, row=2, pady=40)

        bt1 = Button(frame1, text="Voltar", bg="green", width=87, command=lambda: newWindow.destroy())
        bt1.grid()

        #Imagem
        label1 = Label(frame2, image=self.descricao.imagem)
        label1.grid(column=0, row=0)

        #Descricao
        label2 = Label(frame2, text=f"{self.descricao.nome}\n\n"
                                    f"{self.descricao.genero}\n\n"
                                    f"{self.descricao.idade}\n\n"
                                    f"{self.descricao.duracao}min\n\n"
                                    f"{self.descricao.dublado}", font=("Arial", 20))

        label2.grid(column=1, row=0, ipadx=120)

        #Horarios       |Azul = dublado | amarelo = legendado|
        btn1 = Button(frame3, text=self.descricao.horarios[0], font=("Arial", 15), bg="LightBlue",
                      command=lambda: (self.janela_poltrona(), newWindow.destroy(),
                                       self.escolhe_horario(self.descricao.horarios[0])))
        btn1.grid(column=0, row=0, padx=50)

        btn2 = Button(frame3, text=self.descricao.horarios[1], font=("Arial", 15), bg="LightBlue",
                      command=lambda: (self.janela_poltrona(), newWindow.destroy(),
                                       self.escolhe_horario(self.descricao.horarios[1])))
        btn2.grid(column=1, row=0, padx=50)

        btn3 = Button(frame3, text=self.descricao.horarios[2], font=("Arial", 15), bg="Yellow",
                      command=lambda: (self.janela_poltrona(), newWindow.destroy(),
                                       self.escolhe_horario(self.descricao.horarios[2])))
        btn3.grid(column=2, row=0, padx=50)

        newWindow.grab_set()  #Impede acessar a janela de fundo até sair da atual

    def janela_pagamento(self):
        print()
        #Criar janela pagamento

    def centraliza_janela(self):
        self.window.geometry(f"+{int((self.window.winfo_screenwidth() / 2) - (900 / 2))}+"
                             f"{int((self.window.winfo_screenheight() / 2) - (600 / 2))}")

    def voltar(self):
        self.window.destroy()
        janela = Principal(self.carrinho)
        janela.run()

    def escolhe_horario(self, horario):
        self.horario = horario

    def escolhe_poltrona(self, poltrona):
        self.poltrona = poltrona

    def escolhe_ingresso(self, tipo):
        self.tipo_ingresso = tipo

    def valor_ingresso(self, valor):
        self.valor = valor

    def run(self):
        self.window.mainloop()


class Pagamento:
    def __init__(self):
        print()