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


