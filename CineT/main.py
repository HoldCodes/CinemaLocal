import janelas
import loginGui
from modulos import *

class Carrinho:
    def __init__(self):
        self.filme = 0      # A ideia aqui seria tratar o filme e as comidas atraves de códigos tipo pipoca é 9
        self.comida = []    # e conforme for o codigo checar no banco de dados ou txt e pegar o valor do produto
        self.total = 0

    def seleciona_filme(self, codigo):
        self.filme = codigo

    def seleciona_comida(self, codigo):
        self.comida.append(codigo)

    def custo_total(self):
        #conferir no banco de dados/txt
        print()


def main():

    carrinho = Carrinho()


    loginGui.LoginScreen()

if __name__ == '__main__':
    main()
