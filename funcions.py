

# Criar função que calcula f(x) = 4 ** 2 + 1
def calcula_f_de_x(x):
    # Calcula o resultado de x ** 2 + 1 e armazena o resultado em f_de_x
    f_de_x = x ** 2 + 1

    # Retorna o valor de f_de_x para que seja possível reutilizar em possíveis novas novas expressões
    return f_de_x


# Chamando a função calcula_f_de_x() passando um parâmetro para que
# seja possível efetuar o calculo e obter o resultado como retorno
calcula_f_de_x(6)

