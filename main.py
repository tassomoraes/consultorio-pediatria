#CRIA PRONTUÁRIO
def criar_protuario(dic_protuarios, ultimo_num_paciente):
    prontuario = {}
    num_paciente = ultimo_num_paciente + 1
    prontuario['nome_crianca'] = input("Nome da crianca: ")
    prontuario['sexo'] = input("Sexo da criança: ")
    #prontuario['telefone_respons'] = input("Telefone do responsável pela criança: ")
    prontuario['nome_mae'] = input("Nome da mãe: ")
    prontuario['nome_pai'] = input("Nome do pai: ")
    #prontuario['qtd_irmaos'] = input("Quantidade de irmãos: ")
    #prontuario['religiao'] = input("Religião: ")
    prontuario['peso'] = input("Peso atual: ")
    prontuario['IMC'] = input("IMC atual: ")
    prontuario['altura'] = input("Altura atual: ")
    prontuario['perim_cefalico'] = input("Perimetro cefálico atual: ")
    #prontuario['data_consulta'] = input("Data da consulta: ")
    #prontuario['novo_contato'] = [nome, telefone]
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
    opcao = input(menu)
    return opcao

#ATUALIZAR
def atualizar_prontuario_por_numero(dic_prontuarios, numero):

    if (len(dic_prontuarios) < 1) or (numero not in dic_prontuarios.keys()):
        print("Nenhum prontuário encontrado!")
    else:
        prontuario = dic_prontuarios[numero]
        opcao = ""
        while (opcao != "não"):
            opcao = imprime_menu_atualizar()
            if(opcao == "1"):
                prontuario['nome_crianca'] = input("\tDigite o novo nome: ")
            elif(opcao == "2"):
                prontuario['sexo'] = input("\tDigite o novo sexo: ")
            elif(opcao == "3"):
                prontuario['nome_mae'] = input("\tDigite o novo nome da mãe: ")
            elif(opcao == "4"):
                prontuario['nome_pai'] = input("\tDigite o novo nome do pai: ")
            elif(opcao == "5"):
                prontuario['peso'] = input("\tDigite o novo peso: ")
            elif(opcao == "6"):
                prontuario['IMC'] = input("\tDigite o novo IMC: ")
            elif(opcao == "7"):
                prontuario['altura'] = input("\tDigite o nova altura: ")
            elif(opcao == "8"):
                prontuario['perim_cefalico'] = input("\tDigite o novo perímetro cefálico: ")
            else:
                print("Entrada inválida!")

            opcao = input("\tDeseja alterar mais alguma informação? ")

        print("---Contao atualizado---\n")
        busca_prontuario_por_numero(dic_prontuarios,numero)

#BUSCA PRONTUÁRIO
def busca_prontuario_por_numero(dic_prontuarios, numero):

    if (len(dic_prontuarios) < 1) or (numero not in dic_prontuarios.keys()):
        print("Nenhum prontuário encontrado!")
    else:
        prontuario = dic_prontuarios[numero]

        print(f"Nome: {prontuario['nome_crianca']}\n"
              f"Sexo: {prontuario['sexo']}\n"
              #f"Telefone do Responsável: {prontuario['telefone_respons']}"
              f"Mãe: {prontuario['nome_mae']}\n"
              f"Pai: {prontuario['nome_pai']}\n"
              #f"Irmãos: {prontuario['qtd_irmaos']}"
              #f"Religião: {prontuario['religiao']}"
              f"Peso: {prontuario['peso']}\n"
              f"IMC: {prontuario['IMC']}\n"
              f"Altura: {prontuario['altura']}\n"
              f"Perimétro cefálico: {prontuario['perim_cefalico']}\n"
              )

#REMOVER PRONTUARIO
def remove_prontuario(dic_prontuarios, numero):

    if (len(dic_prontuarios) < 1) or (numero not in dic_prontuarios.keys()):
        print("Nenhum prontuário encontrado!")
    else:
        dic_prontuarios.pop(numero)


