"""Instituição: Faculdade SENAI
Unidade Curricular: Algoritmos e Programação
Professor: Paulo Roberto Pasqualotti
Alunos: Giovanni de Aguirre Tamanini
Leonardo de Freitas Mafra
Data: 11/12/2022"""

# Importando módulos
import random

# Definindo variáveis
passageiros_onibus = 0
onibus_lotado = 40
total = 0

# Laço de repetição para cada parada
for parada_onibus in range(1, 21) :

    # Sorteando número de passageiros para embarque e desembarque
    desembarque = random.randint(0, 10)
    embarque = random.randint(0, 10)

    print(f'Parada {parada_onibus}')

    # Condição para a primeira parada (somente embarque)
    if parada_onibus == 1 :
        passageiros_onibus += embarque
        print(f'Embarcaram {embarque} passageiros')

    # Condição para as paradas 2 até 19
    elif parada_onibus >= 2 and parada_onibus < 20 :

        # Condições para desembarque
        if desembarque > passageiros_onibus :
            print(f'Desembarcaram {passageiros_onibus} passageiros')
            passageiros_onibus = 0
        else :
            passageiros_onibus -= desembarque
            print(f'Desembarcaram {desembarque} passageiros')

        # Condições para embarque
        if (embarque + passageiros_onibus) >= onibus_lotado :
            embarque = onibus_lotado - passageiros_onibus
            passageiros_onibus = onibus_lotado
            print(f'Embarcaram {embarque} passageiros')
        else :
            passageiros_onibus += embarque
            print(f'Embarcaram {embarque} passageiros')

    # Condição para a última parada (somente desembarque)
    else :
        desembarque = passageiros_onibus
        print(f'Desembarcaram todos os {desembarque} passageiros')
        print(f'Total de {total} passageiros na linha.')
        break

    print(f'Continuam {passageiros_onibus} passageiros no ônibus\n')
    total += embarque