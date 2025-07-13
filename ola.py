def q1 ():
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    saldo = float(input('Digite seu saldo: '))
    print(f'Olá, {nome}! Você tem {idade} anos e seu saldo é de R$ {saldo}')

def q2 ():
    n1 = int(input('Digite n1: '))
    n2 = int(input('Digite n2: '))

    print(f'A soma de {n1} + {n2} é: {n1+n2}')
    print(f'A subitração de {n1} - {n2} é: {n1-n2}')
    print(f'A multiplicação de {n1} * {n2} é: {n1*n2}')
    print(f'A divisão de {n1} / {n2} é: {n1/n2}')
    print(f'O resultado de {n1} elevado a {n2} é: {n1**n2}')

def q3 ():
    n1 = int(input('Digite a idade de n1: '))
    n2 = int(input('Digite a idade de n2: '))

    if n1 == n2:
        print(f'N1:Idade {n1} tem a mesma idade de N2:Idade {n2} ! ')
    elif n1 > n2:
        print(f'N1:Idade {n1} é mais velho que N2:Idade {n2} ! ')
    else:
        print(f'N2:Idade {n2} é mais velho que N1:Idade {n1} ! ')

def q4 ():
    nota1 = float(input('Digite uma nota de 0 a 10: '))
    nota2 = float(input('Digite uma nota de 0 a 10: '))
    nota3 = float(input('Digite uma nota de 0 a 10: '))
    media = (nota1 + nota2 + nota3) / 3
    print(f'A media do produto X é: {media}')
    if media >= 9:
        print('Excelente produto! ')
    if media > 7 and  8.9:
        print('Produto satisfatorio! ')
    else:
        print('Produto com problema! ')

def q5 ():
    




questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')