import matplotlib.pyplot as plt
import numpy as np

# mostra o gráfico da curva de crescimento comparando com
# as curvas fornecidas pela OMS
def curva_de_crescimento_peso(dados_y, nome_paciente):
    #pegando apenas o primeiro nome
    nome_paciente = nome_paciente.split()[0]

    # a quantidade de meses passadas referente ao peso atual
    x_curva =           [0  ,2  ,4  ,12  ,24  ,36  ,60  ]

    # referência de acordo com os meses de vida
    y_curva = np.array([[2  ,4  ,5  ,7   ,8.7 ,10  ,12.4],
                        [2.5,4.4,5.5,7.8 ,9.8 ,11.3,14  ],
                        [3.5,5.6,7  ,9.7 ,12.2,14.4,18.3],
                        [4.5,7  ,8.9,12  ,15.2,18.2,24.1],
                        [5  ,8  ,10 ,13.4,17.1,20.9,27.9]])

    plt.plot(x_curva, y_curva[4], color='black',label="acima")
    plt.plot(x_curva, y_curva[3], color='red',label="lim.sup")
    plt.plot(x_curva, y_curva[2], color='black',label="abaixo")
    plt.plot(x_curva, y_curva[1], color='red',label="lim.inf")
    plt.plot(x_curva, y_curva[0], color='green',label="normal")

    if(len(dados_y) < len(x_curva)):
        x_curva = x_curva[:len(dados_y)]
    plt.scatter(x_curva, dados_y, color="blue",label=nome_paciente)

    plt.legend()

    plt.title("Curva de Crescimento - Peso x Meses")
    plt.ylabel("Peso (Kg)")
    plt.xlabel("Meses")

    plt.show()

def porcentagem_meninos_meninas(dicionario):
    pass


