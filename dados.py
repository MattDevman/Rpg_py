from random import randint
from cores import *


class Dados:
    
    info_dado = 0


class JogarDados(Dados):

    def jogar_dados(self):
        self.info_dado = randint(1,6)
        
        if self.info_dado >= 3:
            print(f'''
            =================================================
            =                   # Dado #                    =
            =        O Resultado do dado foi: {VERDE+str(self.info_dado)+RESET}             =
            =                                               =
            =           {VERDE}Ação executada com sucesso!{RESET}         =
            =================================================

            ''')
        
        elif self.info_dado < 3:
            print(f'''
            =================================================
            =                   # Dado #                    =
            =        O Resultado do dado foi: {VERMELHO+str(self.info_dado)+RESET}             =
            =                                               =
            =         {VERMELHO}Ação não executada corretamente!{RESET}      =
            =================================================

            ''')
    

