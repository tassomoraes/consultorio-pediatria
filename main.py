#CRIA PRONTUÁRIO
def criar_protuario(dic_protuarios, ultimo_num_paciente):
    prontuario = {}
    lista_chaves = ["Nome", "Sexo", "Mãe", "Pai", "Peso", "IMC", "Altura", "Perimétro Cefálico"]
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
        prontuario[chave] = input(dado_input+": ")

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

#REMOVER PRONTUARIO
def remove_prontuario_por_numero(dic_prontuarios, numero):

    #verifica se o prontuário existe ou não
    if (len(dic_prontuarios) < 1) or (numero not in dic_prontuarios.keys()):
        print("Nenhum prontuário encontrado!")
    else:
        dic_prontuarios.pop(numero)
        print("Paciente removido!")

#LISTAR PRONTUÁRIOS
def listar_prontuarios(dic_prontuarios):
    for num_prontuario in prontuarios:
        print(f"---PRONTUÁRIO N: {num_prontuario}---")
        busca_prontuario_por_numero(dic_prontuarios, num_prontuario)

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

prontuarios = {}
ultimo_paciente = 0
opcao = ""

while (opcao != "0"):

    imprime_menu()
    opcao = input("Digite uma das opções: ")

    if (opcao == "1"):
        print("\nCadastrar novo paciente:")
        ultimo_paciente = criar_protuario(prontuarios,ultimo_paciente)

    elif (opcao == "2"):
        print("\nAtualizar paciente:")
        numero = int(input("Digite o número do paciente: "))
        atualizar_prontuario_por_numero(prontuarios,numero)

    elif (opcao == "3"):
        print("\nRemover paciente:")
        numero = int(input("Digite o número do paciente: "))
        remove_prontuario_por_numero(prontuarios, numero)

    elif (opcao == "4"):
        print("\nAtualizar paciente:")
        numero = int(input("Digite o número do paciente: "))
        atualizar_prontuario_por_numero(prontuarios, numero)

    elif (opcao == "5"):
        print("\nListando prontuários:")
        listar_prontuarios(prontuarios)

    elif (opcao != "0"):
        print("Opção invalida!")

