import random

class tabuleiro:
    def __init__(self):
        #Criando 4 colunas com lista default e 3 itens
        self.tabuleiro = {x:[0,0,0] for x in range(1,4)}

    
    def mostrar_tabuleiro(self):
        print(f' {self.tabuleiro[1][0]}  |  {self.tabuleiro[2][0]}  |  {self.tabuleiro[3][0]} ')
        print('_______________')
        print(f' {self.tabuleiro[1][1]}  |  {self.tabuleiro[2][1]}  |  {self.tabuleiro[3][1]} ')
        print('_______________')
        print(f' {self.tabuleiro[1][2]}  |  {self.tabuleiro[2][2]}  |  {self.tabuleiro[3][2]} ')

    def fazer_jogada(self,coluna,linha, valor):
        self.tabuleiro[coluna][linha] = valor

    def checar_resultados(self):
        lista_resultados = list(self.tabuleiro.values())

        while True:
            
            #Verificação vertical
            for tipo in ['X','O']:
                for i in lista_resultados:
                    contagem = i.count(tipo)
                    if contagem == 3:
                        print('Vencedor:',tipo)
                        break

            break

             
jogo = tabuleiro()

jogo.mostrar_tabuleiro()