#include <iostream>
using namespace std;

void mostra2x2(int arr_1[][2]);
void mostra2x17(int arr_2[][17]);
void codifica(int cod[][2], int mensagem[][17]);
void decodifica(int decod[][2], int codificada[][17]);

int A = 1, B = 2, C = 3, D = 4, E = 5, F = 6, G = 7, H = 8, I = 9, J = 10, K = 11, L = 12, M = 13, N = 14,
O = 15, P = 16, Q = 17, R = 18, S = 19, T = 20, U = 21, V = 22, W = 23, X = 24, Y = 25, Z = 26,
ponto = 27, virgula = 28, exclamacao = 29, interrogacao = 30, espaco = 31, nulo = 32;

int cod[2][2] = { {4, 1}, {3, 1} };
int decod[2][2] = { {1, -1}, {-3, 4} };

void mostra2x2(int arr_1[][2])
{
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            cout << arr_1[i][j] << " ";
        }
        cout << endl;
    }
}

void mostra2x17(int arr_2[][17])
{
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 17; j++) {
            cout << arr_2[i][j] << " ";
        }
        cout << endl;
    }
}

void codifica(int cod[][2], int mensagem[][17])
{
    cout << "Criptografando matriz mensagem usando COD... \n" << endl;
    cout << "Matriz criptografada:" << endl;
    int codificada[2][17] = { {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                          {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0} };

    for (int linha = 0; linha < 2; linha++) {
        for (int coluna = 0; coluna < 17; coluna++) {
            for (int interno = 0; interno < 2; interno++) {
                codificada[linha][coluna] += cod[linha][interno] * mensagem[interno][coluna];
            }
            cout << codificada[linha][coluna] << " ";
        }
        cout << "\n";
    }
    cout << endl;
}

void decodifica(int decod[][2], int codificada[][17])
{
    cout << "Descriptografando matriz usando DECOD..." << endl;
    int mensagem[2][17] = { {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
                           {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0} };
    for (int linha = 0; linha < 2; linha++) {
        for (int coluna = 0; coluna < 17; coluna++) {
            for (int interno = 0; interno < 2; interno++) {
                mensagem[linha][coluna] += decod[linha][interno] * codificada[interno][coluna];
            }
            //cout << mensagem[linha][coluna] << " ";
        }
        //cout << "\n";
    }
    cout << endl;
    cout << "Mensagem descriptografada: \n";
    for (int linha = 0; linha < 2; linha++) {
        for (int coluna = 0; coluna < 17; coluna++) {
            switch (mensagem[linha][coluna]) {
            case 1:
                cout << "A";
                break;
            case 2:
                cout << "B";
                break;
            case 3:
                cout << "C";
                break;
            case 4:
                cout << "D";
                break;
            case 5:
                cout << "E";
                break;
            case 6:
                cout << "F";
                break;
            case 7:
                cout << "G";
                break;
            case 8:
                cout << "H";
                break;
            case 9:
                cout << "I";
                break;
            case 10:
                cout << "J";
                break;
            case 11:
                cout << "K";
                break;
            case 12:
                cout << "L";
                break;
            case 13:
                cout << "M";
                break;
            case 14:
                cout << "N";
                break;
            case 15:
                cout << "O";
                break;
            case 16:
                cout << "P";
                break;
            case 17:
                cout << "Q";
                break;
            case 18:
                cout << "R";
                break;
            case 19:
                cout << "S";
                break;
            case 20:
                cout << "T";
                break;
            case 21:
                cout << "U";
                break;
            case 22:
                cout << "V";
                break;
            case 23:
                cout << "W";
                break;
            case 24:
                cout << "X";
                break;
            case 25:
                cout << "Y";
                break;
            case 26:
                cout << "Z";
                break;
            case 27:
                cout << ".";
                break;
            case 28:
                cout << ",";
                break;
            case 29:
                cout << "!";
                break;
            case 30:
                cout << "?";
                break;
            case 31:
                cout << " ";
                break;
            case 32:
                cout << "0";
                break;
            default:
                cout << "Erro";
            }
        }
    }
    cout << endl;
}