from modulos import *
from telaAdministrador import userBdGui
from telaAdministrador import filmesBdGui
from telaAdministrador import alimentosGui
from telaAdministrador import sessoesGui

class adminGui():
    def __init__(self):
        adminGui= Tk()
        self.adminGui = adminGui
        self.createGui()
        adminGui.mainloop()

    def createGui(self):
        self.adminGui.title('Pagina do administrador')
        self.adminGui.geometry("900x600")
        self.adminGui.resizable(True, True)
        self.adminGui.minsize(900, 600)
        self.frame_content = Frame(self.adminGui, bg='yellow')
        self.frame_content.place(relx=0.25, rely=0, relwidth=1, relheight=1)
        self.framesAdmin()

    def framesAdmin(self):
        self.frame_left_btn=Frame(self.adminGui, bg='red')
        self.frame_left_btn.place(relx=0, rely=0, relwidth=0.25, relheight=1)


        btn_add_user = Button(self.frame_left_btn,text='Gerenciar usuarios', command = self.openLogin)
        btn_add_user.place(relx=0, rely=0, relwidth=1, relheight=0.15)

        btn_admin = Button(self.frame_left_btn, text='Gerenciar sessoes',command=self.openSessoes)
        btn_admin.place(relx=0, rely=0.15, relwidth=1, relheight=0.15)

        btn_film = Button(self.frame_left_btn, text='Gerenciar filmes',command=self.openFilmes)
        btn_film.place(relx=0, rely=0.3, relwidth=1, relheight=0.15)

        btn_food = Button(self.frame_left_btn, text='Gerenciar alimentos', command = self.openAlimentos)
        btn_food.place(relx=0, rely=0.45, relwidth=1, relheight=0.15)

    def openAlimentos(self):
            self.frame_content.destroy()
            self.frame_content = Frame(self.adminGui)
            self.frame_content.place(relx=0.25, rely=0, relwidth=1, relheight=1)
            alimentosGui.alimentosGui(self.frame_content)
    def openLogin(self):
            self.frame_content.destroy()
            self.frame_content = Frame(self.adminGui)
            self.frame_content.place(relx=0.25, rely=0, relwidth=1, relheight=1)
            userBdGui.usuarioGui(self.frame_content)
    def openFilmes(self):
            self.frame_content.destroy()
            self.frame_content = Frame(self.adminGui)
            self.frame_content.place(relx=0.25, rely=0, relwidth=1, relheight=1)
            filmesBdGui.filmesGui(self.frame_content)
    def openSessoes(self):
            self.frame_content.destroy()
            self.frame_content = Frame(self.adminGui)
            self.frame_content.place(relx=0.25, rely=0, relwidth=1, relheight=1)
            sessoesGui.sessoesGui(self.frame_content)