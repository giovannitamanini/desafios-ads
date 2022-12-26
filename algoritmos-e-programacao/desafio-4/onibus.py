"""Instituição: Faculdade SENAI
   Unidade Curricular: Algoritmos e Programação
   Professor: Paulo Roberto Pasqualotti
   Alunos: Giovanni de Aguirre Tamanini
           Leonardo de Freitas Mafra
   Data: 11/12/2022"""

import random

lotacao_maxima_onibus = 40

def desembarcaPassageiros(parada, passageiros) :
    
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
            print("Não desembarcaram passageiros!")
        else :
            print("Desembarcaram",passageiros_que_saem,"passageiros")
            passageiros -= passageiros_que_saem

    return passageiros

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
 
        return [passageiros, passageiros_que_entram] 
