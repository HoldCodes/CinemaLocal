from modulos import *
import reserva

class sessoesGui():
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
        # texto preço e entrada para preço
        self.lb_horario = Label(self.frame_data_body, text="Selecione o horário")
        self.lb_horario.place(relx=0.3, rely=0.25, relwidth=0.2, relheight=0.1)
        self.user_input_horario = StringVar(self.frame_data_body)
        self.categorias_horario = ("14:30","18:00", "20:00")
        self.user_input_horario.set("14:30")
        self.popup_menu2 = OptionMenu(self.frame_data_body, self.user_input_horario, *self.categorias_horario)
        self.popup_menu2.place(relx=0.3, rely=0.35, relwidth=0.2, relheight=0.1)

        # botao drop down para categorias de alimentos separados em "pipoca, bebida e doce"
        self.lb_categorias = Label(self.frame_data_body, text="Selecione o filme")
        self.lb_categorias.place(relx=0.3, rely=0.65, relwidth=0.2, relheight=0.1)

        self.user_input_filme = StringVar(self.frame_data_body)
        todos_filmes = self.listaFilmes()
        print(todos_filmes)
        self.categorias = todos_filmes
        self.user_input_filme.set(todos_filmes[0])

        self.popup_menu = OptionMenu(self.frame_data_body, self.user_input_filme, *self.categorias)
        self.popup_menu.place(relx=0.3, rely=0.75, relwidth=0.2, relheight=0.1)
    def frameTreeList(self):
        self.lista_tree = ttk.Treeview(self.frame_treeList, height=3, column=("col1", "col2", "col3"))
        self.lista_tree.heading("#0", text="")
        self.lista_tree.heading("#1", text="Código da sessão")
        self.lista_tree.heading("#2", text="Filme")
        self.lista_tree.heading("#3", text="Horario sessão")


        self.lista_tree.column("#0", width=1, stretch=NO)
        self.lista_tree.column("#1", width=30)
        self.lista_tree.column("#2", width=200)
        self.lista_tree.column("#3", width=100)

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
    def listaFilmes(self):
        self.conecta_bd()
        self.cursor.execute(
            """SELECT id,filmes.nome_filme FROM filmes ORDER BY id""")
        lista = self.cursor.fetchall()
        self.desconecta_bd()
        return lista
    def insertUserButton(self):
        self.conecta_bd()
        #quebrando a string
        user_filme = self.user_input_filme.get().partition(",")
        self.cursor.execute(
            """ INSERT INTO secao(filmes_id, horario_secao) VALUES(?,?)""",
            (user_filme[0][1:], self.user_input_horario.get()))
        self.conn.commit()
        self.desconecta_bd()
        self.selectButton()
    def selectButton(self):
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.conecta_bd()
        # armazena na variavel lista os campos do banco de dados
        lista = self.cursor.execute(
            """ SELECT secao.id, filmes.nome_filme,horario_secao FROM secao, filmes WHERE filmes.id = secao.filmes_id """)
        lista = self.cursor.fetchall()
        for i in lista:
            # insere na treevie
            self.lista_tree.insert("", END, values=i)

        self.buttonClear()
        self.desconecta_bd()
    def buttonClear(self):
        self.codigo_entry.delete(0, END)
    def buttonDelete(self):
        self.conecta_bd()
        # por algum motivo tive que passar uma tupla pra funcionar
        self.cursor.execute('DELETE FROM secao WHERE id=?', [self.codigo_entry.get()])
        self.conn.commit()
        self.desconecta_bd()
        self.buttonClear()
        self.selectButton()
    def buttonSearch(self):
        self.conecta_bd()
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.codigo_entry.insert(END, '%')
        nome = self.codigo_entry.get()
        self.cursor.execute("""SELECT secao.id, filmes.nome_filme,horario_secao FROM secao, filmes WHERE filmes.id = secao.filmes_id AND secao.id LIKE '%s'""" % nome)
        verifica_nome = self.cursor.fetchall()
        for i in verifica_nome:
            self.lista_tree.insert("", END, values=i)
        self.buttonClear()
        self.desconecta_bd()
    def doubleClick(self, event):
        # gambiarra, casting pra Entry
        self.entry = Entry(self.frame_data_top)
        entry = self.user_input_filme.get()
        self.entry2 = Entry(self.frame_data_top)
        entry2 = self.user_input_horario.get()
        self.buttonClear()
        self.lista_tree.selection()

        for i in self.lista_tree.selection():
            col1, col2, col3= self.lista_tree.item(i, 'values')
            self.codigo_entry.insert(END, col1)
            self.entry2.insert(END, col2)
            self.entry.insert(END, col2)

"""if __name__=='__main__':
    win=Tk()
    win.geometry('900x600')
    filmesBdGui.filmesGui(win)
    win.mainloop()"""