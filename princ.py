import func
from time import sleep
op=[1,2,3]
blok=0
while True:
    func.cab('GERENCIADOR DE SENHAS')
    print('\033[1;33m1>\033[m \033[1;34mLOGIN\033[m')
    print('\033[1;33m2>\033[m \033[1;34mNOVO CADASTRO\033[m')
    print('\033[1;33m3>\033[m \033[1;34mSAIR\033[m')
    func.linha()
    opi=int(input('\033[1;33mOPÇÃO: \033[m'))
    if opi not in op:
        print('\033[1;31mOPÇÃO INVALIDA!\033[m')
    if opi == 2:
        func.cab('CADASTRO')
        cu= str(input('\033[1;33m>\033[m \033[1;34mDIGITE O NOME DE USUARIO: \033[m'))
        cs= str(input('\033[1;33m>\033[m \033[1;34mDIGTE UMA SENHA: \033[m'))
        if not func.ex(cu):
            func.cri(f'{cu}.txt')
            func.cada(f'{cu}.txt',cs,'at')
            print('\033[1;32mUSUARIO CRIADO COM SUCESSO!\033[m')
    if opi == 3:
        print('\033[1;31mSISTEMA FINALIZADO!\033[m')
        break
    if opi == 1:
        while True:
            func.cab('LOGIN')
            id= str(input('\033[1;33m> \033[m\033[1;34mDIGITE O NOME DE ÚSUARIO: \033[m'))
            pas= str(input('\033[1;33m> \033[m\033[1;34mDIGITE O A SENHA: \033[m'))
            try:
                a = open(f'{id}.txt', 'rt')
            except:
                func.linha()
                blok+=1
                print('\033[1;31mERRO: USUARIO NÃO ENCONTRADO!\033[m')
            else:
                rnh = a.readline().strip()
                if f'{rnh}' == f'{pas}':
                    func.lar(f'{id}.txt')
                    break
                else:
                    blok+=1
                    print('\033[1;31mERRO: SENHA INCORRETA\033[m')
            if blok == 3:
                print('\033[1;31mAÇÕES BLOQUEADAS POR 1min!\033[m')
                blok=0
                sleep(60)




