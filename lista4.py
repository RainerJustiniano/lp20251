import random
#import names
from produtos import listar_produtos
'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1():
    lista = []
    for _ in range(15):
        lista.append(random.randrange(100))
    print(lista)
    numero = int(input('Digite um numero a ser buscado: '))
    try:
        posicao = lista.index(numero)
    except ValueError:
        print(f'{numero} não localizado na lista')
    else:
        print(f'Localizado na posição: {posicao}')

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada.
def q2():
    letras = []
    for _ in range(10):
        letras.append(chr(random.randrange(65,91)))
    cont = 1 
    for c in letras:
        print(f'{cont}: {c}')
        cont+=1

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)
def q21():
    qtde = int(input('Qtde de caracteres para a senha: ',8,20))
    senha = ''
    for _ in range(qtde):
        senha+=chr(random.randrange(40,127))
    print(f'Senha sugerida: {senha}')   
    
#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q3 ():
    arquivo = open('questao.csv','r')
    for linha in arquivo:
        numeros = linha.split(';')
        resultado = ''
        for numero in numeros:
            resultado+=f'{numero}\t{"PAR" if int(numero)%2==0 else "IMPAR"}\n'
        arquivo_saida = open('questao.out','w')
        arquivo_saida.write(resultado)
    arquivo.close()
    arquivo_saida.colse()


#4 . Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q4 ():





#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5():
    diario = []
    
    for _ in range(15):
        aluno = dict()
        aluno['nome'] = names.get_first_name()
        aluno['n1'] = random.randrange(0,11)
        aluno['n2'] = random.randrange(0,11)
        aluno['media'] = round((aluno['n1'] + aluno['n2'])/2,1)
        aluno['situacao'] = 'AP' if aluno['media'] >= 6 else 'RP'
        diario.append(aluno)

    resultado = 'NOME\tN1\tN2\tMEDIA\tSITUACAO\n'
    for a in diario:
        resultado += f'{a['nome']}\t{a['n1']}\t{a['n2']}\t{a['media']}\t{a['situacao']}\n'
    print(resultado)


#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q6():
    salario = []
    contchar = 65
    for _ in range(20):
        prof = dict()
        prof['nome'] = chr(contchar)
        contchar += 1
        prof['sal'] = round(random.randrange(800,1564))
        prof['nsal'] = prof['sal'] + (prof['sal'] * 0.08)
        salario.append(prof)
    
    listasalario = 'NOME\tSALARIO\tNOVOSALARIO\n'
    for a in salario:
        listasalario += f'{a['nome']}\t{a['sal']}\t{a['nsal']  }\n'
    print(listasalario)




#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%

def q7():
    nomes_produtos = [
        "Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar", "Café", "Sal", "Farinha", "Leite", "Manteiga",
        "Pão", "Presunto", "Queijo", "Frango", "Carne", "Peixe", "Biscoito", "Chocolate", "Refrigerante", "Suco",
        "Água", "Iogurte", "Sabonete", "Shampoo", "Condicionador", "Papel Higiênico", "Pasta de Dente", "Escova", "Detergente", "Sabão em Pó",
        "Alface", "Tomate", "Cebola", "Alho", "Cenoura", "Batata", "Maçã", "Banana", "Laranja", "Uva",
        "Chiclete", "Balas", "Leite Condensado", "Creme de Leite", "Molho de Tomate", "Sardinha", "Atum", "Palmito", "Ervilha", "Milho",
        "Fubá", "Aveia", "Granola", "Pipoca", "Torrada", "Requeijão", "Margarina", "Amaciante", "Desinfetante", "Água Sanitária",
        "Cerveja", "Vinho", "Whisky", "Vodka", "Energético", "Barra de Cereal", "Rosquinha", "Bolo", "Croissant", "Pizza Congelada",
        "Hambúrguer", "Salsicha", "Linguiça", "Queijo Prato", "Queijo Minas", "Presunto Parma", "Lasanha", "Escondidinho", "Feijoada", "Panqueca",
        "Sopa", "Molho Branco", "Tempero", "Ketchup", "Mostarda", "Maionese", "Picles", "Champignon", "Azeitona", "Seleta de Legumes",
        "Esponja", "Saco de Lixo", "Luvas", "Desodorante", "Cotonete", "Absorvente", "Sabão em Barra", "Água com Gás", "Suco Natural", "Gelatina"
    ]
   
    def listar_produtos():
        return random.choice(nomes_produtos)

    precos_compra = []
    precos_venda = []
    produtos_mercado = []

    lucro_menor_10 = 0
    lucro_entre_10_e_20 = 0
    lucro_maior_20 = 0

    for i in range(100):
        compra = round(random.uniform(10.0, 100.0), 2)
        margem = random.uniform(0.05, 0.5)
        venda = round(compra * (1 + margem), 2)
        produto = listar_produtos()

        precos_compra.append(compra)
        precos_venda.append(venda)
        produtos_mercado.append(produto)

        lucro = ((venda - compra) / compra) * 100

        if lucro < 10:
            lucro_menor_10 += 1
        elif 10 <= lucro <= 20:
            lucro_entre_10_e_20 += 1
        else:
            lucro_maior_20 += 1

    print("\n--- Resumo de Lucros (Dados Simulados) ---")
    print(f"Mercadorias com lucro < 10%: {lucro_menor_10}")
    print(f"Mercadorias com 10% <= lucro <= 20%: {lucro_entre_10_e_20}")
    print(f"Mercadorias com lucro > 20%: {lucro_maior_20}")
    print(f"\n{'Tabela de preços':>40}")
    print(f"\n{'N°':<4}{'Produto':>13}{'Compra':>22}{'Venda':>19}{'Lucro':>19}")
    print("_" * 82)
    for i in range(100):
        lucro_percentual = ((precos_venda[i] - precos_compra[i]) / precos_compra[i]) * 100
        print(f"{i+1:03d} - {produtos_mercado[i]:<20} | Compra: R$ {precos_compra[i]:>6.2f} | Venda: R$ {precos_venda[i]:>6.2f} | Lucro: {lucro_percentual:>6.2f}%")


#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
def q8():
    lista_produtos = [
        "Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar", "Café", "Sal", "Farinha", "Leite", "Manteiga",
        "Pão", "Presunto", "Queijo", "Frango", "Carne", "Peixe", "Biscoito", "Chocolate", "Refrigerante", "Suco",
        "Água", "Iogurte", "Sabonete", "Shampoo", "Condicionador", "Papel Higiênico", "Pasta de Dente", "Escova", "Detergente", "Sabão em Pó"
    ]
    
    produtos = {}
    codigo = 0
    quantidade = 0
    valor_compra = 0
    valor_venda = 0
    for i in range(30):
        print(f'\nProduto: {lista_produtos[i]}')
        codigo = round(random.randrange(1,31))
        quantidade = round(random.randrange(1,10))
        valor_compra = round(random.uniform(10.0, 100.0), 2)
        valor_venda = round(random.uniform(10.0, 100.0), 2)
        produtos[codigo] = {
            'nome': lista_produtos[i],
            'quantidade': quantidade,
            'compra': valor_compra,
            'venda': valor_venda
        }
    opcao = input('Digite 1 para listar todos os produtos ou 2 para buscar por código: ')
    if opcao == '1':
        print('Código\tNome\tQtd\tCompra\tVenda\n')
        for cod, p in produtos.items():
             print(f"{cod}\t{p['nome']:<15}{p['quantidade']}\tR$ {p['compra']:.2f}\tR$ {p['venda']:.2f}")
    elif opcao == "2":
        codigo = input("Digite o código do produto: ")
        if codigo in produtos:
            p = produtos[codigo]
            print(f"\nProduto: {p['nome']}")
            print(f"Quantidade: {p['quantidade']}")
            print(f"Valor de compra: R$ {p['compra']:.2f}")
            print(f"Valor de venda: R$ {p['venda']:.2f}")
        else:
            print("Produto não encontrado.")
    else:
        print("Opção inválida.")



#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#um vetor e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')