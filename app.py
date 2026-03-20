import random

class PosicaoOcupadaError(Exception):
    pass

class tabuleiro:
    def __init__(self):
        self.tabuleiro = {x:[' ',' ',' '] for x in range(1,4)}

    
    def mostrar_tabuleiro(self):
        print(f' {self.tabuleiro[1][0]}  |  {self.tabuleiro[2][0]}  |  {self.tabuleiro[3][0]} ')
        print('_______________')
        print(f' {self.tabuleiro[1][1]}  |  {self.tabuleiro[2][1]}  |  {self.tabuleiro[3][1]} ')
        print('_______________')
        print(f' {self.tabuleiro[1][2]}  |  {self.tabuleiro[2][2]}  |  {self.tabuleiro[3][2]} ')

    def fazer_jogada(self,coluna,linha, valor):
        if not(self.tabuleiro[coluna][linha] == ' '): 
            raise PosicaoOcupadaError("Posição já está ocupada.")
        else:
            self.tabuleiro[coluna][linha] = valor

    def checar_resultados(self):

        vencedor = None
        while True:
            #Verificação Vertical
            for tipo in ['X','O']:
                for coluna in self.tabuleiro.values():
                    contagem = coluna.count(tipo)

                    if contagem == 3:
                        print('Vencedor (Vertical):',tipo)
                        vencedor = tipo
                        return vencedor

            #Verificação Horizontal
            for tipo in ['X','O']:
                for _ in range(3):
                    temp = []
                    for coluna in self.tabuleiro.values():
                        '''Adiciona posição por posição na lista temp,
                        depois conta tipos e retorna vencedor caso 3 iguais ou reinicia lista temp
                        '''
                        temp.append(coluna[_])
                    contagem = temp.count(tipo)
                    
                    if contagem == 3:
                        print('Vencedor (Horizontal):',tipo)
                        vencedor = tipo
                        return vencedor
                    temp.clear()

            #Verificações Diagonal Crescente
            for tipo in ['X','O']:
                ident = 0
                temp = []
                for coluna in self.tabuleiro.values():
                    temp.append(coluna[ident])
                    ident += 1

                contagem = temp.count(tipo)

                if contagem == 3:
                    print('Vencedor (Diag. crescente):',tipo)
                    vencedor = tipo
                    return vencedor 
                temp.clear()

            #Verificações Diagonal Decrescente
            for tipo in ['X','O']:
                ident = 2
                temp = []

                for coluna in self.tabuleiro.values():
                    temp.append(coluna[ident])
                    ident -= 1
                contagem = temp.count(tipo)

                if contagem == 3:
                    print('Vencedor (Diag. Decrescente):',tipo)
                    vencedor = tipo
                    return vencedor
                temp.clear()
                        
            return vencedor
                          
jogo = tabuleiro()

jogo.mostrar_tabuleiro()