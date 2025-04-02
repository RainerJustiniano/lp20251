'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q01():
    print('João Paulo')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q02():
    print('30 + 27')

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q03():
    media = (5 + 8 + 12) / 3
    print(media)


#4. Faça um programa que leia e imprima um número inteiro.
def q04():
    numero = int(input('Digite um numero:'))
    print(numero)

#5. Faça um programa que leia dois números reais e os imprima.
def q05():
    num1 = float(input('Digite num1:'))
    num2 = float(input('Digite num2:'))
    print(num1,num2)


#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q06():
    num = int(input('Digite um numero: '))
    print(f'Antecessor:{num-1}')
    print(f'Sucessor:{num+1}')

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q07():
    Nome = input('Digite o nome: ')
    Endereço = input('Digite o endereço: ')
    Telefone = input('Digite o telefone: ')
    
    print(f'Nome: {Nome}, Endereço: {Endereço}, Telefone: {Telefone}')
    
 
#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q08():
    num1 = int(input('Digite num1: '))
    num2 = int(input('Digite num2: '))
    print(num1 - num2)


#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q09():
    num = float(input('Digite um numero: '))
    #num = num/4
    print(num/4)


#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    num3 = float(input('num3: '))
    media = (num1 + num2 + num3) / 3
    print(media)


#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = float(input('num1: '))
    num2 = float(input('num2: '))
    ad = (num1 + num2)
    sub = (num1 - num2)
    mult = (num1 * num2)
    div = (num1 / num2)
    texto = f'''
    Adição:{ad}
    Subtração:{sub}
    Multiplicação:{mult}
    Divisão:{div}
    '''
    print(texto)


#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    num = float(input('num: '))
    num = num ** 2
    print (num)


#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    Saldo = float(input('Digite o saldo da conta: ')) 
    Nsaldo = (Saldo * 0.02)
    Saldof = (Saldo + Nsaldo)

    print (Saldof)

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).  
def q14():
    base = float(input('Digite a base do retangulo: ')) 
    altura = float(input('Digite a altura do retangulo: '))
    Perimetro = (base*2 + altura*2)
    Área = (base * altura)
    print (f'O perimetro é {Perimetro} e a área é {Área}.')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor_produto = float(input('Valor do produto: R$ '))
    percentual_desconto = float(input('Percentual do desconto: '))
    valor_desconto = round(valor_produto * percentual_desconto/100, 2)
    valor_produto_desconto = valor_produto - valor_desconto
    resultado = f'''
    Valor do produto: R$ {valor_produto}
    Valor do desconto: ({percentual_desconto}%): R$ {valor_desconto}
    Valor final do Produto: R$ {valor_produto_desconto}
    '''
    print(resultado)



#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    salario = float(input('Valor do salario: R$ '))
    reajuste_salario = float(input('Valor do reajste: R$ '))
    salario_reajstado = round(salario * reajuste_salario/100, 2)
    resultado = f'''
    Valor do salario: R$ {salario}
    Reajste do salario: R$ {salario_reajstado}
    Salario reajustado: R$ {salario + salario_reajstado}
    '''
    print(resultado)
q16()
#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17 ():
    C = float(input('Digite a temperatura em C: '))
    F = (9 * C + 160) / 5
    print(F)



#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    T = float(input('Digite o tempo de viagem (em horas): '))
    V = float(input('Digite a velocidade (em km/h): '))
    D = T * V
    L = D / 12
    Texto = f'''
    Distancia percorrida: {D} 
    Litros de combustivel gasto: {L}
    Tempo de viagem: {T} horas.
    '''
    print(Texto)




#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19(): 
    prestacao = float(input('Digite o valor da prestação em atraso (R$): '))
    taxa = float(input('Digite a taxa de juros (em porcentagem): '))
    tempo = float(input('Digite o período de atraso (Em dias): '))

    juros = prestacao * (taxa/100) * tempo
    texto = f'''
    O valor da prestação atrasada é: {prestacao} reais.
    O período de atraso foi de {tempo} dias.
    Os juros acumulados são de: {juros} reais.
    O valor final da prestação é: {prestacao + juros} reais.
 '''
    print(texto)



#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.