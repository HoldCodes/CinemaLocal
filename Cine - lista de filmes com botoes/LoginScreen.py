import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3


class buttonMethods:
    def loginDb(self, login, password):
        db = sqlite3.connect('login.sqlite')
        #linha abaixo cria uma tabela se ela nao existe
        db.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
        """linha abaixo insere no banco de dados o login como admin e senha como admin, entretanto, quando o programa é 
        fechado a insercao abaixo nao fica salvo no arquivo login.sqlite"""
        db.execute("INSERT INTO login(username, password) VALUES('admin','admin')")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM login WHERE username=? AND password=?", (login, password))
        row = cursor.fetchone()
        if row:
            messagebox.showinfo(title="Login aceito", message="Login realizado com sucesso")
            # vai para a nova tela de adm quando for criada
            self.buttonDestroy()
        else:
            messagebox.showinfo(title="Login aceito", message="Falha no login, tente novamente")

    def buttonClear(self, entry1, entry2):
        entry1.delete(0, END)
        entry2.delete(0, END)

    def buttonDestroy(self):
        login_screen.destroy()


class LoginScreen(buttonMethods):
    def __init__(self, main_window):
        global login_screen  # precisava acessar pelos metodos de botões para destruir a janela
        login_screen = Toplevel(main_window)
        self.login_screen = login_screen
        self.login_screen.transient(main_window)
        self.loginInterface()

    def loginInterface(self):
        self.login_screen.title('Login screen')
        self.login_screen.geometry("900x600")
        self.login_screen.focus_force()
        self.login_screen.grab_set()
        self.login_screen.resizable(True, True)
        self.login_screen.minsize(900, 600)
        self.loginFrames()

    def loginFrames(self):
        """tive que usar essa func StringVar para passar como parametro na func de loginDb,
        para o metodo loginDb conseguir comparar com o banco de dados o input do usuario tem que ser em string,
        por algum motivo quando é realizado a leitura da entrada do usuario ela não é no formato string e o casting
        para string também nao funcionava
         """
        login = tkinter.StringVar()
        password = tkinter.StringVar()

        #cria frame 1 para titulo
        frame_title = Frame(self.login_screen)
        frame_title.place(relx=0, rely=0, relwidth=1, relheight=0.10)
        label_title = Label(frame_title, text='Sistema CINELOCAL TESTE', font=('verdana', 25))
        label_title.place(relx=0, rely=0, relwidth=1, relheight=1)

        #cria frame 2 para texto e entrada do usuario
        frame_body = Frame(self.login_screen)
        frame_body.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.6)

        label_login_text = Label(frame_body, text='Login:', font=('verdana', 15))
        label_login_text.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.1)
        entry_login = Entry(frame_body, textvariable=login, font=('verdana', 15))
        entry_login.place(relx=0.35, rely=0.1, relwidth=0.6, relheight=0.1)

        label_password_text = Label(frame_body, text='Senha:', font=('verdana', 15))
        label_password_text.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.1)
        entry_password = Entry(frame_body, textvariable=password, font=('verdana', 15), show='*')
        entry_password.place(relx=0.35, rely=0.2, relwidth=0.6, relheight=0.1)

        #cria frame 3 para botões
        frame_buttons = Frame(self.login_screen)
        frame_buttons.place(relx=0.25, rely=0.80, relwidth=0.5, relheight=0.10)
        button_login = Button(frame_buttons, text='Login',
                              command=lambda: buttonMethods.loginDb(self, login.get(), password.get()))
        button_login.place(relx=0.15, rely=0, relwidth=0.25, relheight=0.8)
        button_clear = Button(frame_buttons, text='Limpar',
                              command=lambda: buttonMethods.buttonClear(self, entry_login, entry_password))
        button_clear.place(relx=0.4, rely=0, relwidth=0.25, relheight=0.8)
        button_destroy = Button(frame_buttons, text='Fechar Janela',
                                command=self.buttonDestroy)
        button_destroy.place(relx=0.65, rely=0, relwidth=0.25, relheight=0.8)
