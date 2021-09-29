
def criar_protuario(dic_protuarios, ultimo_num_paciente):
    prontuario = {}
    num_paciente = ultimo_num_paciente + 1
    prontuario['nome_crianca'] = input("Nome da crianca: ")
    prontuario['sexo'] = input("Sexo da criança: ")
    prontuario['telefone_respons'] = input("Telefone do responsável pela criança: ")
    prontuario['nome_mae'] = input("Nome da mãe: ")
    prontuario['nome_pai'] = input("Nome do pai: ")
    prontuario['qtd_irmaos'] = input("Quantidade de irmãos: ")
    prontuario['religiao'] = input("Religião: ")
    prontuario['peso'] = input("Peso atual: ")
    prontuario['IMC'] = input("IMC atual: ")
    prontuario['altura'] = input("Altura atual: ")
    prontuario['perim_cefalico'] = input("Perimetro cefálico atual: ")
    #prontuario['data_consulta'] = input("Data da consulta: ")
    #prontuario['novo_contato'] = [nome, telefone]
    dic_protuarios[num_paciente] = prontuario
    print(num_paciente)
    return num_paciente

prontuarios = {}
ultimo_paciente = 0
criar = "sim"
while criar == "sim":
    criar = input("Deseja criar um novo prontuário? ")
    ultimo_paciente = criar_protuario(prontuarios, ultimo_paciente)
    print(ultimo_paciente)

    print(prontuarios)

