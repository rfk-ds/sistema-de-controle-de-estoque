estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"

estoque = {}
for produto in estoque_inicial.split("#"):
    descricao, codigo, quantidade, custo, preco = produto.split(";")
    estoque[codigo] = {
        "descricao": descricao,
        "quantidade": int(quantidade),
        "custo": float(custo),
        "preco": float(preco)
    }

def cadastrar(descricao, codigo, quantidade, custo, preco):
    """
    Função para cadastrar um novo produto no estoque

    Parâmetros:
    descricao (str): Descrição do produto
    codigo (str): Código do produto
    quantidade (str): Quantidade do produto
    custo (str): Custo do produto
    preco (str): Preço do produto

    Retornos:
    str: Mensagem de sucesso ou erro
    """
    if codigo in estoque:
        return "Produto já cadastrado"
    estoque[codigo] = {
        "descricao": descricao,
        "quantidade": int(quantidade),
        "custo": float(custo),
        "preco": float(preco)
    }
    return "Produto cadastrado com sucesso"

def listar():
    """
    Função para listar todos os produtos do estoque
    """
    for codigo, info in estoque.items():
        print(f"Descrição: {info['descricao']}, Código: {codigo}, Quantidade: {info['quantidade']}, Custo: {info['custo']}, Preço: {info['preco']}")

def ordenar():
    """
    Função para ordenar os produtos do estoque pela quantidade disponível
    """
    produtos_ordenados = sorted(estoque.items(), key=lambda item: item[1]['quantidade'])
    for codigo, info in produtos_ordenados:
        print(f"Descrição: {info['descricao']}, Código: {codigo}, Quantidade: {info['quantidade']}, Custo: {info['custo']}, Preço: {info['preco']}")

def buscar(descricao, codigo):
    """
    Função para buscar um produto no estoque

    Parâmetros:
    descricao (str): Descrição do produto
    codigo (str): Código do produto

    Retornos:
    str: Mensagem de erro
    """
    for codigo, info in estoque.items():
        if descricao in info['descricao'] or codigo == codigo:
            print(f"Descrição: {info['descricao']}, Código: {codigo}, Quantidade: {info['quantidade']}, Custo: {info['custo']}, Preço: {info['preco']}")
            return
        print("Produto não encontrado")

def remover(codigo):
    """
    Função para remover um produto do estoque

    Parâmetros:
    codigo (str): Código do produto

    Retornos:
    str: Mensagem de sucesso ou erro
    """
    if codigo in estoque:
        del estoque[codigo]
        return "Produto removido com sucesso"
    return "Produto não encontrado"

def esgotados():
    """
    Função para listar os produtos esgotados do estoque

    """
    for codigo, info in estoque.items():
        if info['quantidade'] == 0:
            print(f"Descrição: {info['descricao']}, Código: {codigo}, Quantidade: {info['quantidade']}, Custo: {info['custo']}, Preço: {info['preco']}")

def baixa_quantidade(limite=10):
    """
    Função para listar os produtos com quantidade abaixo de um limite

    Parâmetros:
    limite (int): Limite de quantidade
    """
    for codigo, info in estoque.items():
        if info['quantidade'] < limite:
            print(f"Descrição: {info['descricao']}, Código: {codigo}, Quantidade: {info['quantidade']}, Custo: {info['custo']}, Preço: {info['preco']}")

def atualizar_quantidade(codigo, quantidade):
    """
    Função para atualizar a quantidade de um produto no estoque

    Parâmetros:
    codigo (str): Código do produto
    quantidade (int): Quantidade a ser atualizada

    Retornos:
    str: Mensagem de sucesso ou erro
    """
    if codigo in estoque:
        estoque[codigo]['quantidade'] += quantidade
        return "Quantidade atualizada com sucesso"
    return "Produto não encontrado"

def atualizar_preco(codigo, preco):
    """
    Função para atualizar o preço de um produto no estoque

    Parâmetros:
    codigo (str): Código do produto
    preco (float): Preço a ser atualizado

    Retornos:
    str: Mensagem de sucesso ou erro
    """
    if codigo in estoque:
        estoque[codigo]['preco'] = preco
        return "Preço atualizado com sucesso"
    return "Produto não encontrado"

def calcular_total():
    """
    Função para calcular o valor total do estoque

    Retornos:
    float: Valor total do estoque
    """
    total = 0
    for info in estoque.values():
        total += info['quantidade'] * info['preco']
    return total

def lucro_presumido():
    """
    Função para calcular o lucro presumido do estoque

    Retornos:
    float: Lucro presumido do estoque
    """
    lucro = 0
    for info in estoque.values():
        lucro += info['quantidade'] * (info['preco'] - info['custo'])
    return lucro

def relatorio():
    """
    Função para exibir um relatório geral do estoque
    """
    for codigo, info in estoque.items():
        print(f"Descrição: {info['descricao'].ljust(30)} Código: {codigo.rjust(3)} Quantidade: {str(info['quantidade']).rjust(2)} Custo: {str(info['custo']).rjust(7)} Preço: {str(info['preco']).rjust(7)} Total: {(info['quantidade'] * info['preco'])}")
    print(f"Custo total: {sum(info['quantidade'] * info['custo'] for info in estoque.values())}")
    print(f"Faturamento total: {sum(info['quantidade'] * info['preco'] for info in estoque.values())}")

def menu():
    """
    Função para exibir e selecionar opções do menu interativo
    """
    print("\n")
    print("------------ MENU ------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Ordenar")
    print("4 - Buscar")
    print("5 - Remover")
    print("6 - Esgotados")
    print("7 - Baixa quantidade")
    print("8 - Atualizar quantidade")
    print("9 - Atualizar preço")
    print("10 - Calcular total")
    print("11 - Lucro presumido")
    print("12 - Relatório")
    print("0 - Sair")
    print("\n")

    opcao = input("Escolha uma opção: ")
    print("\n")

    if opcao == "1":
        descricao = input("Descrição: ")
        codigo = input("Código: ")
        quantidade = input("Quantidade: ")
        custo = input("Custo: ")
        preco = input("Preço: ")
        print(cadastrar(descricao, codigo, quantidade, custo, preco))
    elif opcao == "2":
        listar()
    elif opcao == "3":
        ordenar()
    elif opcao == "4":
        print("Pesquisar por: \n\n1 - Descrição\n2 - Código\n")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            descricao = input("Descrição: ")
            buscar(descricao, "")
        elif opcao == "2":
            codigo = input("Código: ")
            buscar("", codigo)
    elif opcao == "5":
        codigo = input("Código: ")
        print(remover(codigo))
    elif opcao == "6":
        esgotados()
    elif opcao == "7":
        limite = input("Limite: ")
        baixa_quantidade(int(limite))
    elif opcao == "8":
        codigo = input("Código: ")
        quantidade = input("Quantidade: ")
        print(atualizar_quantidade(codigo, int(quantidade)))
    elif opcao == "9":
        codigo = input("Código: ")
        preco = input("Preço: ")
        print(atualizar_preco(codigo, float(preco)))
    elif opcao == "10":
        print(calcular_total())
    elif opcao == "11":
        print(lucro_presumido())
    elif opcao == "12":
        relatorio()
    elif opcao == "0":
        return
    menu()

menu()