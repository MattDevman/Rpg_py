from time import sleep
from personagem import *
from cores import *
import os
from dados import *
from batalha import *
########################################################################################################
def limpar():
    os.system('clear')

def rollDice():
        print(f'                                     {AMARELO}Jogando dados....{RESET}')
        sleep(3)
        JogarDados.jogar_dados(Dados)
########################################################################################################

limpar()
print(f'''
===============================================================
                    Menu de Testes
===============================================================

{AZUL}1- Criar novo personagem{RESET}
{AZUL}2- Personagens salvos{RESET}
{AZUL}3- Exit{RESET}

''')

menu_escolha = int(input('-> '))

if menu_escolha == 1:
    Personagem.setNick(Avatar)
    limpar()
    print('''
===============================================================
                Personagem Principal
===============================================================    
''')

    Personagem.getInfos(Avatar), print('\n')
    print(MAGENTA+'EQUIPAMENTOS ATUAIS\n'+RESET)
    Personagem.getInfoEquips(Avatar)
    print('\nProsseguir? (sim/nao) ')
    newHistory = str(input('-> ')).lower()
    if newHistory == 'sim':
        limpar()
        print(f'''
                  ============================== O COMEÇO =========================== \n       
Tudo se passa nos anos de 1830, onde um aventureiro chamado {Avatar.nick} ficou perdido depois de um forte temporal...
ele acorda em um lugar desconhecido onde o céu era totalmente escuro e a unica luz que conseguia enchergar era apenas
da lua avermelhada de sangue!

Sem saber onde estava se deparou com uma mochila com alguns itens, tudo parecia ser apenas um jogo, um pesadelo...
contudo, após inumeras tentativas de acordar percebeu que aquilo era real, sua vida seria apenas uma busca insaciavel.

    Após se deparar com uma caverna, {Avatar.nick} percebe que uma tempestade se aproxima cada vez mais,
correndo para dentro da caverna!

- Logo percebe que não enchergava nada, uma voz susurrou em seu ouvido...

                {AMARELO}"Bem vindo a minha masmorra, MUHAHAHAHA, está com sorte {Avatar.nick}?"{RESET}
                        
    Irei explicar a unica regras: - Tudo será decidido com um jogo de dados.

Vamos começar...

{BRANCO}Uma tocha em sua frente se acende clareando um pouco sua visão.
Um dado é lançado: Se o dado cair maior que 3 você conseguirá executar a ação, caso contrario nada será feito!{RESET}
        ''')
        input('Pressione enter para Começar ')
        rollDice()
        if Dados.info_dado >= 3:
            print(f'''- {VERDE}{Avatar.nick} pegou com sucesso a tocha e conseguiu iluminar um caminho a sua frente.{RESET}
    
    Vendo mais adiante {Avatar.nick} viu algo se mechendo na escuridão, logo percebeu que era uma criatura...
tendo em vista apenas uma mochila sem nenhuma arma, restou para o heroi apenas possibilidades..
FICAR, LUTAR E {VERMELHO}MORRER{RESET} OU FUGIR COMO UM COVARDE!            
            ''')
            input('Pressione enter para Começar ')
        elif Dados.info_dado < 3:
            print(f'''{VERMELHO}- {Avatar.nick} não pegou obteve sucesso pegar a tocha!{RESET}
    Ouvindo alguns barulhos {Avatar.nick} sentiu algo se mechendo na escuridão, logo percebeu que era uma criatura...
tendo em vista apenas uma mochila sem nenhuma arma, restou para o heroi apenas possibilidades..
FICAR, LUTAR E {VERMELHO}MORRER{RESET} OU FUGIR COMO UM COVARDE!        
            ''')
            input('Pressione enter para Começar ')
        
        p_escolha1 = input(''' 
                    FICAR ou FUGIR?\n
->  ''').lower()
        limpar()
        if p_escolha1 == 'ficar':
            Mecanica.Luta_start(Batalha)
            print(f'''
{Infos.mob_spawn(Batalha)} 

1 - Lutar                       2 - Magia
3 - Item                        4 - Fugir
            
            ''')


elif menu_escolha == 2:
    Personagem.getInfos(Avatar)
elif menu_escolha == 3:
    print('Saindo...')
    sleep(1)
    exit()
