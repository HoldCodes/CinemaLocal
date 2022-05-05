from modulos import *


class usuarioGui():
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

        self.btn_novo = Button(self.frame_data_top, text="Novo", command=self.insertUserButton)
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
        self.lb_user = Label(self.frame_data_body, text="Usuario")
        self.lb_user.place(relx=0.03, rely=0.05, relwidth=0.7, relheight=0.1)
        self.user_entry = Entry(self.frame_data_body)
        self.user_entry.place(relx=0.03, rely=0.15, relwidth=0.7, relheight=0.1)
        # texto preço e entrada para preço
        self.lb_password = Label(self.frame_data_body, text="Senha")
        self.lb_password.place(relx=0.3, rely=0.25, relwidth=0.2, relheight=0.1)
        self.password_entry = Entry(self.frame_data_body)
        self.password_entry.place(relx=0.3, rely=0.35, relwidth=0.2, relheight=0.1)
        # botao drop down para categorias de alimentos separados em "pipoca, bebida e doce"
        self.lb_categorias = Label(self.frame_data_body, text="Selecione a categoria")
        self.lb_categorias.place(relx=0.3, rely=0.65, relwidth=0.2, relheight=0.1)
        self.user_input = StringVar(self.frame_data_body)
        self.categorias = ("Usuario", "Administrador")
        self.user_input.set("Usuario")
        self.popup_menu = OptionMenu(self.frame_data_body, self.user_input, *self.categorias)
        self.popup_menu.place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)

    def frameTreeList(self):
        self.lista_tree = ttk.Treeview(self.frame_treeList, height=3, column=("col1", "col2", "col3","col4"))
        self.lista_tree.heading("#0", text="")
        self.lista_tree.heading("#1", text="Código")
        self.lista_tree.heading("#2", text="Usuario")
        self.lista_tree.heading("#3", text="Senha")
        self.lista_tree.heading("#4", text="Categoria")


        self.lista_tree.column("#0", width=1, stretch=NO)
        self.lista_tree.column("#1", width=30)
        self.lista_tree.column("#2", width=200)
        self.lista_tree.column("#3", width=100)
        self.lista_tree.column("#4", width=100)

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

    def insertUserButton(self):

        self.conecta_bd()
        self.cursor.execute(
            """ INSERT INTO login(username,password,categoria) VALUES(?,?,?)""",
            (self.user_entry.get(), self.password_entry.get(), self.user_input.get()))
        self.conn.commit()
        self.desconecta_bd()
        self.selectButton()

    def selectButton(self):
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.conecta_bd()
        # armazena na variavel lista os campos do banco de dados
        lista = self.cursor.execute(
            """ SELECT id, username, password, categoria FROM login ORDER BY username ASC;""")

        for i in lista:
            # insere na treeview
            self.lista_tree.insert("", END, values=i)

        self.buttonClear()
        self.desconecta_bd()

    def buttonClear(self):
        self.codigo_entry.delete(0, END)
        self.user_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def buttonDelete(self):
        self.conecta_bd()
        # por algum motivo tive que passar uma tupla pra funcionar
        self.cursor.execute('DELETE FROM login WHERE id=?', [self.codigo_entry.get()])
        self.conn.commit()
        self.desconecta_bd()
        self.buttonClear()

        self.selectButton()

    def buttonSearch(self):
        self.conecta_bd()
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.user_entry.insert(END, '%')
        nome = self.user_entry.get()
        self.cursor.execute("""SELECT id, username,password,categoria
                FROM login WHERE username LIKE '%s' ORDER BY username ASC""" % nome)
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

        self.lista_tree.selection()

        for i in self.lista_tree.selection():
            col1, col2, col3, col4 = self.lista_tree.item(i, 'values')
            self.codigo_entry.insert(END, col1)
            self.user_entry.insert(END, col2)
            self.password_entry.insert(END, col3)
            self.entry.insert(END, col4)

