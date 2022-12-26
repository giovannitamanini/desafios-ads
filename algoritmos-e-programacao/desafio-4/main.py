"""Instituição: Faculdade SENAI
   Unidade Curricular: Algoritmos e Programação
   Professor: Paulo Roberto Pasqualotti
   Alunos: Giovanni de Aguirre Tamanini
           Leonardo de Freitas Mafra
   Data: 11/12/2022"""

# Importando módulos
import onibus as bus

# Definição das varíaveis
passageiros = 0
total_de_passageiros = 0
lotacao_maxima_onibus = 40
inf_passageiros = [0, 0]

# Algoritmo com a chamada de funções
for parada in range(1, 21) :
  
      print("Parada Número",parada)
      passageiros = bus.desembarcaPassageiros(parada, inf_passageiros[0])
      inf_passageiros = bus.embarcaPassageiros(parada, passageiros)
      if parada < 20 :
          print("Quantidade atual de passageiros:", inf_passageiros[0],"\n")
      if parada == 20 :
          print("Total de passageiros na viagem:",total_de_passageiros,"\n")
          break
      total_de_passageiros += inf_passageiros[1]
