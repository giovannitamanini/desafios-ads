#include <iostream>
#include <cmath>
#include "cripto.h"
using namespace std;

int main()
{
    cout << "Mensagem a ser enviada: ESTUDAR PARA TRANSFORMAR O MUNDO!\n" << endl;

    /* Abaixo é possível modificar a mensagem, desde que seja respeitado o limite de caracteres (34) e que
    seja uma matriz 2x17. A relação caracteres/inteiros está definido no header file Criptografia.h */

    int mensagem[2][17] = { {E, S, T, U, D, A, R, espaco, P, A, R, A, espaco, T, R, A, N},
                            {S, F, O, R, M, A, R, espaco, O, espaco, M, U, N, D, O, exclamacao, espaco} };

    codifica(cod, mensagem);

    cout << "Enviar matriz criptografada para o receptor." << endl;

    return 0;
}