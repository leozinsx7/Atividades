agenda = []
alterada = False

def pede_valor(campo, padrão=""):
    # Pede pra o usuario digitar um numero
    valor = input(f"{campo}: ")
    return valor if valor else padrão

def mostra_dados(nome, telefone, cidade, endereço, uf):
    # Mostra os dados de um contato, agora com cidade, endereço e UF
    print(f"Nome: {nome} Telefone: {telefone} Cidade: {cidade} Endereço: {endereço} UF: {uf}")

def pede_nome_arquivo():
    # Pede o nome do arquivo onde vamos salvar ou ler os contatos
    return input("Nome do arquivo: ")

def pesquisa(nome):
    # Procura um contato pelo nome. Se encontrar, retorna a posição dele na lista
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def verifica_repeticao(nome):
    # Verifica se o nome já está na agenda
    return pesquisa(nome) is not None

def novo():
    # Adiciona um novo contato à agenda
    global agenda, alterada
    nome = pede_valor("Nome")
    if verifica_repeticao(nome):
        print("Erro: Contato com este nome já existe.")
        return
    telefone = pede_valor("Telefone")
    cidade = pede_valor("Cidade")
    endereço = pede_valor("Endereço")
    uf = pede_valor("UF")
    agenda.append([nome, telefone, cidade, endereço, uf])
    alterada = True

def confirma(operação):
    # Pergunta ao usuário se ele confirma a operação (S para sim, N para não)
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
    # Remove um contato da agenda
    global agenda, alterada
    nome = pede_valor("Nome")
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

def altera():
    # Modifica os dados de um contato que já existe
    global alterada
    p = pesquisa(pede_valor("Nome"))
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        cidade = agenda[p][2]
        endereço = agenda[p][3]
        uf = agenda[p][4]
        print("Encontrado:")
        mostra_dados(nome, telefone, cidade, endereço, uf)
        novo_nome = pede_valor("Nome", nome)  # Se não digitar nada, mantém o valor atual
        if verifica_repeticao(novo_nome) and novo_nome.lower() != nome.lower():
            print("Erro: Contato com este nome já existe.")
            return
        novo_telefone = pede_valor("Telefone", telefone)
        nova_cidade = pede_valor("Cidade", cidade)
        novo_endereço = pede_valor("Endereço", endereço)
        nova_uf = pede_valor("UF", uf)
        if confirma("alteração") == "S":
            agenda[p] = [novo_nome, novo_telefone, nova_cidade, novo_endereço, nova_uf]
            alterada = True
    else:
        print("Nome não encontrado.")

def lista():
    # Mostra todos os contatos na agenda
    print("\nAgenda\n\n------")
    for posição, e in enumerate(agenda):
        print(f"Posição: {posição} ", end="")
        mostra_dados(e[0], e[1], e[2], e[3], e[4])
    print("------\n")

def lê_última_agenda_gravada():
    # Lê o último arquivo de agenda gravado, se houver
    última = última_agenda()
    if última is not None:
        leia_arquivo(última)

def última_agenda():
    # Tenta pegar o nome do último arquivo de agenda
    try:
        with open("ultima agenda.dat", "r", encoding="utf-8") as arquivo:
            última = arquivo.readline().strip()
    except FileNotFoundError:
        return None
    return última

def atualiza_última(nome):
    # Atualiza o nome do último arquivo de agenda gravado
    with open("ultima agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def leia_arquivo(nome_arquivo):
    # Lê o arquivo de contatos e atualiza a agenda
    global agenda, alterada
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            agenda = [linha.strip().split("#") for linha in arquivo]
        alterada = False
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

def lê():
    # Lê a agenda de um arquivo escolhido pelo usuário
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Quer gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_última(nome_arquivo)

def ordena():
    # Ordena a agenda por nome
    global alterada
    agenda.sort(key=lambda x: x[0].lower())  # Ordena os contatos por nome em minúsculas
    alterada = True

def grava():
    # Salva a agenda em um arquivo
    global alterada
    if not alterada:
        print("Você não fez nenhuma alteração. Quer gravar mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for e in agenda:
                arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")
        atualiza_última(nome_arquivo)
        alterada = False
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")

def valida_faixa_inteiro(pergunta, inicio, fim):
    # Pede um número inteiro dentro de um intervalo específico
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido. Digite um número entre {inicio} e {fim}.")

def menu():
    # Mostra o menu e pede a opção do usuário
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

# Tenta carregar a última agenda que foi gravada
lê_última_agenda_gravada()

# Loop principal do programa
while True:
    opção = menu()
    if opção == 0:
        break  # Sai do programa
    elif opção == 1:
        novo()  # Adiciona um novo contato
    elif opção == 2:
        altera()  # Modifica um contato existente
    elif opção == 3:
        apaga()  # Remove um contato
    elif opção == 4:
        lista()  # Mostra todos os contatos
    elif opção == 5:
        grava()  # Salva a agenda em um arquivo
    elif opção == 6:
        lê()  # Lê uma agenda de um arquivo
    elif opção == 7:
        ordena()  # Ordena a agenda por nome
