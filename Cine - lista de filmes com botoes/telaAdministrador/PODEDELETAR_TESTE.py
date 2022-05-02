from modulos import *

class buttonsFunc:
    ##BOTAO LOGIN e loginDb
    def buttonClearLogin(self, entry1, entry2):
        entry1.delete(0, END)
        entry2.delete(0, END)
    def buttonDestroyLogin(self):
        self.login_screen.destroy()
    #BOTAO E OUTROS PARA ADM INSERIR, REMOVER, PROCURAR ALIMENTOS
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.preco = self.preco_entry.get()
        self.categoria = self.user_input.get()
    def conecta_bd(self):
        self.conn=sqlite3.connect("../cinemalocal.bd")
        self.cursor=self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()

    def criaTabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alimentos(
            cod INTEGER PRIMARY KEY,
            nome_alimento CHAR(30) NOT NULL,
            preco_alimento FLOAT(6) NOT NULL,
            categoria_alimento CHAR(10)
        );
    """)
        self.conn.commit()
        self.desconecta_bd()

    def insertButton(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO alimentos (nome_alimento,preco_alimento,categoria_alimento) VALUES(?,?,?)""",(self.nome,self.preco,self.categoria))
        self.conn.commit()
        self.desconecta_bd()
        self.selectButton()
    def selectButton(self):
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.conecta_bd()
        #armazena na variavel lista os campos do banco de dados
        lista = self.cursor.execute(""" SELECT cod, nome_alimento, preco_alimento, categoria_alimento FROM alimentos ORDER BY nome_alimento ASC;""")

        for i in lista:
            #insere na treeview
            self.lista_tree.insert("", END, values=i)

        self.buttonClear()
        self.desconecta_bd()
    def buttonClear(self):
        self.codigo_entry.delete(0, END)
        self.preco_entry.delete(0, END)
        self.nome_entry.delete(0, END)

    def buttonDelete(self):
        self.variaveis()
        self.conecta_bd()
        #por algum motivo tive que passar uma tupla pra funcionar
        self.cursor.execute('DELETE FROM alimentos WHERE cod=?', [self.codigo])
        self.conn.commit()

        self.desconecta_bd()
        self.buttonClear()

        self.selectButton()
    def buttonSearch(self):
        self.conecta_bd()
        self.lista_tree.delete(*self.lista_tree.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute("""SELECT cod, nome_alimento,preco_alimento,categoria_alimento
               FROM alimentos WHERE nome_alimento LIKE '%s' ORDER BY nome_alimento ASC""" % nome)
        verifica_nome = self.cursor.fetchall()
        for i in verifica_nome:
            self.lista_tree.insert("", END, values=i)
            self.buttonClear()
            self.desconecta_bd()

    def doubleClick(self, event):
        self.buttonClear()
        #gambiarra, casting pra Entry
        self.entry = Entry(self.frame_data_top)
        entry=self.user_input.get()

        self.lista_tree.selection()

        for i in self.lista_tree.selection():
            col1, col2, col3, col4= self.lista_tree.item(i,'values')
            self.codigo_entry.insert(END,col1)
            self.nome_entry.insert(END,col2)
            self.preco_entry.insert(END, col3)
            self.entry.insert(END, col4)

