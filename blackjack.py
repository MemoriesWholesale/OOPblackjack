from tkinter import *
from tkinter.ttk import *
#Comment out the line below if not on MacOSX and change the names of the options 'bg' and 'fg' in the Button to 'background' and 'foreground'
from tkmacosx import Button
import tkinter.font as font
from random import shuffle
import time

casino = Tk()
casino.title('Blackjack')
casino.geometry('1400x800')

table = Canvas(casino,height=800,width=1400,background='green',highlightbackground='green')
table.pack()

playerlabel = Label(table,background='green',text='Player\n\nCards:\n?\nTotals:\n?\nCurrent Bet:\n?\nTotal Winnings: \n?')
playerlabel.place(in_=table,relx=.3,rely=.65)
playerbox = Canvas(table,borderwidth=2,background='green',highlightbackground='white',height=225,width=150)
playerbox.place(in_=table, relx=.45,rely=.6)

def totals(cards):
            basesum = 0
            aces = 0
            for c in cards:
                if c[0] == 'A':
                    aces += 1
                elif c[0].isdigit():
                    basesum += int(c[:-1])
                else:
                    basesum += 10
            acesums = [basesum]
            for n in range(aces):
                acesums = [s + 1 for s in acesums] + [s + 11 for s in acesums]
            return set(acesums)

ornaments = font.Font(family = 'Bodoni Ornaments',size=20)
acefont = font.Font(family = 'Courier New',size=80)

class Card:
    def __init__(self,name):
        self.rank = name[:-1]
        self.suit = name[-1]
    def display(self,position):
        if self.rank in {'J','Q','K'}:
            cardstock = Canvas(table,bg='white',height=200,width=125)
            cardstock.create_text(65,185,text='AYZAYZA',fill=f"{'red' if self.suit in {'♥', '♦'} else 'black'}",font=ornaments)
            if self.rank == 'K':
                if self.suit == '♠':
                    cardstock.create_text(65,50,text='🂮',fill="black",font= 'Batang 210 bold')
                elif self.suit == '♥':   
                    cardstock.create_text(65,50,text='🂾',fill="red",font= 'Batang 210 bold')
                elif self.suit == '♦':
                    cardstock.create_text(65,50,text='🃎',fill="red",font= 'Batang 210 bold')      
                elif self.suit == '♣':
                    cardstock.create_text(65,50,text='🃞',fill="black",font= 'Batang 210 bold')    
            elif self.rank == 'Q':
                if self.suit == '♠':
                    cardstock.create_text(65,50,text='🂭',fill="black",font= 'Batang 210 bold')
                elif self.suit == '♥':   
                    cardstock.create_text(65,50,text='🂽',fill="red",font= 'Batang 210 bold')           
                elif self.suit == '♦':
                    cardstock.create_text(65,50,text='🃍',fill="red",font= 'Batang 210 bold')  
                elif self.suit == '♣':
                    cardstock.create_text(65,50,text='🃝',fill="black",font= 'Batang 210 bold')
            else:
                if self.suit == '♠':
                    cardstock.create_text(65,50,text='🂫',fill="black",font= 'Batang 210 bold')
                elif self.suit == '♥':   
                    cardstock.create_text(65,50,text='🂻',fill="red",font= 'Batang 210 bold')             
                elif self.suit == '♦':
                    cardstock.create_text(65,50,text='🃋',fill="red",font= 'Batang 210 bold')                 
                elif self.suit == '♣':
                    cardstock.create_text(65,50,text='🃛',fill="black",font= 'Batang 210 bold')

        else:
            cardstock = Canvas(table,bg='white',height=200,width=125)
            cardstock.create_text(20,5,anchor=NE,text=self.rank,fill=f"{'red' if self.suit in {'♥', '♦'} else 'black'}",font='Batang 12 bold')
            cardstock.create_text(20,20,anchor=NE,text=self.suit,fill=f"{'red' if self.suit in {'♥', '♦'} else 'black'}",font= 'Batang 12 bold')
            if self.rank.isdigit():
                cardstock.create_text(40,100,text='\n\n'.join([self.suit for i in range(int(self.rank)//2)]),fill=f"{'red' if self.suit in {'♥', '♦'} else 'black'}",font= 'Batang 16 bold')
                cardstock.create_text(90,100,text='\n\n'.join([self.suit for i in range(int(self.rank)//2)]),fill=f"{'red' if self.suit in {'♥', '♦'} else 'black'}",font= 'Batang 16 bold')
                if int(self.rank)%2 != 0:  
                    cardstock.create_text(65,100,text=self.suit,fill=f"{'red' if self.suit in {'♥', '♦'} else 'black'}",font= 'Batang 16 bold')
            else:
                cardstock.create_text(65,100,text=self.suit,fill=f"{'red' if self.suit in {'♥', '♦'} else 'black'}",font= acefont)
    
        cardstock.place(in_= table, relx = position[0], rely = position[1], anchor = CENTER)
    def displayback(self,position):
        cardstock = Canvas(table,bg='red',height=200,width=125)
        cardstock.create_line(65,0,65,200,width=125,dash=(1,3))
        cardstock.place(in_= table, relx = position[0], rely = position[1], anchor = CENTER)   

class Deck:
    def __init__(self,cards=[]):
        for suit in ['♠', '♥', '♦', '♣']:
            for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                cards.append(rank + suit)
        shuffle(cards)
        self.cards = cards

class Human:
    def __init__(self,cards = [],cardpos = None):
        self.cards = cards
        self.cardpos = cardpos
    def blackjack(self):
        return 21 in totals(self.cards)

class Dealer(Human):
    def __init__(self,cards=[],cardpos=[.5,.2],cardtodeal = None,deck = None):
        super().__init__(cards,cardpos)
        self.cardtodeal = cardtodeal
        self.deck = deck
    def deal(self,player):
        self.cardtodeal = self.deck.cards.pop()
        cardstock = table.create_rectangle(100,300,225,500,fill='red',outline='black')
        stockline = table.create_line(160,300,160,500,width=125,dash=(1,3))
        xinc = ((player.cardpos[0] * 1400) - 100)/100
        yinc = ((player.cardpos[1] * 800) - 300)/100
        while True:
            table.move(cardstock,xinc,yinc)
            table.move(stockline,xinc,yinc)
            casino.update()
            time.sleep(.01)
            dealtpos = table.coords(cardstock)
            xl,yl,xr,yr = dealtpos
            if abs(700 - xl) <= 200:
                table.delete(cardstock)
                table.delete(stockline)
                player.hit(self.cardtodeal)
                break
    def dealself(self):
        self.cardtodeal = (self.deck.cards.pop())
        cardimage = Card(self.cardtodeal)
        cardstock = table.create_rectangle(100,300,225,500,fill='red',outline='black')
        stockline = table.create_line(160,300,160,500,width=125,dash=(1,3))
        xinc = ((self.cardpos[0] * 1400) - 100)/100
        yinc = ((self.cardpos[1] * 800) - 300)/100
        while True:
            table.move(cardstock,xinc,yinc)
            table.move(stockline,xinc,yinc)
            casino.update()
            time.sleep(.01)
            dealtpos = table.coords(cardstock)
            xl,yl,xr,yr = dealtpos
            if abs(700 - xl) <= 200:
                table.delete(cardstock)
                table.delete(stockline)
                if len(self.cards):
                    self.cards.append(self.cardtodeal)
                    cardimage.display(self.cardpos)
                    self.cardpos[0] += .01
                    self.cardpos[1] += .05
                else:
                    self.cards.append(self.cardtodeal)
                    cardimage.displayback(self.cardpos)
                    self.cardpos[0] += .01
                    self.cardpos[1] += .05
                break
    def fliphole(self):
        invisicard = Canvas(table,background='green',highlightbackground='green',height=200,width=125)
        invisicard.place(in_=table,relx=.51,rely=.25,anchor=CENTER)
        cardimage = Card(self.cards[0])
        time.sleep(.2)
        cardimage.display([.5,.2])
        cardimage = Card(self.cards[1])
        cardimage.display(self.cardpos)
        self.cardpos[0] += .01
        self.cardpos[1] += .05


class Player(Human):
    def __init__(self,name,game=None,dealer=None,cards=[],cardpos = [.5,.75],currentbet = 0,standing = False,winnings = 0):
        super().__init__(cards,cardpos)
        self.name = name
        self.game = game
        self.currentbet = currentbet
        self.winnings = winnings
        self.standing = standing
        self.cardpos = cardpos
        self.dealer = dealer
    def bet(self):
        betprompt = Toplevel()
        betprompt.geometry('300x100')
        betprompt.title("Starting bet")
        betpromptframe = Frame(betprompt)
        betpromptframe.pack()
        betpromptlabel = Label(betpromptframe,text = f'Enter your bet, {self.name}')
        betpromptlabel.pack()
        betentry = Entry(betpromptframe)
        betentry.pack()
        def placebet():
            self.currentbet = [int(betentry.get()) if len(betentry.get()) > 0 else 0][0]
            betprompt.destroy()
            self.dealer.deal(self)
            self.dealer.deal(self)
            self.dealer.dealself()
            self.dealer.dealself()
            deckimage = Card('this is the deck')
            for n in range(48):
                pos = [(.1+(.0003*n)),(.2+(.0009*n))]
                deckimage.displayback(pos)
            playerlabel.config(text=f"{self.name}\n\nCards:\n{', '.join(self.cards)}\nTotals:\n{totals(self.cards)}\nCurrent Bet:\n${self.currentbet}\nTotal Winnings: \n${self.winnings}")
            self.game.checkblackjack()
        betbutton = Button(betpromptframe,text='Bet',command = lambda:placebet())
        betbutton.pack()
    def hit(self,card):
        self.cards.append(card)
        cardimage = Card(card)
        cardimage.display(self.cardpos)
        playerlabel.config(text=f"{self.name}\n\nCards:\n{', '.join(self.cards)}\nTotals:\n{totals(self.cards)}\nCurrent Bet:\n${self.currentbet}\nTotal Winnings: \n${self.winnings}")
        self.cardpos[0] += .01
        self.cardpos[1] += .05
        if min(totals(self.cards)) > 21:
            self.bust()
    def stand(self):
        self.dealer.fliphole()
        while len([t for t in totals(self.dealer.cards) if t <= 21]) and 17 > max([t for t in totals(self.dealer.cards) if t <= 21]):
            time.sleep(.2)
            self.dealer.dealself()
        self.game.endround()
    def bust(self):
        bustmsg = Toplevel()
        bustmsg.title('Busted!')
        self.winnings -= self.currentbet
        bustframe = Frame(bustmsg)
        bustframe.pack()
        busttext = Label(bustframe, text = f'You busted and lost {self.currentbet} dollars! Do you want to play another round?')
        busttext.pack()
        def roundstarter():
            bustmsg.destroy()
            self.game.newround()
        yesbtn = Button(bustframe,text='Yes',command = lambda: roundstarter())
        yesbtn.pack()
        nobtn = Button(bustframe,text='No',command = lambda: bustmsg.destroy())
        nobtn.pack()


class Game:
    def __init__(self,player,currentround = 0):
        self.dealer = Dealer()
        self.player = Player(player,self,self.dealer)
        self.currentround = currentround
    def newround(self):
        self.currentround += 1
        clearstrip = Canvas(table,background='green',highlightbackground='green',height=750,width=300)
        clearstrip.place(in_=table,relx=.45,rely=.05)
        cleanbottom = Canvas(table,background='green',highlightbackground='green',height=20,width=1400)
        cleanbottom.place(in_=table,relx=0,rely=.99)
        newbox = Canvas(table,borderwidth=2,background='green',highlightbackground='white',height=225,width=150)
        newbox.place(in_=table, relx=.45,rely=.6)
        self.dealer.cards = []
        self.dealer.cardpos = [.5,.2]
        self.player.currentbet = 0
        self.player.cardpos = [.5,.75]
        self.player.cards = []
        playerlabel.config(text=f'{self.player.name}\n\nCards:\n{self.player.cards}\nTotals:\n{totals(self.player.cards)}\nCurrent Bet:\n${self.player.currentbet}\nTotal Winnings: \n${self.player.winnings}')
        deck = Deck([])
        self.dealer.deck = deck
        self.player.bet()
        def tryhit(player):
            if len(player.cards) < 2:
                nicetry = Toplevel()
                nicetry.title('Nice Try!')
                nicetry.geometry('200x100')
                nicetryframe = Frame(nicetry)
                nicetryframe.pack()
                nicetrytext = Label(nicetryframe,text='You have to bet first!')
                nicetrytext.pack()
                okbtn = Button(nicetryframe,text='OK',command = lambda: nicetry.destroy())
                okbtn.pack()
            else:
                self.dealer.deal(player)
        hitbutton = Button(table,text='Hit',command = lambda: tryhit(self.player))
        hitbutton.place(relx=.75,rely=.8)
        def trystand(player):
            if len(player.cards) < 2:
                nicetry = Toplevel()
                nicetry.title('Nice Try!')
                nicetry.geometry('200x100')
                nicetryframe = Frame(nicetry)
                nicetryframe.pack()
                nicetrytext = Label(nicetryframe,text='You have to bet first!')
                nicetrytext.pack()
                okbtn = Button(nicetryframe,text='OK',command = lambda: nicetry.destroy())
                okbtn.pack()
            else:
                player.stand()
        standbutton = Button(table,text='Stand',command = lambda: trystand(self.player))
        standbutton.place(relx=.75,rely=.85)
    def checkblackjack(self):
        time.sleep(.2)
        if self.player.blackjack():
            if self.dealer.cards[1][0] in {'1','J','Q','K','A'}:
                time.sleep(.1)
                self.dealer.fliphole()
                if self.dealer.blackjack():
                    playerpush = Toplevel()
                    playerpush.title('Push!')
                    pushframe = Frame(playerpush)
                    pushframe.pack()
                    pushmsg = Label(pushframe,text="You both hit blackjack--nobody wins! Do you want to play another round?")
                    pushmsg.pack()
                    def roundstarter():
                        playerpush.destroy()
                        self.newround()
                    yesbtn = Button(pushframe,text='Yes',command = lambda: roundstarter())
                    yesbtn.pack()
                    nobtn = Button(pushframe,text='No',command = lambda: playerpush.destroy())
                    nobtn.pack()
                else:
                    time.sleep(.1)
                    self.player.winnings += (self.player.currentbet * 3)//2
                    playerwin = Toplevel()
                    playerwin.title('BLACKJACK!')
                    winframe = Frame(playerwin)
                    winframe.pack()
                    winmsg = Label(winframe,text=f'You hit Blackjack! You win {(self.player.currentbet * 3)//2} dollars! Do you want to play another round?')
                    winmsg.pack()
                    def roundstarter():
                        playerwin.destroy()
                        self.newround()
                    yesbtn = Button(winframe,text='Yes',command = lambda: roundstarter())
                    yesbtn.pack()
                    nobtn = Button(winframe,text='No',command = lambda: playerwin.destroy())
                    nobtn.pack()
            else:
                time.sleep(.1)
                self.player.winnings += (self.player.currentbet * 3)//2
                playerwin = Toplevel()
                playerwin.title('BLACKJACK!')
                winframe = Frame(playerwin)
                winframe.pack()
                winmsg = Label(winframe,text=f'You hit Blackjack! You win {(self.player.currentbet * 3)//2} dollars! Do you want to play another round?')
                winmsg.pack()
                def roundstarter():
                    playerwin.destroy()
                    self.newround()
                yesbtn = Button(winframe,text='Yes',command = lambda: roundstarter())
                yesbtn.pack()
                nobtn = Button(winframe,text='No',command = lambda: playerwin.destroy())
                nobtn.pack()

    def endround(self):
        if min(totals(self.dealer.cards)) > 21:
            time.sleep(.1)
            self.player.winnings += self.player.currentbet
            dealerbust = Toplevel()
            dealerbust.title('Dealer Busted!')
            dbustframe = Frame(dealerbust)
            dbustframe.pack()
            dbustmsg = Label(dbustframe,text=f'The Dealer has busted! You win {self.player.currentbet} dollars! Do you want to play another round?')
            dbustmsg.pack()
            def roundstarter():
                dealerbust.destroy()
                self.newround()
            yesbtn = Button(dbustframe,text='Yes',command = lambda: roundstarter())
            yesbtn.pack()
            nobtn = Button(dbustframe,text='No',command = lambda: dealerbust.destroy())
            nobtn.pack()
        elif max([t for t in totals(self.dealer.cards) if t <= 21]) > max([t for t in totals(self.player.cards) if t <= 21]):
            time.sleep(.1)
            self.player.winnings -= self.player.currentbet
            playerlose = Toplevel()
            playerlose.title('Dealer Wins!')
            loseframe = Frame(playerlose)
            loseframe.pack()
            losemsg = Label(loseframe,text=f'The Dealer has won! You lose {self.player.currentbet} dollars! Do you want to play another round?')
            losemsg.pack()
            def roundstarter():
                playerlose.destroy()
                self.newround()
            yesbtn = Button(loseframe,text='Yes',command = lambda: roundstarter())
            yesbtn.pack()
            nobtn = Button(loseframe,text='No',command = lambda: playerlose.destroy())
            nobtn.pack()
        elif max([t for t in totals(self.dealer.cards) if t <= 21]) == max([t for t in totals(self.player.cards) if t <= 21]):
            time.sleep(.1)
            playerpush = Toplevel()
            playerpush.title('Push!')
            pushframe = Frame(playerpush)
            pushframe.pack()
            pushmsg = Label(pushframe,text="It's a push--nobody wins! Do you want to play another round?")
            pushmsg.pack()
            def roundstarter():
                playerpush.destroy()
                self.newround()
            yesbtn = Button(pushframe,text='Yes',command = lambda: roundstarter())
            yesbtn.pack()
            nobtn = Button(pushframe,text='No',command = lambda: playerpush.destroy())
            nobtn.pack()
        else:
            time.sleep(.1)
            self.player.winnings += self.player.currentbet
            playerwin = Toplevel()
            playerwin.title('Winner!')
            winframe = Frame(playerwin)
            winframe.pack()
            winmsg = Label(winframe,text=f'You have won! You win {self.player.currentbet} dollars! Do you want to play another round?')
            winmsg.pack()
            def roundstarter():
                playerwin.destroy()
                self.newround()
            yesbtn = Button(winframe,text='Yes',command = lambda: roundstarter())
            yesbtn.pack()
            nobtn = Button(winframe,text='No',command = lambda: playerwin.destroy())
            nobtn.pack()

newgamestart = Toplevel()
newgamestart.geometry('300x100')
newgamestart.title('New Game')
startframe = Frame(newgamestart)
startframe.pack()
startlabel = Label(startframe,text = 'Enter your name')
startlabel.pack()
nameentry = Entry(startframe)
nameentry.pack()
def gamestarter():
    newgame = Game(nameentry.get())
    newgamestart.destroy()
    playerlabel.config(text=f'{newgame.player.name}\n\nCards:\n?\nTotals:\n?\nCurrent Bet:\n?\nTotal Winnings: \n$0')
    newgame.newround()
startbutton = Button(startframe,text='Play Blackjack',command=lambda:gamestarter())
startbutton.pack()



casino.mainloop()


