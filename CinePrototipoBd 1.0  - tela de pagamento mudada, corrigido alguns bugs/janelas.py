from modulos import *
from reserva import Reserva
from reserva import Filminho
from reserva import sessoes
import pagamento
import loginGui
# Logo: 170x40
# Filmes em cartaz: 170x300
# Botões laterais: 175x105
# Ambos os banners: 725x100

class funcDb():
    def conecta_bd(self):
        self.conn = sqlite3.connect("cinemalocal.bd")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

class Principal(funcDb):
    def __init__(self):
        self.window = Tk()
        self.window.geometry('900x600')
        self.window.resizable(False, False)
        # self.window.overrideredirect(True)  # Desativa os botoes padroes da janela
        self.centraliza_janela()

        self.frame1 = Frame(self.window, width=175, height=600, borderwidth=0, relief="solid")  # Barra Lateral
        self.frame2 = Frame(self.window, width=725, height=50, borderwidth=1, relief="solid")  # Nome do cinema
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
        self.frame3.grid_propagate(False)  # O grid não se ajusta automaticamente e sim as medidas impostas acima
        self.frame4.grid_propagate(False)
        self.frame5.grid_propagate(False)
        # self.frame6.grid_propagate(False)

        my_img1 = ImageTk.PhotoImage(Image.open("Imagens/filme1.png"))
        my_img2 = ImageTk.PhotoImage(Image.open("Imagens/filme2.png"))
        my_img3 = ImageTk.PhotoImage(Image.open("Imagens/filme3.png"))
        my_img4 = ImageTk.PhotoImage(Image.open("Imagens/filme4.png"))
        my_img5 = ImageTk.PhotoImage(Image.open("Imagens/filme5.png"))
        my_img6 = ImageTk.PhotoImage(Image.open("Imagens/filme6.png"))
        my_img7 = ImageTk.PhotoImage(Image.open("Imagens/filme7.png"))
        my_img8 = ImageTk.PhotoImage(Image.open("Imagens/filme8.png"))
        #self.my_img9 = ImageTk.PhotoImage(Image.open("Imagens/icon_comidas.png"))

        self.image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8]
        # Adicionando os elementos aos frames

        # Frame 1
        self.imag2 = PhotoImage(file=r"Imagens/lego2.png")
        self.nome_cine = Label(self.frame1, text="teste3", image=self.imag2)
        self.nome_cine.grid(column=0, row=0)

        self.imag3 = PhotoImage(file=r"Imagens/175x105-00000000.png")

        self.imag7 = PhotoImage(file=r"Imagens/btn_filmes.png")
        self.my_img10 = ImageTk.PhotoImage(Image.open("Imagens/icon_retirar.png"))
        self.my_img11 = ImageTk.PhotoImage(Image.open("Imagens/icon_carrinho.png"))
        self.imag12 = PhotoImage(file=r"Imagens/icon_login.png")
        self.imag13 = PhotoImage(file=r"Imagens/icon_pedidos.png")

        self.btn_filmes = Button(self.frame1, image=self.imag7, command=lambda: self.abrir_janela())
        self.btn_filmes.grid()

        #self.btn_comidas = Button(self.frame1, image=self.my_img9)
        #self.btn_comidas.grid()
        self.btn_pedidos = Button(self.frame1, image=self.imag13)
        self.btn_pedidos.grid()

        self.btn_retirar = Button(self.frame1, image=self.my_img10)
        self.btn_retirar.grid()

        self.btn_adm = Button(self.frame1, image=self.imag12, command=lambda: loginGui.LoginScreen())
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

        self.imag4 = PhotoImage(file=r"Imagens/filme1.png")

        self.film1 = Button(self.frame4, pady=25, image=self.image_list[0])
        self.film1.grid(column=1, row=0, pady=18, padx=2)

        self.film2 = Button(self.frame4, pady=25, image=self.image_list[1])
        self.film2.grid(column=2, row=0, pady=18, padx=2)

        self.film3 = Button(self.frame4, pady=25, image=self.image_list[2])
        self.film3.grid(column=3, row=0, pady=18, padx=2)

        self.film4 = Button(self.frame4, pady=25, image=self.image_list[3])
        self.film4.grid(column=4, row=0, pady=18, padx=2)

        ''' CODIGO DO SLIDER
        self.avanca = 1 
        self.volta = 0
        self.button_forward = Button(self.frame4, text=">>", command=lambda: self.avancar())
        self.button_forward.grid(column=5, row=0)

        self.button_back = Button(self.frame4, text="<<", command=lambda: self.voltar())
        self.button_back.grid(column=0, row=0)
        '''

        # Frame 5
        self.logo = Label(self.frame5, text="teste5")
        self.logo.grid()

    ''' CODIGO DO SLIDER
    def avancar(self):
        global button_forward
        global button_back
        # global button_back
        self.imag4 = PhotoImage(file=r"Imagens/filme2.png")
        self.film1 = Button(self.frame4, pady=25, image=self.image_list[0 + self.avanca])
        self.film1.grid(column=1, row=0, pady=18, padx=2)

        self.film2 = Button(self.frame4, pady=25, image=self.image_list[1 + self.avanca])
        self.film2.grid(column=2, row=0, pady=18, padx=2)

        self.film3 = Button(self.frame4, pady=25, image=self.image_list[2 + self.avanca])
        self.film3.grid(column=3, row=0, pady=18, padx=2)

        self.film4 = Button(self.frame4, pady=25, image=self.image_list[3 + self.avanca])
        self.film4.grid(column=4, row=0, pady=18, padx=2)
        print(self.avanca)
        self.avanca = self.avanca + 1

        if self.avanca > 4:
            self.avanca = 4

    def voltar(self):
        global button_forward
        global button_back

        if self.avanca > 1:
            self.volta = self.avanca - (2 * (self.avanca - 1))
            self.imag4 = PhotoImage(file=r"Imagens/filme2.png")
            self.film1 = Button(self.frame4, pady=25, image=self.image_list[0 - self.volta])
            self.film1.grid(column=1, row=0, pady=18, padx=2)

            self.film2 = Button(self.frame4, pady=25, image=self.image_list[1 - self.volta])
            self.film2.grid(column=2, row=0, pady=18, padx=2)

            self.film3 = Button(self.frame4, pady=25, image=self.image_list[2 - self.volta])
            self.film3.grid(column=3, row=0, pady=18, padx=2)

            self.film4 = Button(self.frame4, pady=25, image=self.image_list[3 - self.volta])
            self.film4.grid(column=4, row=0, pady=18, padx=2)

            print("volta ", self.avanca)
            self.avanca = self.avanca - 1
        else:
            self.avanca = 2
    CODIGO DO SLIDER '''

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
        janela_filme = Filme()
        janela_filme.run()
    def centraliza_janela(self):
        self.window.geometry(f"+{int((self.window.winfo_screenwidth() / 2) - (900 / 2))}+"
                             f"{int((self.window.winfo_screenheight() / 2) - (600 / 2))}")
    def run(self):
        self.window.mainloop()

class Filme(funcDb):
    def __init__(self):
        self.window = Tk()
        self.window.geometry('900x600')
        self.window.resizable(False, False)
        # self.window.overrideredirect(True)
        self.centraliza_janela()
        # cria novo pedido
        self.reserva = Reserva()
        # self.carrinho = carrinho

        self.frame1 = Frame(self.window, borderwidth=0, relief="solid")  # Barra Lateral
        self.frame2 = Frame(self.window, borderwidth=0, relief="solid")  # Nome do cinema

        self.frame1.grid(column=0, row=0, sticky="N,S,E,W")
        self.frame2.grid(column=0, row=1, sticky="N,S,E,W", padx=1)

        # Imagem do filme 222 x 285

        self.btn1 = Button(self.frame1, text="Voltar", bg="green",
                           command=lambda: (self.deleta_coisas(), self.voltar()), width=130)
        self.btn1.grid(column=0, row=0)
        self.filmes_catalogo = []
        self.lista_label = []
        # LOOP PARA PREENCHER OS OITO FILMES DA TELA DE SELEÇÃO
        for i in range(0, 2):
            for j in range(0, 4):
                index = (i * 4) + j + 1
                self.filmes_catalogo.append(Filminho(index))
                self.lista_label.append(
                    Button(self.frame2, image=self.filmes_catalogo[index - 1].poster_filme, borderwidth=0,
                           command=lambda x=((i * 4) + j + 1): (self.janela_horarios(self.filmes_catalogo[x - 1]))))
                self.lista_label[index - 1].grid(column=j, row=i)

    def deleta_coisas(self):
        self.reserva.deleta_reserva()
        del self.filmes_catalogo
        del self.lista_label

    def janela_horarios(self, filme):
        newWindow = tkinter.Toplevel()
        self.filmeInfo = filme
        newWindow.resizable(False, False)
        newWindow.geometry(f"600x450+"
                           f"{int((newWindow.winfo_screenwidth() / 2) - (600 / 2))}+"
                           f"{int((newWindow.winfo_screenheight() / 2) - (450 / 2))}")

        frame1 = Frame(newWindow)
        frame2 = Frame(newWindow)
        frame3 = Frame(newWindow)

        frame1.grid(column=0, row=0)
        frame2.grid(column=0, row=1, sticky="w")
        frame3.grid(column=0, row=2, pady=40)

        bt1 = Button(frame1, text="Voltar", bg="green", width=87, command=lambda: (newWindow.destroy()))
        bt1.grid()

        # Imagem
        self.imag_info = ImageTk.PhotoImage(self.filmeInfo.get_poster())
        label1 = Button(frame2, image=self.imag_info)
        label1.grid(column=0, row=0)

        # Descricao
        label2 = Label(frame2, text=f"{self.filmeInfo.nome_filme}\n\n"
                                    f"{self.filmeInfo.genero_filme}\n\n"
                                    f"{self.filmeInfo.idade_filme}\n\n"
                                    f"{self.filmeInfo.duracao_filme}min\n\n"
                                    f"{self.filmeInfo.dublado}", font=("Arial", 20))

        label2.grid(column=1, row=0, ipadx=120)

        # Horarios       |Azul = dublado | amarelo = legendado|
        # não consegui deixar essa parte automatico
        self.bgF = "Pink"
        if filme.dublado == 'Legendado':
            self.bgF = "Yellow"
        else:
            self.bgF = "LightBlue"
        #se der tempo eu melhoro essa parte de horario
        seco = sessoes()
        horarios_disp = seco.busca_horario_id(self.filmeInfo.id)
        lista_bt = []
        for i in range(len(horarios_disp)):
            lista_bt.append(Button(frame3, text='Sessão ' + str(horarios_disp[i][1]) + '\n' + horarios_disp[i][0],
                                   font=("Arial", 15), bg=self.bgF,
                                   command=lambda x=i: (
                                   self.reserva.set_sessao(horarios_disp[x][2]), self.janela_poltrona(),
                                   newWindow.destroy())))
            lista_bt[i].grid(column=i, row=0, padx=50)

        newWindow.grab_set()  # Impede acessar a janela de fundo até sair da atual

    def janela_pagamento(self):
        print()
        # Criar janela pagamento

    def centraliza_janela(self):
        self.window.geometry(f"+{int((self.window.winfo_screenwidth() / 2) - (900 / 2))}+"
                             f"{int((self.window.winfo_screenheight() / 2) - (600 / 2))}")

    def voltar(self):
        self.window.destroy()
        janela = Principal()
        janela.run()


    def run(self):
        self.window.mainloop()


    def janela_poltrona(self):
        # garbage collector estava me ferrando no loop, por isso tem que ser global
        global imgPoltrona
        self.sala_poltrona = self.reserva.get_sala_poltrona()
        self.conecta_bd()
        self.atualiza_dados_db()
        self.btn_poltrona = []

        self.newWindow = tkinter.Toplevel()
        self.newWindow.resizable(False, False)
        self.newWindow.geometry(f"600x450+"
                                f"{int((self.newWindow.winfo_screenwidth() / 2) - (600 / 2))}+"
                                f"{int((self.newWindow.winfo_screenheight() / 2) - (450 / 2))}")
        frame1 = Frame(self.newWindow)
        frame2 = Frame(self.newWindow)
        self.frame3 = Frame(self.newWindow)
        frame4 = Frame(self.newWindow)


        frame1.grid(column=0, row=0)
        frame2.grid(column=0, row=1)
        self.frame3.grid(column=0, row=2)
        frame4.grid(column=0, row=3, pady=10)

        # Frame 1
        bt1 = Button(frame1, text="Voltar", bg="green", width=87,
                     command=lambda: (self.newWindow.destroy()))
        bt1.grid()

        # Frame 2
        label = Label(frame2, text="Escolha a Poltrona ", font=("Arial", 20))
        label.grid()

        self.img1 = PhotoImage(file=r"Imagens/Filmes/pol2.png")
        self.img2 = PhotoImage(file=r"Imagens/Filmes/pol.png")
        self.img3 = PhotoImage(file=r"Imagens/Filmes/pol3.png")
        # Frame 3

        for i in range(0, 5):
            for j in range(0, 5):
                # tentei separar em função essas condicionais, mas garbage collector não deixa
                index = (i * 5) + j + 1
                if (self.dados[index-1] == 1):
                    imgPoltrona = self.img1
                elif (self.dados[index-1] == 2):
                    imgPoltrona = self.img3
                else:
                    imgPoltrona = self.img2
                self.btn_poltrona.append(Button(self.frame3, image=imgPoltrona, compound=BOTTOM, text=index,
                                                command=lambda x=((i * 5) + j + 1): self.escolhe_poltrona(x)))
                self.btn_poltrona[index - 1].grid(column=j, row=i)
        # Frame 4
        #btn_confirma = Button(frame4, text="Avançar", font=("Arial", 20), fg="White", background="Black", command=self.btn_confirma)
        btn_confirma = Button(frame4, text="Avançar", font=("Arial", 20), fg="White", background="Black", command=lambda:pagamento.Store(self.window, self.reserva, self, self.newWindow))
        btn_confirma.grid(ipadx=110)
        self.newWindow.grab_set()

    def btn_confirma(self):
        if (2 in self.dados):
            for i in range(len(self.dados)):
                if self.dados[i] == 2:
                    self.reserva.add_ticket()
                    self.altera_status_poltrona(i+1, 1)
            #pagamento.Store(self.window, self.reserva, self)
        else:
            messagebox.showinfo(title="Poltrona invalida", message="Selecione uma poltrona vazia")
    def atualiza_dados_db(self):
        self.cursor.execute("SELECT * FROM poltronas WHERE poltrona_id=" + str(self.reserva.get_sala_poltrona()))
        self.dados = self.cursor.fetchone()
        #seleciona todas poltronas menos o id, que esta no indice 0
        self.dados = self.dados[1:]
    def escolhe_poltrona(self, poltrona):
        if (self.dados[poltrona-1] == 1):
            messagebox.showinfo(title="Erro", message="Selecione uma poltrona vazia")
        elif (self.dados[poltrona-1] == 2):
            imgPoltrona = self.img2
            self.altera_status_poltrona(poltrona, 0)
            self.btn_poltrona[poltrona - 1].configure(image=imgPoltrona)
        else:
            imgPoltrona = self.img3
            self.altera_status_poltrona(poltrona, 2)
            self.btn_poltrona[poltrona - 1].configure(image=imgPoltrona)
    def altera_status_poltrona(self, poltrona, status):
        self.conecta_bd()
        # gambiarra pra selecionar a coluna pela query, não é possivel inserir variavel na busca direta na query de coluna,ex SET "p"+poltrona
        poltronaString = "p" + str(poltrona)
        query = """ UPDATE poltronas SET {coluna} = {stat} WHERE poltrona_id = {id}""".format(coluna=poltronaString,
                                                                                              stat=str(status), id=str(
                self.reserva.get_sala_poltrona()))
        self.cursor.execute(query)
        self.conn.commit()
        self.atualiza_dados_db()
