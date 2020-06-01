op=[1,2,3]
from time import sleep

def linha(a='=',b=40):
    print(a*b)


def cab(a):
    linha()
    print(f'\033[1;35m{a}\033[m'.center(47))
    linha()


def cri(nome):
    try:
        a= open(nome,'wt+')
        a.close()
    except:
        print('\033[1;31mERRO! Não foi possivél criar um arquivo!\033[m')
    else:
        print('\033[1;32mArquivo criado com SUCESSO!\033[m')


def ex(nome):
    try:
        a= open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cada(ar,sen,id = 0):
    try:
        a= open(ar,'at')
    except:
        print('Houve um problema para abrir o arquivo!')
    else:
        a.write(f'{sen}')
        a.close()


def lar(arq):
        while True:
            cab('MENU DO USUARIO')
            print('\033[1;33m1>\033[m \033[1;34mVER SENHAS\033[m')
            print('\033[1;33m2>\033[m \033[1;34mCADASTRAR SENHA\033[m')
            print('\033[1;33m3>\033[m \033[1;34mSAIR\033[m')
            opi=int(input('\033[1;33mOPÇÃO: \033[m'))
            if opi not in op:
                print('\033[1;31mOPÇÃO INVALIDA\033[m')
            else:
                if opi == 1:
                    try:
                        c = open(arq, 'rt')
                    except:
                        print('Erro ao ler o arquivo! ')
                    else:
                        print('\033[33;1m> \033[m\033[1;34mSENHAS:\033[m')
                        linha('-')
                        print(c.read())
                        c.close()

                if opi == 2:
                    cab('NOVA SENHA')
                    ser=str(input('\033[1;33m>\033[m \033[1;34mSERVIÇO: \033[m'))
                    usa=str(input('\033[1;33m>\033[m \033[1;34mNOME DE USUARIO: \033[m'))
                    pah=str(input('\033[1;33m>\033[m \033[1;34mSENHA: \033[m'))
                    try:
                        c= open(arq, 'at')
                    except:
                        print('Erro ao ler o arquivo! ')
                    else:
                        c.write(f'\n\033[32;1mSERVICO: {ser}, NOME DE USUARIO: {usa}, SENHA: {pah} \033[m')
                        c.close()
                        print('\033[1;33m>\033[m \033[32;1mDADOS SALVOS COM SUCESSO!\033[m')
                if opi == 3:
                    print(('\033[1;31mSAINDO\033[m'),end='')
                    for t in range(0,3):
                        print(('.'),end='')
                        sleep(0.6)
                    print('')
                    break
