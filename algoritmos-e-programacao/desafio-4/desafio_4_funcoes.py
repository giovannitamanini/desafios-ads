"""Instituição: Faculdade SENAI
   Unidade Curricular: Algoritmos e Programação
   Professor: Paulo Roberto Pasqualotti
   Aluno: Giovanni de Aguirre Tamanini
   Data: 11/12/2022"""

# Importação dos módulos necessários
import random
    
# Definição das varíaveis
paradas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
inf_passageiros = [0, 0]
passageiros = 0
passageiros_que_entram = 0
passageiros_que_saem = 0
total_de_passageiros = 0
lotacao_maxima_onibus = 40

# Definição da função para o embarque dos passageiros
def embarcaPassageiros(parada, passageiros) :

    if parada < 20 :
        passageiros_que_entram = random.randint(0, 10)

        if (passageiros + passageiros_que_entram) < lotacao_maxima_onibus :
            print("Embarcaram",passageiros_que_entram,"passageiros.")
            passageiros += passageiros_que_entram
        elif passageiros == lotacao_maxima_onibus :
            passageiros_que_entram = 0
            print("Não foi possível embarcar passageiros. Ônibus lotado!")
        else :
            passageiros_que_entram = lotacao_maxima_onibus - passageiros
            print("Embarcaram",passageiros_que_entram,"passageiros.")
            passageiros = lotacao_maxima_onibus

        inf_passageiros = [passageiros, passageiros_que_entram]

        return inf_passageiros

# Definição da função para o desembarque dos passageiros
def desembarcaPassageiros(parada, passageiros) :

    if parada == 1 :
        print("Início da linha de ônibus.")
    
    if parada > 1 :

        passageiros_que_saem = random.randint(0,10)

        if parada == 20 :
            passageiros_que_saem = passageiros
            print("Desembarcaram todos os",passageiros_que_saem,"passageiros restantes.")
        elif passageiros_que_saem > passageiros :
            passageiros_que_saem = passageiros
            print("Desembarcaram todos os passageiros!")
            passageiros = 0
        elif passageiros_que_saem == 0 :
            print("Não desenbarcaram passageiros!")
        else :
            print("Desembarcaram",passageiros_que_saem,"passageiros")
            passageiros -= passageiros_que_saem

    return passageiros

# Laço de repetição para todas as paradas de ônibus
for parada in paradas :

    print("Parada Número",parada)
    passageiros = desembarcaPassageiros(parada, inf_passageiros[0])
    inf_passageiros = embarcaPassageiros(parada, passageiros)
    if parada < 20 :
        print("Quantidade atual de passageiros:", inf_passageiros[0],"\n")
    if parada == 20 :
        print("Total de passageiros na viagem:",total_de_passageiros,"\n")
        break
    total_de_passageiros += inf_passageiros[1]