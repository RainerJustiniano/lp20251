# produtos.py

produtos_mercado = [
    "Arroz", "Feijão", "Macarrão", "Açúcar", "Sal", "Farinha de trigo", "Óleo de soja",
    "Leite", "Café", "Achocolatado", "Molho de tomate", "Extrato de tomate", "Milho verde (lata)",
    "Ervilha (lata)", "Sardinha (lata)", "Atum (lata)", "Biscoito doce", "Biscoito salgado",
    "Pão de forma", "Pão francês", "Margarina", "Manteiga", "Requeijão", "Queijo mussarela",
    "Presunto", "Mortadela", "Iogurte", "Creme de leite", "Leite condensado", "Suco de fruta",
    "Refrigerante", "Água mineral", "Cerveja", "Vinho", "Carne bovina", "Frango",
    "Linguiça", "Peixe", "Ovos", "Batata", "Cenoura", "Beterraba", "Tomate", "Cebola",
    "Alho", "Pimentão", "Alface", "Couve", "Espinafre", "Banana", "Maçã", "Laranja",
    "Limão", "Mamão", "Melancia", "Abacaxi", "Sabonete", "Shampoo", "Condicionador",
    "Creme dental", "Escova de dente", "Fio dental", "Papel higiênico", "Absorvente",
    "Fralda descartável", "Sabão em pó", "Sabão em barra", "Amaciante", "Detergente",
    "Desinfetante", "Esponja de aço", "Esponja de cozinha", "Vassoura", "Rodo", "Pá de lixo",
    "Saco de lixo", "Pano de chão", "Guardanapo", "Papel toalha", "Alumínio", "Filme PVC",
    "Pão de queijo", "Pizza congelada", "Lasanha congelada", "Nuggets", "Hambúrguer congelado",
    "Sorvete", "Picolé", "Chocolate", "Bala", "Chiclete", "Cereal matinal", "Aveia",
    "Granola", "Fermento em pó", "Leite em pó", "Temperos (sazon)", "Caldo de galinha",
    "Maionese", "Ketchup", "Mostarda"
]

def listar_produtos():
    """Retorna a lista completa de produtos."""
    return produtos_mercado

def buscar_produto(termo):
    """
    Busca produtos que contenham o termo (case-insensitive).
    
    Exemplo:
    buscar_produto("leite") -> ['Leite', 'Creme de leite', 'Leite condensado', 'Leite em pó']
    """
    return [produto for produto in produtos_mercado if termo.lower() in produto.lower()]
