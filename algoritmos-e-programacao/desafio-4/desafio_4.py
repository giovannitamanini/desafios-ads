"""Instituição: Faculdade SENAI
   Unidade Curricular: Algoritmos e Programação
   Professor: Paulo Roberto Pasqualotti
   Aluno: Giovanni de Aguirre Tamanini
          Leonardo de Freitas Mafra
   Data: 11/12/2022"""

import random

paradas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
passageiros = 0
passageiros_que_entram = 0
passageiros_que_saem = 0
total_de_passageiros = 0

lotacao_maxima_onibus = 40

for parada in paradas :

    print("Parada Número",parada)

    if parada > 1 :

        if parada == 20 :
            passageiros_que_saem = passageiros
            print("Desembarcaram todos os",passageiros_que_saem,"passageiros restantes.")
            print("O total de passageiros na viagem foi de",total_de_passageiros,"\n")
            break

        passageiros_que_saem = random.randint(0,10)

        if passageiros_que_saem > passageiros :
            passageiros_que_saem = passageiros
            print("Desembarcaram",passageiros_que_saem,"passageiros")
            passageiros = 0
        elif passageiros_que_saem == 0 :
            print("Não desenbarcaram passageiros!")
        else :
            print("Desembarcaram",passageiros_que_saem,"passageiros")
            passageiros -= passageiros_que_saem

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

    print("Quantidade atual de passageiros:",passageiros,"\n")
    total_de_passageiros += passageiros_que_entram