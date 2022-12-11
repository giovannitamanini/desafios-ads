'''Alunos: Giovanni de Aguirre Tamanini
           Leonardo de Freitas Mafra
Disciplina: Algoritmos e Programação
Professor: Paulo Roberto Pasqualotti
UNISENAI'''
#-------------------------------------------------------------------------------------------------------------------
#Criação de listas e variáveis para testar as condicionais
margemA = ['pai', 'mae', 'filho1', 'filho2', 'filha1', 'filha2', 'guarda', 'prisioneira']
margemB = []
jangada = []
qtPA = len(margemA)
qtPB = len(margemB)
qtPJ = len(jangada)
#-------------------------------------------------------------------------------------------------------------------
# Condicional para avaliar situação na jangada. Está pronta!!!
if (qtPJ == 1 or qtPJ == 2) and (
    'pai' in jangada or 'mae' in jangada or 'guarda' in jangada) and not (
        'prisioneira' in jangada and 'guarda' not in jangada) and not (
            'mae' in jangada and ('filho1' in jangada or 'filho2' in jangada)) and not (
                'pai' in jangada and ('filha1' in jangada or 'filha2' in jangada)):
    print('Jangada OK')
else:
    print('Problema na jangada')
#-------------------------------------------------------------------------------------------------------------------
# Condicional para avaliar situação da margem A (quanto aos personagens na margem A)
if(qtPA <= 8) and (
    (qtPA == 0 or 'pai' in margemA or 'mae' in margemA or 
    'filho1' in margemA or 'filho2' in margemA or 
    'filha1' in margemA or 'filha2' in margemA or 
    'guarda' in margemA or 'prisioneira' in margemA) and not 
        ('prisioneira' in margemA and 'guarda' not in margemA and qtPA > 1) and not 
            (('mae' in margemA and 'pai' not in margemA) and ('filho1' in margemA or 'filho2' in margemA)) and not 
                (('pai' in margemA and 'mae' not in margemA) and ('filha1' in margemA or 'filha2' in margemA))) :
    print('Margem A OK')
else:
    print('Problema na Margem A')
#-------------------------------------------------------------------------------------------------------------------
# Condicional para avaliar situação da margem B (quanto aos personagens na margem B)
if(qtPB >= 0 and qtPB <= 8) and (
    (qtPB == 0 or 'pai' in margemB or 'mae' in margemB or 
    'filho1' in margemB or 'filho2' in margemB or 
    'filha1' in margemB or 'filha2' in margemB or 
    'guarda' in margemB or 'prisioneira' in margemB) and not 
        ('prisioneira' in margemB and 'guarda' not in margemB and qtPB > 1) and not 
            (('mae' in margemB and 'pai' not in margemB) and ('filho1' in margemB or 'filho2' in margemB)) and not 
                (('pai' in margemB and 'mae' not in margemB) and ('filha1' in margemB or 'filha2' in margemB))) :
    print('Margem B OK')
else:
    print('Problema na Margem B')
#-------------------------------------------------------------------------------------------------------------------
# Condicional para avaliar situação ao chegar na margem B (quanto ao fim do jogo)
if('pai' in margemB and 'mae' in margemB and 
'filho1' in margemB and 'filho2' in margemB and 'filha1' in margemB and 'filha2' in margemB and 
'guarda' in margemB and 'prisioneira' in margemB) :
    print("Fim de jogo")
#-------------------------------------------------------------------------------------------------------------------