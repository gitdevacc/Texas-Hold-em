import card
class Table(): 
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle()
        self.middle=[self.deck.pop(),self.deck.pop(),self.deck.pop()]
    def deal_hand(self):
        if len(d)!=0:
            return [self.deck.pop(),self.deck.pop()]
        else:
            self.deck=Deck()
    def table_middle(self):
        print('Current flop:', self.middle)
        print('Please place your bets.')
        if len(d)!=0:
            self.middle.append(self.deck.pop())
            print('Shared card has been dealt has been dealt. Current cards in middle:', self.middle)
            return self.middle
        else:
            self.deck=Deck()
class Hand():
    def __init__(self):
        t=Table()
        self.hand=[t.deal_hand()]
    