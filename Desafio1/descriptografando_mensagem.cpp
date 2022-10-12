#include <iostream>
#include "cripto.h"
using namespace std;

int main()
{
    cout << "Matriz com mensagem criptografada recebida: " << endl;
    int codificada[2][17] = { {39, 82, 95, 102, 29, 5, 90, 155, 79, 35, 85, 25, 138, 84, 87, 33, 87},
                              {34, 63, 75, 81, 25, 4, 72, 124, 63, 34, 67, 24, 107, 64, 69, 32, 73} };
    mostra2x17(codificada);
    cout << endl;

    decodifica(decod, codificada);

    return 0;
}