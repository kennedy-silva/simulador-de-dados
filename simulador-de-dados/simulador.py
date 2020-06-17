from random import randint

print('-' * 30)
print('SEJA BEM VINDO AO SIMULADOR DE DADOS')
print('-' * 30)

print('Você quer jogar o dado?')
escolha = input('Digite [SIM] para rodar e [NÃO] para não rodar: ').strip().lower()
print('-' * 30)

while True:
    if escolha == 'sim':
        numero_escolhido = randint(1, 6)
        print('Número aleatório:',numero_escolhido)
        print('-' * 30)

        while True:
            print('Você quer jogar o dado novamente?')
            escolha = input('Digite [SIM] para rodar e [NÃO] para não rodar: ').strip().lower()
            print('-' * 30)
            if escolha == 'sim':
                numero_escolhido = randint(1, 6)
                print('Número aleatório:',numero_escolhido)
                print('-' * 30)
            else:
                print('o dado não será rodado')
                print('-' * 30)
                break
    else:
        print('o dado não será rodado')
        print('-' * 30)
    break
