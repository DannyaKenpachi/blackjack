from random import randint

def charactors_card():
    mast = ['Черви', 'Буби', 'Пики', 'Крести']
    value_card = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'валет' : 10, 'дама' : 10, 
                'король' : 10, 'туз' : 11}
    return mast, value_card

class Koloda_Card():

    koloda = {}

    def __init__(self, mast , value_card):
        self.mast = mast
        self.value_card = value_card

    def create_koloda(self):
        for i in self.value_card.keys():
            for j in self.mast:
                self.koloda[i + ' ' + j] = self.value_card[i]
        return self.koloda
    
class Bank():

    summa = int(input('Введите общий банк: '))

    def __init__(self):
        pass

    def dep(self, hod):
        if hod > self.summa:
            hod = 'Сумма ставки превышает банк'
            return self.summa, hod
        else:
            self.summa -= hod
            return self.summa, hod
        
    def win(self, cash):
        self.summa += cash * 2
        return self.summa
    
    def zer(self, cash):
        self.summa += cash
        return self.summa
    
def stavka_player():
    t = True
    while t:
        step = int(input('Введите сумму ставки: '))
        hod = bank1.dep(step)[1]
        if hod != 'Сумма ставки превышает банк':
            t = False
    return hod

def game():
    rz = razdacha(2, koloda_card1.create_koloda())
    global cards_diler
    cards_diler = Ruka_cards(rz[0], rz[1])
    rz = razdacha(2, new_koloda)
    global cards_player
    cards_player = Ruka_cards(rz[0], rz[1])
    pokaz_ruk(1)

def razdacha(m, koloda):
    kol_k = list(koloda.keys())
    n = 0
    pt = 0
    ryka_card = []
    while n < m:
        card = randint(0, len(koloda) - 1)
        pd1 = Podchet_ochkov(kol_k[card], koloda)
        pt += pd1.points()[0]
        ryka_card.append(kol_k[card])
        n += 1
    global new_koloda
    new_koloda = pd1.koloda
    return pt, ryka_card

def pokaz_ruk(id):
    if id == 1:
        print('Карты дилера:')
        for i in cards_diler.ruka[:1]:
            print(i)
        print('Карты игрока:')
        for i in cards_player.ruka:
            print(i)
    elif id == 2:
        print('Карты игрока:')
        for i in cards_player.ruka:
            print(i)
    elif id == 3:
        print('Карты дилера:')
        for i in cards_diler.ruka:
            print(i)

        
class Podchet_ochkov():

    pt = 0

    def __init__(self, naz_card, koloda):
        self.naz_card = naz_card
        self.koloda = koloda

    def points(self):
        self.pt = self.koloda[self.naz_card]
        del self.koloda[self.naz_card]
        return self.pt, self.koloda
    
class Ruka_cards():

    def __init__(self, pt, ruka):
        self.pt = pt
        self.ruka = ruka

    def dobor_ruki(self, new_card, new_pt):
        self.pt += new_pt
        self.ruka.append(''.join(new_card))
        return self.pt, self.ruka

def dobor():
    n = 0
    t = True
    while t:
        vopros = input('Добор? ')
        if vopros.lower() == 'да':
            ruka = razdacha(1, new_koloda)
            cards_player.dobor_ruki(ruka[1], ruka[0])
            pokaz_ruk(2)
        else:
            t = False
            n = 1
        if cards_player.pt > 21:
            for i in cards_player.ruka:
                if 'туз' in i and n == 0:
                    if input('Поменять туз на 1 ').lower() == 'да':
                        cards_player.pt -= 10
                        n += 1
                        pokaz_ruk(2)
                    else:
                        t = False
                        itog(1)
    if n == 1:
        dobor_diler_and_finish()

def itog(id):
    if id == 1:
        print('Дилер выйграл')
        print(bank1.summa)
        restart()
    elif id == 2:
        print('Игрок выйграл')
        print(bank1.win(stavka))
        restart()
    elif id == 3:
        print('Ничья')
        print(bank1.zer(stavka))
        restart()

def dobor_diler_and_finish():
    pokaz_ruk(3)
    if cards_diler.pt < cards_player.pt:
        while cards_diler.pt < 17:
            ruka_diler = razdacha(1, new_koloda)
            cards_diler.dobor_ruki(ruka_diler[1], ruka_diler[0])
            pokaz_ruk(3)
        if cards_diler.pt > 21 or cards_diler.pt < cards_player.pt:
            itog(2)
        elif cards_diler.pt > cards_player.pt:
            itog(1)
    elif cards_diler.pt == cards_player.pt:
        itog(3)
    else:
        itog(1)
    
def restart():
    t = input('Продолжим игру: ')
    if t.lower() == 'да':
        global stavka
        print(bank1.summa)
        stavka = stavka_player()
        game()
        dobor()

koloda_card1 = Koloda_Card(charactors_card()[0], charactors_card()[1])
bank1 = Bank()
stavka = stavka_player()
game()
dobor()