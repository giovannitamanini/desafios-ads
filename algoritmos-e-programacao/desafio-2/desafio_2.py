""" Sendo AB o dia do mês (A sendo a dezena do dia e B sendo a unidade do dia), e CD o mês (C, dezena do mês e D, unidade do mês). 
    Qual o mês de nascimento de uma pessoa, sabendo que: A+B+C+D = 20"""

SOMA_FINAL = 20     # Constante que representa o valor da soma A+B+C+D

# Representação do dia
dezenas_do_dia = [0, 1, 2, 3]   # Lista com valores possíveis para a dezena dos dias
unidades_do_dia = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    # Lista com valores possíveis para a unidade dos dias

# Representação do mês
dezenas_do_mes = [0, 1]     # Lista com valores possíveis para a dezena dos meses
unidades_do_mes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    # Lista com valores possíveis para a unidade dos meses

# Somas dos dias (dezena_do_dia + unidade_do_dia)
lista_de_somas_dos_dias = [] 

for dezena in dezenas_do_dia :

    for unidade in unidades_do_dia:

        if dezena == 3 and unidade > 1 :
            break

        if dezena != 0 or unidade != 0 :
            soma_do_dia = dezenas_do_dia[dezena]+unidades_do_dia[unidade]
            lista_de_somas_dos_dias.append(soma_do_dia)

#print(lista_de_somas_dos_dias)

# Somas dos meses (dezena_do_mes + unidade_do_mes)
lista_de_somas_dos_meses = []

for dezena in dezenas_do_mes :

    for unidade in unidades_do_mes :

        if unidade > 2 and dezena == 1 :
            break

        if dezena != 0 or unidade != 0 :
            soma_do_mes = dezenas_do_mes[dezena] + unidades_do_mes[unidade]
            lista_de_somas_dos_meses.append(soma_do_mes)

#print(lista_de_somas_dos_meses)

# Somas dos dias e meses
contador_de_dias = 1
contador_de_meses = 1

for soma_dia in lista_de_somas_dos_dias :

    for soma_mes in lista_de_somas_dos_meses :
        soma = soma_dia + soma_mes

        if soma == SOMA_FINAL :
            print("Data possível: " + str(contador_de_dias) + "/" + str(contador_de_meses))

        contador_de_meses += 1

    contador_de_dias += 1
    contador_de_meses = 1 # Resetando o mês após laço dos dias finalizar