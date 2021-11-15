from personagem import *
from cores import *
from dados import *
from mochila import *
from monstros import *
import time
import random


class Batalha:
    
    list_mobs = ['Zombie comum',
                     'Zombie Bomber',   
                     'Zombie fantasma']

    def getInfos(self):
        avatarInfos = [
                VERDE+'Nome: '+RESET+Avatar.nick,
                VERDE+'HP: '+RESET+str(Avatar.hp),
                VERDE+'Classe: '+RESET+Avatar.classe,
                VERDE+'LVL: '+RESET+str(Avatar.lvl),
                VERDE+'Exp: '+RESET+str(Avatar.exp)

                ]
        for i in avatarInfos:
                print(i)

class Infos(Batalha):

        def infoAvatar(self):
                avatarInfos = [
                        VERDE+'Nome: '+RESET+Avatar.nick,
                        VERDE+'HP: '+RESET+str(Avatar.hp),
                        VERDE+'Classe: '+RESET+Avatar.classe,
                        VERDE+'LVL: '+RESET+str(Avatar.lvl),
                        VERDE+'Exp: '+RESET+str(Avatar.exp)                 
                ]
                for i in avatarInfos:
                        print(i)


        def mob_spawn(self):
                mob_sp = random.choice(self.list_mobs)
                if mob_sp == Zombies.z_comum.nome:
                        print(f'''
Monstro: {mob_sp}                Hp: {Zombies.z_comum.hp}
                        ''')
                elif mob_sp == Zombies.z_bomber.nome:
                        print(f'''
Monstro: {mob_sp}                Hp: {Zombies.z_bomber.hp}
                        ''')
                elif mob_sp == Zombies.z_fantasma.nome:
                        print(f'''
Monstro: {mob_sp}                Hp: {Zombies.z_fantasma.hp}
                        ''')
                

class Mecanica(Batalha):
        def Luta_start(self):
                print(f'''
================================================================
 {VERDE+'Nome: '+RESET+Avatar.nick}          {VERDE+'HP: '+RESET+str(Avatar.hp)}          {VERDE+'Classe: '+RESET+Avatar.classe}  
      
 {VERDE+'LVL: '+RESET+str(Avatar.lvl)}          {VERDE+'Exp: '+RESET+str(Avatar.exp)} 
   
===============================================================
                ''')



