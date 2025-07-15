import random
#1. Faça um programa que gere aleatoriamente 15 números inteiros em uma lista
#   e depois permita que o usuário digite um número inteiro para ser buscado
#   na lista, se for encontrado o programa deve imprimir a posição desse
#   número na lista, caso contrário, deve imprimir a mensagem: "Não encontrado!".
#   (2,5pt)
def q1 ():
    lista = [random.randint(0,50) for _ in range(15)]
    print(lista)
    num = int(input('Digite o numero a ser buscado! '))
    if num in lista:
        print(f'O numero buacado se encontra na lista na posição {lista.index(num)}')
    else:
        print('Numero não enconrtrado')


#2. Complemente a questão 1 sem utilizar o recurso de ordenação. O programa
#   deve  imprimir ao final: o maior e o menor número da lista, o percentual
#   de números pares e a média dos elementos da lista. (2,5pt)
def q2 ():
    maior = 0
    menor = 51
    perc_par = 0
    media_ele = 0
    lista = [random.randint(0, 50) for _ in range(15)]
    print(lista)
    for num in lista:
        if num  % 2 == 0:
            perc_par += 1

    arq = open('resultado.txt', 'w')

    arq.write(f'maior numero da lista é {max(lista)}\n')
    arq.write(f'menor numero da lista é {min(lista)}\n')
    arq.write(f'o percentual de pares na lista é {perc_par/15*100:.2f}%\n')
    arq.write(f'A meida da lista é {sum(lista) / len(lista):.2f}\n')
    arq.close()

    print(f'maior numero da lista é {max(lista)}')
    print(f'menor numero da lista é {min(lista)}')
    print(f'o percentual de pares na lista é {perc_par/15*100:.2f}%')
    print(f'A meida da lista é {sum(lista) / len(lista):.2f}')

    





q2 ()

#. Altere a questão 1 ou 2 da prova, para que os 15 números da lista não sejam
#   mais aleatórios, e sim provenientes de um arquivo de nome "entrada.csv", cuja
#   primeira e única linha do arquivo, contenha os 15 números separados por
#   ponto e vírgula (;). (2,5pt)

#4. Complemente a questão 1, 2 ou 3 da prova, para que o resultado apresentado
#   em tela, seja gravado em um arquivo de nome "resultado.txt". (2,5pt)
 