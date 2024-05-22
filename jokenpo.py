#importando o randint do módulo random
from random import randint
#local para armazenar as opcoes de jogadas e gerar uma jogada aleatoria e armazena-la
opcoes = ('pedra', 'papel', 'tesoura')
sorteio = randint(0,2)

print("Opções : \n"
      "[0] = PEDRA\n"
      "[1] = PAPEL\n"
      "[2] = TESOURA")
#solicitar jogada do usuario e armazena-la
jogadaPlayer = int(input("Qual a sua jogada ? "))

print('-'*30)
print('Computador joga => {}'.format(opcoes[sorteio]))
print('Player joga => {}'.format(opcoes[jogadaPlayer]))
print('-'*30)
#verificações de casos
if sorteio == 0:
    if jogadaPlayer == 0:
        print('Empate. Os dois jogaram pedra.')
    elif jogadaPlayer == 1:
        print('Vitória do Player : papel vence pedra.')
    elif jogadaPlayer == 2:
        print('Vitória do Computador : pedra vence tesoura')
    else:
        print('Jogada inválida.')

if sorteio == 1:
    if jogadaPlayer == 0:
        print('Vitória do computador : papel vence pedra')
    elif jogadaPlayer == 1:
        print('Empate. os dois jogaram papel')
    elif jogadaPlayer == 2:
        print('Vitória do player : tesoura vence papel')
    else:
        print('Jogada inválida.')

if sorteio == 2:
    if jogadaPlayer == 0:
        print('Vitória do player : pedra vence tesoura')
    elif jogadaPlayer == 1:
        print('Vitória do computador : tesoura vence papel.')
    elif jogadaPlayer == 2:
        print('Empate. os dois jogaram tesoura')
    else:
        print('Jogada inválida.')