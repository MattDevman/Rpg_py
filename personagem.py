from mochila import Mochila
from cores import *
from tqdm import tqdm

class Avatar:
    nick = 'None'
    hp = 'None'
    classe = 'None'
    lvl = 'None'
    exp = '0 / 100'
    exp_progress = 'None'
    armadura = []
    equips = []

class Personagem(Avatar):
    def setNick(self):
        self.nick = input('Digite o nome do personagem: ')
        self.hp = 100
        self.classe = 'Humano'
        self.lvl = 1
        self.exp = 0
        self.exp_progress_bar = lambda bar: tqdm(range(100))
        self.exp_progress = self.exp_progress_bar
        self.armadura = self.armadura + [
            Mochila.armadura[0],
            Mochila.armadura[1],
            Mochila.armadura[2],
            Mochila.armadura[3]
        ]
        
        
    def getInfoEquips(self):
        armadurasInfo = [
            f'Capacete: {VERMELHO+self.armadura[0][0]+RESET}',
            f'Peitoral: {VERMELHO+self.armadura[1][0]+RESET}',
            f'Calças: {VERMELHO+self.armadura[2][0]+RESET}',
            f'Botas: {VERMELHO+self.armadura[3][0]+RESET}'
        ]
        
        for i in armadurasInfo:
            print(i)


    def getInfos(self):
        avatarInfos = [
            VERDE+'Nome: '+RESET+self.nick,
            VERDE+'HP: '+RESET+str(self.hp),
            VERDE+'Classe: '+RESET+self.classe,
            VERDE+'LVL: '+RESET+str(self.lvl),
            VERDE+'Exp: '+RESET+str(self.exp)

            ]
        
        for i in avatarInfos:
            print(i)
        return self
