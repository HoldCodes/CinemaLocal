from tkinter import *


class Filme:
    def __init__(self):
        self.nome = ""
        self.genero = ""
        self.idade = 0
        self.duracao = 0
        self.dublado = ""
        self.horarios = ["14 : 30", "16 : 00", "20 : 00"]     #A principio o cinema oferece 3 horarios
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 1.png")

    def filme1(self):
        self.nome = "1917"
        self.genero = "Guerra"
        self.idade = 18
        self.duracao = 110
        self.dublado = "Dublado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 1.png")

    def filme2(self):
        self.nome = "Morbius"
        self.genero = "Ficcao"
        self.idade = 14
        self.duracao = 120
        self.dublado = "Dublado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 2.png")

    def filme3(self):
        self.nome = "Sing 2"
        self.genero = "Animacao"
        self.idade = 10
        self.duracao = 80
        self.dublado = "Dublado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 3.png")

    def filme4(self):
        self.nome = "Cidade Perdida"
        self.genero = "Aventura"
        self.idade = 14
        self.duracao = 140
        self.dublado = "Dublado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 4.png")

    def filme5(self):
        self.nome = "Batman"
        self.genero = "Acao"
        self.idade = 16
        self.duracao = 180
        self.dublado = "Dublado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 5.png")

    def filme6(self):
        self.nome = "Sonic 2"
        self.genero = "Aventura"
        self.idade = 16
        self.duracao = 120
        self.dublado = "Dublado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 6.png")


    def filme7(self):
        self.nome = "Medida Provisoria"
        self.genero = "Drama"
        self.idade = 16
        self.duracao = 150
        self.dublado = "Dublado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 7.png")


    def filme8(self):
        self.nome = "Turma da Monica"
        self.genero = "Infantil"
        self.idade = 12
        self.duracao = 110
        self.dublado = "Legendado"
        self.imagem = PhotoImage(file=r"Imagens/Filmes/filme 8.png")


    # Toda essa parte aqui poderia poderia pegar os dados de um banco de dados/txt