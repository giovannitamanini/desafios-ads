//criptografando_mensagem.cpp
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
    cout << "Mensagem a ser enviada: ESTUDAR PARA TRANSFORMAR O MUNDO!\n" << endl;

    /* Abaixo é possível modificar a mensagem, desde que seja respeitado o limite de caracteres (34) pois 
    a mensagem deve ser guardada em uma matriz 2x17. A relação caracteres/inteiros está definido no header 
    file cripto.h */
    int mensagem[2][17] = { {E, S, T, U, D, A, R, espaco, P, A, R, A, espaco, T, R, A, N},
                            {S, F, O, R, M, A, R, espaco, O, espaco, M, U, N, D, O, exclamacao, espaco} };
    mostra2x17(mensagem);
    cout << endl;

    /*Chamada da função codifica que utiliza como parâmetros de entrada a matriz COD e a matriz mensagem
    declarada acima. A implementação da função está no header file cripto.h*/
    codifica(cod, mensagem);

    cout << "Copiar matriz criptografada no console e enviar para o receptor." << endl;

    return 0;
}