import random

class tabuleiro:
    def __init__(self):
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

        #Verificação vertical
        while True:

            for tipo in ['X','O']:
                for coluna in self.tabuleiro.values():
                    contagem = coluna.count(tipo)
                    if contagem == 3:
                        print('Vencedor:',tipo)
                        break
                
            break
                          
jogo = tabuleiro()

jogo.fazer_jogada(1,1,'X')

jogo.mostrar_tabuleiro()