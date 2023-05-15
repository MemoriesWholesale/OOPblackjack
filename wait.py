from tkinter import *
root = Tk()

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




def message():
    L['text'] = 'I LIKE ICE CREAM'

def delay():
    L['text'] = 'Wait for it...'
    root.after(2000, message)

L = Label(root, text="Please click the button.")
L.pack()

B = Button(root, text="button", command=delay)
B.pack()

root.mainloop()