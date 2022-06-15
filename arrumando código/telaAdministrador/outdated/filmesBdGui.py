from modulos import *
from tkinter import filedialog


class filmesGui():
    def __init__(self, frame):
        self.frame_content=frame
        self.framesData()
        self.selectButton()

    def framesData(self):
        #frame conteudo topo
        self.frame_data_top = Frame(self.frame_content, bg='#e5ffff')
        self.frame_data_top.place(relx=0, rely=0, relwidth=0.75, relheight=0.1)
        #frame conteudo do meio
        self.frame_data_body = Frame(self.frame_content, bg='pink')
        self.frame_data_body.place(relx=0, rely=0.1, relwidth=1, relheight=0.4)
        #frame lista
        self.frame_treeList = Frame(self.frame_content)
        self.frame_treeList.place(relx=0, rely=0.5, relwidth=0.8, relheight=0.8)

        self.frameDataTop()
        self.frameDataBody()
        self.frameTreeList()
    def frameDataTop(self):

        self.btn_limpar = Button(self.frame_data_top, text="Limpar", command=self.buttonClear)
        self.btn_limpar.place(relx=0.15, rely=0.2, relwidth=0.1, relheight=0.6)

        self.btn_buscar = Button(self.frame_data_top, text="Buscar", command=self.buttonSearch)
        self.btn_buscar.place(relx=0.25, rely=0.2, relwidth=0.1, relheight=0.6)

        self.btn_novo = Button(self.frame_data_top, text="Novo", command=self.insertMovieButton)
        self.btn_novo.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.6)

        self.btn_delete = Button(self.frame_data_top, text="Apagar", command=self.buttonDelete)
        self.btn_delete.place(relx=0.6, rely=0.2, relwidth=0.1, relheight=0.6)

        # texto e nome entrada codigo
        self.lb_codigo = Label(self.frame_data_top, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.2, relwidth=0.08, relheight=0.3)
        self.codigo_entry = Entry(self.frame_data_top)
        self.codigo_entry.place(relx=0.05, rely=0.5, relwidth=0.08, relheight=0.3)
    def frameDataBody(self):
        # texto nome e entrada nome
        self.lb_nome = Label(self.frame_data_body, text="Nome do filme")
        self.lb_nome.place(relx=0.03, rely=0.05, relwidth=0.25, relheight=0.1)
        self.nome_entry = Entry(self.frame_data_body)
        self.nome_entry.place(relx=0.03, rely=0.15, relwidth=0.25, relheight=0.1)
        # texto preço e entrada para preço
        self.lb_genero = Label(self.frame_data_body, text="Genero")
        self.lb_genero.place(relx=0.03, rely=0.3, relwidth=0.2, relheight=0.1)
        self.genero_entry = Entry(self.frame_data_body)
        self.genero_entry.place(relx=0.03, rely=0.4, relwidth=0.2, relheight=0.1)

        self.lb_idade = Label(self.frame_data_body, text="Idade")
        self.lb_idade.place(relx=0.3, rely=0.05, relwidth=0.2, relheight=0.1)
        self.idade_entry = Entry(self.frame_data_body)
        self.idade_entry.place(relx=0.3, rely=0.15, relwidth=0.2, relheight=0.1)

        self.lb_duracao = Label(self.frame_data_body, text="Duracao(INT) em minutos")
        self.lb_duracao.place(relx=0.53, rely=0.05, relwidth=0.2, relheight=0.1)
        self.duracao_entry = Entry(self.frame_data_body)
        self.duracao_entry.place(relx=0.53, rely=0.15, relwidth=0.2, relheight=0.1)

        # botao drop down para categorias de alimentos separados em "pipoca, bebida e doce"
        self.lb_horario = Label(self.frame_data_body, text="Selecione o valor do ingresso em reais")
        self.lb_horario.place(relx=0.03, rely=0.55, relwidth=0.25, relheight=0.1)
        self.user_input = StringVar(self.frame_data_body)
        self.categorias = ("39,99", "49,99", "60,00")
        self.user_input.set("39,99")
        self.popup_menu = OptionMenu(self.frame_data_body, self.user_input, *self.categorias)
        self.popup_menu.place(relx=0.03, rely=0.65, relwidth=0.25, relheight=0.1)

        self.entry_dub = StringVar()
        self.dub = Radiobutton(self.frame_data_body, text='Dublado', variable=self.entry_dub, value='Dublado')
        self.dub.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.1)
        self.leg = Radiobutton(self.frame_data_body, text='Legendado', variable=self.entry_dub, value='Legendado')
        self.leg.place(relx=0.3, rely=0.4, relwidth=0.2, relheight=0.1)

        self.lb_poster = Label(self.frame_data_body, text="Selecione um poster abaixo")
        self.lb_poster.place(relx=0.40, rely=0.55, relwidth=0.25, relheight=0.1)
        self.btn_poster = Button(self.frame_data_body, text="Abrir imagem", command=self.buttonUploadImage)
        self.btn_poster.place(relx=0.40, rely=0.65, relwidth=0.25, relheight=0.1)
        self.poster_entry = Entry()
        self.poster_entry=0

    def buttonUploadImage(self):
        self.get_imageFilename = filedialog.askopenfilename(title="select image",initialdir="Imagens", filetypes=(("png", "*.png"),("jpg", "*.jpg"), ("Allfile", "*.*")))
        #caso o danado só abra a telinha de upload e feche em seguida
        if self.get_imageFilename=="":
            self.poster_entry = 0
        else:
            self.poster_entry = self.convertToBinaryData(self.get_imageFilename)
    def convertToBinaryData(self, filename):
        # precisa converter pra binario para armazenar no banco de dados
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def frameTreeList(self):
        self.lista_tree = ttk.Treeview(self.frame_treeList, height=3, column=("col1", "col2", "col3","col4","col5"))
        self.lista_tree.heading("#0", text="")
        self.lista_tree.heading("#1", text="Código")
        self.lista_tree.heading("#2", text="Nome")
        self.lista_tree.heading("#3", text="Genero")
        self.lista_tree.heading("#4", text="Valor ingresso")
        self.lista_tree.heading("#5", text="Dublado/Legendado")


        self.lista_tree.column("#0", width=1, stretch=NO)
        self.lista_tree.column("#1", width=20)
        self.lista_tree.column("#2", width=200)
        self.lista_tree.column("#3", width=100)
        self.lista_tree.column("#4", width=50)
        self.lista_tree.column("#5", width=100)

        self.lista_tree.place(relx=0, rely=0, relwidth=0.90, relheight=0.5)

        style = ttk.Style()
        style.configure("Treeview",
                        background="silver",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="silver")
        style.map('Treeview',
                  background=[('selected', 'blue')])
        self.scrool_list = Scrollbar(self.frame_treeList, orient='vertical')
        self.lista_tree.configure(yscroll=self.scrool_list.set)
        self.scrool_list.place(relx=0.90, rely=0, relwidth=0.04, relheight=0.5)
        # chamada pra funcao de evento doubleclick
        self.lista_tree.bind('<Double-1>', self.doubleClick)

    def conecta_bd(self):
        self.conn = sqlite3.connect("cinemalocal.bd")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def insertMovieButton(self):
            self.conecta_bd()
            self.cursor.execute(
                """ INSERT INTO filmes(nome_filme,genero_filme,idade_filme,duracao_filme, valor_ingresso, poster_filme, dublado) VALUES(?,?,?,?,?,?,?)""",
                (self.nome_entry.get(), self.genero_entry.get(), self.idade_entry.get(), self.duracao_entry.get(), self.user_input.get(), self.poster_entry, self.entry_dub.get()))
            self.conn.commit()
            #pra imagem nao ficar salva nos proximos aperto de botao
            self.poster_entry = 0
            self.desconecta_bd()
            self.selectButton()

    def selectButton(self):
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.conecta_bd()
        # armazena na variavel lista os campos do banco de dados
        lista = self.cursor.execute(
            """ SELECT id, nome_filme, genero_filme, valor_ingresso ,dublado  FROM filmes ORDER BY nome_filme ASC;""")

        for i in lista:
            # insere na treeview
            self.lista_tree.insert("", END, values=i)

        self.buttonClear()
        self.desconecta_bd()

    def buttonClear(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.genero_entry.delete(0, END)
        self.idade_entry.delete(0, END)
        self.duracao_entry.delete(0, END)

    def buttonDelete(self):
        self.conecta_bd()
        # por algum motivo tive que passar uma tupla pra funcionar
        self.cursor.execute('DELETE FROM filmes WHERE id=?', [self.codigo_entry.get()])
        self.conn.commit()
        self.cursor.execute('UPDATE filmes SET id=id-1 WHERE id > ?', [self.codigo_entry.get()])
        self.conn.commit()
        self.desconecta_bd()
        self.buttonClear()

        self.selectButton()

    def buttonSearch(self):
        self.conecta_bd()
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute("""SELECT id, nome_filme,genero_filme,valor_ingresso, dublado
                FROM filmes WHERE nome_filme LIKE '%s' ORDER BY nome_filme ASC""" % nome)
        verifica_nome = self.cursor.fetchall()
        for i in verifica_nome:
            self.lista_tree.insert("", END, values=i)
            self.buttonClear()
            self.desconecta_bd()

    def doubleClick(self, event):
        self.buttonClear()
        # gambiarra, casting pra Entry
        self.entry = Entry(self.frame_data_top)
        entry = self.user_input.get()
        self.entry2 = Entry()
        entry2=self.entry_dub


        self.lista_tree.selection()

        for i in self.lista_tree.selection():
            col1, col2, col3, col4,col5 = self.lista_tree.item(i, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.genero_entry.insert(END, col3)
            self.entry.insert(END, col4)
            self.entry2.insert(END,col5)


