from __future__ import print_function
import random

class Card(object):

    mrank=['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    msuit=['Clubs','Diamonds','Hearts','Spades']

    def __init__(self,rank,suit,ifu):
        self.rank = rank
        self.suit = suit
        self.ifu = ifu

    def getvalue(self):
        value = 0
        if self.ifu == True:
            ans=[i for i, x in enumerate(self.mrank) if x == self.rank]
            value = ans[0]+1
            if value > 10: value=10
        return value

    def flip(self):
        self.ifu = not self.ifu

class Player(object):

    def __init__(self,name):
        self.mhand = []
        self.name = name

    def add(self,pcard):
        self.mhand.append(pcard)

    def GetTotal(self):
        if len(self.mhand) == 0:
            return 0
        if  self.mhand[0].getvalue() == 0:
            return 0

        total = 0
        for index in range(len(self.mhand)):
            total = total + self.mhand[index].getvalue()

        self.containsAce = False
        for index in range(len(self.mhand)):
            if self.mhand[index].rank == 'ace':
                self.containsAce = True

        if (self.containsAce == True) and (total <= 11):
            total = total + 10
        return total

    def IsBusted(self):
        return self.GetTotal() > 21

    def Bust(self):
        print (self.name + " busts.\n")

    def IsHitting(self):
        print (self.name + ", do you want a hit?")
        ans = raw_input()
        return (ans == 'y' or ans == 'Y')

    def Win(self):
        print (self.name + " wins.\n")

    def Lose(self):
        print (self.name + " loses.\n")

    def Push(self):
        print (self.name + " pushes.\n")

    def Display(self):
        print(self.name + " hand is:")
        for i in range(0,len(self.mhand)):

            print(self.mhand[i].rank+" of "+self.mhand[i].suit)
        print(self.GetTotal())

class House(object):

    def __init__(self,name="House"):
        self.mhand = []
        self.name = name

    def add(self,pcard):
        self.mhand.append(pcard)

    def GetTotal(self):
        if len(self.mhand) == 0:
            return 0
        if  self.mhand[0].getvalue() == 0:
            return 0

        total = 0
        for index in range(len(self.mhand)):
            total = total + self.mhand[index].getvalue()

        self.containsAce = False
        for index in range(len(self.mhand)):
            if self.mhand[index].rank == 'ace':
                self.containsAce = True

        if (self.containsAce == True) and (total <= 11):
            total = total + 10
        return total

    def IsBusted(self):
        return self.GetTotal() > 21

    def Bust(self):
        print (self.name + " busts.\n")

    def IsHitting(self):
        return (self.GetTotal() <= 16)

    def FlipFirstCard(self):
       if len(self.mhand) == 0:
           print ("No card to flip!")
       else:
           self.mhand[0].flip()

    def Display(self):
        print("House hand is:")
        for i in range(0,len(self.mhand)):
            print(self.mhand[i].rank+" of "+self.mhand[i].suit)
        print(self.GetTotal())


""" generate deck """
class Deck(object):


    def __init__(self):
        self.mdeck = []
        for psuit in range(4):
            for prank in range(13):
                pcard = Card(Card.mrank[prank],Card.msuit[psuit],True)
                self.mdeck.append(pcard)

    def shuffle(self):
        random.shuffle(self.mdeck)

    def deal(self,aplayer):
        if len(self.mdeck) == 0:
            print ("Out of cards!\n")
        else:
            aplayer.add(self.mdeck[-1])
            self.mdeck.pop()

    def AddCards(self,aplayer):

        while (aplayer.IsBusted() != True and aplayer.IsHitting()):
            self.deal(aplayer)
            aplayer.Display()
            if(aplayer.IsBusted()):
                aplayer.Bust()


""" main """

print("Welcome to Blackjack!\n")
print("Enter your name:")
pname=raw_input()
again = 'y'

while (again != 'n' and again != 'N'):

    """ init """
    deck = Deck()
    player1 = Player(pname)
    house = House()
    deck.shuffle()

    """ first round """
    deck.deal(player1)
    deck.deal(house)
    deck.deal(player1)
    deck.deal(house)
    house.FlipFirstCard()
    player1.Display()

    deck.AddCards(player1)
    house.FlipFirstCard()
    house.Display()
    deck.AddCards(house)

    if (house.IsBusted()):
        if (not player1.IsBusted()):
            player1.Win()
        elif (player1.IsBusted()):
            print("Nodoby wins.")
    elif (not player1.IsBusted()):
        if (player1.GetTotal() > house.GetTotal()):
            player1.Win()
        elif (player1.GetTotal() < house.GetTotal()):
            player1.Lose()
        else:
            player1.Push()
    elif (player1.IsBusted()):
        if (not house.IsBusted()):
            player1.Lose()

    print("\nDo you want to play again?")
    again = raw_input()




