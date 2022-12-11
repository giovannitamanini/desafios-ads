import copy
import time
from os import system, name

# Lugar no estado para cada personagem
PAI = 0
MAE = 1
FILHO_1 = 2
FILHO_2 = 3
FILHA_1 = 4
FILHA_2 = 5
POLICIAL = 6
PRISIONEIRA = 7
BARCO = 8

# Estado inicial
ESTADO_INICIAL = ["A", "A", "A", "A", "A", "A", "A", "A", "A"]

# Definindo função para a regra da prisioneira
def regraDaPrisioneira(estado) :
    return estado[POLICIAL] == estado[PRISIONEIRA] or (
        estado[PRISIONEIRA] != estado[PAI] 
        and estado[PRISIONEIRA] != estado[MAE] 
        and estado[PRISIONEIRA] != estado[FILHO_1] 
        and estado[PRISIONEIRA] != estado[FILHO_2] 
        and estado[PRISIONEIRA] != estado[FILHA_1] 
        and estado[PRISIONEIRA] != estado[FILHA_2]
    )

# Definindo função para a regra das filhas
def regraDaFilha(estado) :
    return (estado[FILHA_1] == estado[MAE] or estado[FILHA_1] != estado[PAI]) and (
        estado[FILHA_2] == estado[MAE] or estado[FILHA_2] != estado[PAI]
        )

# Definindo função para a regra dos filhos
def regraDoFilho(estado) :
    return (estado[FILHO_1] == estado[PAI] or estado[FILHO_1] != estado[MAE]) and (
        estado[FILHO_2] == estado[PAI] or estado[FILHO_2] != estado[MAE]
        )

# Definindo função para checar se o estado dado é válido
def ePermitido(estado) :
    return regraDaPrisioneira(estado) and regraDaFilha(estado) and regraDoFilho(estado)

# Definindo função para checar se o objetivo de passar todoas as pessoas foi concluído
def estaConcluido(estado) :
    return estado == ["B", "B", "B", "B", "B", "B", "B", "B", "B"]

# Gerando todos os movimentos possíveis
def gerandoMovimentos(estado) :
    for outro in [PAI, MAE, FILHO_1, FILHO_2, FILHA_1, FILHA_2, POLICIAL, PRISIONEIRA] :
        if estado[PAI] == estado[outro] == estado[BARCO] :
            mova = copy.deepcopy(estado)
            mova[PAI] = "A" if estado[PAI] == "B" else "B"
            mova[outro] = "A" if estado[outro] == "B" else "B"
            mova[BARCO] = "A" if estado[BARCO] == "B" else "B"
            yield mova

        if estado[MAE] == estado[outro] == estado[BARCO] :
            mova = copy.deepcopy(estado)
            mova[MAE] = "A" if estado[MAE] == "B" else "B"
            mova[outro] = "A" if estado[outro] == "B" else "B"
            mova[BARCO] = "A" if estado[BARCO] == "B" else "B"
            yield mova

        if estado[POLICIAL] == estado[outro] == estado[BARCO] :
            mova = copy.deepcopy(estado)
            mova[POLICIAL] = "A" if estado[POLICIAL] == "B" else "B"
            mova[outro] = "A" if estado[outro] == "B" else "B"
            mova[BARCO] = "A" if estado[BARCO] == "B" else "B"
            yield mova

# Definindo função para filtrar somente os movimentos válidos
def movimentosValidos(lista_de_estados) :
    listaValida = []
    for estado in lista_de_estados :
        if ePermitido(estado) and estado not in listaValida :
            listaValida.append(estado)
    return listaValida

# Difinindo função onde fazemos uma pesquisa limitada em profundidade, usando uma lista de estados_anteriores para rastrear onde estivemos. Esta função retorna apenas uma resposta vencedora.
def pesquisaLimitadaProfunda(estado, estados_anteriores, maxProfundidade) :
    estados_anteriores.append(estado)

    if estaConcluido(estado) :
        return estados_anteriores

    if maxProfundidade <= 0 :
        return None

    for movimento in movimentosValidos(gerandoMovimentos(estado)) :
        if movimento not in estados_anteriores :
            resultado = pesquisaLimitadaProfunda(movimento, estados_anteriores, maxProfundidade - 1)
            if resultado is not None :
                return resultado
            estados_anteriores.pop()
    
    return None

# Definindo função que imprime um estado no terminal
def mostra(estado) :
    NOMES_DOS_PERSONAGENS = [
        "PAI",
        "MAE",
        "FILHO_1",
        "FILHO_2",
        "FILHA_1",
        "FILHA_2",
        "POLICIAL",
        "PRISIONEIRA",
    ]
    espaco = " " * 10
    textoPlano = "|| {} |                | {} ||"

    print("=" * 46)
    print(textoPlano.format(espaco, espaco))

    for i in range(0, 8) :
        nomeDoPersonagem = NOMES_DOS_PERSONAGENS[i] + " " * (10 - len(NOMES_DOS_PERSONAGENS[i]))

        if estado[i] == "A" :
            print(textoPlano.format(nomeDoPersonagem, espaco))
        else :
            print(textoPlano.format(espaco, nomeDoPersonagem))

        if i == 3 :
            if estado[8] == "B" :
                print("||", espaco, "|           \\___/|", espaco, "||")
            else :
                print("||", espaco, "|\\___/           |", espaco, "||")
            
    print(textoPlano.format(espaco, espaco))
    print("=" * 46)

# Função que mostra caminho no terminal com a ajuda da função mostra()
def mostraCaminho(lista_de_estados, atraso) :
    for estado in lista_de_estados :
        mostra(estado)
        time.sleep(atraso)
        limpa()

# Função que limpa o terminal
def limpa() :

    # Para Windows
    if name == "nt" :
        _ = system("cls")

    # Para Mac e Linux(os.name é 'posix')
    else :
        _ = system("clear")

# Função main
def main() :
    lista_de_estados = pesquisaLimitadaProfunda(
        ["A", "A", "A", "A", "A", "A", "A", "A", "A"], [], 30
    )

    inputDoUsuario = input(
        "Por favor, digite o número do estado que você quer ver (0 à 17) ou digite 'caminho' para mostrar o caminho ou digite 'sair' para sair: "
    )

    while inputDoUsuario != "sair" :
        try :

            if inputDoUsuario == "caminho" :
                limpa()
                mostraCaminho(lista_de_estados, 1.5)

            else :
                mostra(lista_de_estados[int(inputDoUsuario)])

            inputDoUsuario = input(
                "Por favor, digite o número do estado que você quer ver (0 à 17) ou digite 'caminho' para mostrar o caminho ou digite 'sair' para sair: "
            )
        except :
            print("Por favor entre um valor válido.")
            inputDoUsuario = input(
                "Por favor, digite o número do estado que você quer ver (0 à 17) ou digite 'caminho' para mostrar o caminho ou digite 'sair' para sair: "
            )
            continue

main()