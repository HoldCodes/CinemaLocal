from modulos import *
from telaAdministrador import adminGui

class LoginScreen():
    def __init__(self, main_window2):
        global next_window
        self.next_window = main_window2
        self.login_screen = Toplevel(main_window2)
        self.login_screen.transient(main_window2)
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
        self.frameTitle()
        self.frameBody()
        self.frameButtons()

    def frameTitle(self):
        frame_title = Frame(self.login_screen)
        frame_title.place(relx=0, rely=0, relwidth=1, relheight=0.10)
        label_title = Label(frame_title, text='Sistema CINELOCAL TESTE', font=('verdana', 25))
        label_title.place(relx=0, rely=0, relwidth=1, relheight=1)

    def frameBody(self):
        self.login = tkinter.StringVar()
        self.password = tkinter.StringVar()

        frame_body = Frame(self.login_screen)
        frame_body.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.6)

        label_login_text = Label(frame_body, text='Login:', font=('verdana', 15))
        label_login_text.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.1)
        self.entry_login = Entry(frame_body, textvariable=self.login, font=('verdana', 15))
        self.entry_login.place(relx=0.35, rely=0.1, relwidth=0.6, relheight=0.1)

        label_password_text = Label(frame_body, text='Senha:', font=('verdana', 15))
        label_password_text.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.1)
        self.entry_password = Entry(frame_body, textvariable=self.password, font=('verdana', 15), show='*')
        self.entry_password.place(relx=0.35, rely=0.2, relwidth=0.6, relheight=0.1)

    def frameButtons(self):
        frame_buttons = Frame(self.login_screen)
        frame_buttons.place(relx=0.25, rely=0.80, relwidth=0.5, relheight=0.10)
        button_login = Button(frame_buttons, text='Login',
                              command=lambda: self.loginDb(self.login.get(), self.password.get(), self.next_window))
        button_login.place(relx=0.15, rely=0, relwidth=0.25, relheight=0.8)
        button_clear = Button(frame_buttons, text='Limpar',
                              command=lambda: self.buttonClearLogin(self.entry_login, self.entry_password))
        button_clear.place(relx=0.4, rely=0, relwidth=0.25, relheight=0.8)
        button_destroy = Button(frame_buttons, text='Fechar Janela',
                                command=self.login_screen.destroy)
        button_destroy.place(relx=0.65, rely=0, relwidth=0.25, relheight=0.8)

        ##BOTAO LOGIN e loginDb

    def buttonClearLogin(self, entry1, entry2):
        entry1.delete(0, END)
        entry2.delete(0, END)

    def buttonDestroyLogin(self):
        self.login_screen.destroy()

    def loginDb(self, login, password, next_window):
        self.conecta_bd()
        # linha abaixo cria uma tabela se ela nao existe
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT, id INTEGER, categoria TEXT)')
        self.cursor.execute(
            "INSERT INTO login(username, password,categoria) VALUES('admin','admin', 'Administrador')")
        self.cursor.execute("SELECT * FROM login WHERE username=? AND password=? AND categoria=?", (login, password,'Administrador'))
        row = self.cursor.fetchone()
        if row:
            self.desconecta_bd()
            messagebox.showinfo(title="Login aceito", message="Login realizado com sucesso")
            self.buttonDestroyLogin()
            adminGui.adminGui(self.next_window)
        else:
            messagebox.showinfo(title="Login negado", message="Falha no login, tente novamente")

        ##BOTAO LOGIN e loginDb

    def conecta_bd(self):
        self.conn = sqlite3.connect("cinemalocal.bd")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

