from numpy import mean
from numpy import std
from numpy import correlate
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
import unittest

Q={'q0', 'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23', 'q24','q25','q26','q27','q28','q29','q30','q31','q32', 'q33','q34', 'q35'}
S={'0', '1'}
G={'0','1', 'X', 'Y', 'A', 'B', '.',' '}
F={'q12', 'q25', 'q29','q30', 'q33', 'q35'}
D={
    ('q0', '1'):('q0','1','R'),
    ('q0', '0'):('q0','0','R'),
    ('q0', 'Y'):('q0','Y','R'),
    ('q0', 'A'):('q0','A','R'),
    ('q0', '.'):('q0','.','R'),
    ('q0', ' '):('q1','.','L'),
    ('q1', ' '):('q7',' ','R'),
    ('q1', 'A'):('q1','A','L'),
    ('q1', '0'):('q1','0','L'),
    ('q1', 'Y'):('q1','Y','L'),
    ('q1', '.'):('q1','.','L'),
    ('q1', '1'):('q2','Y','L'),
    ('q2', '1'):('q2','1','L'),
    ('q2', '0'):('q3','X','R'),
    ('q3', ' '):('q4','A','L'),
    ('q3', 'Y'):('q3','Y','R'),
    ('q3', 'X'):('q3','X','R'),
    ('q3', '.'):('q3','.','R'),
    ('q3', 'A'):('q3','A','R'),
    ('q3', '1'):('q3','1','R'),
    ('q4', '1'):('q4','1','L'),
    ('q4', 'A'):('q4','A','L'),
    ('q4', 'Y'):('q4','Y','L'),
    ('q4', '.'):('q4','.','L'),
    ('q4', 'X'):('q4','X','L'),
    ('q4', '0'):('q3','X','R'),
    ('q4', ' '):('q5',' ','R'),
    ('q5', 'X'):('q5','0','R'),
    ('q5', '1'):('q6','1','L'),
    ('q5', 'Y'):('q6','Y','L'),
    ('q6', '0'):('q6','0','L'),
    ('q6', ' '):('q0',' ','R'),
    ('q7', '0'):('q7',' ','R'),
    ('q7', 'Y'):('q7',' ','R'),
    ('q7', '.'):('q7',' ','R'),
    ('q7', 'A'):('q8','A','L'),
    ('q8', ' '):('q9',' ','R'),
    ('q9', 'A'):('q9','A','R'),
    ('q9', '.'):('q10','.','R'),
    ('q10', ' '):('q11',' ','L'),
    ('q10', 'A'):('q13','A','L'),
    ('q11', 'A'):('q11','0','L'),
    ('q11', '.'):('q11',' ','L'),
    ('q11', ' '):('q12',' ','R'),
    ('q13', '.'):('q13','.','L'),
    ('q13', 'A'):('q13','A','L'),
    ('q13', ' '):('q14',' ','R'),
    ('q14', 'A'):('q15',' ','R'),
    ('q14', '.'):('q20',' ','R'),
    ('q15', 'A'):('q15','A','R'),
    ('q15', '.'):('q16','.','R'),
    ('q16', '.'):('q19','.','L'),
    ('q16', 'A'):('q17','B','R'),
    ('q17', 'A'):('q17','A','R'),
    ('q17', 'B'):('q17','B','R'),
    ('q17', '.'):('q17','.','R'),
    ('q17', ' '):('q18','A','L'),
    ('q18', 'A'):('q18','A','L'),
    ('q18', '.'):('q18','.','L'),
    ('q18', 'B'):('q16','B','R'),
    ('q19', 'B'):('q19','A','L'),
    ('q19', '.'):('q19','.','L'),
    ('q19', 'A'):('q19','A','L'),
    ('q19', ' '):('q14',' ','R'),
    ('q20', 'A'):('q20',' ','R'),
    ('q20', '.'):('q21',' ','R'),
    ('q21', '.'):('q21','.','R'),
    ('q21', 'A'):('q21','A','R'),
    ('q21', ' '):('q22','.','L'),
    ('q22', 'A'):('q22','A','L'),
    ('q22', '.'):('q23','.','L'),
    ('q23', '.'):('q23','.','L'),
    ('q23', 'A'):('q23','A','L'),
    ('q23', ' '):('q14',' ','R'),
    ('q22', ' '):('q24',' ','R'),
    ('q24', 'A'):('q24','0','R'),
    ('q24', '.'):('q25',' ','L'),
    ('q26', '1'):('q27','1','R'),
    ('q26', ' '):('q30','0','R'),
    ('q26', '0'):('q31','0','R'),
    ('q27', '1'):('q27','1','R'),
    ('q27', ' '):('q28',' ','L'),
    ('q27', '0'):('q35','0','R'),
    ('q28', '1'):('q28',' ','L'),
    ('q28', ' '):('q29',' ','R'),
    ('q31', ' '):('q32',' ','L'),
    ('q31', '1'):('q34','1','R'),
    ('q31', '0'):('q31','0','R'),
    ('q32', '0'):('q32',' ','L'),
    ('q32', ' '):('q33','0','R'),
    ('q34', '0'):('q35','0','R'),
    ('q34', '1'):('q34','1','R'),
    ('q34', ' '):('q36',' ','L'),
    ('q36', '0'):('q36','0','L'),
    ('q36', '1'):('q36','1','L'),
    ('q36', ' '):('q0',' ','R'),
}
MT = (Q, S, G, D, 'q26',' ', F)

palavra = '000000000000000'

def analisaPalavra(maquina, palavra):
    estados_finais = maquina[6]
    estado_inicial = maquina[4]
    direcao = ''
    palavra_final = ''
    palavra_list = list(palavra)
    i = 0
    estado_atual = estado_inicial
    palavra_completa = False
    iteracoes = 0
    print('Palavra: ', palavra,'\n')

    while palavra_completa == False:
        for estadof in estados_finais:
            if estadof!= 'q35' and estado_atual == estadof:
                palavra_completa = True
                print('A palavra '+ palavra + ' foi aceita em ' + str(iteracoes) + ' iterações')
                print('Palavra final: ' + palavra_final.join(palavra for palavra in palavra_list if palavra != ' '))
            elif estadof == 'q35' and estado_atual == estadof:
                palavra_completa = True
                print('A palavra '+ palavra + ' foi rejeitada em ' + str(iteracoes) + ' iterações por não estar no formato 0^a1^b')
        for delta in maquina[3]:
            if (i + 1) > len(palavra_list):
                palavra_list.append(' ') 
            if i < 0:
                palavra_list = [' '] + palavra_list
                i = 0
            if estado_atual == delta[0] and palavra_list[i] == delta[1]:
                iteracoes += 1
                transicao = maquina[3][delta]
                simbolo_ant = palavra_list[i]
                palavra_list[i] = transicao[1]
                if transicao[2] == 'R':
                    direcao = 'direita'
                    i += 1
                else:
                    direcao = 'esquerda'
                    i -= 1
                if estado_atual != transicao[0]:
                    print('Sai do estado ' + estado_atual + ' para o estado ' + transicao[0] + ' trocando o simbolo ' + simbolo_ant + ' pelo símbolo' + transicao[1] + ' em direção a ' + direcao)
                    print('\nFita:', palavra_list, '\n')
                    estado_atual = transicao[0]
                    break
                elif estado_atual == transicao[0]:
                    print('Permanece no ' + estado_atual + ' lê o simbolo ' + simbolo_ant + ' e anda em direção a ' + direcao)
                    print('\nFita:', palavra_list, '\n')
                    break
analisaPalavra(MT, palavra)

#Palavras Aleatórias usadas no gráfico
#01 011 001 0011 00111 00011 001111 000111 0011111 0001111 00011111 00000111 00001111 00011111 000000111 0000001111 0000011111 0000001111 0000000011 0000000001 0001111111
 
# data1 = [2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8, 9, 10]
# data2 = [37, 96, 58, 198, 495, 1070, 1811, 2619, 9276, 70887, 21621, 74376, 70887, 1745562] 
 
#Dispersão A - B
#data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#data2 = [37, 96, 177, 282, 411, 564, 741, 942, 1167, 1416] 
#data2 = [37, 58, 83, 112, 145, 182, 223, 268, 317, 370] 
 
# pyplot.scatter(data1, data2)
# pyplot.title('Gráfico de Dispersão')
# pyplot.xlabel("Tempo de Execução")
# pyplot.xlabel("Tamanho da Palavra")
# pyplot.show()