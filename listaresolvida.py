# 1. Imprime seu nome
def q1():
    print("Seu Nome")

# 2. Imprime o produto de 30 e 27
def q2():
    print(30 * 27)

# 3. Imprime a média aritmética de 5, 8, 12
def q3():
    print((5 + 8 + 12) / 3)

# 4. Lê e imprime um número inteiro
def q4():
    n = int(input("Digite um número inteiro: "))
    print(n)

# 5. Lê dois números reais e imprime-os
def q5():
    a = float(input("Digite o primeiro número real: "))
    b = float(input("Digite o segundo número real: "))
    print(a, b)

# 6. Lê um número inteiro e imprime antecessor e sucessor
def q6():
    n = int(input("Digite um número inteiro: "))
    print("Antecessor:", n-1)
    print("Sucessor:", n+1)

# 7. Lê nome, endereço e telefone e imprime
def q7():
    nome = input("Nome: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    print("Nome:", nome)
    print("Endereço:", endereco)
    print("Telefone:", telefone)

# 8. Lê dois inteiros e imprime a subtração
def q8():
    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))
    print("Subtração:", a - b)

# 9. Lê um real e imprime 1/4 deste número
def q9():
    n = float(input("Digite um número real: "))
    print(n / 4)

# 10. Lê 3 reais e imprime a média
def q10():
    a = float(input())
    b = float(input())
    c = float(input())
    print("Média:", (a+b+c)/3)

# 11. Lê dois reais e imprime as 4 operações
def q11():
    a = float(input())
    b = float(input())
    print("Soma:", a+b)
    print("Subtração:", a-b)
    print("Multiplicação:", a*b)
    print("Divisão:", a/b if b != 0 else "Divisão por zero")

# 12. Lê um real e imprime o quadrado
def q12():
    n = float(input())
    print("Quadrado:", n*n)

# 13. Lê saldo e imprime novo saldo com reajuste de 2%
def q13():
    saldo = float(input("Saldo: "))
    novo = saldo * 1.02
    print("Novo saldo:", novo)

# 14. Lê base e altura de retângulo, imprime perímetro e área
def q14():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    perimetro = 2*base + 2*altura
    area = base * altura
    print("Perímetro:", perimetro)
    print("Área:", area)

# 15. Lê valor, percentual desconto e imprime desconto e valor final
def q15():
    valor = float(input("Valor do produto: "))
    perc = float(input("Percentual de desconto: "))
    desconto = valor * perc / 100
    final = valor - desconto
    print("Desconto:", desconto)
    print("Valor com desconto:", final)

# 16. Lê salário e percentual de reajuste, imprime novo salário
def q16():
    salario = float(input("Salário atual: "))
    perc = float(input("Percentual de reajuste: "))
    novo = salario * (1 + perc/100)
    print("Novo salário:", novo)

# 17. Lê graus Celsius, converte para Fahrenheit
def q17():
    c = float(input("Temperatura em °C: "))
    f = (9*c + 160) / 5
    print("Temperatura em Fahrenheit:", f)

# 18. Consumo de combustível em viagem
def q18():
    tempo = float(input("Tempo de viagem (horas): "))
    velocidade = float(input("Velocidade média (km/h): "))
    distancia = tempo * velocidade
    litros = distancia / 12
    print("Distância:", distancia)
    print("Combustível consumido:", litros)

# 19. Prestação em atraso (juros simples)
def q19():
    valor = float(input("Valor da prestação: "))
    taxa = float(input("Taxa de juros (%): "))
    tempo = int(input("Período de atraso (meses): "))
    juros = valor * (taxa/100) * tempo
    total = valor + juros
    print("Valor da prestação atrasada:", valor)
    print("Período de atraso:", tempo)
    print("Juros:", juros)
    print("Valor total com juros:", total)

# 20. Conversão dólar para real
def q20():
    valor_dolar = float(input("Valor em dólar: "))
    cotacao = float(input("Cotação do dólar: "))
    valor_real = valor_dolar * cotacao
    print("Valor em reais: R$", valor_real)

def q21():
    a = int(input("Digite o primeiro valor: "))
    b = int(input("Digite o segundo valor: "))
    soma = a + b
    if soma > 10:
        print(soma)

def q22():
    a = int(input())
    b = int(input())
    soma = a + b
    if soma > 20:
        print(soma + 8)
    else:
        print(soma - 5)

def q23():
    n = int(input("Digite um número: "))
    if n % 3 == 0:
        print("É múltiplo de 3")
    else:
        print("Não é múltiplo de 3")

def q24():
    n = int(input("Digite um número: "))
    print("Divisível por 5" if n % 5 == 0 else "Não divisível por 5")

def q25():
    n = int(input("Digite um número: "))
    if n % 3 == 0 and n % 7 == 0:
        print("Divisível por 3 e por 7")
    else:
        print("Não é divisível por 3 e por 7")

def q26():
    salario = float(input("Salário bruto: "))
    prestacao = float(input("Valor da prestação: "))
    if prestacao <= salario * 0.3:
        print("Empréstimo concedido")
    else:
        print("Empréstimo não concedido")

def q27():
    n = int(input())
    print("Está entre 20 e 50" if 20 <= n <= 50 else "Não está entre 20 e 50")

def q28():
    n = int(input())
    if n > 20:
        print("Maior do que 20")
    elif n == 20:
        print("Igual a 20")
    else:
        print("Menor do que 20")

def q29():
    nascimento = int(input("Ano de nascimento: "))
    ano_atual = int(input("Ano atual: "))
    if nascimento > ano_atual or nascimento < 1900:
        print("Ano de nascimento inválido")
    else:
        print("Idade:", ano_atual - nascimento)

def q30():
    a = int(input())
    b = int(input())
    c = int(input())
    lista = [a, b, c]
    lista.sort()
    print(lista)

def q31():
    a = int(input())
    b = int(input())
    c = int(input())
    print("Maior:", max(a, b, c))

def q32():
    idade = int(input("Idade: "))
    if idade >= 18 and idade <= 65:
        print("Maior de idade")
    if idade < 18:
        print("Menor de idade")
    if idade > 65:
        print("Maior de 65 anos")

def q33():
    nome = input("Nome: ")
    p1 = float(input("Nota 1: "))
    p2 = float(input("Nota 2: "))
    media = (p1 + p2) / 2
    print(f"Aluno: {nome}")
    print(f"Nota 1: {p1}")
    print(f"Nota 2: {p2}")
    print(f"Média: {media}")
    if media >= 7:
        print("Aprovado")
    elif media < 3:
        print("Reprovado")
    else:
        print("Em Prova Final")

def q34():
    salario = float(input("Salário: "))
    if salario <= 600:
        print("Isento")
    elif salario <= 1200:
        print("Desconto: 20% =", salario * 0.2)
    elif salario <= 2000:
        print("Desconto: 25% =", salario * 0.25)
    else:
        print("Desconto: 30% =", salario * 0.3)

def q35():
    valor = float(input("Valor de compra: "))
    if valor < 20:
        venda = valor * 1.45
    else:
        venda = valor * 1.30
    print("Valor de venda:", venda)

def q36():
    idade = int(input())
    if 5 <= idade <= 7:
        print("Infantil A")
    elif 8 <= idade <= 10:
        print("Infantil B")
    elif 11 <= idade <= 13:
        print("Juvenil A")
    elif 14 <= idade <= 17:
        print("Juvenil B")
    elif idade >= 18:
        print("Sênior")
    else:
        print("Idade fora das categorias")

def q37():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    if idade <= 10:
        valor = 30
    elif idade <= 29:
        valor = 60
    elif idade <= 45:
        valor = 120
    elif idade <= 59:
        valor = 150
    elif idade <= 65:
        valor = 250
    else:
        valor = 400
    print(f"{nome} paga R$ {valor:.2f}")

def q38():
    n = int(input())
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if 1 <= n <= 12:
        print(meses[n-1])
    else:
        print("Não existe mês com este número")

def q39():
    p1 = int(input("Pontos jogador 1: "))
    p2 = int(input("Pontos jogador 2: "))
    p3 = int(input("Pontos jogador 3: "))
    lista = [p1, p2, p3]
    lista.sort(reverse=True)
    print("Ordem decrescente:", lista)
    soma = sum(lista)
    if soma > 100:
        print("Média:", soma / 3)
    else:
        print("Equipe desclassificada")

def q40():
    saldo = float(input("Saldo médio: "))
    if saldo <= 500:
        print("Nenhum crédito")
    elif saldo <= 1000:
        print("Crédito:", saldo * 0.3)
    elif saldo <= 3000:
        print("Crédito:", saldo * 0.4)
    else:
        print("Crédito:", saldo * 0.5)

def q41():
    livro = input("Nome do livro: ")
    tipo = input("Tipo de usuário (professor/aluno): ").lower()
    if tipo == "professor":
        dias = 10
    else:
        dias = 3
    print(f"Nome do livro: {livro}")
    print(f"Tipo de usuário: {tipo}")
    print(f"Total de dias: {dias}")

def q42():
    percurso = float(input("Percurso em km: "))
    tipo = input("Tipo do carro (A/B/C): ").upper()
    if tipo == "A":
        consumo = percurso / 12
    elif tipo == "B":
        consumo = percurso / 9
    elif tipo == "C":
        consumo = percurso / 8
    else:
        print("Tipo inválido")
        return
    print(f"Consumo estimado: {consumo:.2f} litros")

def q43():
    pratos = {"vegetariano": 180, "peixe": 230, "frango": 250, "carne": 350}
    sobremesas = {"abacaxi": 75, "sorvete diet": 110, "mousse diet": 170, "mousse chocolate": 200}
    bebidas = {"chá": 20, "suco de laranja": 70, "suco de melão": 100, "refrigerante diet": 65}
    prato = input("Prato: ").lower()
    sobremesa = input("Sobremesa: ").lower()
    bebida = input("Bebida: ").lower()
    total = pratos.get(prato, 0) + sobremesas.get(sobremesa, 0) + bebidas.get(bebida, 0)
    print(f"Total de calorias: {total}")

def q44():
    placa = input("Placa: ")
    ultimo_digito = int(placa[-1])
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if 1 <= ultimo_digito <= 9:
        print(f"Renovação em {meses[ultimo_digito - 1]}")
    elif ultimo_digito == 0:
        print("Renovação em Outubro")
    else:
        print("Placa inválida!")

def q45():
    indice = float(input("Índice de poluição: "))
    if indice >= 0.5:
        print("Intimação para 1º, 2º e 3º grupos")
    elif indice >= 0.4:
        print("Intimação para 1º e 2º grupos")
    elif indice >= 0.3:
        print("Intimação para 1º grupo")
    else:
        print("Índice aceitável")

    def q46():
    for i in range(1, 101):
        print(i)

def q47():
    for i in range(100, 0, -1):
        if i % 2 == 0:
            print(i)

def q48():
    for i in range(1, 501):
        if i % 5 == 0:
            print(i)

def q49():
    for _ in range(20):
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").upper()
        if sexo == 'M' and idade > 21:
            print(nome)

def q50():
    a = int(input("1º número (positivo): "))
    b = int(input("2º número (positivo): "))
    produto = 0
    for _ in range(b):
        produto += a
    print("Produto:", produto)

def q51():
    a, b = 1, 1
    print(a, b, end=' ')
    for _ in range(18):
        c = a + b
        print(c, end=' ')
        a, b = b, c
    print()

def q52():
    nomes = []
    notas1 = []
    notas2 = []
    medias = []
    for _ in range(15):
        nome = input("Nome: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        nomes.append(nome)
        notas1.append(n1)
        notas2.append(n2)
        medias.append((n1 + n2)/2)
    for i in range(15):
        print(nomes[i], notas1[i], notas2[i], medias[i])
    print("Média geral:", sum(medias)/15)

def q53():
    for _ in range(10):
        nome = input("Nome: ")
        salario = float(input("Salário bruto: "))
        if salario < 1300:
            ir = 0
        elif salario < 2300:
            ir = salario * 0.1
        else:
            ir = salario * 0.15
        print(f"{nome} - IRRF: R$ {ir:.2f}")

def q54():
    total = exc = reg = bom = soma_exc = 0
    for _ in range(20):
        idade = int(input("Idade: "))
        op = int(input("Opinião (3=excelente, 2=bom, 1=regular): "))
        total += 1
        if op == 3:
            exc += 1
            soma_exc += idade
        elif op == 2:
            bom += 1
        elif op == 1:
            reg += 1
    print("Média idades excelente:", soma_exc/exc if exc else 0)
    print("Quantidade regular:", reg)
    print("Percentual bom:", (bom/total)*100 if total else 0)

def q55():
    peso_geral = 0
    idade_geral = 0
    for t in range(30):
        pesos = []
        idades = []
        for _ in range(12):
            peso = float(input(f"Peso atleta {t+1}: "))
            idade = int(input(f"Idade atleta {t+1}: "))
            pesos.append(peso)
            idades.append(idade)
        print(f"Time {t+1}: Peso médio {sum(pesos)/12:.2f}, Idade média {sum(idades)/12:.2f}")
        print("Mais pesado:", max(pesos))
        print("Mais jovem:", min(idades))
        peso_geral += sum(pesos)
        idade_geral += sum(idades)
    print("Peso médio geral:", peso_geral/(30*12))
    print("Idade média geral:", idade_geral/(30*12))

def q56():
    cont = 0
    while True:
        n = int(input())
        if n == 0:
            break
        if 100 <= n <= 200:
            cont += 1
    print("Quantidade entre 100 e 200:", cont)

def q57():
    a, b = 5000000, 7000000
    anos = 0
    while a <= b:
        a += a * 0.03
        b += b * 0.02
        anos += 1
    print("Anos necessários:", anos)

def q58():
    cons1 = cons2 = cons3 = 0
    while True:
        num = int(input("Número consumidor (0 encerra): "))
        if num == 0:
            break
        kwh = float(input("kWh consumidos: "))
        tipo = int(input("Tipo (1=residencial, 2=comercial, 3=industrial): "))
        if tipo == 1:
            preco = 0.3
            cons1 += kwh
        elif tipo == 2:
            preco = 0.5
            cons2 += kwh
        elif tipo == 3:
            preco = 0.7
            cons3 += kwh
        else:
            print("Tipo inválido")
            continue
        print("Custo total:", kwh*preco)
    print("Total residencial:", cons1)
    print("Total comercial:", cons2)
    print("Total industrial:", cons3)
    med = (cons1 + cons2)/2 if (cons1+cons2) else 0
    print("Média consumo tipos 1 e 2:", med)

def q59():
    while True:
        n = int(input("Digite um inteiro >=1 (menor encerra): "))
        if n < 1:
            break
        fat = 1
        for i in range(2, n+1):
            fat *= i
        print(f"Fatorial de {n}: {fat}")

def q60():
    menos21 = mais50 = 0
    while True:
        idade = int(input("Idade (0 encerra): "))
        if idade == 0:
            break
        if idade < 21:
            menos21 +=1
        if idade > 50:
            mais50 +=1
    print("Menos de 21 anos:", menos21)
    print("Mais de 50 anos:", mais50)

def q61():
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    quoc = 0
    while dividendo >= divisor:
        dividendo -= divisor
        quoc += 1
    print("Quociente:", quoc)
    print("Resto:", dividendo)

def q62():
    total = 0
    while True:
        num = int(input("Número do pedido (0 encerra): "))
        if num == 0:
            break
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        preco = float(input("Preço unitário: "))
        qtd = int(input("Quantidade: "))
        pedido = preco * qtd
        total += pedido
        print(f"Pedido {num}: R$ {pedido:.2f}")
    print("Total da compra: R$ {:.2f}".format(total))

def q63():
    total = 0
    while True:
        conta = int(input("Número da conta (0 encerra): "))
        if conta == 0:
            break
        nome = input("Nome: ")
        dias = int(input("Dias: "))
        diaria = 30 * dias
        if dias < 10:
            taxa = 15 * dias
        else:
            taxa = 8 * dias
        conta_total = diaria + taxa
        total += conta_total
        print(f"{nome} - Conta: {conta_total} - Número da conta: {conta}")
    print("Total faturado: R$ {:.2f}".format(total))

def q64():
    turmas = int(input("Quantidade de turmas: "))
    for _ in range(turmas):
        alunos = int(input("Alunos na turma: "))
        notas = []
        aprovados = 0
        for _ in range(alunos):
            nota = float(input("Nota: "))
            notas.append(nota)
            if nota >= 7:
                aprovados += 1
        media = sum(notas)/alunos
        reprovados = alunos - aprovados
        print(f"Turma: Média {media:.2f}, Aprovados {aprovados}, Reprovados {reprovados}, %Reprovados: {reprovados*100/alunos:.2f}")

def q65():
    times = [0,0,0,0,0]
    soma_bota = 0
    qtd_bota = 0
    rj_outros = 0
    nit_flu = 0
    while True:
        time = int(input("Time (0 encerra): "))
        if time == 0:
            break
        local = int(input("Local (1=RJ,2=Niterói,3=Outros): "))
        salario = float(input("Salário: "))
        times[time-1] += 1
        if time == 2:
            soma_bota += salario
            qtd_bota += 1
        if local == 1 and time == 5:
            rj_outros += 1
        if local == 2 and time == 1:
            nit_flu += 1
    print("Torcedores por clube:", times)
    print("Média salarial Botafogo:", soma_bota/qtd_bota if qtd_bota else 0)
    print("RJ torcedores outros clubes:", rj_outros)
    print("Niterói torcedores Fluminense:", nit_flu)

def q66():
    acima200 = 0
    mais_pessoal = 0
    total = 0
    soma_alim = 0
    soma_outras = 0
    soma_pessoal = 0
    soma_familiar = 0
    while True:
        renda_pessoal = float(input("Renda pessoal (0 encerra): "))
        if renda_pessoal == 0:
            break
        renda_familiar = float(input("Renda familiar: "))
        gasto_alim = float(input("Gasto alimentação: "))
        gasto_outras = float(input("Gasto outras despesas: "))
        if gasto_outras > 200:
            acima200 += 1
        if renda_pessoal > renda_familiar:
            mais_pessoal += 1
        total += 1
        soma_alim += gasto_alim
        soma_outras += gasto_outras
        soma_pessoal += renda_pessoal
        soma_familiar += renda_familiar
    print("Porcentagem que gasta acima de R$200 em outras despesas:", (acima200/total)*100 if total else 0)
    print("Número de alunos com renda pessoal maior que familiar:", mais_pessoal)
    print("Porcentagem gasta com alimentação:", (soma_alim/(soma_pessoal+soma_familiar)*100) if (soma_pessoal+soma_familiar) else 0)
    print("Porcentagem gasta com outras despesas:", (soma_outras/(soma_pessoal+soma_familiar)*100) if (soma_pessoal+soma_familiar) else 0)

def q67():
    total = 0
    max_multas = 0
    carteira_max = 0
    while True:
        carteira = int(input("Carteira (0 encerra): "))
        if carteira == 0:
            break
        num_multas = int(input("Número de multas: "))
        valor = 0
        for _ in range(num_multas):
            multa = float(input("Valor multa: "))
            valor += multa
        print(f"Dívida motorista {carteira}: R$ {valor:.2f}")
        total += valor
        if num_multas > max_multas:
            max_multas = num_multas
            carteira_max = carteira
    print("Total arrecadado:", total)
    print("Carteira com maior número de multas:", carteira_max)

def q68():
    mais_alta_fem = ""
    alt_fem = 0
    mais_pesado_masc = ""
    peso_masc = 0
    soma_idade = 0
    total = 0
    while True:
        nome = input("Nome (@ encerra): ")
        if nome == "@":
            break
        sexo = input("Sexo (M/F): ").upper()
        idade = int(input("Idade: "))
        peso = float(input("Peso: "))
        altura = float(input("Altura: "))
        total += 1
        soma_idade += idade
        if sexo == "F" and altura > alt_fem:
            alt_fem = altura
            mais_alta_fem = nome
        if sexo == "M" and peso > peso_masc:
            peso_masc = peso
            mais_pesado_masc = nome
    print("Atleta feminina mais alta:", mais_alta_fem)
    print("Atleta masculino mais pesado:", mais_pesado_masc)
    print("Média de idade dos atletas:", soma_idade/total if total else 0)

def q69():
    total_litros = 0
    while True:
        v = float(input("Velocidade (negativa encerra): "))
        if v < 0:
            break
        t = float(input("Tempo: "))
        dist = v * t
        litros = dist / 10
        print(f"Distância: {dist}, Litros: {litros}")
        total_litros += litros
    print("Total de litros gastos:", total_litros)

def q70():
    total_ir = 0
    isentos = 0
    while True:
        cic = int(input("CIC (0 encerra): "))
        if cic == 0:
            break
        dep = int(input("Dependentes: "))
        renda = float(input("Renda bruta anual: "))
        abat = dep * 600
        renda_liq = renda - abat
        if renda_liq <= 1000:
            ir = 0
            isentos += 1
        elif renda_liq <= 5000:
            ir = renda_liq * 0.15
        else:
            ir = renda_liq * 0.25
        total_ir += ir
        print(f"CIC: {cic}, Imposto: R${ir:.2f}")
    print("Total arrecadado:", total_ir)
    print("Contribuintes isentos:", isentos)

def q71():
    canais = {4:0, 5:0, 7:0, 12:0}
    total = 0
    while True:
        canal = int(input("Canal (0 encerra): "))
        if canal == 0:
            break
        pessoas = int(input("Pessoas assistindo: "))
        if canal in canais:
            canais[canal] += pessoas
            total += pessoas
    for c in canais:
        perc = (canais[c]/total)*100 if total else 0
        print(f"Canal {c}: {perc:.2f}%")

def q72():
    melhor_cr = 0
    while True:
        mat = int(input("Matrícula (1-5000, fora encerra): "))
        if not (1 <= mat <= 5000):
            break
        qtd = int(input("Disciplinas: "))
        notas = []
        for _ in range(qtd):
            notas.append(float(input("Nota: ")))
        cr = sum(notas)/qtd
        print(f"Matrícula {mat}: CR={cr:.2f}")
        if qtd >= 5 and cr > melhor_cr:
            melhor_cr = cr
    print("Melhor CR (5 ou + disciplinas):", melhor_cr)

def q73():
    mais50 = alt10_20 = qtd10_20 = peso40 = total = 0
    while True:
        idade = int(input("Idade (-1 encerra): "))
        if idade == -1:
            break
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))
        total += 1
        if idade > 50:
            mais50 += 1
        if 10 <= idade <= 20:
            alt10_20 += altura
            qtd10_20 += 1
        if peso < 40:
            peso40 += 1
    print("Idade > 50:", mais50)
    print("Média altura 10-20:", alt10_20/qtd10_20 if qtd10_20 else 0)
    print("Porcentagem <40kg:", (peso40/total)*100 if total else 0)

def q74():
    total = lim = alim = hig = 0
    while True:
        valor = float(input("Valor (0 encerra): "))
        if valor == 0:
            break
        codigo = input("Código (L/A/H): ").upper()
        total += valor
        if codigo == "L":
            lim += valor
        elif codigo == "A":
            alim += valor
        elif codigo == "H":
            hig += valor
    print("Total vendido:", total)
    print("Limpeza:", lim)
    print("Alimentação:", alim)
    print("Higiene:", hig)

def q75():
    cas = sol = viu = desq = qtd = soma_viu = 0
    while True:
        idade = int(input("Idade (<0 encerra): "))
        if idade < 0:
            break
        estado = input("Estado civil (C/S/V/D): ").upper()
        qtd += 1
        if estado == "C":
            cas += 1
        elif estado == "S":
            sol += 1
        elif estado == "V":
            viu += 1
            soma_viu += idade
        elif estado == "D":
            desq += 1
    print("Casados:", cas)
    print("Solteiros:", sol)
    print("Média idade viúvos:", soma_viu/viu if viu else 0)
    print("Porcentagem desquitados:", (desq/qtd)*100 if qtd else 0)

def q76():
    lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(15)]
    busca = int(input("Digite um número para buscar: "))
    if busca in lista:
        print("Posição:", lista.index(busca))
    else:
        print("Nao encontrado!")

def q77():
    letras = [input(f"Digite a {i+1}ª letra: ") for i in range(10)]
    for idx, l in enumerate(letras, 1):
        print(f"{idx} - {l}")

def q78():
    import random
    qtde = int(input("Quantidade de caracteres da senha: "))
    senha = ''.join([chr(random.randint(40, 126)) for _ in range(qtde)])
    print("Senha sugerida:", senha)

def q79():
    lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(15)]
    for idx, n in enumerate(lista, 1):
        tipo = "par" if n % 2 == 0 else "ímpar"
        print(f"{idx}: {n} - {tipo}")

def q80():
    lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(8)]
    mult6 = sum(1 for n in lista if n % 6 == 0)
    for n in lista:
        print(n)
    print("Total múltiplos de 6:", mult6)

def q81():
    salarios = [float(input(f"Salário {i+1}: ")) for i in range(20)]
    novos = [s * 1.08 for s in salarios]
    for idx, (old, new) in enumerate(zip(salarios, novos), 1):
        print(f"{idx}: Original: {old:.2f} - Novo: {new:.2f}")

def q82():
    compra = [float(input(f"Preço de compra {i+1}: ")) for i in range(100)]
    venda = [float(input(f"Preço de venda {i+1}: ")) for i in range(100)]
    menos10 = entre10e20 = mais20 = 0
    for c, v in zip(compra, venda):
        lucro = (v-c)/c * 100
        if lucro < 10:
            menos10 += 1
        elif lucro <= 20:
            entre10e20 += 1
        else:
            mais20 += 1
    print("Lucro <10%:", menos10)
    print("Lucro 10%-20%:", entre10e20)
    print("Lucro >20%:", mais20)

def q83():
    produtos = {}
    for _ in range(30):
        cod = input("Código: ")
        qtd = int(input("Quantidade: "))
        compra = float(input("Valor compra: "))
        venda = float(input("Valor venda: "))
        produtos[cod] = {"quant": qtd, "compra": compra, "venda": venda}
    busca = input("Digite o código para listar (ou enter para todos): ")
    if busca == "":
        for cod, dados in produtos.items():
            print(f"{cod}: {dados}")
    else:
        print(produtos.get(busca, "Não encontrado"))

def q84():
    conj1 = [int(input(f"Conjunto 1, elemento {i+1}: ")) for i in range(10)]
    conj2 = [int(input(f"Conjunto 2, elemento {i+1}: ")) for i in range(10)]
    comuns = set(conj1) & set(conj2)
    print("Elementos comuns:", comuns)

def q85():
    import math
    lista = [int(input(f"Elemento {i+1}: ")) for i in range(10)]
    fatoriais = [math.factorial(n) for n in lista]
    print("Fatoriais:", fatoriais)
    maior = max(lista)
    menor = min(lista)
    pares = sum(1 for n in lista if n % 2 == 0)
    print("Maior:", maior)
    print("Menor:", menor)
    print("Percentual pares:", pares/10*100)
    print("Média:", sum(lista)/10)

def q86():
    lista = [int(input(f"Elemento {i+1}: ")) for i in range(10)]
    maior = max(lista)
    menor = min(lista)
    pares = sum(1 for n in lista if n % 2 == 0)
    print("Maior:", maior)
    print("Menor:", menor)
    print("Percentual pares:", pares/10*100)
    print("Média:", sum(lista)/10)

def q87():
    mesas = [5] * 30  # 30 mesas com 5 lugares cada
    ocupados = 0
    while ocupados < 150:
        cod = int(input("Código da mesa (1 a 30, 0 encerra): "))
        if cod == 0:
            break
        if not 1 <= cod <= 30:
            print("Mesa inválida")
            continue
        lugares = int(input("Quantidade de lugares: "))
        if lugares <= mesas[cod-1]:
            mesas[cod-1] -= lugares
            ocupados += lugares
            print("Reserva realizada")
        else:
            print("Não há lugares suficientes nesta mesa!")
    print("Reservas encerradas.")

def q88():
    voos = {}
    for _ in range(10):
        num = input("Número do voo: ")
        lugares = int(input("Lugares disponíveis: "))
        voos[num] = lugares
    while True:
        cliente = input("Carteira identidade (Enter para sair): ")
        if cliente == "":
            break
        voo = input("Número do voo desejado (0 encerra): ")
        if voo == "0":
            break
        if voo in voos and voos[voo] > 0:
            voos[voo] -= 1
            print("Reserva confirmada para", cliente, "no voo", voo)
        else:
            print("Voo inexistente ou lotado.")

def q89():
    lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(50)]
    quadrados = [n**2 for n in lista]
    print("Quadrados:", quadrados)

def q90():
    nums = []
    for _ in range(100):
        n = int(input("Digite um número (0 encerra): "))
        if n == 0:
            break
        nums.append(n)
    if nums:
        ultimo = nums[-1]
        iguais = sum(1 for n in nums if n == ultimo)
        print("Quantidade iguais ao último número:", iguais)
    else:
        print("Nenhum número digitado.")

def q91():
    lista = [float(input(f"Digite o {i+1}º número real: ")) for i in range(100)]
    media = sum(lista)/100
    iguais30 = sum(1 for n in lista if n == 30)
    maior_media = sum(1 for n in lista if n > media)
    iguais_media = sum(1 for n in lista if n == media)
    print("Iguais a 30:", iguais30)
    print("Maiores que a média:", maior_media)
    print("Iguais à média:", iguais_media)

def q92():
    lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(30)]
    print("Ordem inversa:", list(reversed(lista)))

def q93():
    lista = [int(input(f"Valor {i+1}: ")) for i in range(20)]
    sem_repetidos = sorted(set(lista))
    print("Lista ordenada sem repetidos:", sem_repetidos)

def q94():
    contatos = {}
    for _ in range(30):
        codigo = input("Código: ")
        telefone = input("Telefone: ")
        contatos[codigo] = telefone
    busca = input("Digite o código para buscar: ")
    print("Telefone:", contatos.get(busca, "Não encontrado."))

def q95():
    alunos = []
    for _ in range(100):
        mat = input("Matrícula: ")
        media = float(input("Média: "))
        alunos.append((media, mat))
    alunos.sort(reverse=True)  # ordem decrescente de média
    for media, mat in alunos:
        print(f"Matrícula: {mat}, Média: {media}")


questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')