import random
import os

class PosicaoOcupadaError(Exception):
    pass

class tabuleiro:
    def __init__(self):
        self.tabuleiro = {x:[' ',' ',' '] for x in range(1,4)}

    def embaralhar_escolhas(self):
        print('-'*15,'Jogo da Velha', '-'*15)

        escolhas = ['X','O']
        random.shuffle(escolhas)
        return escolhas

    def mostrar_tabuleiro(self):
        print(f' {self.tabuleiro[1][0]}  |  {self.tabuleiro[2][0]}  |  {self.tabuleiro[3][0]} ')
        print('---------------')
        print(f' {self.tabuleiro[1][1]}  |  {self.tabuleiro[2][1]}  |  {self.tabuleiro[3][1]} ')
        print('---------------')
        print(f' {self.tabuleiro[1][2]}  |  {self.tabuleiro[2][2]}  |  {self.tabuleiro[3][2]} \n')

    def jogadas_disponiveis(self):
        #Gera tupla de chave e posição disponível
        dicionario_disponiveis = [
            (key,i) 
            for key,lista in self.tabuleiro.items() 
            for i,valor in enumerate(lista) 
            if valor == ' ']

        return dicionario_disponiveis
    
    def fazer_jogada(self,coluna=None,linha=None, valor=str, tipo_jogador=int):

        if tipo_jogador == 1:
            if not(self.tabuleiro[coluna][linha] == ' '): 
                raise PosicaoOcupadaError("Posição já está ocupada.")
            else:
                self.tabuleiro[coluna][linha] = valor

        elif tipo_jogador == 2:
            escolha_computer = random.choice(self.jogadas_disponiveis())
            coluna_computador = escolha_computer[0]
            linha_computador = escolha_computer[1]
            
            self.tabuleiro[coluna_computador][linha_computador] = valor

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
        
class jogador:
    def __init__(self,nome,tipo,valor,tabuleiro):
        self.nome = nome
        self.tipo = tipo #1: Player1 | 2: Computador
        self.valor = valor
        self.tabuleiro = tabuleiro

    def mostrar_escolha(self):
        print(f'{self.nome}: {self.valor}')

    def fazer_jogada(self,coluna=None,linha=None):
        
        if self.tipo == 1:
            coluna = int(input('Qual coluna? (Entre 1 e 3): '))
            linha = int(input('Qual a linha (Entre 0 e 2): '))

        os.system("cls")

        self.tabuleiro.fazer_jogada(coluna,linha,self.valor,self.tipo)
        self.tabuleiro.mostrar_tabuleiro()
        self.tabuleiro.checar_resultados()
                   
jogo = tabuleiro()


while True:

    escolhas = jogo.embaralhar_escolhas()

    player1 = jogador("Player1",1,escolhas[0],jogo)
    computer = jogador("Computador",2,escolhas[1],jogo)

    player1.mostrar_escolha()
    computer.mostrar_escolha()

    if player1.valor == 'X':
        player1.fazer_jogada()
        rodada = 1
    else:
        computer.fazer_jogada()
        rodada = 0

    while True:
        if rodada == 1:
            computer.fazer_jogada()
            rodada = 0

        elif rodada == 0:
            player1.fazer_jogada()
            rodada = 1

        #Checa se retorno de resultados não é None e checa se ainda tem jogadas disponíves e retorna False caso tenha
        if not(jogo.checar_resultados() is None) or not(bool(jogo.jogadas_disponiveis())): break
    
    break