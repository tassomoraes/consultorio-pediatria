#CRIA PRONTUÁRIO
def criar_protuario(dic_protuarios, ultimo_num_paciente,lista_chaves):
    prontuario = {}
    lista_input = ["Digite o nome da criança",
                   "Digite o sexo da criança",
                   "Digite o nome da mãe",
                   "Digite o nome do pai",
                   "Digite o peso atual",
                   "Digite o IMC atual",
                   "Digite a altura atual",
                   "Digite o perímetro cefálico atual"]

    chaves_input = zip(lista_chaves,lista_input)

    num_paciente = ultimo_num_paciente + 1      #sempre incrementa a partir do ultimo criado

    for chave, dado_input in chaves_input:
        if(chave == "Peso" or chave == "IMC" or chave == "Altura" or chave == "Perimétro Cefálico"):
            prontuario[chave] = [float(input(dado_input + ": "))]
        else:
            prontuario[chave] = input(dado_input + ": ")

    dic_protuarios[num_paciente] = prontuario

    return num_paciente

#MENU ATUALIZAR
def imprime_menu_atualizar():
    menu = """
    ####### MENU #######
    1 - Nome
    2 - Sexo
    3 - Nome da mãe 
    4 - Nome do pai
    5 - Peso
    6 - IMC
    7 - Altura
    8 - Perímetro cefálico
    0 - Sair
    ####################
        
Qual informação você deseja atualizar: """
    opcao = int(input(menu))
    return opcao

#ATUALIZAR
def atualizar_prontuario_por_numero(dic_prontuarios, numero):

    #verifica se o prontuário existe ou não
    if (len(dic_prontuarios) < 1) or (numero not in dic_prontuarios.keys()):
        print("Nenhum prontuário encontrado!")
    else:
        prontuario = dic_prontuarios[numero]
        opcao = ""
        #chaves recebe uma lista das chaves do dicionário
        chaves = list(prontuario.keys())

        busca_prontuario_por_numero(dic_prontuarios, numero)
        # pergunta qual dado atualizar
        while (opcao != "não"):
            indice = imprime_menu_atualizar()    #recebe um inteiro
            #se o indice estiver entre 1 e a quantidade de chaves
            if(indice >= 1 and indice <= len(chaves)):
                novo_valor = input(f"\tDigite o novo valor de {chaves[indice-1]}: ")
                prontuario[chaves[indice-1]] = novo_valor

            elif(opcao != 0):
                print("Entrada inválida!")

            opcao = input("\tDeseja alterar mais alguma informação? ")


        print("---Contao atualizado---")
        busca_prontuario_por_numero(dic_prontuarios,numero)

#BUSCA PRONTUÁRIO
def busca_prontuario_por_numero(dic_prontuarios, numero):

    #verifica se o prontuário existe ou não
    if (len(dic_prontuarios) < 1) or (numero not in dic_prontuarios.keys()):
        print("Nenhum prontuário encontrado!")
    else:
        prontuario = dic_prontuarios[numero]

        for chave in prontuario.keys():
            print(f"{chave}: {prontuario[chave]}")

#REMOVER PRONTUARIO POR NÚMERO
def remove_prontuario_por_numero(dic_prontuarios, numero):

    #verifica se o prontuário existe ou não
    if (len(dic_prontuarios) < 1) or (numero not in dic_prontuarios.keys()):
        print("Nenhum prontuário encontrado!")
    else:
        dic_prontuarios.pop(numero)
        print("Paciente removido!")

#REMOVER PRONTUÁRIO POR NOME
def remove_prontuario(dic_prontuarios, nome_paciente):

    lista_prontuarios = {}
    for numero, prontuario in dic_prontuarios.items():
        if nome_paciente in prontuario["Nome"]:
            lista_prontuarios[numero] = prontuario

    if (len(lista_prontuarios) == 1):
        numero = list(lista_prontuarios.keys())[0]
        remove_prontuario_por_numero(dic_prontuarios,numero)
    else:
        listar_prontuarios(lista_prontuarios)
        opcao = int(input("Digite o número do prontuário a ser removido: "))
        remove_prontuario_por_numero(dic_prontuarios,opcao)

#LISTAR PRONTUÁRIOS
def listar_prontuarios(dic_prontuarios):
    # verifica se o prontuário existe ou não
    if (len(dic_prontuarios) < 1):
        print("Nenhum prontuário encontrado!")
    else:
        print(f"N. do prontuário -   Paciente")
        for num_prontuario in dic_prontuarios:
            nome = dic_prontuarios[num_prontuario]['Nome']
            print(f" \t\t{num_prontuario}\t\t - \t {nome}")
            #busca_prontuario_por_numero(dic_prontuarios, num_prontuario)

#IMRPIME MENU
def imprime_menu():
    menu = """
    ####### MENU #######
    1 - Cadastrar
    2 - Buscar
    3 - Remover 
    4 - Atualizar
    5 - Listar
    0 - Sair
    ####################
    """
    print(menu)

#SALVA ARQUIVO
def salva_arquivo(dic_prontuarios, ultimo_paciente, arquivo):

    arquivo.write(str(ultimo_paciente)+"\n")
    for num_pront, dic_pront in dic_prontuarios.items():
        arquivo.write(f"{num_pront}-")
        nome, sexo, mae, pai, peso, imc, altura, pc = dic_pront.values()
        arquivo.write(f"Nome:{nome},")
        arquivo.write(f"Sexo:{sexo},")
        arquivo.write(f"Mãe:{mae},")
        arquivo.write(f"Pai:{pai},")
        arquivo.write(f"Peso:{peso},")
        arquivo.write(f"IMC:{imc},")
        arquivo.write(f"Altura:{altura},")
        arquivo.write(f"Perimétro Cefálico:{pc}\n")

        arquivo.flush()

#LER AQUIVO
def ler_arquivo(dic_prontuarios, nome_arquivo):
    arquivo = open(nome_arquivo,"r")
    linhas = arquivo.readlines()

    # a primeira linha do arquivo contem o número do ultimo prontuário criado
    num_ult_prontuario = int(linhas[0].strip())    # remove o \n e converte em inteiro
    linhas.remove(linhas[0])

    for linha in linhas:
        numero, dados = linha.split("-")  # separa a chave do primeiro dicionário (número do prontuário)
        num_prontuario = int(numero)

        prontuario = {}
        for item in dados.split(","):   # separa os itens do segundo dicionário
            chave, dado = item.split(":")   # separa a chave do dado
            prontuario[chave] = dado

        prontuario["Perimétro Cefálico"] = dado.strip()
        dic_prontuarios[num_prontuario] = prontuario

    arquivo.close()
    return num_ult_prontuario

prontuarios = {}
ultimo_paciente = 0
opcao = ""
nome_do_arquivo = "prontuarios.txt"
lista_dados = ["Nome", "Sexo", "Mãe", "Pai", "Peso", "IMC", "Altura", "Perimétro Cefálico"]

while (opcao != "0"):

    imprime_menu()
    opcao = input("Digite uma das opções: ")

    if (opcao == "1"):
        ultimo_paciente = ler_arquivo(prontuarios,nome_do_arquivo)    # recebe o valor do arquivo
        #print(f"prontuarios antes: {prontuarios}")

        print("\nCadastrar novo paciente:")
        ultimo_paciente = criar_protuario(prontuarios,ultimo_paciente,lista_dados)  # atualiza o valor
        #print(f"prontuarios depois: {prontuarios}")

        arquivo = open(nome_do_arquivo, "w")
        salva_arquivo(prontuarios,ultimo_paciente,arquivo)
        arquivo.close()

    elif (opcao == "2"):
        ultimo_paciente = ler_arquivo(prontuarios,nome_do_arquivo)    # recebe o valor do arquivo

        listar_prontuarios(prontuarios)
        print("\nBuscar paciente:")
        numero = int(input("Digite o número do paciente: "))
        busca_prontuario_por_numero(prontuarios,numero)

    elif (opcao == "3"):
        ultimo_paciente = ler_arquivo(prontuarios,nome_do_arquivo)    # recebe o valor do arquivo

        print("\nRemover paciente:")
        nome = input("Digite o nome do paciente: ")
        remove_prontuario(prontuarios, nome)

        arquivo = open(nome_do_arquivo, "w")
        salva_arquivo(prontuarios,ultimo_paciente,arquivo)
        arquivo.close()

    elif (opcao == "4"):
        ultimo_paciente = ler_arquivo(prontuarios,nome_do_arquivo)    # recebe o valor do arquivo

        listar_prontuarios(prontuarios)
        print("\nAtualizar paciente:")
        numero = int(input("Digite o número do paciente: "))
        atualizar_prontuario_por_numero(prontuarios, numero)

        arquivo = open(nome_do_arquivo, "w")
        salva_arquivo(prontuarios,ultimo_paciente,arquivo)
        arquivo.close()

    elif (opcao == "5"):
        ultimo_paciente = ler_arquivo(prontuarios,nome_do_arquivo)    # recebe o valor do arquivo

        print("\nListando prontuários:")
        listar_prontuarios(prontuarios)

    elif (opcao != "0"):
        print("Opção invalida!")
