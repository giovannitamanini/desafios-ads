//descriptografando_mensagem.cpp
//11 de outubro de 2022
//Autor: Giovanni de Aguirre Tamanini
/*Projeto feito para realização do Desafio 1 proposto na disciplina Matemática e Estatística do curso
Análise e Desenvolvimento de Sistemas do SENAI-SC*/
//Professor: Rafael Bomaro Ferreira

#include <iostream>
#include "cripto.h" //Incluindo cripto.h
using namespace std;

int main()
{
    cout << "Matriz com mensagem criptografada recebida: " << endl;

    /*Abaixo adiciona-se a matriz codificada 2x17 com 34 caracteres*/
    int codificada[2][17] = { {39, 82, 95, 102, 29, 5, 90, 155, 79, 35, 85, 25, 138, 84, 87, 33, 87},
                              {34, 63, 75, 81, 25, 4, 72, 124, 63, 34, 67, 24, 107, 64, 69, 32, 73} };
    mostra2x17(codificada);
    cout << endl;

    /*Chamada da função decodifica que utiliza como parâmetros de entrada a matriz DECOD e a matriz 
    codificada declarada acima. A implementação da função está no header file cripto.h*/
    decodifica(decod, codificada);

    return 0;
}